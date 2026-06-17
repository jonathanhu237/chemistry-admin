import { useMemo, useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { App as AntApp, Button, Card, Empty, Select, Space, Statistic, Table, Tooltip, Typography } from "antd";
import type { TableColumnsType } from "antd";

import { api, apiBase, getAuthToken } from "../../api";
import type { AnalyticsDashboard, ClassItem, Experiment } from "../../api";
import { PageTitle } from "../../components/PageTitle";
import { QueryState } from "../../components/QueryState";

const { Text } = Typography;

type MatrixRow = AnalyticsDashboard["matrix"][number];

export function AnalyticsPage() {
  const { message } = AntApp.useApp();
  const classes = useQuery({ queryKey: ["classes"], queryFn: () => api<ClassItem[]>("/api/admin/classes") });
  const [classId, setClassId] = useState<string>();
  const activeClassId = classId || classes.data?.[0]?.id;
  const dashboard = useQuery({
    queryKey: ["analytics-dashboard", activeClassId],
    queryFn: () => api<AnalyticsDashboard>(`/api/admin/analytics/classes/${activeClassId}/dashboard`),
    enabled: Boolean(activeClassId),
  });

  const exportReport = async () => {
    if (!activeClassId) return;
    const response = await fetch(`${apiBase}/api/admin/analytics/classes/${activeClassId}/export`, {
      headers: { Authorization: `Bearer ${getAuthToken()}` },
    });
    if (!response.ok) {
      message.error("导出失败");
      return;
    }
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `class-${activeClassId}-experiment-mastery.csv`;
    link.click();
    URL.revokeObjectURL(url);
  };

  const matrixColumns: TableColumnsType<MatrixRow> = useMemo(() => {
    const experiments = dashboard.data?.experiments || [];
    return [
      {
        title: "学生",
        dataIndex: "student_name",
        fixed: "left",
        width: 190,
        render: (_value: unknown, row: MatrixRow) => (
          <Space orientation="vertical" size={1} className="analytics-student-cell">
            <Text strong>{row.student_name || row.student_id}</Text>
            <Text type="secondary">{row.student_id}</Text>
          </Space>
        ),
      },
      {
        title: "均分",
        dataIndex: "average_score",
        fixed: "left",
        width: 92,
        sorter: (a: MatrixRow, b: MatrixRow) => (a.average_score || 0) - (b.average_score || 0),
        render: (value: number | undefined) => <ScorePill score={value ?? 0} />,
      },
      ...experiments.map((experiment) => ({
        title: <ExperimentColumnTitle experiment={experiment} />,
        width: 154,
        align: "center" as const,
        render: (_value: unknown, row: MatrixRow) => (
          <ScorePill
            score={row.experiments[experiment.id]?.mastery_score ?? 50}
            muted={!row.experiments[experiment.id]?.has_mastery}
            evidenceCount={row.experiments[experiment.id]?.evidence_count}
          />
        ),
      })),
    ];
  }, [dashboard.data?.experiments]);

  const experimentCount = dashboard.data?.experiments.length || 0;
  const tableScrollX = Math.max(980, 282 + experimentCount * 154);

  return (
    <Space orientation="vertical" size={18} className="full analytics-page">
      <PageTitle
        title="学情分析"
        description="班级实验分数总览"
        extra={<Button onClick={() => void exportReport()}>导出分数</Button>}
      />
      <Card className="analytics-toolbar-card">
        <Space wrap size={12}>
          <Select
            placeholder="选择班级"
            style={{ width: 280 }}
            value={activeClassId}
            onChange={(value) => setClassId(value)}
            options={(classes.data || []).map((item) => ({ value: item.id, label: item.class_name }))}
          />
          <Text type="secondary">未答题实验按 50 分计入。</Text>
        </Space>
      </Card>
      <QueryState loading={dashboard.isLoading} error={dashboard.error} empty={!activeClassId}>
        <div className="stat-grid analytics-stat-grid">
          <Card>
            <Statistic title="班级人数" value={dashboard.data?.metrics.class_size || 0} />
          </Card>
          <Card>
            <Statistic title="班级均分" value={dashboard.data?.metrics.average_score || 0} precision={1} suffix="分" />
          </Card>
          <Card>
            <Statistic title="实验数量" value={dashboard.data?.metrics.published_experiments || 0} />
          </Card>
          <Card>
            <Statistic title="已有答题学生" value={dashboard.data?.metrics.active_students || 0} />
          </Card>
        </div>
        <Card
          title="学生实验分数"
          extra={<Text type="secondary">{dashboard.data?.matrix.length || 0} 名学生</Text>}
          className="analytics-matrix-card"
        >
          <Table
            rowKey="student_id"
            size="small"
            scroll={{ x: tableScrollX, y: "calc(100vh - 390px)" }}
            dataSource={dashboard.data?.matrix || []}
            columns={matrixColumns}
            pagination={{ pageSize: 20, showSizeChanger: false }}
            locale={{ emptyText: <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description="暂无学生" /> }}
          />
        </Card>
      </QueryState>
    </Space>
  );
}

function ExperimentColumnTitle({ experiment }: { experiment: Experiment }) {
  const family = experimentFamily(experiment);
  const title = cleanExperimentTitle(experiment.title);
  return (
    <Tooltip title={`${family ? `${family} / ` : ""}${title}`}>
      <div className="analytics-experiment-title">
        <strong>{title}</strong>
        <span>{family || experiment.code}</span>
      </div>
    </Tooltip>
  );
}

function ScorePill({
  score,
  muted = false,
  evidenceCount = 0,
}: {
  score: number;
  muted?: boolean;
  evidenceCount?: number;
}) {
  const title = muted ? "暂无答题证据，按默认 50 分计入" : `答题证据 ${evidenceCount} 条`;
  return (
    <Tooltip title={title}>
      <span className={`analytics-score-pill ${scoreTone(score)} ${muted ? "is-default" : ""}`}>{formatScore(score)}</span>
    </Tooltip>
  );
}

function formatScore(value: number) {
  return Number.isInteger(value) ? String(value) : value.toFixed(1);
}

function scoreTone(value: number) {
  if (value < 40) return "score-low";
  if (value < 60) return "score-watch";
  if (value < 80) return "score-steady";
  return "score-high";
}

function cleanExperimentTitle(value: string) {
  return value.replace(/^实验\s*\d+-\d+\s*/, "").trim();
}

function experimentFamily(experiment: Experiment) {
  const metadata = experiment.metadata || {};
  const parentTitle = typeof metadata.parent_title === "string" ? metadata.parent_title : "";
  return cleanExperimentTitle(parentTitle);
}
