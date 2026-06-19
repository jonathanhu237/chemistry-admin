import { Button, Card, Flex, Input, Select, Space, Table, Tag, Typography } from "antd";

import type { Experiment } from "../../../api/experiments";
import { QueryState } from "../../../components/QueryState";
import { statusTag } from "../../../lib/status";
import { experimentVideoCandidates, formatChapterTitle } from "../../../lib/resourceUtils";

const { Text } = Typography;

export type ExperimentStatusSummary = {
  total: number;
  draft: number;
  published: number;
  archived: number;
};

export function ExperimentListSection({
  loading,
  error,
  filteredExperiments,
  statusSummary,
  experimentKeyword,
  chapterId,
  statusFilter,
  chapterOptions,
  chapterTitleById,
  hasFilters,
  onKeywordChange,
  onChapterChange,
  onStatusChange,
  onResetFilters,
  onSelectExperiment,
}: {
  loading: boolean;
  error: unknown;
  filteredExperiments: Experiment[];
  statusSummary: ExperimentStatusSummary;
  experimentKeyword: string;
  chapterId?: string;
  statusFilter?: string;
  chapterOptions: Array<{ value: string; label: string }>;
  chapterTitleById: Map<string, string>;
  hasFilters: boolean;
  onKeywordChange: (value: string) => void;
  onChapterChange: (value?: string) => void;
  onStatusChange: (value?: string) => void;
  onResetFilters: () => void;
  onSelectExperiment: (experiment: Experiment) => void;
}) {
  return (
    <>
      <Card className="toolbar-card">
        <Space orientation="vertical" size={14} className="full">
          <Flex justify="space-between" align="center" gap={14} wrap="wrap">
            <Space size={12} wrap className="experiment-filter-controls">
              <Text className="filter-group-label">筛选范围</Text>
              <Select allowClear placeholder="全部章节" style={{ width: 300 }} value={chapterId} onChange={onChapterChange} options={chapterOptions} />
              <Select
                allowClear
                placeholder="全部状态"
                style={{ width: 160 }}
                value={statusFilter}
                onChange={onStatusChange}
                options={[
                  { value: "draft", label: "草稿" },
                  { value: "published", label: "已发布" },
                  { value: "archived", label: "已归档" },
                ]}
              />
            </Space>
            <Input.Search
              allowClear
              placeholder="搜索实验名称"
              value={experimentKeyword}
              onChange={(event) => onKeywordChange(event.target.value)}
              style={{ width: 320 }}
            />
          </Flex>
          <Flex justify="space-between" align="center" gap={14} wrap="wrap">
            <Space size={8} wrap className="experiment-filter-summary">
              {loading ? (
                <Text type="secondary">正在加载实验...</Text>
              ) : (
                <>
                  <Text type="secondary">当前范围共 {statusSummary.total} 个实验</Text>
                  <Tag>草稿 {statusSummary.draft}</Tag>
                  <Tag color="green">已发布 {statusSummary.published}</Tag>
                  <Tag>已归档 {statusSummary.archived}</Tag>
                  {experimentKeyword.trim() ? <Tag color="blue">搜索结果 {filteredExperiments.length}</Tag> : null}
                </>
              )}
            </Space>
            <Button disabled={!hasFilters} onClick={onResetFilters}>
              重置筛选
            </Button>
          </Flex>
        </Space>
      </Card>
      <Card>
        <QueryState loading={loading} error={error} empty={!filteredExperiments.length}>
          <Table
            rowKey="id"
            dataSource={filteredExperiments}
            columns={[
              { title: "排序", dataIndex: "display_order", width: 88 },
              {
                title: "实验",
                render: (_: unknown, row: Experiment) => (
                  <Space orientation="vertical" size={2}>
                    <Text strong>{row.title}</Text>
                    <Text type="secondary">{row.summary}</Text>
                  </Space>
                ),
              },
              {
                title: "理论章节",
                render: (_: unknown, row: Experiment) => (
                  <Space wrap>
                    {row.chapter_bindings.map((binding) => (
                      <Tag key={binding.chapter_id}>
                        {formatChapterTitle(binding.chapter_title || chapterTitleById.get(binding.chapter_id), binding.chapter_id)}
                      </Tag>
                    ))}
                  </Space>
                ),
              },
              {
                title: "资源",
                width: 170,
                render: (_: unknown, row: Experiment) => (
                  <Space size={6} wrap>
                    <Tag>点位 {experimentVideoCandidates(row).length}</Tag>
                    <Tag color={row.media_resources.length ? "#356f9c" : "default"}>视频 {row.media_resources.length}</Tag>
                  </Space>
                ),
              },
              { title: "状态", width: 110, render: (_: unknown, row: Experiment) => statusTag(row.status) },
              {
                title: "操作",
                width: 90,
                render: (_: unknown, row: Experiment) => <Button onClick={() => onSelectExperiment(row)}>编辑</Button>,
              },
            ]}
          />
        </QueryState>
      </Card>
    </>
  );
}
