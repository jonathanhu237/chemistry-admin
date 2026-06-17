import {
  ButtonHTMLAttributes,
  InputHTMLAttributes,
  ReactNode,
  TextareaHTMLAttributes,
  useCallback,
  useState,
} from "react";

export type FloatingOverlay = "assistant" | "feedback" | "dialog" | "sheet" | null;
export type FloatingOverlayKind = Exclude<FloatingOverlay, null>;

type ButtonVariant = "primary" | "secondary" | "ghost";

function cx(...values: Array<string | false | null | undefined>): string {
  return values.filter(Boolean).join(" ");
}

export function useFloatingOverlayState(initial: FloatingOverlay = null) {
  const [activeOverlay, setActiveOverlay] = useState<FloatingOverlay>(initial);

  const toggleOverlay = useCallback((overlay: FloatingOverlayKind, open: boolean) => {
    setActiveOverlay(open ? overlay : null);
  }, []);

  const resetOverlay = useCallback(() => {
    setActiveOverlay(null);
  }, []);

  return {
    activeOverlay,
    setActiveOverlay,
    toggleOverlay,
    resetOverlay,
  };
}

export function MobileButton({
  variant = "primary",
  fullWidth = true,
  loading = false,
  className,
  children,
  disabled,
  ...props
}: ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: ButtonVariant;
  fullWidth?: boolean;
  loading?: boolean;
}) {
  return (
    <button
      className={cx("mobile-button", `mobile-button--${variant}`, fullWidth && "mobile-button--full", className)}
      disabled={disabled || loading}
      {...props}
    >
      {children}
    </button>
  );
}

export function MobileIconButton({ className, ...props }: ButtonHTMLAttributes<HTMLButtonElement>) {
  return <button className={cx("mobile-icon-button", className)} {...props} />;
}

export function MobileField({ className, ...props }: InputHTMLAttributes<HTMLInputElement>) {
  return <input className={cx("mobile-field", className)} {...props} />;
}

export function MobileTextArea({ className, ...props }: TextareaHTMLAttributes<HTMLTextAreaElement>) {
  return <textarea className={cx("mobile-textarea", className)} {...props} />;
}

export function MobileStatus({
  icon,
  text,
  tone = "neutral",
  className,
}: {
  icon: ReactNode;
  text: ReactNode;
  tone?: "neutral" | "error" | "empty";
  className?: string;
}) {
  return (
    <div className={cx("mobile-status", `mobile-status--${tone}`, className)} aria-live={tone === "error" ? "assertive" : "polite"}>
      {icon}
      <span>{text}</span>
    </div>
  );
}

export function MobileEmptyState({
  icon,
  children,
  className,
}: {
  icon?: ReactNode;
  children: ReactNode;
  className?: string;
}) {
  return (
    <div className={cx("mobile-empty-state", className)}>
      {icon}
      {typeof children === "string" ? <span>{children}</span> : children}
    </div>
  );
}

export function MobileFloatingOverlay({
  family,
  open,
  className,
  children,
}: {
  family: FloatingOverlayKind;
  open: boolean;
  className?: string;
  children: ReactNode;
}) {
  return (
    <aside
      className={cx("mobile-floating-overlay", `mobile-floating-overlay--${family}`, open && "open", className)}
      data-overlay-family={family}
      data-overlay-open={open ? "true" : "false"}
    >
      {children}
    </aside>
  );
}
