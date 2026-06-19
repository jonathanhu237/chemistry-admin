import { Alert, Button, Flex, Input, Modal, Space, Table, Tag, Typography } from "antd";
import { EyeOutlined, VideoCameraOutlined } from "@ant-design/icons";

import type { ExperimentVideoPoint } from "../../../api/experiments";
import type { MediaAsset } from "../../../api/media";
import { QueryState } from "../../../components/QueryState";
import { formatBytes } from "../../../lib/format";
import { statusTag } from "../../../lib/status";
import { isPreviewableVideo, mediaAssetType } from "../../../lib/resourceUtils";

const { Text } = Typography;

type MutationLike = {
  isPending: boolean;
  mutate: (value: { experimentId?: string; point: ExperimentVideoPoint | null; assetIds: string[]; assetMap: Map<string, MediaAsset> }) => void;
};

export type VideoPreviewTarget = {
  id: string;
  title: string;
  original_file_name: string;
  mime_type?: string | null;
  upload_status?: string | null;
};

export function VideoBindingModal({
  referencePoint,
  currentExperimentId,
  assets,
  filteredAssets,
  loading,
  error,
  assetKeyword,
  selectedAssetIds,
  referencedAssetIds,
  currentPointAssetIds,
  referenceAssetMap,
  addPointResources,
  onKeywordChange,
  onSelectedAssetIdsChange,
  onPreview,
  onClose,
}: {
  referencePoint: ExperimentVideoPoint | null;
  currentExperimentId?: string;
  assets: MediaAsset[];
  filteredAssets: MediaAsset[];
  loading: boolean;
  error: unknown;
  assetKeyword: string;
  selectedAssetIds: string[];
  referencedAssetIds: Set<string>;
  currentPointAssetIds: Set<string>;
  referenceAssetMap: Map<string, MediaAsset>;
  addPointResources: MutationLike;
  onKeywordChange: (value: string) => void;
  onSelectedAssetIdsChange: (value: string[]) => void;
  onPreview: (value: VideoPreviewTarget) => void;
  onClose: () => void;
}) {
  return (
    <Modal
      title={referencePoint ? `为「${referencePoint.point_title}」绑定视频` : "绑定视频"}
      open={Boolean(referencePoint)}
      width={980}
      onCancel={onClose}
      footer={[
        <Button key="cancel" onClick={onClose}>
          取消
        </Button>,
        <Button
          key="save"
          type="primary"
          loading={addPointResources.isPending}
          disabled={!selectedAssetIds.length}
          onClick={() =>
            addPointResources.mutate({
              experimentId: currentExperimentId,
              point: referencePoint,
              assetIds: selectedAssetIds,
              assetMap: referenceAssetMap,
            })
          }
        >
          保存绑定
        </Button>,
      ]}
    >
      <Space orientation="vertical" size={14} className="full">
        <Alert type="info" showIcon title="这里只能绑定已经上传到素材库的视频资源，保存后默认是草稿引用，发布后学生端可见。" />
        <Flex justify="space-between" align="center" gap={12} wrap="wrap">
          <Input.Search
            allowClear
            placeholder="搜索视频标题或文件名"
            value={assetKeyword}
            onChange={(event) => onKeywordChange(event.target.value)}
            style={{ width: 360 }}
          />
          <Text type="secondary">已选择 {selectedAssetIds.length} 个视频</Text>
        </Flex>
        <QueryState loading={loading} error={error} empty={!assets.length}>
          <Table
            rowKey="id"
            dataSource={filteredAssets}
            pagination={{ pageSize: 6, showSizeChanger: false }}
            rowSelection={{
              selectedRowKeys: selectedAssetIds,
              onChange: (keys) => onSelectedAssetIdsChange(keys.map(String)),
              getCheckboxProps: (asset: MediaAsset) => ({
                disabled: !isPreviewableVideo(asset) || referencedAssetIds.has(asset.id),
              }),
            }}
            columns={[
              {
                title: "视频资源",
                render: (_: unknown, asset: MediaAsset) => (
                  <Space size={10} align="start" className="video-asset-name">
                    <div className="video-file-mark">
                      <VideoCameraOutlined />
                    </div>
                    <Space orientation="vertical" size={1}>
                      <Text strong>{asset.title}</Text>
                      <Text type="secondary">{asset.original_file_name}</Text>
                    </Space>
                  </Space>
                ),
              },
              { title: "类型", width: 90, render: (_: unknown, asset: MediaAsset) => mediaAssetType(asset) },
              { title: "大小", width: 100, render: (_: unknown, asset: MediaAsset) => formatBytes(asset.file_size_bytes) },
              { title: "状态", width: 100, render: (_: unknown, asset: MediaAsset) => statusTag(asset.upload_status) },
              {
                title: "绑定状态",
                width: 130,
                render: (_: unknown, asset: MediaAsset) => {
                  if (currentPointAssetIds.has(asset.id)) return <Tag color="green">已在当前点位</Tag>;
                  if (referencedAssetIds.has(asset.id)) return <Tag>已被本实验引用</Tag>;
                  if (!isPreviewableVideo(asset)) return <Tag>不可绑定</Tag>;
                  return <Tag color="blue">可绑定</Tag>;
                },
              },
              {
                title: "操作",
                width: 100,
                render: (_: unknown, asset: MediaAsset) => (
                  <Button
                    size="small"
                    icon={<EyeOutlined />}
                    disabled={!isPreviewableVideo(asset)}
                    onClick={() =>
                      onPreview({
                        id: asset.id,
                        title: asset.title,
                        original_file_name: asset.original_file_name,
                        mime_type: asset.mime_type,
                        upload_status: asset.upload_status,
                      })
                    }
                  >
                    预览
                  </Button>
                ),
              },
            ]}
          />
        </QueryState>
      </Space>
    </Modal>
  );
}
