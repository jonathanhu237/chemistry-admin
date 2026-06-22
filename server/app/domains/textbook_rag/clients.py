from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any


class TextbookRAGClientError(RuntimeError):
    pass


def _request_json(*, url: str, api_key: str, payload: dict[str, Any], timeout: float) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise TextbookRAGClientError(f"request failed: {exc.__class__.__name__}: {str(exc)[:180]}") from exc
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise TextbookRAGClientError("response is not valid JSON") from exc
    if not isinstance(parsed, dict):
        raise TextbookRAGClientError("response JSON must be an object")
    return parsed


def _join_endpoint(base_url: str, default_suffix: str) -> str:
    normalized = base_url.rstrip("/")
    if not normalized:
        return default_suffix
    if normalized.endswith(default_suffix) or normalized.endswith("/embeddings"):
        return normalized
    return f"{normalized}{default_suffix}"


def _rerank_endpoint(base_url: str, model: str) -> str:
    normalized = base_url.rstrip("/")
    if not normalized:
        return "/rerank"
    lower = normalized.lower()
    if lower.endswith(("/rerank", "/reranks", "/text-rerank")):
        return normalized
    if "dashscope" in lower and lower.endswith("/api/v1"):
        return f"{normalized}/services/rerank/text-rerank/text-rerank"
    if "compatible-api" in lower or "compatible-mode" in lower:
        return f"{normalized}/reranks" if model == "qwen3-rerank" else f"{normalized}/rerank"
    return f"{normalized}/rerank"


def _rerank_payload(*, endpoint: str, model: str, query: str, documents: list[str]) -> dict[str, Any]:
    lower = endpoint.lower()
    if "/services/rerank/" in lower or lower.endswith("/text-rerank"):
        return {
            "model": model,
            "input": {"query": query, "documents": documents},
            "parameters": {"return_documents": False, "top_n": len(documents)},
        }
    payload: dict[str, Any] = {"model": model, "query": query, "documents": documents}
    if lower.endswith("/reranks"):
        payload["top_n"] = len(documents)
    return payload


@dataclass(frozen=True)
class QwenEmbeddingClient:
    base_url: str
    api_key: str
    model: str
    dimensions: int | None = None
    timeout_seconds: float = 8.0

    @property
    def ready(self) -> bool:
        return bool(self.base_url and self.api_key and self.model)

    def embed(self, texts: list[str]) -> list[list[float]]:
        if not self.ready:
            raise TextbookRAGClientError("embedding client is not configured")
        if not texts:
            return []
        payload: dict[str, Any] = {"model": self.model, "input": texts}
        if self.dimensions:
            payload["dimensions"] = int(self.dimensions)
        response = _request_json(
            url=_join_endpoint(self.base_url, "/embeddings"),
            api_key=self.api_key,
            payload=payload,
            timeout=self.timeout_seconds,
        )
        data = response.get("data")
        if not isinstance(data, list):
            raise TextbookRAGClientError("embedding response missing data list")
        embeddings: list[list[float]] = []
        for item in data:
            if not isinstance(item, dict) or not isinstance(item.get("embedding"), list):
                raise TextbookRAGClientError("embedding response item missing embedding")
            embedding = [float(value) for value in item["embedding"]]
            if not embedding:
                raise TextbookRAGClientError("embedding response contained an empty vector")
            embeddings.append(embedding)
        if len(embeddings) != len(texts):
            raise TextbookRAGClientError("embedding response count does not match input count")
        return embeddings


@dataclass(frozen=True)
class QwenRerankClient:
    base_url: str
    api_key: str
    model: str
    timeout_seconds: float = 8.0

    @property
    def ready(self) -> bool:
        return bool(self.base_url and self.api_key and self.model)

    def rerank(self, *, query: str, documents: list[str]) -> list[float]:
        if not self.ready:
            raise TextbookRAGClientError("rerank client is not configured")
        if not documents:
            return []
        endpoint = _rerank_endpoint(self.base_url, self.model)
        payload = _rerank_payload(endpoint=endpoint, model=self.model, query=query, documents=documents)
        response = _request_json(
            url=endpoint,
            api_key=self.api_key,
            payload=payload,
            timeout=self.timeout_seconds,
        )
        scores = _extract_rerank_scores(response, len(documents))
        if len(scores) != len(documents):
            raise TextbookRAGClientError("rerank response count does not match document count")
        return scores


def _extract_rerank_scores(response: dict[str, Any], expected_count: int) -> list[float]:
    if isinstance(response.get("scores"), list):
        return [float(score) for score in response["scores"]]
    result_sets: list[Any] = []
    if isinstance(response.get("results"), list):
        result_sets = response["results"]
    elif isinstance(response.get("data"), list):
        result_sets = response["data"]
    elif isinstance(response.get("output"), dict) and isinstance(response["output"].get("results"), list):
        result_sets = response["output"]["results"]
    if not result_sets:
        raise TextbookRAGClientError("rerank response missing scores/results")
    scores = [0.0 for _ in range(expected_count)]
    sequential_scores: list[float] = []
    for index, item in enumerate(result_sets):
        if not isinstance(item, dict):
            sequential_scores.append(float(item))
            continue
        score = item.get("relevance_score", item.get("score", item.get("rerank_score")))
        if score is None:
            raise TextbookRAGClientError("rerank result missing score")
        result_index = item.get("index", item.get("document_index", index))
        try:
            scores[int(result_index)] = float(score)
        except (TypeError, ValueError, IndexError) as exc:
            raise TextbookRAGClientError("rerank result has invalid index") from exc
    if sequential_scores:
        return sequential_scores
    return scores
