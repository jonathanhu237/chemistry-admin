import { useEffect, useMemo, useState } from "react";
import {
  Alert,
  App as AntApp,
  Button,
  Card,
  Checkbox,
  Descriptions,
  Divider,
  Drawer,
  Empty,
  Flex,
  Form,
  Input,
  InputNumber,
  Modal,
  Popconfirm,
  Progress,
  Segmented,
  Select,
  Space,
  Spin,
  Statistic,
  Switch,
  Table,
  Tag,
  Tooltip,
  Typography,
} from "antd";
import {
  CloudUploadOutlined,
  CheckCircleOutlined,
  DeleteOutlined,
  EditOutlined,
  ExperimentOutlined,
  EyeOutlined,
  PauseCircleOutlined,
  PlayCircleOutlined,
  PlusOutlined,
  ReloadOutlined,
  VideoCameraOutlined,
} from "@ant-design/icons";

import type { Experiment, ExperimentVideoPoint, ExperimentVideoPointResource } from "../../api/experiments";
import type { MediaAsset } from "../../api/media";
import { apiBase } from "../../api/http";
import { AuthenticatedImage } from "../../components/AuthenticatedImage";
import { PageTitle } from "../../components/PageTitle";
import { QueryState } from "../../components/QueryState";
import { errorMessage } from "../../lib/errors";
import { formatBytes } from "../../lib/format";
import { statusTag } from "../../lib/status";
import { filterVideoPointsForAdmin, videoPointFilterOptions } from "./experimentFilters";
import type { VideoPointFilter } from "./experimentFilters";
import { ExperimentBasicForm } from "./experimentDetail/ExperimentBasicForm";
import { ExperimentDetailDrawer } from "./experimentDetail/ExperimentDetailDrawer";
import { ExperimentListSection } from "./experimentList/ExperimentListSection";
import {
  useBindPointResourcesMutation,
  useChangePointPublicationMutation,
  useChapters,
  useCreateExperimentMutation,
  useExperimentMediaAssets,
  useExperiments,
  useExperimentVideoPoints,
  usePointResourceActionMutations,
  useSaveExperimentMutation,
  useSavePointContentMutation,
  useSelectedExperiment,
} from "./experimentHooks";
import { hydratePointContentFormValues } from "./pointContent/pointContentMapper";
import type { PointContentFormValues } from "./pointContent/pointContentMapper";
import { PointContentModal } from "./pointContent/PointContentModal";
import { VideoBindingModal } from "./videoBindings/VideoBindingModal";
import type { VideoPreviewTarget } from "./videoBindings/VideoBindingModal";
import { VideoPointResourcesPanel } from "./videoBindings/VideoPointResourcesPanel";
import { VideoPreviewModal } from "./videoBindings/VideoPreviewModal";
import { experimentVideoCandidates, formatChapterTitle, theoryChapters } from "../../lib/resourceUtils";
import "./experiments.css";

const { Text, Title } = Typography;

export function ExperimentsPage() {
  const { message } = AntApp.useApp();
  const chapters = useChapters();
  const [experimentKeyword, setExperimentKeyword] = useState("");
  const [chapterId, setChapterId] = useState<string>();
  const [statusFilter, setStatusFilter] = useState<string>();
  const [selected, setSelected] = useState<Experiment | null>(null);
  const [createOpen, setCreateOpen] = useState(false);
  const [form] = Form.useForm();
  const [createForm] = Form.useForm();
  const [pointContentForm] = Form.useForm<PointContentFormValues>();
  const [videoPointFilter, setVideoPointFilter] = useState<VideoPointFilter>("all");
  const [referencePoint, setReferencePoint] = useState<ExperimentVideoPoint | null>(null);
  const [contentPoint, setContentPoint] = useState<ExperimentVideoPoint | null>(null);
  const [assetKeyword, setAssetKeyword] = useState("");
  const [selectedAssetIds, setSelectedAssetIds] = useState<string[]>([]);
  const [previewTarget, setPreviewTarget] = useState<VideoPreviewTarget | null>(null);
  const [pendingVideoBindingAction, setPendingVideoBindingAction] = useState<{
    bindingId: string;
    action: "publish" | "unpublish" | "delete";
  } | null>(null);
  const searchParams = new URLSearchParams();
  if (chapterId) searchParams.set("chapter_id", chapterId);
  if (statusFilter) searchParams.set("status_filter", statusFilter);
  const params = searchParams.toString() ? `?${searchParams.toString()}` : "";
  const experiments = useExperiments(params);
  const selectedExperiment = useSelectedExperiment(selected?.id);
  const currentExperiment = selectedExperiment.data || selected;
  const currentExperimentId = currentExperiment?.id;
  const experimentVideoPoints = useExperimentVideoPoints(currentExperimentId);
  const mediaAssets = useExperimentMediaAssets(Boolean(referencePoint));
  const currentMetadata = (currentExperiment?.metadata || {}) as Record<string, unknown>;
  const videoCandidates = experimentVideoCandidates(currentExperiment);
  const videoPointItems = useMemo(() => experimentVideoPoints.data?.points || [], [experimentVideoPoints.data?.points]);
  const parentTitle = typeof currentMetadata.parent_title === "string" ? currentMetadata.parent_title : "";
  const moduleTitle = typeof currentMetadata.module_display_title === "string" ? currentMetadata.module_display_title : "";
  const videoPointCount = experimentVideoPoints.data?.total_points ?? videoCandidates.length;
  const resourceCount = experimentVideoPoints.data?.total_resources ?? currentExperiment?.media_resources.length ?? 0;
  const publishedResourceCount =
    experimentVideoPoints.data?.published_resources ??
    currentExperiment?.media_resources.filter((resource) => resource.binding_status === "published").length ??
    0;
  const referencedAssetIds = useMemo(
    () => new Set(videoPointItems.flatMap((point) => point.resources.map((resource) => resource.media_id))),
    [videoPointItems],
  );
  const currentPointAssetIds = useMemo(
    () => new Set(referencePoint?.resources.map((resource) => resource.media_id) || []),
    [referencePoint?.resources],
  );
  const referenceAssets = useMemo(() => mediaAssets.data?.items || [], [mediaAssets.data?.items]);
  const referenceAssetMap = useMemo(() => new Map(referenceAssets.map((asset) => [asset.id, asset])), [referenceAssets]);
  const filteredReferenceAssets = useMemo(() => {
    const keyword = assetKeyword.trim().toLowerCase();
    return referenceAssets.filter((asset) => {
      if (!keyword) return true;
      return `${asset.title} ${asset.original_file_name}`.toLowerCase().includes(keyword);
    });
  }, [assetKeyword, referenceAssets]);
  const filteredVideoPoints = useMemo(() => filterVideoPointsForAdmin(videoPointItems, videoPointFilter), [videoPointFilter, videoPointItems]);

  useEffect(() => {
    if (currentExperiment) {
      form.setFieldsValue({
        title: currentExperiment.title,
        summary: currentExperiment.summary,
        status: currentExperiment.status,
        chapter_ids: currentExperiment.chapter_bindings.map((item) => item.chapter_id),
      });
    }
  }, [currentExperiment, form]);

  useEffect(() => {
    setVideoPointFilter("all");
    setReferencePoint(null);
    setAssetKeyword("");
    setSelectedAssetIds([]);
    setPreviewTarget(null);
    setContentPoint(null);
    pointContentForm.resetFields();
    setPendingVideoBindingAction(null);
  }, [pointContentForm, selected?.id]);

  useEffect(() => {
    setSelectedAssetIds([]);
    setAssetKeyword("");
  }, [referencePoint?.point_key]);

  useEffect(() => {
    if (!contentPoint) {
      pointContentForm.resetFields();
      return;
    }
    pointContentForm.setFieldsValue(hydratePointContentFormValues(contentPoint));
  }, [contentPoint, pointContentForm]);

  useEffect(() => {
    if (!contentPoint) return;
    const updated = videoPointItems.find((point) => point.point_key === contentPoint.point_key);
    if (updated && updated !== contentPoint) setContentPoint(updated);
  }, [contentPoint, videoPointItems]);

  const createExperiment = useCreateExperimentMutation({
    message,
    onCreated: (experiment) => {
      setCreateOpen(false);
      createForm.resetFields();
      setSelected(experiment);
    },
  });
  const submitCreateExperiment = async (status: "draft" | "published") => {
    try {
      const values = await createForm.validateFields();
      createExperiment.mutate({ ...values, status });
    } catch {
      // Ant Design will surface field validation messages beside the inputs.
    }
  };

  const save = useSaveExperimentMutation({
    experimentId: currentExperiment?.id,
    message,
    onSaved: setSelected,
  });

  const addPointResources = useBindPointResourcesMutation({
    message,
    onBound: () => {
      setReferencePoint(null);
      setSelectedAssetIds([]);
      setAssetKeyword("");
    },
  });

  const { publishPointResource, unpublishPointResource, deletePointResource } = usePointResourceActionMutations({
    message,
    onActionStart: (resource, action) => setPendingVideoBindingAction({ bindingId: resource.binding_id, action }),
    onActionSettled: () => setPendingVideoBindingAction(null),
  });

  const savePointContent = useSavePointContentMutation({
    experimentId: currentExperimentId,
    point: contentPoint,
    message,
    onSaved: setContentPoint,
  });

  const changePointPublication = useChangePointPublicationMutation({
    experimentId: currentExperimentId,
    point: contentPoint,
    message,
    onChanged: setContentPoint,
  });

  const isVideoBindingActionPending = (resource: ExperimentVideoPointResource, action: "publish" | "unpublish" | "delete") =>
    pendingVideoBindingAction?.bindingId === resource.binding_id && pendingVideoBindingAction.action === action;
  const isVideoBindingBusy = (resource: ExperimentVideoPointResource) => pendingVideoBindingAction?.bindingId === resource.binding_id;

  const chapterTitleById = useMemo(() => {
    const values = new Map(theoryChapters.map((chapter) => [chapter.chapter_id, formatChapterTitle(chapter.chapter_title, chapter.chapter_id)]));
    (chapters.data || []).forEach((chapter) => {
      values.set(chapter.chapter_id, formatChapterTitle(chapter.chapter_title, chapter.chapter_id));
    });
    return values;
  }, [chapters.data]);
  const chapterOptions = (chapters.data || []).map((chapter) => ({
    value: chapter.chapter_id,
    label: formatChapterTitle(chapter.chapter_title, chapter.chapter_id),
  }));
  const scopedExperiments = experiments.data?.items || [];
  const filteredExperiments = useMemo(() => {
    const keyword = experimentKeyword.trim().toLowerCase();
    if (!keyword) return scopedExperiments;
    return scopedExperiments.filter((experiment) => experiment.title.toLowerCase().includes(keyword));
  }, [experimentKeyword, scopedExperiments]);
  const statusSummary = useMemo(
    () =>
      scopedExperiments.reduce(
        (summary, experiment) => {
          summary.total += 1;
          if (experiment.status === "draft") summary.draft += 1;
          if (experiment.status === "published") summary.published += 1;
          if (experiment.status === "archived") summary.archived += 1;
          return summary;
        },
        { total: 0, draft: 0, published: 0, archived: 0 },
      ),
    [scopedExperiments],
  );
  const pointTargetOptions = useMemo(
    () =>
      videoPointItems
        .filter((point) => point.point_key !== contentPoint?.point_key)
        .map((point) => ({
          value: `${currentExperimentId}::${point.point_key}`,
          label: point.point_title,
        })),
    [contentPoint?.point_key, currentExperimentId, videoPointItems],
  );
  const hasFilters = Boolean(experimentKeyword || chapterId || statusFilter);

  return (
    <Space orientation="vertical" size={18} className="full">
      <PageTitle
        title="实验管理"
        description="管理实验元信息、理论章节与发布状态；视频素材库作为独立模块维护。"
        extra={
          <Button type="primary" icon={<PlusOutlined />} onClick={() => setCreateOpen(true)}>
            新建实验
          </Button>
        }
      />
      <ExperimentListSection
        loading={experiments.isLoading}
        error={experiments.error}
        filteredExperiments={filteredExperiments}
        statusSummary={statusSummary}
        experimentKeyword={experimentKeyword}
        chapterId={chapterId}
        statusFilter={statusFilter}
        chapterOptions={chapterOptions}
        chapterTitleById={chapterTitleById}
        hasFilters={hasFilters}
        onKeywordChange={setExperimentKeyword}
        onChapterChange={setChapterId}
        onStatusChange={setStatusFilter}
        onResetFilters={() => {
          setExperimentKeyword("");
          setChapterId(undefined);
          setStatusFilter(undefined);
        }}
        onSelectExperiment={setSelected}
      />
      <ExperimentDetailDrawer
        open={Boolean(selected)}
        currentExperiment={currentExperiment}
        loading={selectedExperiment.isLoading}
        error={selectedExperiment.error}
        onClose={() => setSelected(null)}
      >
          <Space orientation="vertical" size={16} className="full">
            {currentExperiment ? (
              <div className="experiment-editor-summary">
                <Flex justify="space-between" gap={18} wrap="wrap" align="center">
                  <div className="experiment-editor-summary-main">
                    <Space size={8} wrap>
                      {statusTag(currentExperiment.status)}
                      {currentExperiment.chapter_bindings.slice(0, 3).map((binding) => (
                        <Tag key={binding.chapter_id}>
                          {formatChapterTitle(binding.chapter_title || chapterTitleById.get(binding.chapter_id), binding.chapter_id)}
                        </Tag>
                      ))}
                    </Space>
                    <Title level={4}>{currentExperiment.title}</Title>
                    <Text type="secondary">{currentExperiment.summary || "暂无实验说明"}</Text>
                  </div>
                  <div className="experiment-editor-metrics">
                    <Statistic title="视频点位" value={videoPointCount} />
                    <Statistic title="关联资源" value={resourceCount} />
                    <Statistic title="已发布" value={publishedResourceCount} />
                  </div>
                </Flex>
              </div>
            ) : null}

            <div className="experiment-editor-grid">
              <Space orientation="vertical" size={16} className="full">
                <ExperimentBasicForm form={form} save={save} chapterOptions={chapterOptions} />

                <Card title="来源上下文" className="experiment-context-card">
                  {parentTitle || moduleTitle ? (
                    <Descriptions
                      size="small"
                      column={1}
                      items={[
                        ...(parentTitle ? [{ key: "parent", label: "来源大类", children: parentTitle }] : []),
                        ...(moduleTitle ? [{ key: "module", label: "目录模块", children: moduleTitle }] : []),
                      ]}
                    />
                  ) : (
                    <Text type="secondary">暂无来源上下文</Text>
                  )}
                </Card>
              </Space>

              <VideoPointResourcesPanel
                videoPointCount={videoPointCount}
                resourceCount={resourceCount}
                publishedResourceCount={publishedResourceCount}
                videoPointFilter={videoPointFilter}
                videoPointItems={videoPointItems}
                filteredVideoPoints={filteredVideoPoints}
                loading={experimentVideoPoints.isLoading}
                error={experimentVideoPoints.error}
                publishPointResource={publishPointResource}
                unpublishPointResource={unpublishPointResource}
                deletePointResource={deletePointResource}
                isVideoBindingActionPending={isVideoBindingActionPending}
                isVideoBindingBusy={isVideoBindingBusy}
                onFilterChange={setVideoPointFilter}
                onEditContent={setContentPoint}
                onBindVideo={setReferencePoint}
                onPreview={setPreviewTarget}
              />

            </div>
          </Space>
      </ExperimentDetailDrawer>

      <PointContentModal
        contentPoint={contentPoint}
        form={pointContentForm}
        pointTargetOptions={pointTargetOptions}
        savePointContent={savePointContent}
        changePointPublication={changePointPublication}
        onClose={() => setContentPoint(null)}
      />

      <VideoBindingModal
        referencePoint={referencePoint}
        currentExperimentId={currentExperimentId}
        assets={referenceAssets}
        filteredAssets={filteredReferenceAssets}
        loading={mediaAssets.isLoading}
        error={mediaAssets.error}
        assetKeyword={assetKeyword}
        selectedAssetIds={selectedAssetIds}
        referencedAssetIds={referencedAssetIds}
        currentPointAssetIds={currentPointAssetIds}
        referenceAssetMap={referenceAssetMap}
        addPointResources={addPointResources}
        onKeywordChange={setAssetKeyword}
        onSelectedAssetIdsChange={setSelectedAssetIds}
        onPreview={setPreviewTarget}
        onClose={() => setReferencePoint(null)}
      />

      <VideoPreviewModal
        previewTarget={previewTarget}
        onClose={() => setPreviewTarget(null)}
      />

      <Modal
        title="新建实验"
        open={createOpen}
        onCancel={() => setCreateOpen(false)}
        footer={[
          <Button key="cancel" onClick={() => setCreateOpen(false)}>
            取消
          </Button>,
          <Button key="draft" loading={createExperiment.isPending} onClick={() => void submitCreateExperiment("draft")}>
            保存为草稿
          </Button>,
          <Button key="publish" type="primary" loading={createExperiment.isPending} onClick={() => void submitCreateExperiment("published")}>
            保存并发布
          </Button>,
        ]}
      >
        <Text type="secondary" className="modal-helper">
          填写实验名称和说明，并选择它要显示在哪些理论章节下。
        </Text>
        <Form form={createForm} layout="vertical">
          <Form.Item name="title" label="实验名称" rules={[{ required: true, message: "请输入实验名称" }]}>
            <Input placeholder="例如：氯、溴、碘的置换次序" />
          </Form.Item>
          <Form.Item name="summary" label="实验说明">
            <Input.TextArea rows={3} maxLength={300} showCount className="fixed-textarea" />
          </Form.Item>
          <Form.Item name="chapter_ids" label="理论章节" rules={[{ required: true, message: "请选择至少一个章节" }]}>
            <Select mode="multiple" options={chapterOptions} placeholder="选择章节" />
          </Form.Item>
        </Form>
      </Modal>
    </Space>
  );
}
