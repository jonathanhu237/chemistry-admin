import { Alert, Typography } from "antd";

import type { LearningAssistantRuntime } from "../../api/learningAssistant";
import type { AIConfiguration } from "../../api/settings";
import { formatDateTime, ragRouteSummary, ragStatus } from "./monitoringMappers";
import { LocalQueryState, MetricGrid, MetricTile, ModuleHeader } from "./MonitoringShared";

const { Text } = Typography;

type RagMonitoringModuleProps = {
  aiConfig?: AIConfiguration;
  runtime?: LearningAssistantRuntime;
  loading?: boolean;
  error?: unknown;
  retry?: () => void;
};

export function RagMonitoringModule({ aiConfig, runtime, loading, error, retry }: RagMonitoringModuleProps) {
  const ragRuntime = runtime?.rag_runtime || aiConfig?.rag_runtime;
  const meta = ragStatus(aiConfig, runtime);
  const diagnostics = ragRuntime?.textbook_rag_diagnostics || runtime?.textbook_rag_diagnostics || {};
  const models = ragRuntime?.textbook_rag_models || {};
  const embeddingConfigured = diagnostics.embedding_configured === true;
  const rerankConfigured = diagnostics.rerank_configured === true;
  const esConfigured = diagnostics.elasticsearch_url_configured === true;
  const indexExists = diagnostics.index_exists === true;
  const modelSummary = models.embedding || models.rerank ? `${models.embedding || "-"} / ${models.rerank || "-"}` : "-";

  return (
    <section className="ai-monitor-module">
      <LocalQueryState loading={loading} error={error} retry={retry}>
        <ModuleHeader eyebrow="RAG Runtime" title={meta.headline} description={ragRouteSummary(aiConfig, runtime)} status={meta.label} tone={meta.tone} />
        {runtime?.textbook_rag_error ? (
          <Alert type="warning" showIcon className="ai-monitor-alert" message="教材 RAG 当前不可用" description={runtime.textbook_rag_error} />
        ) : null}
        <MetricGrid>
          <MetricTile label="学生 RAG" value={ragRuntime?.rag_enabled ? "已开启" : "已关闭"} tone={ragRuntime?.rag_enabled ? "good" : "idle"} />
          <MetricTile label="教材 RAG" value={meta.label} tone={meta.tone} />
          <MetricTile label="Query 生成" value={ragRuntime?.query_generation_enabled ? "已开启" : "未开启"} tone={ragRuntime?.query_generation_enabled ? "good" : "idle"} />
          <MetricTile label="最近检测" value={runtime?.checked_at ? formatDateTime(runtime.checked_at, "-") : "尚未检测"} />
          <MetricTile label="关键词 / 向量 / 重排 / 返回" value={ragRuntime ? `${ragRuntime.keyword_top_k} / ${ragRuntime.vector_top_k} / ${ragRuntime.rerank_top_k} / ${ragRuntime.final_top_k}` : "-"} />
          <MetricTile label="Elasticsearch" value={esConfigured ? "已配置" : "缺失"} tone={esConfigured ? "good" : "bad"} />
          <MetricTile label="索引" value={indexExists ? "存在" : (ragRuntime?.textbook_rag_status || "-")} tone={indexExists ? "good" : meta.tone} />
          <MetricTile label="Embedding" value={embeddingConfigured ? "已配置" : "缺失"} tone={embeddingConfigured ? "good" : "bad"} />
          <MetricTile label="Rerank" value={rerankConfigured ? "已配置" : "缺失"} tone={rerankConfigured ? "good" : "bad"} />
          <MetricTile label="索引名" value={ragRuntime?.textbook_rag_index || "-"} />
        </MetricGrid>
        <div className="ai-monitor-long-value">
          <span>模型</span>
          <strong>{modelSummary}</strong>
          <Text type="secondary">
            {ragRuntime?.textbook_rag_message || "外部教材 RAG 使用配置的 Embedding、Rerank 与 Elasticsearch。"}
          </Text>
        </div>
      </LocalQueryState>
    </section>
  );
}
