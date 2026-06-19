import { Alert, Button, Card, Empty, Flex, Popconfirm, Segmented, Space, Spin, Tag, Typography } from "antd";
import {
  CheckCircleOutlined,
  DeleteOutlined,
  EditOutlined,
  PauseCircleOutlined,
  PlayCircleOutlined,
  PlusOutlined,
  VideoCameraOutlined,
} from "@ant-design/icons";

import type { ExperimentVideoPoint, ExperimentVideoPointResource } from "../../../api/experiments";
import { getMediaAssetThumbnailUrl } from "../../../api/media";
import { AuthenticatedImage } from "../../../components/AuthenticatedImage";
import { errorMessage } from "../../../lib/errors";
import { formatBytes } from "../../../lib/format";
import { statusTag } from "../../../lib/status";
import { videoPointFilterOptions } from "../experimentFilters";
import type { VideoPointFilter } from "../experimentFilters";
import type { VideoPreviewTarget } from "./VideoBindingModal";

const { Text } = Typography;

type ResourceMutation = {
  mutate: (resource: ExperimentVideoPointResource) => void;
};

export function VideoPointResourcesPanel({
  videoPointCount,
  resourceCount,
  publishedResourceCount,
  videoPointFilter,
  videoPointItems,
  filteredVideoPoints,
  loading,
  error,
  publishPointResource,
  unpublishPointResource,
  deletePointResource,
  isVideoBindingActionPending,
  isVideoBindingBusy,
  onFilterChange,
  onEditContent,
  onBindVideo,
  onPreview,
}: {
  videoPointCount: number;
  resourceCount: number;
  publishedResourceCount: number;
  videoPointFilter: VideoPointFilter;
  videoPointItems: ExperimentVideoPoint[];
  filteredVideoPoints: ExperimentVideoPoint[];
  loading: boolean;
  error: unknown;
  publishPointResource: ResourceMutation;
  unpublishPointResource: ResourceMutation;
  deletePointResource: ResourceMutation;
  isVideoBindingActionPending: (resource: ExperimentVideoPointResource, action: "publish" | "unpublish" | "delete") => boolean;
  isVideoBindingBusy: (resource: ExperimentVideoPointResource) => boolean;
  onFilterChange: (value: VideoPointFilter) => void;
  onEditContent: (point: ExperimentVideoPoint) => void;
  onBindVideo: (point: ExperimentVideoPoint) => void;
  onPreview: (target: VideoPreviewTarget) => void;
}) {
  return (
    <Card
      title={
        <Flex justify="space-between" align="center" gap={12} wrap="wrap">
          <span>点位视频引用</span>
          <Space size={6} wrap>
            <Tag>点位 {videoPointCount}</Tag>
            <Tag color={resourceCount ? "blue" : "default"}>已引用 {resourceCount}</Tag>
            <Tag color={publishedResourceCount ? "green" : "default"}>已发布 {publishedResourceCount}</Tag>
          </Space>
        </Flex>
      }
      className="video-reference-card"
    >
      <Space orientation="vertical" size={14} className="full">
        <Flex justify="space-between" align="center" gap={12} wrap="wrap" className="video-reference-toolbar">
          <Segmented value={videoPointFilter} onChange={(value) => onFilterChange(value as VideoPointFilter)} options={videoPointFilterOptions} />
          <Text type="secondary">当前列表只绑定实验点位相关的视频，发布后进入学生端实验视频库。</Text>
        </Flex>

        {loading ? (
          <div className="center-panel">
            <Spin />
          </div>
        ) : error ? (
          <Alert type="error" showIcon title="点位视频加载失败" description={errorMessage(error)} />
        ) : !videoPointItems.length ? (
          <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description="暂无视频点位" />
        ) : !filteredVideoPoints.length ? (
          <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} description="当前筛选下没有点位" />
        ) : (
          <div className="video-point-list">
            {filteredVideoPoints.map((point) => {
              const pointIndex = videoPointItems.findIndex((item) => item.point_key === point.point_key) + 1;
              return (
                <div className="video-point-card" key={point.point_key}>
                  <Flex justify="space-between" align="start" gap={12} wrap="wrap" className="video-point-header">
                    <Space size={12} align="start" className="video-point-heading">
                      <span className="video-point-index">{pointIndex}</span>
                      <div className="video-point-title">
                        <Text strong>{point.point_title}</Text>
                        <Space size={6} wrap>
                          <Tag color={point.content?.content_status === "published" ? "green" : point.content?.content_status === "draft" ? "orange" : "default"}>
                            内容 {point.content?.content_status || "missing"}
                          </Tag>
                          <Tag color={point.validation?.complete ? "green" : "red"}>{point.validation?.complete ? "完整" : `缺 ${point.validation?.errors.length || 0}`}</Tag>
                          <Tag color={point.index_state?.sync_status === "failed" ? "red" : point.index_state?.sync_status === "synced" ? "green" : "blue"}>
                            索引 {point.index_state?.sync_status || "pending"}
                          </Tag>
                          <Tag color={point.resource_count ? "blue" : "default"}>已引用 {point.resource_count}</Tag>
                          <Tag color={point.published_count ? "green" : "default"}>已发布 {point.published_count}</Tag>
                        </Space>
                      </div>
                    </Space>
                    <Space size={8} wrap>
                      <Button icon={<EditOutlined />} onClick={() => onEditContent(point)}>
                        编辑内容
                      </Button>
                      <Button type={point.resource_count ? "default" : "primary"} icon={<PlusOutlined />} onClick={() => onBindVideo(point)}>
                        绑定视频
                      </Button>
                    </Space>
                  </Flex>

                  <div className="point-content-summary">
                    <Text type="secondary">
                      {point.content?.principle_mode === "equation"
                        ? point.content?.principle_equation || "未填写方程式原理"
                        : point.content?.principle_text || "未填写文字原理"}
                    </Text>
                    <Text type="secondary">{point.content?.phenomenon_explanation || "未填写现象解释"}</Text>
                  </div>

                  {point.resources.length ? (
                    <div className="video-point-resources">
                      {point.resources.map((resource) => {
                        const resourceTitle = resource.media_title || resource.title || resource.binding_title || resource.original_file_name;
                        const thumbnailSrc = resource.thumbnail_relative_path ? getMediaAssetThumbnailUrl(resource.media_id) : null;
                        const resourceBusy = isVideoBindingBusy(resource);
                        return (
                          <div className="video-point-resource" key={resource.binding_id}>
                            <button
                              type="button"
                              className={thumbnailSrc ? "video-resource-thumb has-image" : "video-resource-thumb"}
                              disabled={resource.upload_status !== "ready"}
                              aria-label={`预览视频：${resourceTitle}`}
                              title={resource.upload_status === "ready" ? "预览视频" : "视频尚未就绪，无法预览"}
                              onClick={() =>
                                onPreview({
                                  id: resource.media_id,
                                  title: resource.media_title || resourceTitle,
                                  original_file_name: resource.original_file_name,
                                  mime_type: resource.mime_type,
                                  upload_status: resource.upload_status,
                                })
                              }
                            >
                              <AuthenticatedImage src={thumbnailSrc} alt={resourceTitle} className="video-resource-thumb-image" />
                              <div className="video-resource-thumb-fallback">
                                <VideoCameraOutlined />
                              </div>
                              {resource.upload_status === "ready" ? (
                                <span className="video-resource-thumb-play">
                                  <PlayCircleOutlined />
                                </span>
                              ) : null}
                            </button>
                            <div className="video-point-resource-main">
                              <Text strong className="video-point-resource-title">
                                {resourceTitle}
                              </Text>
                              <Text type="secondary" className="video-point-resource-file">
                                {resource.original_file_name}
                              </Text>
                              <Space size={6} wrap>
                                {statusTag(resource.upload_status)}
                                {statusTag(resource.binding_status)}
                                <Text type="secondary">{formatBytes(resource.file_size_bytes)}</Text>
                              </Space>
                            </div>
                            <Space size={8} wrap className="video-point-resource-actions">
                              {resource.binding_status === "published" ? (
                                <Button
                                  size="small"
                                  icon={<PauseCircleOutlined />}
                                  disabled={resourceBusy}
                                  loading={isVideoBindingActionPending(resource, "unpublish")}
                                  onClick={() => unpublishPointResource.mutate(resource)}
                                >
                                  取消发布
                                </Button>
                              ) : (
                                <Button
                                  size="small"
                                  type="primary"
                                  icon={<CheckCircleOutlined />}
                                  disabled={resource.upload_status !== "ready" || resourceBusy}
                                  loading={isVideoBindingActionPending(resource, "publish")}
                                  onClick={() => publishPointResource.mutate(resource)}
                                >
                                  发布引用
                                </Button>
                              )}
                              <Popconfirm
                                title="移除视频引用？"
                                description="只删除该实验点位对视频的引用关系，不会删除视频素材本身。"
                                okText="移除"
                                cancelText="取消"
                                okButtonProps={{ danger: true }}
                                onConfirm={() => deletePointResource.mutate(resource)}
                              >
                                <Button
                                  size="small"
                                  danger
                                  icon={<DeleteOutlined />}
                                  disabled={resourceBusy}
                                  loading={isVideoBindingActionPending(resource, "delete")}
                                >
                                  移除引用
                                </Button>
                              </Popconfirm>
                            </Space>
                          </div>
                        );
                      })}
                    </div>
                  ) : (
                    <button type="button" className="video-point-empty" onClick={() => onBindVideo(point)}>
                      <PlusOutlined />
                      <span>还没有绑定视频</span>
                      <Text type="secondary">点击从视频素材库选择资源</Text>
                    </button>
                  )}
                </div>
              );
            })}
          </div>
        )}
      </Space>
    </Card>
  );
}
