import type { ReactNode } from "react";
import { Drawer } from "antd";

import type { Experiment } from "../../../api/experiments";
import { QueryState } from "../../../components/QueryState";

export function ExperimentDetailDrawer({
  open,
  currentExperiment,
  loading,
  error,
  onClose,
  children,
}: {
  open: boolean;
  currentExperiment: Experiment | null | undefined;
  loading: boolean;
  error: unknown;
  onClose: () => void;
  children: ReactNode;
}) {
  return (
    <Drawer
      title={currentExperiment ? `编辑实验：${currentExperiment.title}` : "编辑实验"}
      open={open}
      onClose={onClose}
      size={1180}
      className="experiment-editor-drawer"
    >
      <QueryState loading={loading} error={error} empty={!currentExperiment}>
        {children}
      </QueryState>
    </Drawer>
  );
}
