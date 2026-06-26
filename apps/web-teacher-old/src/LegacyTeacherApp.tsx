import { FormEvent, type ReactNode, useEffect, useState } from "react";

import {
  createQuestionWorkbenchSession,
  getAnalyticsDashboard,
  getAuthToken,
  legacyTeacherErrorMessage,
  listLegacyVideoPoints,
  listCatalogQuestionBank,
  listClasses,
  listExperiments,
  listQuestionBanks,
  loadCurrentUser,
  setLegacyVideoPointRecommendation,
  setAuthToken,
  teacherLogin,
  type AnalyticsDashboard,
  type CatalogQuestionBankNode,
  type ClassItem,
  type Experiment,
  type LegacyVideoPointItem,
  type QuestionBankSummary,
  type User,
} from "./api";

const logoSrc = `${import.meta.env.BASE_URL}assets/sysu-lockup-red.svg`;
const emblemSrc = `${import.meta.env.BASE_URL}assets/sysu-emblem-red.svg`;
const forbiddenPathSegments = ["/learning-assistant", "/ai-config", "/monitoring", "/rag", "/agent", "/provider", "/web-admin"];

type RouteKey = "overview" | "experiments" | "recommend" | "question-bank" | "scores";

function currentPath(): string {
  return window.location.pathname || "/";
}

function navigate(path: string): void {
  window.history.pushState({}, "", path);
  window.dispatchEvent(new Event("popstate"));
}

function usePath(): string {
  const [path, setPath] = useState(currentPath);
  useEffect(() => {
    const update = () => setPath(currentPath());
    window.addEventListener("popstate", update);
    return () => window.removeEventListener("popstate", update);
  }, []);
  return path;
}

function isForbiddenPath(path: string): boolean {
  return forbiddenPathSegments.some((segment) => path.startsWith(segment));
}

function routeFromPath(path: string): RouteKey {
  if (path.startsWith("/experiments")) return "experiments";
  if (path.startsWith("/recommend")) return "recommend";
  if (path.startsWith("/question-bank")) return "question-bank";
  if (path.startsWith("/scores")) return "scores";
  return "overview";
}

export function LegacyTeacherApp() {
  const path = usePath();
  const [user, setUser] = useState<User | null>(null);
  const [checkingSession, setCheckingSession] = useState(Boolean(getAuthToken()));

  useEffect(() => {
    if (!getAuthToken()) return;
    let active = true;
    setCheckingSession(true);
    loadCurrentUser()
      .then((value) => {
        if (active && (value.role === "admin" || value.role === "teacher")) setUser(value);
      })
      .catch(() => {
        if (active) setUser(null);
      })
      .finally(() => {
        if (active) setCheckingSession(false);
      });
    return () => {
      active = false;
    };
  }, []);

  useEffect(() => {
    if (isForbiddenPath(path)) navigate("/");
  }, [path]);

  if (checkingSession) {
    return <div className="legacy-teacher-loading">正在载入教师端...</div>;
  }

  if (!user) return <LoginScreen onLogin={setUser} />;

  const activeRoute = routeFromPath(isForbiddenPath(path) ? "/" : path);

  return (
    <div className="legacy-teacher-shell">
      <aside className="legacy-sidebar">
        <img src={emblemSrc} alt="" className="legacy-sidebar-emblem" />
        <img src={logoSrc} alt="中山大学" className="legacy-sidebar-logo" />
        <strong>无机化学实验教学平台</strong>
        <nav aria-label="旧版教师导航">
          <NavButton active={activeRoute === "overview"} label="工作台" path="/" />
          <NavButton active={activeRoute === "experiments"} label="实验资源" path="/experiments" />
          <NavButton active={activeRoute === "recommend"} label="推荐学习" path="/recommend" />
          <NavButton active={activeRoute === "question-bank"} label="AI出题与题库" path="/question-bank" />
          <NavButton active={activeRoute === "scores"} label="学情分数" path="/scores" />
        </nav>
      </aside>
      <div className="legacy-teacher-main">
        <header className="legacy-teacher-header">
          <div>
            <span>BKT 教学管理工作台</span>
            <strong>{user.display_name || user.username}</strong>
          </div>
          <button
            className="text-button"
            onClick={() => {
              setAuthToken("");
              window.location.assign("/");
            }}
          >
            退出
          </button>
        </header>
        {activeRoute === "experiments" ? (
          <ExperimentsPage />
        ) : activeRoute === "recommend" ? (
          <RecommendLearningPage />
        ) : activeRoute === "question-bank" ? (
          <QuestionBankPage />
        ) : activeRoute === "scores" ? (
          <ScoresPage />
        ) : (
          <OverviewPage />
        )}
      </div>
    </div>
  );
}

function NavButton({ active, label, path }: { active: boolean; label: string; path: string }) {
  return (
    <button className={active ? "active" : ""} onClick={() => navigate(path)}>
      {label}
    </button>
  );
}

function LoginScreen({ onLogin }: { onLogin: (user: User) => void }) {
  const [username, setUsername] = useState("admin");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  const submit = async (event: FormEvent) => {
    event.preventDefault();
    setSubmitting(true);
    setError("");
    try {
      const response = await teacherLogin(username, password);
      if (response.user.role !== "admin" && response.user.role !== "teacher") {
        throw new Error("该账号不能进入教师端。");
      }
      setAuthToken(response.access_token);
      onLogin(response.user);
    } catch (caught) {
      setError(legacyTeacherErrorMessage(caught));
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="legacy-teacher-login">
      <section className="legacy-teacher-login-card">
        <img src={logoSrc} alt="中山大学" />
        <span className="eyebrow">Teacher Console Classic</span>
        <h1>无机化学实验教学管理平台</h1>
        <p>围绕实验资源、AI出题、教师审核、题库建设、学生测评和 BKT 学情分数形成教学反馈闭环。</p>
        <form onSubmit={submit}>
          <label>
            账号
            <input value={username} onChange={(event) => setUsername(event.target.value)} autoComplete="username" />
          </label>
          <label>
            密码
            <input type="password" value={password} onChange={(event) => setPassword(event.target.value)} autoComplete="current-password" />
          </label>
          {error ? <div className="legacy-error">{error}</div> : null}
          <button className="primary-button" disabled={submitting}>
            {submitting ? "登录中..." : "进入教师端"}
          </button>
        </form>
      </section>
    </div>
  );
}

function OverviewPage() {
  const [experiments, setExperiments] = useState<Experiment[]>([]);
  const [classes, setClasses] = useState<ClassItem[]>([]);
  const [banks, setBanks] = useState<QuestionBankSummary[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    Promise.all([listExperiments(), listClasses(), listQuestionBanks()])
      .then(([experimentResponse, classResponse, bankResponse]) => {
        setExperiments(experimentResponse.items || []);
        setClasses(classResponse || []);
        setBanks(bankResponse.items || []);
      })
      .catch((caught) => setError(legacyTeacherErrorMessage(caught)));
  }, []);

  const questionCount = banks.reduce((sum, item) => sum + item.banks.reduce((bankSum, bank) => bankSum + Number(bank.question_count || 0), 0), 0);

  return (
    <section className="legacy-teacher-page">
      <PageHead eyebrow="BKT 闭环" title="教学工作台" description="以实验为知识单元，串起 AI出题、教师审核、学生测评、掌握度更新、视频推荐和学情分数。" />
      {error ? <div className="legacy-error">{error}</div> : null}
      <div className="legacy-metric-grid">
        <Metric label="实验资源" value={experiments.length} />
        <Metric label="班级" value={classes.length} />
        <Metric label="题库题目" value={questionCount} />
        <Metric label="核心模型" value="BKT" />
      </div>
      <div className="legacy-flow" aria-label="BKT 教学反馈闭环">
        {["教材与实验资料", "AI出题", "教师审核", "学生测评", "BKT掌握度", "视频推荐", "学情分数"].map((item) => (
          <span key={item}>{item}</span>
        ))}
      </div>
      <div className="legacy-panel-grid">
        <Panel title="实验知识图谱式导航" text="元素、元素性质、实验和视频资源按知识单元串联，比单纯章节目录更贴近无机化学实验教学。" />
        <Panel title="智能组卷依据" text="掌握度偏低、证据不足和未充分测量的实验点位会优先进入测评计划。" />
        <Panel title="教师反馈回路" text="教师查看班级与学生学情分数，定位薄弱实验点并安排复习与再测。" />
      </div>
    </section>
  );
}

function ExperimentsPage() {
  const [experiments, setExperiments] = useState<Experiment[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    listExperiments()
      .then((response) => setExperiments(response.items || []))
      .catch((caught) => setError(legacyTeacherErrorMessage(caught)));
  }, []);

  return (
    <section className="legacy-teacher-page">
      <PageHead eyebrow="实验资源" title="实验与视频资源" description="查看共享实验资源、已发布题目和待审核草稿，旧版教师端不拆分数据库或题库。" />
      {error ? <div className="legacy-error">{error}</div> : null}
      <div className="legacy-table">
        <div className="legacy-table-head cols-5">
          <span>实验</span>
          <span>状态</span>
          <span>视频</span>
          <span>已发布题</span>
          <span>待审核</span>
        </div>
        {experiments.slice(0, 40).map((item) => (
          <div className="legacy-table-row cols-5" key={item.id}>
            <span>
              <strong>{item.title}</strong>
              <small>{item.code || item.id}</small>
            </span>
            <span>{item.status}</span>
            <span>{item.media_resources?.length ?? 0}</span>
            <span>{item.published_question_count ?? 0}</span>
            <span>{Number(item.draft_question_count || 0) + Number(item.generated_draft_count || 0)}</span>
          </div>
        ))}
      </div>
    </section>
  );
}

function RecommendLearningPage() {
  const [points, setPoints] = useState<LegacyVideoPointItem[]>([]);
  const [query, setQuery] = useState("");
  const [draft, setDraft] = useState("");
  const [busyNodeId, setBusyNodeId] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const load = (nextQuery = query) => {
    setError("");
    return listLegacyVideoPoints(nextQuery)
      .then((response) => setPoints(response.items || []))
      .catch((caught) => setError(legacyTeacherErrorMessage(caught)));
  };

  useEffect(() => {
    load("");
  }, []);

  const submit = (event: FormEvent) => {
    event.preventDefault();
    const nextQuery = draft.trim();
    setQuery(nextQuery);
    load(nextQuery);
  };

  const toggleRecommendation = async (point: LegacyVideoPointItem) => {
    setError("");
    setMessage("");
    setBusyNodeId(point.node_id);
    try {
      const response = await setLegacyVideoPointRecommendation(point.node_id, !point.is_recommended, point.recommended_order ?? 0);
      setPoints(response.items || []);
      setMessage(!point.is_recommended ? `已设为推荐学习：${point.title}` : `已取消推荐学习：${point.title}`);
      setDraft("");
      setQuery("");
    } catch (caught) {
      setError(legacyTeacherErrorMessage(caught));
    } finally {
      setBusyNodeId("");
    }
  };

  return (
    <section className="legacy-teacher-page">
      <PageHead eyebrow="推荐学习" title="推荐学习点位" description="手动设置旧版学生端视频库的推荐学习点位；推荐点位会在学生端视频库优先显示，并带有推荐学习标记。" />
      {error ? <div className="legacy-error">{error}</div> : null}
      {message ? <div className="legacy-success">{message}</div> : null}
      <form className="legacy-admin-search" onSubmit={submit}>
        <input value={draft} onChange={(event) => setDraft(event.target.value)} placeholder="搜索点位、现象、试剂或目录" />
        <button className="primary-button" type="submit">
          搜索
        </button>
        {query ? (
          <button
            className="text-button"
            type="button"
            onClick={() => {
              setDraft("");
              setQuery("");
              load("");
            }}
          >
            返回全部点位
          </button>
        ) : null}
      </form>
      <div className="legacy-table legacy-recommend-table">
        <div className="legacy-table-head cols-recommend">
          <span>点位</span>
          <span>目录</span>
          <span>视频</span>
          <span>状态</span>
          <span>操作</span>
        </div>
        {points.map((point) => {
          const path = point.catalog_path?.slice(0, -1).join(" / ") || "实验视频库";
          return (
            <div className="legacy-table-row cols-recommend" key={point.node_id}>
              <span>
                <strong>{point.title}</strong>
                <small>{point.summary || point.snippet || point.node_id}</small>
              </span>
              <span>{path}</span>
              <span>{point.published_media_count || 0}</span>
              <span>{point.is_recommended ? <b className="legacy-pill">推荐学习</b> : "普通点位"}</span>
              <span>
                <button className={point.is_recommended ? "secondary-button" : "primary-button"} disabled={busyNodeId === point.node_id} onClick={() => toggleRecommendation(point)}>
                  {busyNodeId === point.node_id ? "保存中..." : point.is_recommended ? "取消推荐" : "设为推荐"}
                </button>
              </span>
            </div>
          );
        })}
        {!points.length ? <div className="legacy-empty-row">没有找到点位。</div> : null}
      </div>
    </section>
  );
}

function QuestionBankPage() {
  const [banks, setBanks] = useState<QuestionBankSummary[]>([]);
  const [nodes, setNodes] = useState<CatalogQuestionBankNode[]>([]);
  const [selectedExperimentId, setSelectedExperimentId] = useState("");
  const [prompt, setPrompt] = useState("围绕实验现象、操作安全和结论判断生成 5 道客观题。");
  const [sessionMessage, setSessionMessage] = useState("");
  const [reviewMessage, setReviewMessage] = useState("草稿生成后需教师通过、退回修改或暂不入库。");
  const [error, setError] = useState("");
  const selectedExperiment = banks.find((item) => item.id === selectedExperimentId) || banks[0];

  useEffect(() => {
    Promise.all([listQuestionBanks(), listCatalogQuestionBank()])
      .then(([bankResponse, catalogResponse]) => {
        setBanks(bankResponse.items || []);
        setNodes(catalogResponse.items || []);
        setSelectedExperimentId(bankResponse.items?.[0]?.id || "");
      })
      .catch((caught) => setError(legacyTeacherErrorMessage(caught)));
  }, []);

  const createSession = async () => {
    if (!selectedExperiment) return;
    setError("");
    setSessionMessage("");
    try {
      const session = await createQuestionWorkbenchSession({
        mode: "create",
        experiment_id: selectedExperiment.id,
        prompt,
      });
      setSessionMessage(`已创建教师审核会话：${session.id}`);
      setReviewMessage("草稿已进入教师审核，确认后才会进入学生可见题库。");
    } catch (caught) {
      setError(legacyTeacherErrorMessage(caught));
    }
  };

  return (
    <section className="legacy-teacher-page">
      <PageHead eyebrow="AI出题" title="题库建设与教师审核" description="教师选择实验或点位上下文后生成客观题草稿，再审核通过、退回修改或暂不入库。" />
      {error ? <div className="legacy-error">{error}</div> : null}
      <div className="legacy-question-layout">
        <aside className="legacy-list-panel">
          <h2>实验题库</h2>
          {banks.slice(0, 30).map((item) => (
            <button className={item.id === selectedExperiment?.id ? "active" : ""} key={item.id} onClick={() => setSelectedExperimentId(item.id)}>
              <span>{item.title}</span>
              <small>{item.banks.reduce((sum, bank) => sum + Number(bank.question_count || 0), 0)} 题</small>
            </button>
          ))}
        </aside>
        <div className="legacy-workbench">
          <section className="legacy-card">
            <span className="eyebrow">出题依据</span>
            <h2>{selectedExperiment?.title || "请选择实验"}</h2>
            <p>依据教材与实验资料生成题目草稿，教师确认后再进入学生测评与 BKT 掌握度计算。</p>
            <label>
              出题要求
              <textarea value={prompt} onChange={(event) => setPrompt(event.target.value)} />
            </label>
            <button className="primary-button" onClick={createSession} disabled={!selectedExperiment}>
              AI出题
            </button>
            {sessionMessage ? <div className="legacy-success">{sessionMessage}</div> : null}
          </section>
          <section className="legacy-card">
            <h2>教师审核</h2>
            <p>{reviewMessage}</p>
            <div className="legacy-review-actions">
              <button onClick={() => setReviewMessage("教师审核通过后，题目按共享题库规则进入学生测评。")}>通过入库</button>
              <button onClick={() => setReviewMessage("已退回修改，需补充教材依据或实验资料依据。")}>退回修改</button>
              <button onClick={() => setReviewMessage("已暂不入库，学生端不会看到该草稿。")}>暂不入库</button>
            </div>
          </section>
          <section className="legacy-card">
            <h2>点位覆盖</h2>
            <div className="legacy-table compact">
              <div className="legacy-table-head cols-4">
                <span>点位</span>
                <span>类型</span>
                <span>已发布题</span>
                <span>依据</span>
              </div>
              {nodes.slice(0, 12).map((node, index) => (
                <div className="legacy-table-row cols-4" key={node.node_id}>
                  <span>{node.title}</span>
                  <span>{node.node_kind === "point" ? "实验点" : "目录"}</span>
                  <span>{node.counts.published_count}</span>
                  <span>{index % 2 === 0 ? "教材依据" : "实验资料依据"}</span>
                </div>
              ))}
            </div>
          </section>
        </div>
      </div>
    </section>
  );
}

function ScoresPage() {
  const [classes, setClasses] = useState<ClassItem[]>([]);
  const [classId, setClassId] = useState("");
  const [dashboard, setDashboard] = useState<AnalyticsDashboard | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    listClasses()
      .then((items) => {
        setClasses(items || []);
        setClassId(items?.[0]?.id || "");
      })
      .catch((caught) => setError(legacyTeacherErrorMessage(caught)));
  }, []);

  useEffect(() => {
    if (!classId) return;
    getAnalyticsDashboard(classId)
      .then(setDashboard)
      .catch((caught) => setError(legacyTeacherErrorMessage(caught)));
  }, [classId]);

  return (
    <section className="legacy-teacher-page">
      <PageHead eyebrow="学情分数" title="BKT 班级学情" description="用学生测评和学习活动沉淀掌握度证据，帮助教师定位薄弱实验点并安排跟进。" />
      {error ? <div className="legacy-error">{error}</div> : null}
      <select value={classId} onChange={(event) => setClassId(event.target.value)} aria-label="选择班级">
        {classes.map((item) => (
          <option key={item.id} value={item.id}>
            {item.class_name}
          </option>
        ))}
      </select>
      <div className="legacy-metric-grid">
        <Metric label="学生数" value={dashboard?.metrics.class_size ?? 0} />
        <Metric label="活跃学生" value={dashboard?.metrics.active_students ?? 0} />
        <Metric label="平均分" value={(dashboard?.metrics.average_score ?? 0).toFixed(1)} />
        <Metric label="完成率" value={`${(dashboard?.metrics.completion_rate ?? 0).toFixed(1)}%`} />
      </div>
      <div className="legacy-table">
        <div className="legacy-table-head cols-4">
          <span>学生</span>
          <span>平均分</span>
          <span>掌握度证据</span>
          <span>状态</span>
        </div>
        {(dashboard?.matrix || []).slice(0, 30).map((row) => {
          const evidence = Object.values(row.experiment_groups || {}).reduce((sum, item) => sum + Number(item.evidence_count || 0), 0);
          return (
            <div className="legacy-table-row cols-4" key={row.student_id}>
              <span>
                <strong>{row.student_name || row.student_id}</strong>
                <small>{row.student_id}</small>
              </span>
              <span>{(row.average_score ?? 0).toFixed(1)}</span>
              <span>{evidence}</span>
              <span>{evidence > 0 ? "已有BKT证据" : "待测评"}</span>
            </div>
          );
        })}
      </div>
    </section>
  );
}

function PageHead({ eyebrow, title, description }: { eyebrow: string; title: string; description: string }) {
  return (
    <div className="legacy-page-head">
      <span className="eyebrow">{eyebrow}</span>
      <h1>{title}</h1>
      <p>{description}</p>
    </div>
  );
}

function Metric({ label, value }: { label: string; value: ReactNode }) {
  return (
    <div className="legacy-metric">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function Panel({ title, text }: { title: string; text: string }) {
  return (
    <article className="legacy-card">
      <h2>{title}</h2>
      <p>{text}</p>
    </article>
  );
}
