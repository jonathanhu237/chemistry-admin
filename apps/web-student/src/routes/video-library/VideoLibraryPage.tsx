import { FormEvent, useEffect, useMemo, useState } from "react";
import { useNavigate, useSearch } from "@tanstack/react-router";
import { ArrowUpLeft, Atom, ChevronRight, FlaskConical, FolderOpen, History, LoaderCircle, Search, Video, X } from "lucide-react";
import type {
  StudentCatalogBreadcrumb,
  StudentCatalogChapterResponse,
  StudentCatalogNodeCard,
  StudentHomeVideoFeedItem,
  StudentLearningPageResponse,
  StudentLearningProfileSummary,
  StudentVideoLibraryResultItem,
  StudentVideoLibraryRouteTarget,
  StudentVideoLibrarySearchResponse,
} from "../../api";
import {
  errorMessage,
  getStudentCatalogNode,
  getStudentChapterCatalog,
  getStudentHomeVideoFeed,
  getStudentLearningPage,
  searchStudentVideoLibrary,
  studentMediaUrl,
} from "../../api";
import { navigateToAiChat, navigateToCatalogNode, navigateToChapter, navigateToPoint } from "../../app/router/navigation";
import type { StudentRouteSearch } from "../../app/router/routeTypes";
import { useDetailBack } from "../../app/shell/useDetailBack";
import { type AssistantContext } from "../../features/assistant/assistantContext";
import { catalogPathLabel } from "../../features/catalog/CatalogNodeCards";
import { formatChapterEntryTitle } from "../../features/learning/learningFormat";
import { MobileEmptyState } from "../../mobile/primitives";
import { BackArrowIcon } from "../../shared/mobile/BackArrowIcon";
import { LearningState } from "../../shared/mobile/LearningState";

const VIDEO_LIBRARY_SEARCH_HISTORY_KEY = "student.videoLibrarySearch.history.v1";
const LEARNING_SEARCH_HISTORY_KEY = "student.catalogSearch.history.v1";
const MAX_SEARCH_HISTORY = 8;
const DEFAULT_HISTORY_ROWS = 6;
const DEFAULT_VIDEO_ROWS = 6;
const MIN_VIDEO_ROWS_BEFORE_HIDING_TERMS = 4;

type SearchScope = "video" | "learning";

type CatalogSearchRecord = {
  node: StudentCatalogNodeCard;
  breadcrumbs: StudentCatalogBreadcrumb[];
};

function compactSearch(search: Record<string, string | null | undefined>): Record<string, string> {
  return Object.fromEntries(
    Object.entries(search)
      .map(([key, value]) => [key, String(value || "").trim()] as const)
      .filter(([, value]) => value.length > 0),
  );
}

function compactText(value: string | null | undefined): string {
  return String(value || "").trim();
}

function readVideoLibrarySearchHistory(storageKey: string): string[] {
  try {
    const payload = window.localStorage.getItem(storageKey);
    const parsed = payload ? JSON.parse(payload) : [];
    return Array.isArray(parsed)
      ? parsed.filter((item): item is string => typeof item === "string" && Boolean(item.trim())).slice(0, MAX_SEARCH_HISTORY)
      : [];
  } catch {
    return [];
  }
}

function writeVideoLibrarySearchHistory(storageKey: string, items: string[]) {
  try {
    window.localStorage.setItem(storageKey, JSON.stringify(items.slice(0, MAX_SEARCH_HISTORY)));
  } catch {
    // Local history is a convenience layer; storage failures should not block search.
  }
}

function rememberVideoLibrarySearchQuery(storageKey: string, query: string): string[] {
  const text = compactText(query);
  if (!text) return readVideoLibrarySearchHistory(storageKey);
  const next = [text, ...readVideoLibrarySearchHistory(storageKey).filter((item) => item !== text)].slice(0, MAX_SEARCH_HISTORY);
  writeVideoLibrarySearchHistory(storageKey, next);
  return next;
}

function compactCatalogPath(path: string[] | null | undefined): string {
  const cleanPath = (path || []).map((part) => part.trim()).filter(Boolean);
  if (cleanPath.length <= 2) return cleanPath.join(" / ");
  return `${cleanPath[0]} / ${cleanPath[cleanPath.length - 1]}`;
}

function catalogBreadcrumbForNode(node: StudentCatalogNodeCard): StudentCatalogBreadcrumb {
  return {
    node_id: node.node_id,
    title: node.title,
    node_kind: node.node_kind,
    chapter_id: node.chapter_id,
  };
}

function catalogRecordPath(record: CatalogSearchRecord): string {
  return catalogPathLabel([...record.breadcrumbs, catalogBreadcrumbForNode(record.node)]);
}

function catalogRecordParentLabel(record: CatalogSearchRecord, rootLabel: string): string {
  return record.breadcrumbs[record.breadcrumbs.length - 1]?.title || rootLabel;
}

function catalogNodeMeta(node: StudentCatalogNodeCard): string {
  if (node.node_kind === "point") return (node.published_media_count || node.media_count) > 0 ? "视频点位" : "实验点位";
  return "目录";
}

function catalogRecordMatches(record: CatalogSearchRecord, query: string): boolean {
  const path = catalogRecordPath(record);
  return [record.node.title, record.node.summary, catalogNodeMeta(record.node), path].filter(Boolean).join(" ").toLowerCase().includes(query);
}

async function buildCatalogSearchIndex(chapterId: string): Promise<{
  chapter: StudentCatalogChapterResponse;
  records: CatalogSearchRecord[];
}> {
  const chapter = await getStudentChapterCatalog(chapterId);
  const records: CatalogSearchRecord[] = chapter.nodes.map((node) => ({ node, breadcrumbs: [] }));
  const visited = new Set<string>();

  async function visit(nodes: StudentCatalogNodeCard[]) {
    for (const node of nodes) {
      if (node.node_kind !== "directory" || visited.has(node.node_id)) continue;
      visited.add(node.node_id);
      const detail = await getStudentCatalogNode(node.node_id);
      const childRecords = detail.children.map((child) => ({ node: child, breadcrumbs: detail.breadcrumbs }));
      records.push(...childRecords);
      await visit(detail.children);
    }
  }

  await visit(chapter.nodes);
  return { chapter, records };
}

function isVideoResult(item: StudentVideoLibraryResultItem): boolean {
  return item.type === "video_point" || item.type === "experiment";
}

function isDirectoryResult(item: StudentVideoLibraryResultItem): boolean {
  return item.type === "chapter_experiment" || item.type === "knowledge_point";
}

function aiContextFromResult(item: StudentVideoLibraryResultItem, target: StudentVideoLibraryRouteTarget): AssistantContext {
  return {
    context_type: target.node_id ? "learning_point" : "learning_home",
    context_title: target.context_title || item.title,
    context_summary: target.context_summary || item.snippet || item.subtitle,
    chapter_id: target.chapter_id || undefined,
    point_node_id: target.node_id || undefined,
    source_node_id: target.source_node_id || undefined,
    catalog_path: target.catalog_path || undefined,
    prompts: [
      target.prompt || `解释“${item.title}”这个实验现象`,
      "这个现象对应哪些反应原理？",
      "我应该先看哪个实验点位？",
    ],
  };
}

type VideoLibraryDefaultVideo = {
  id: string;
  title: string;
  subtitle: string;
  snippet: string;
  badges: string[];
  chapterLabel: string;
  thumbnailUrl: string;
  target?: StudentVideoLibraryRouteTarget | null;
};

function learningChapterLabel(target: StudentVideoLibraryRouteTarget | null | undefined, profiles: StudentLearningProfileSummary[]): string {
  if (!target) return "";
  const profile =
    profiles.find((item) => Boolean(target.profile_id) && item.profile_id === target.profile_id) ||
    profiles.find((item) => Boolean(target.chapter_id) && item.chapter_id === target.chapter_id);
  return profile ? formatChapterEntryTitle(profile) : "";
}

function thumbnailUrlForTarget(target: StudentVideoLibraryRouteTarget | null | undefined, feedItems: StudentHomeVideoFeedItem[]): string {
  if (!target) return "";
  const feedItem = feedItems.find((item) => {
    const ids = [item.node_id, item.placement_node_id, item.canonical_point_id].filter(Boolean);
    return [target.node_id, target.placement_node_id, target.canonical_point_id].some((id) => Boolean(id) && ids.includes(id || ""));
  });
  return feedItem?.video.thumbnail_path ? studentMediaUrl(feedItem.video.thumbnail_path) : "";
}

function defaultVideoFromFeed(item: StudentHomeVideoFeedItem, profiles: StudentLearningProfileSummary[]): VideoLibraryDefaultVideo {
  return {
    id: `feed:${item.id}`,
    title: item.title,
    subtitle: compactCatalogPath(item.catalog_path) || item.summary,
    snippet: item.snippet || item.summary,
    badges: item.badges,
    chapterLabel: learningChapterLabel(item.target, profiles),
    thumbnailUrl: item.video.thumbnail_path ? studentMediaUrl(item.video.thumbnail_path) : "",
    target: item.target,
  };
}

function defaultVideoFromSearchResult(
  item: StudentVideoLibraryResultItem,
  profiles: StudentLearningProfileSummary[],
  feedItems: StudentHomeVideoFeedItem[] = [],
): VideoLibraryDefaultVideo {
  return {
    id: `search:${item.id}`,
    title: item.title,
    subtitle: compactCatalogPath(item.target?.catalog_path) || item.subtitle,
    snippet: item.snippet,
    badges: item.badges,
    chapterLabel: learningChapterLabel(item.target, profiles),
    thumbnailUrl: thumbnailUrlForTarget(item.target, feedItems),
    target: item.target,
  };
}

export function VideoLibraryPage({ scope = "video" }: { scope?: SearchScope }) {
  const navigate = useNavigate();
  const search = useSearch({ strict: false }) as StudentRouteSearch;
  const isLearningScope = scope === "learning";
  const routePath = isLearningScope ? "/search" : "/video-library";
  const historyStorageKey = isLearningScope ? LEARNING_SEARCH_HISTORY_KEY : VIDEO_LIBRARY_SEARCH_HISTORY_KEY;
  const defaultSource = isLearningScope ? "chapter" : "home";
  const goBack = useDetailBack(search.from || defaultSource);
  const query = search.q || "";
  const [draft, setDraft] = useState(query);
  const [history, setHistory] = useState<string[]>(() => readVideoLibrarySearchHistory(historyStorageKey));
  const [payload, setPayload] = useState<StudentVideoLibrarySearchResponse | null>(null);
  const [homeFeedItems, setHomeFeedItems] = useState<StudentHomeVideoFeedItem[]>([]);
  const [learningPage, setLearningPage] = useState<StudentLearningPageResponse | null>(null);
  const [catalogRecords, setCatalogRecords] = useState<CatalogSearchRecord[]>([]);
  const [chapterTitle, setChapterTitle] = useState("");
  const [catalogLoading, setCatalogLoading] = useState(false);
  const [catalogError, setCatalogError] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const hasQuery = query.trim().length > 0;
  const learningProfiles = learningPage?.profiles || [];
  const activeChapterId = search.chapterId || learningPage?.active_profile?.chapter_id || "";
  const learningRootLabel = learningPage?.active_profile ? formatChapterEntryTitle(learningPage.active_profile) : chapterTitle;

  const routeSearchForQuery = (nextQuery: string) =>
    compactSearch({
      from: search.from || defaultSource,
      profileId: isLearningScope ? search.profileId || "" : "",
      chapterId: isLearningScope ? search.chapterId || activeChapterId || "" : "",
      sourceNodeId: isLearningScope ? search.sourceNodeId || "" : "",
      catalogPath: isLearningScope ? search.catalogPath || "" : "",
      elementSymbol: isLearningScope ? search.elementSymbol || "" : "",
      q: nextQuery,
    });

  useEffect(() => setDraft(query), [query]);

  useEffect(() => {
    const timer = window.setTimeout(() => {
      const nextQuery = draft.trim();
      if (nextQuery === query) return;
      void navigate({
        to: routePath,
        search: routeSearchForQuery(nextQuery),
        replace: true,
      });
    }, 240);
    return () => window.clearTimeout(timer);
  }, [draft, navigate, query, routePath, routeSearchForQuery]);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError("");
    searchStudentVideoLibrary(query)
      .then((response) => {
        if (!cancelled) setPayload(response);
      })
      .catch((requestError) => {
        if (!cancelled) setError(errorMessage(requestError));
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [query]);

  useEffect(() => {
    let cancelled = false;
    getStudentHomeVideoFeed(hasQuery ? 16 : DEFAULT_VIDEO_ROWS)
      .then((response) => {
        if (!cancelled) setHomeFeedItems(response.items || []);
      })
      .catch(() => {
        if (!cancelled) setHomeFeedItems([]);
      });
    return () => {
      cancelled = true;
    };
  }, [hasQuery]);

  useEffect(() => {
    let cancelled = false;
    getStudentLearningPage(isLearningScope ? search.profileId : undefined)
      .then((response) => {
        if (!cancelled) setLearningPage(response);
      })
      .catch(() => {
        if (!cancelled) setLearningPage(null);
      });
    return () => {
      cancelled = true;
    };
  }, [isLearningScope, search.profileId]);

  useEffect(() => {
    if (!isLearningScope || !activeChapterId) {
      setCatalogRecords([]);
      setChapterTitle("");
      setCatalogError("");
      setCatalogLoading(false);
      return;
    }
    let cancelled = false;
    setCatalogLoading(true);
    setCatalogError("");
    buildCatalogSearchIndex(activeChapterId)
      .then(({ chapter, records }) => {
        if (cancelled) return;
        setChapterTitle(chapter.chapter_title);
        setCatalogRecords(records);
      })
      .catch((requestError) => {
        if (!cancelled) setCatalogError(errorMessage(requestError));
      })
      .finally(() => {
        if (!cancelled) setCatalogLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [activeChapterId, isLearningScope]);

  const searchItems = useMemo(() => payload?.groups.flatMap((group) => group.items) || [], [payload]);
  const videoResultItems = useMemo(() => {
    const seen = new Set<string>();
    return searchItems.filter((item) => {
      const key = item.target?.node_id || item.id || item.title;
      if (!isVideoResult(item) || seen.has(key)) return false;
      seen.add(key);
      return true;
    });
  }, [searchItems]);
  const videoResults = useMemo(
    () => videoResultItems.map((item) => defaultVideoFromSearchResult(item, learningProfiles, homeFeedItems)),
    [homeFeedItems, learningProfiles, videoResultItems],
  );
  const directoryResults = useMemo(() => {
    if (!isLearningScope) return [];
    const seen = new Set<string>();
    return searchItems.filter((item) => {
      const key = item.target?.profile_id || item.target?.chapter_id || item.id || item.title;
      if (!isDirectoryResult(item) || seen.has(key)) return false;
      seen.add(key);
      return true;
    });
  }, [isLearningScope, searchItems]);
  const catalogDirectoryResults = useMemo(() => {
    if (!isLearningScope || !hasQuery) return [];
    const loweredQuery = query.trim().toLowerCase();
    const directoryById = new Map(catalogRecords.filter((record) => record.node.node_kind === "directory").map((record) => [record.node.node_id, record]));
    const seen = new Set<string>();
    const results: CatalogSearchRecord[] = [];
    catalogRecords.forEach((record) => {
      if (!catalogRecordMatches(record, loweredQuery)) return;
      const directoryRecord =
        record.node.node_kind === "directory" ? record : directoryById.get(record.breadcrumbs[record.breadcrumbs.length - 1]?.node_id || "");
      if (!directoryRecord || seen.has(directoryRecord.node.node_id)) return;
      seen.add(directoryRecord.node.node_id);
      results.push(directoryRecord);
    });
    return results.slice(0, 10);
  }, [catalogRecords, hasQuery, isLearningScope, query]);
  const defaultVideos = useMemo(() => {
    const seen = new Set<string>();
    const rows = [
      ...homeFeedItems.map((item) => defaultVideoFromFeed(item, learningProfiles)),
      ...(payload?.browse.recommended || []).map((item) => defaultVideoFromSearchResult(item, learningProfiles, homeFeedItems)),
    ].filter((item) => {
      const key = item.target?.node_id || item.target?.placement_node_id || item.title;
      if (!key || seen.has(key)) return false;
      seen.add(key);
      return true;
    });
    return rows.slice(0, DEFAULT_VIDEO_ROWS);
  }, [homeFeedItems, learningProfiles, payload?.browse.recommended]);
  const recommendedTerms = useMemo(
    () =>
      (payload?.browse.chips || [])
        .map((chip) => compactText(chip.query || chip.label))
        .filter((term, index, source) => Boolean(term) && source.indexOf(term) === index)
        .slice(0, 6),
    [payload?.browse.chips],
  );
  const visibleHistory = history.slice(0, DEFAULT_HISTORY_ROWS);
  const showDefaultBrowse =
    !hasQuery && !error && (defaultVideos.length > 0 || recommendedTerms.length > 0 || visibleHistory.length > 0 || (!loading && Boolean(payload)));
  const showLoadingState = loading && hasQuery && !payload;
  const showErrorState = Boolean(error) && (hasQuery || defaultVideos.length === 0);
  const showPayloadBanner = Boolean(payload?.message && payload.status !== "ok" && payload.status !== "empty");

  const submitSearch = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const nextQuery = draft.trim();
    setHistory(rememberVideoLibrarySearchQuery(historyStorageKey, nextQuery));
    void navigate({
      to: routePath,
      search: routeSearchForQuery(nextQuery),
      replace: false,
    });
  };

  const useQuery = (nextQuery: string) => {
    const text = compactText(nextQuery);
    setDraft(text);
    setHistory(rememberVideoLibrarySearchQuery(historyStorageKey, text));
    void navigate({
      to: routePath,
      search: routeSearchForQuery(text),
      replace: true,
    });
  };

  const openTarget = (target: StudentVideoLibraryRouteTarget | null | undefined, title: string, contextItem?: StudentVideoLibraryResultItem) => {
    if (!target) return;
    const openSource = isLearningScope ? "search" : "video-library";
    if (target.kind === "point_detail" && target.node_id) {
      navigateToPoint(navigate, target.node_id, {
        from: openSource,
        profileId: target.profile_id,
        chapterId: target.chapter_id,
        sourceNodeId: target.source_node_id,
        catalogPath: target.catalog_path?.join(" / "),
        propertyKey: target.property_key,
        propertyTitle: target.property_title,
        elementSymbol: target.element_symbol,
        pointTitle: target.point_title || title,
      });
      return;
    }
    if (target.kind === "chapter_detail" && target.profile_id) {
      navigateToChapter(navigate, target.profile_id, {
        from: openSource,
        propertyKey: target.property_key,
        elementSymbol: target.element_symbol,
      });
      return;
    }
    if (target.kind === "ai_chat") {
      navigateToAiChat(
        navigate,
        aiContextFromResult(
          contextItem || {
            id: title,
            type: "ai_prompt",
            title,
            subtitle: target.context_title || "",
            snippet: target.context_summary || "",
            score: 0,
            badges: [],
            action_label: "问问Atom",
            target,
          },
          target,
        ),
        openSource,
      );
    }
  };

  const openResult = (item: StudentVideoLibraryResultItem) => {
    if (hasQuery) setHistory(rememberVideoLibrarySearchQuery(historyStorageKey, query));
    openTarget(item.target, item.title, item);
  };

  const openDefaultVideo = (item: VideoLibraryDefaultVideo) => {
    openTarget(item.target, item.title);
  };

  const openSearchVideo = (item: VideoLibraryDefaultVideo) => {
    if (hasQuery) setHistory(rememberVideoLibrarySearchQuery(historyStorageKey, query));
    openTarget(item.target, item.title);
  };

  const openCatalogRecord = (record: CatalogSearchRecord) => {
    const path = catalogRecordPath(record);
    navigateToCatalogNode(navigate, record.node.node_id, {
      from: "search",
      profileId: search.profileId,
      chapterId: record.node.chapter_id || activeChapterId,
      catalogPath: path,
      elementSymbol: search.elementSymbol,
    });
  };

  return (
    <section className="video-library-shell" aria-label="实验视频库">
      <header className="video-library-header">
        <form className="video-library-search" role="search" onSubmit={submitSearch}>
          <button className="video-library-back" type="button" aria-label="返回" onClick={goBack}>
            <BackArrowIcon />
          </button>
          <div className="video-library-search-pill">
            <input
              type="search"
              value={draft}
              onChange={(event) => setDraft(event.currentTarget.value)}
              placeholder="搜实验现象、试剂、点位"
              aria-label="搜索实验视频库"
            />
            {draft ? (
              <button className="video-library-clear" type="button" aria-label="清空搜索" onClick={() => setDraft("")}>
                <X size={22} />
              </button>
            ) : null}
          </div>
        </form>
      </header>
      <section className="video-library-page" aria-label="实验视频库">
        {showPayloadBanner ? <div className={`video-library-banner ${payload?.status}`}>{payload?.message}</div> : null}
        {showLoadingState ? <LearningState icon={<LoaderCircle className="spin" size={23} />} text="正在检索实验视频库" /> : null}
        {showErrorState ? <LearningState icon={<FlaskConical size={23} />} text={error} /> : null}

        {showDefaultBrowse ? (
          <DefaultBrowse
            history={visibleHistory}
            recommendedVideos={defaultVideos}
            recommendedTerms={recommendedTerms}
            onUseQuery={useQuery}
            onOpenVideo={openDefaultVideo}
          />
        ) : null}

        {!loading && !error && payload && hasQuery ? (
          <SearchResults
            query={query.trim()}
            scope={scope}
            videoResults={videoResults}
            directoryResults={directoryResults}
            catalogDirectoryResults={catalogDirectoryResults}
            catalogLoading={catalogLoading}
            catalogError={catalogError}
            learningRootLabel={learningRootLabel}
            onOpenVideo={openSearchVideo}
            onOpenDirectory={openResult}
            onOpenCatalogRecord={openCatalogRecord}
          />
        ) : null}
      </section>
    </section>
  );
}

function SearchResults({
  query,
  scope,
  videoResults,
  directoryResults,
  catalogDirectoryResults,
  catalogLoading,
  catalogError,
  learningRootLabel,
  onOpenVideo,
  onOpenDirectory,
  onOpenCatalogRecord,
}: {
  query: string;
  scope: SearchScope;
  videoResults: VideoLibraryDefaultVideo[];
  directoryResults: StudentVideoLibraryResultItem[];
  catalogDirectoryResults: CatalogSearchRecord[];
  catalogLoading: boolean;
  catalogError: string;
  learningRootLabel: string;
  onOpenVideo: (item: VideoLibraryDefaultVideo) => void;
  onOpenDirectory: (item: StudentVideoLibraryResultItem) => void;
  onOpenCatalogRecord: (record: CatalogSearchRecord) => void;
}) {
  const isLearningScope = scope === "learning";
  const hasDirectoryResults = directoryResults.length > 0 || catalogDirectoryResults.length > 0;
  const hasAnyResults = videoResults.length > 0 || hasDirectoryResults;
  const heading = isLearningScope ? `关于“${query}”的学习结果` : `关于“${query}”的实验视频`;

  return (
    <section className="video-library-results" aria-live="polite" aria-label={isLearningScope ? "学习搜索结果" : "实验视频搜索结果"}>
      <div className="video-library-query-head">
        <h3>{heading}</h3>
      </div>

      {isLearningScope && (hasDirectoryResults || catalogLoading || catalogError) ? (
        <section className="video-library-result-section" aria-label="目录结果">
          <h4>目录结果</h4>
          {directoryResults.length || catalogDirectoryResults.length ? (
            <div className="video-library-row-list">
              {directoryResults.map((item) => (
                <DirectoryResultRow
                  key={item.id}
                  title={item.title}
                  subtitle={compactCatalogPath(item.target?.catalog_path) || item.subtitle || item.snippet}
                  onClick={() => onOpenDirectory(item)}
                />
              ))}
              {catalogDirectoryResults.map((record) => (
                <DirectoryResultRow
                  key={record.node.node_id}
                  title={record.node.title}
                  subtitle={catalogRecordPath(record)}
                  eyebrow={catalogRecordParentLabel(record, learningRootLabel || "学习目录")}
                  onClick={() => onOpenCatalogRecord(record)}
                />
              ))}
            </div>
          ) : catalogLoading ? (
            <div className="video-library-inline-state">
              <LoaderCircle className="spin" size={17} />
              <span>正在检索目录</span>
            </div>
          ) : catalogError ? (
            <div className="video-library-inline-state">
              <FolderOpen size={17} />
              <span>{catalogError}</span>
            </div>
          ) : null}
        </section>
      ) : null}

      {videoResults.length ? (
        <section className="video-library-result-section" aria-label="实验视频">
          {isLearningScope ? <h4>实验视频</h4> : null}
          <div className="video-library-row-list">
            {videoResults.map((item) => (
              <SearchVideoRow key={item.id} item={item} onClick={() => onOpenVideo(item)} />
            ))}
          </div>
        </section>
      ) : null}

      {!hasAnyResults && !catalogLoading ? (
        <p className="video-library-simple-empty">这里什么都没有哦👀</p>
      ) : null}
    </section>
  );
}

function SearchVideoRow({ item, onClick }: { item: VideoLibraryDefaultVideo; onClick: () => void }) {
  const path = item.subtitle || item.snippet || "实验视频";
  return (
    <button className={`video-library-search-video-row${item.thumbnailUrl ? " has-cover" : ""}`} type="button" onClick={onClick} disabled={!item.target}>
      <span className="video-library-row-icon">
        <Video size={25} />
      </span>
      <span className="video-library-row-copy">
        <strong>{item.title}</strong>
        <small>{path}</small>
        {item.chapterLabel ? <span className="video-library-row-chapter-tag">{item.chapterLabel}</span> : null}
      </span>
      {item.thumbnailUrl ? (
        <span className="video-library-row-cover" aria-hidden="true">
          <img src={item.thumbnailUrl} alt="" loading="lazy" />
        </span>
      ) : null}
      <ArrowUpLeft className="video-library-row-arrow" size={27} />
    </button>
  );
}

function DirectoryResultRow({
  title,
  subtitle,
  eyebrow,
  onClick,
}: {
  title: string;
  subtitle: string;
  eyebrow?: string;
  onClick: () => void;
}) {
  return (
    <button className="video-library-directory-row" type="button" onClick={onClick}>
      <span className="video-library-row-icon">
        <FolderOpen size={25} />
      </span>
      <span className="video-library-row-copy">
        <strong>{title}</strong>
        <small>{subtitle || eyebrow || "学习目录"}</small>
        {eyebrow && subtitle !== eyebrow ? <span className="video-library-row-chapter-tag">{eyebrow}</span> : null}
      </span>
      <ChevronRight className="video-library-row-arrow" size={23} />
    </button>
  );
}

function DefaultBrowse({
  history,
  recommendedVideos,
  recommendedTerms,
  onUseQuery,
  onOpenVideo,
}: {
  history: string[];
  recommendedVideos: VideoLibraryDefaultVideo[];
  recommendedTerms: string[];
  onUseQuery: (query: string) => void;
  onOpenVideo: (item: VideoLibraryDefaultVideo) => void;
}) {
  const showTerms = recommendedTerms.length > 0 && recommendedVideos.length < MIN_VIDEO_ROWS_BEFORE_HIDING_TERMS;
  return (
    <section className="video-library-default">
      {history.length ? (
        <section className="video-library-default-section" aria-label="搜索历史">
          <div className="video-library-simple-head">
            <h3>历史记录</h3>
          </div>
          <div className="video-library-row-list">
            {history.map((item) => (
              <button className="video-library-query-row" key={item} type="button" onClick={() => onUseQuery(item)}>
                <History size={27} />
                <span>{item}</span>
                <ArrowUpLeft size={27} />
              </button>
            ))}
          </div>
        </section>
      ) : null}

      {recommendedVideos.length ? (
        <section className="video-library-default-section" aria-label="推荐视频">
          <div className="video-library-simple-head">
            <h3>推荐视频</h3>
          </div>
          <div className="video-library-row-list">
            {recommendedVideos.map((item) => (
              <RecommendedVideoRow key={item.id} item={item} onClick={() => onOpenVideo(item)} />
            ))}
          </div>
        </section>
      ) : null}

      {showTerms ? (
        <section className="video-library-default-section" aria-label="推荐搜索">
          <div className="video-library-simple-head">
            <h3>推荐搜索</h3>
          </div>
          <div className="video-library-row-list">
            {recommendedTerms.map((item) => (
              <button className="video-library-query-row" key={item} type="button" onClick={() => onUseQuery(item)}>
                <Search size={27} />
                <span>{item}</span>
                <ArrowUpLeft size={27} />
              </button>
            ))}
          </div>
        </section>
      ) : null}

      {!recommendedVideos.length && !recommendedTerms.length ? (
        <MobileEmptyState className="empty-learning-card" icon={<FlaskConical size={20} />}>
            <span>暂无可展示的实验视频内容。</span>
        </MobileEmptyState>
      ) : null}
    </section>
  );
}

function RecommendedVideoRow({ item, onClick }: { item: VideoLibraryDefaultVideo; onClick: () => void }) {
  const path = item.subtitle || item.snippet || "实验视频";
  return (
    <button className={`video-library-recommend-row${item.thumbnailUrl ? " has-cover" : ""}`} type="button" onClick={onClick} disabled={!item.target}>
      <span className="video-library-row-icon">
        <Video size={25} />
      </span>
      <span className="video-library-row-copy">
        <strong>{item.title}</strong>
        <small>{path}</small>
        {item.chapterLabel ? <span className="video-library-row-chapter-tag">{item.chapterLabel}</span> : null}
      </span>
      {item.thumbnailUrl ? (
        <span className="video-library-row-cover" aria-hidden="true">
          <img src={item.thumbnailUrl} alt="" loading="lazy" />
        </span>
      ) : null}
      <ArrowUpLeft className="video-library-row-arrow" size={27} />
    </button>
  );
}

function VideoResultButton({ item, onClick }: { item: StudentVideoLibraryResultItem; onClick: () => void }) {
  const icon = item.type === "ai_prompt" ? <Atom size={20} /> : item.type === "chapter_experiment" ? <FlaskConical size={20} /> : <Video size={20} />;
  const actionLabel = item.type === "ai_prompt" ? "问问Atom" : item.action_label || "打开";
  return (
    <button className="video-result-card" type="button" onClick={onClick} disabled={!item.target}>
      <span className="video-result-icon">{icon}</span>
      <span className="video-result-copy">
        <strong>{item.title}</strong>
        {item.subtitle ? <small>{item.subtitle}</small> : null}
        {item.snippet ? <em>{item.snippet}</em> : null}
        {item.badges.length ? (
          <span className="video-result-badges">
            {item.badges.slice(0, 3).map((badge) => (
              <b key={badge}>{badge}</b>
            ))}
          </span>
        ) : null}
      </span>
      <span className="video-result-action">
        <small>{actionLabel}</small>
        <ChevronRight size={17} />
      </span>
    </button>
  );
}
