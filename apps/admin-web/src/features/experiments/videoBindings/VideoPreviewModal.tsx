import { useEffect, useState } from "react";
import { Alert, Modal, Space, Spin, Typography } from "antd";

import { getAuthToken } from "../../../api/auth";
import { getMediaAssetFileUrl } from "../../../api/media";
import { errorMessage } from "../../../lib/errors";
import type { VideoPreviewTarget } from "./VideoBindingModal";

const { Text } = Typography;

export function VideoPreviewModal({
  previewTarget,
  onClose,
}: {
  previewTarget: VideoPreviewTarget | null;
  onClose: () => void;
}) {
  const [previewUrl, setPreviewUrl] = useState<string>();
  const [previewLoading, setPreviewLoading] = useState(false);
  const [previewError, setPreviewError] = useState("");

  useEffect(() => {
    let objectUrl: string | undefined;
    let cancelled = false;
    setPreviewUrl(undefined);
    setPreviewError("");
    setPreviewLoading(false);
    if (!previewTarget || previewTarget.upload_status !== "ready") {
      return undefined;
    }
    setPreviewLoading(true);
    const headers = new Headers();
    const token = getAuthToken();
    if (token) {
      headers.set("Authorization", `Bearer ${token}`);
    }
    void fetch(getMediaAssetFileUrl(previewTarget.id), { headers })
      .then(async (response) => {
        if (!response.ok) {
          throw new Error(response.status === 409 ? "视频文件尚未就绪，无法预览" : "视频预览加载失败");
        }
        return response.blob();
      })
      .then((blob) => {
        if (cancelled) return;
        objectUrl = URL.createObjectURL(blob);
        setPreviewUrl(objectUrl);
      })
      .catch((error) => {
        if (!cancelled) setPreviewError(errorMessage(error));
      })
      .finally(() => {
        if (!cancelled) setPreviewLoading(false);
      });
    return () => {
      cancelled = true;
      if (objectUrl) URL.revokeObjectURL(objectUrl);
    };
  }, [previewTarget]);

  return (
    <Modal title={previewTarget?.title || "视频预览"} open={Boolean(previewTarget)} width={860} footer={null} onCancel={onClose}>
      <Space orientation="vertical" size={14} className="full">
        <Text type="secondary">{previewTarget?.original_file_name}</Text>
        <div className="experiment-video-preview-stage">
          {previewLoading ? (
            <Spin />
          ) : previewError ? (
            <Alert type="error" showIcon title="预览失败" description={previewError} />
          ) : previewUrl ? (
            <video src={previewUrl} controls className="video-preview-player" />
          ) : (
            <Text type="secondary">正在准备预览...</Text>
          )}
        </div>
      </Space>
    </Modal>
  );
}
