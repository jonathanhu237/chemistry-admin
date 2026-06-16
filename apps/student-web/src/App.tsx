import { FormEvent, useEffect, useMemo, useState } from "react";
import {
  CheckCircle2,
  FlaskConical,
  LoaderCircle,
  LockKeyhole,
  LogIn,
  LogOut,
  ShieldCheck,
  UserRound,
} from "lucide-react";
import logoUrl from "./assets/sysu-logo.svg";
import {
  AuthUser,
  LoginResponse,
  changeStudentPassword,
  errorMessage,
  getAuthToken,
  loadCurrentUser,
  logout,
  setAuthToken,
  studentLogin,
} from "./api";

type ViewState = "checking" | "login" | "password" | "home";

function normalizeStudentId(value: string): string {
  return value.trim().toUpperCase();
}

function isStudent(response: LoginResponse): boolean {
  return response.user.role === "student";
}

function App() {
  const [user, setUser] = useState<AuthUser | null>(null);
  const [checking, setChecking] = useState(true);
  const [sessionError, setSessionError] = useState("");

  useEffect(() => {
    if (!getAuthToken()) {
      setChecking(false);
      return;
    }
    loadCurrentUser()
      .then((currentUser) => {
        if (currentUser.role !== "student") {
          setAuthToken("");
          setSessionError("请使用学生账号登录");
          return;
        }
        setUser(currentUser);
      })
      .catch(() => {
        setAuthToken("");
      })
      .finally(() => setChecking(false));
  }, []);

  const view: ViewState = useMemo(() => {
    if (checking) return "checking";
    if (!user) return "login";
    if (user.must_change_password) return "password";
    return "home";
  }, [checking, user]);

  const acceptLogin = (response: LoginResponse) => {
    if (!isStudent(response)) {
      setAuthToken("");
      setSessionError("请使用学生账号登录");
      return;
    }
    setSessionError("");
    setAuthToken(response.access_token);
    setUser(response.user);
  };

  const handleLogout = async () => {
    await logout();
    setUser(null);
  };

  return (
    <main className="app-shell">
      <section className="brand-rail" aria-label="中山大学化学学院">
        <div className="brand-seal">
          <img src={logoUrl} alt="中山大学校徽" />
        </div>
        <div>
          <p>中山大学化学学院</p>
          <h1>元素实验</h1>
        </div>
      </section>

      {view === "checking" ? <LoadingPanel /> : null}
      {view === "login" ? <LoginPanel sessionError={sessionError} onLogin={acceptLogin} /> : null}
      {view === "password" && user ? <PasswordPanel user={user} onChanged={acceptLogin} /> : null}
      {view === "home" && user ? <HomePanel user={user} onLogout={handleLogout} /> : null}
    </main>
  );
}

function LoadingPanel() {
  return (
    <section className="auth-panel compact-panel" aria-live="polite">
      <LoaderCircle className="spin" size={24} />
      <p>正在恢复登录状态</p>
    </section>
  );
}

function LoginPanel({
  sessionError,
  onLogin,
}: {
  sessionError: string;
  onLogin: (response: LoginResponse) => void;
}) {
  const [studentId, setStudentId] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(sessionError);

  useEffect(() => setError(sessionError), [sessionError]);

  const submit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const normalizedId = normalizeStudentId(studentId);
    if (!normalizedId || !password) return;
    setLoading(true);
    setError("");
    try {
      const response = await studentLogin(normalizedId, password);
      onLogin(response);
    } catch (requestError) {
      setError(errorMessage(requestError));
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="auth-panel">
      <div className="panel-heading">
        <span className="panel-icon">
          <UserRound size={19} />
        </span>
        <div>
          <p>学生入口</p>
          <h2>学号登录</h2>
        </div>
      </div>

      <form onSubmit={submit} className="auth-form">
        <label>
          <span>学号</span>
          <input
            value={studentId}
            onChange={(event) => setStudentId(event.target.value)}
            placeholder="请输入学号"
            autoComplete="username"
            inputMode="text"
          />
        </label>
        <label>
          <span>密码</span>
          <input
            value={password}
            onChange={(event) => setPassword(event.target.value)}
            placeholder="请输入密码"
            type="password"
            autoComplete="current-password"
          />
        </label>
        {error ? <div className="form-error">{error}</div> : null}
        <button className="primary-action" type="submit" disabled={loading || !studentId.trim() || !password}>
          {loading ? <LoaderCircle className="spin" size={18} /> : <LogIn size={18} />}
          <span>{loading ? "正在登录" : "登录"}</span>
        </button>
      </form>
    </section>
  );
}

function PasswordPanel({ user, onChanged }: { user: AuthUser; onChanged: (response: LoginResponse) => void }) {
  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const canSubmit = Boolean(currentPassword) && newPassword.length >= 8 && newPassword === confirmPassword;

  const submit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!canSubmit) return;
    setLoading(true);
    setError("");
    try {
      const response = await changeStudentPassword(currentPassword, newPassword);
      onChanged(response);
    } catch (requestError) {
      setError(errorMessage(requestError));
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="auth-panel">
      <div className="panel-heading">
        <span className="panel-icon warning">
          <LockKeyhole size={19} />
        </span>
        <div>
          <p>{user.student_id || user.username}</p>
          <h2>修改初始密码</h2>
        </div>
      </div>

      <form onSubmit={submit} className="auth-form">
        <label>
          <span>当前密码</span>
          <input
            value={currentPassword}
            onChange={(event) => setCurrentPassword(event.target.value)}
            placeholder="首次登录为初始密码"
            type="password"
            autoComplete="current-password"
          />
        </label>
        <label>
          <span>新密码</span>
          <input
            value={newPassword}
            onChange={(event) => setNewPassword(event.target.value)}
            placeholder="至少 8 位"
            type="password"
            autoComplete="new-password"
          />
        </label>
        <label>
          <span>确认新密码</span>
          <input
            value={confirmPassword}
            onChange={(event) => setConfirmPassword(event.target.value)}
            placeholder="再次输入新密码"
            type="password"
            autoComplete="new-password"
          />
        </label>
        {newPassword && newPassword.length < 8 ? <div className="form-hint">新密码至少 8 位</div> : null}
        {confirmPassword && newPassword !== confirmPassword ? <div className="form-hint">两次输入的新密码不一致</div> : null}
        {error ? <div className="form-error">{error}</div> : null}
        <button className="primary-action" type="submit" disabled={loading || !canSubmit}>
          {loading ? <LoaderCircle className="spin" size={18} /> : <ShieldCheck size={18} />}
          <span>{loading ? "正在保存" : "保存并继续"}</span>
        </button>
      </form>
    </section>
  );
}

function HomePanel({ user, onLogout }: { user: AuthUser; onLogout: () => void }) {
  return (
    <section className="auth-panel success-panel">
      <div className="success-mark">
        <CheckCircle2 size={30} />
      </div>
      <div className="success-copy">
        <p>登录已完成</p>
        <h2>{user.display_name}</h2>
      </div>
      <div className="student-summary">
        <div>
          <span>学号</span>
          <strong>{user.student_id || user.username}</strong>
        </div>
        <div>
          <span>班级</span>
          <strong>{user.class_name || "未绑定"}</strong>
        </div>
      </div>
      <div className="next-banner">
        <FlaskConical size={20} />
        <span>学习页面即将接入</span>
      </div>
      <button className="secondary-action" type="button" onClick={onLogout}>
        <LogOut size={18} />
        <span>退出登录</span>
      </button>
    </section>
  );
}

export default App;
