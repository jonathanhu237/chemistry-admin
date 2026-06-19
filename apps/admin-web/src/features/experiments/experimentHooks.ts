import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";

import type { ApiList } from "../../api/common";
import type { Experiment, ExperimentVideoPoint, ExperimentVideoPointResource } from "../../api/experiments";
import {
  bindExperimentPointResource,
  changeExperimentPointPublication,
  createExperiment as createExperimentRequest,
  deleteExperimentPointResource,
  getExperiment,
  listExperimentVideoPoints,
  listExperiments,
  publishExperimentPointResource,
  saveExperimentPointContent,
  saveExperimentPointRelatedLinks,
  unpublishExperimentPointResource,
  updateExperiment,
} from "../../api/experiments";
import type { MediaAsset } from "../../api/media";
import { listMediaAssets } from "../../api/media";
import type { Chapter } from "../../api/resources";
import { listChapters } from "../../api/resources";
import { errorMessage } from "../../lib/errors";
import {
  buildPointContentRequest,
  buildPointPublicationRequest,
  buildPointRelatedLinksRequest,
} from "./pointContent/pointContentMapper";
import type { PointContentFormValues } from "./pointContent/pointContentMapper";

type MessageApi = {
  success: (content: string) => void;
  error: (content: string) => void;
};

export function useChapters() {
  return useQuery({ queryKey: ["chapters"], queryFn: listChapters });
}

export function useExperiments(params = "") {
  return useQuery<ApiList<Experiment>>({
    queryKey: ["admin-experiments", params],
    queryFn: () => listExperiments(params),
  });
}

export function useSelectedExperiment(experimentId?: string) {
  return useQuery({
    queryKey: ["admin-experiment", experimentId],
    queryFn: () => getExperiment(experimentId || ""),
    enabled: Boolean(experimentId),
  });
}

export function useExperimentVideoPoints(experimentId?: string) {
  return useQuery({
    queryKey: ["experiment-video-points", experimentId],
    queryFn: () => listExperimentVideoPoints(experimentId || ""),
    enabled: Boolean(experimentId),
  });
}

export function useExperimentMediaAssets(enabled: boolean) {
  return useQuery({
    queryKey: ["media-assets"],
    queryFn: () => listMediaAssets(200),
    enabled,
  });
}

export function useExperimentDataInvalidation() {
  const queryClient = useQueryClient();

  const invalidateExperimentData = (experimentId?: string) => {
    void queryClient.invalidateQueries({ queryKey: ["admin-experiments"] });
    void queryClient.invalidateQueries({ queryKey: ["question-banks"] });
    if (experimentId) {
      void queryClient.invalidateQueries({ queryKey: ["admin-experiment", experimentId] });
    }
  };

  const invalidateVideoReferenceData = (experimentId?: string) => {
    invalidateExperimentData(experimentId);
    if (experimentId) {
      void queryClient.invalidateQueries({ queryKey: ["experiment-video-points", experimentId] });
    }
    void queryClient.invalidateQueries({ queryKey: ["media-assets"] });
  };

  return { invalidateExperimentData, invalidateVideoReferenceData };
}

export function useCreateExperimentMutation({
  message,
  onCreated,
}: {
  message: MessageApi;
  onCreated: (experiment: Experiment) => void;
}) {
  const { invalidateExperimentData } = useExperimentDataInvalidation();
  return useMutation({
    mutationFn: (values: { title: string; summary?: string; status: string; chapter_ids: string[] }) =>
      createExperimentRequest({
        title: values.title,
        summary: values.summary,
        status: values.status || "draft",
        chapter_ids: values.chapter_ids || [],
      }),
    onSuccess: (experiment) => {
      message.success("实验已创建");
      onCreated(experiment);
      invalidateExperimentData(experiment.id);
    },
    onError: (error) => message.error(errorMessage(error)),
  });
}

export function useSaveExperimentMutation({
  experimentId,
  message,
  onSaved,
}: {
  experimentId?: string;
  message: MessageApi;
  onSaved: (experiment: Experiment) => void;
}) {
  const { invalidateExperimentData } = useExperimentDataInvalidation();
  return useMutation({
    mutationFn: (values: { title: string; summary?: string; status: string; chapter_ids: string[] }) => {
      if (!experimentId) {
        throw new Error("请先选择实验");
      }
      return updateExperiment(experimentId, {
        title: values.title,
        summary: values.summary,
        status: values.status,
        chapter_ids: values.chapter_ids || [],
      });
    },
    onSuccess: (experiment) => {
      message.success("实验已保存");
      onSaved(experiment);
      invalidateExperimentData(experiment.id);
    },
    onError: (error) => message.error(errorMessage(error)),
  });
}

export function useBindPointResourcesMutation({
  message,
  onBound,
}: {
  message: MessageApi;
  onBound: (experimentId?: string) => void;
}) {
  const { invalidateVideoReferenceData } = useExperimentDataInvalidation();
  return useMutation({
    mutationFn: async ({
      experimentId,
      point,
      assetIds,
      assetMap,
    }: {
      experimentId?: string;
      point: ExperimentVideoPoint | null;
      assetIds: string[];
      assetMap: Map<string, MediaAsset>;
    }) => {
      if (!experimentId || !point) {
        throw new Error("请先选择实验点位");
      }
      if (!assetIds.length) {
        throw new Error("请选择需要绑定的视频资源");
      }
      return Promise.all(
        assetIds.map((assetId) => {
          const asset = assetMap.get(assetId);
          return bindExperimentPointResource(experimentId, point.point_key, {
            media_asset_id: assetId,
            title: asset?.title || point.point_title,
            status: "draft",
          });
        }),
      );
    },
    onSuccess: (_payload, variables) => {
      message.success("视频已绑定到点位");
      onBound(variables.experimentId);
      invalidateVideoReferenceData(variables.experimentId);
    },
    onError: (error) => message.error(errorMessage(error)),
  });
}

export function usePointResourceActionMutations({
  message,
  onActionStart,
  onActionSettled,
}: {
  message: MessageApi;
  onActionStart: (resource: ExperimentVideoPointResource, action: "publish" | "unpublish" | "delete") => void;
  onActionSettled: () => void;
}) {
  const { invalidateVideoReferenceData } = useExperimentDataInvalidation();
  const publishPointResource = useMutation({
    mutationFn: publishExperimentPointResource,
    onMutate: (resource) => onActionStart(resource, "publish"),
    onSuccess: (_, resource) => {
      message.success("视频引用已发布");
      invalidateVideoReferenceData(resource.experiment_id);
    },
    onError: (error) => message.error(errorMessage(error)),
    onSettled: onActionSettled,
  });
  const unpublishPointResource = useMutation({
    mutationFn: unpublishExperimentPointResource,
    onMutate: (resource) => onActionStart(resource, "unpublish"),
    onSuccess: (_, resource) => {
      message.success("视频引用已取消发布");
      invalidateVideoReferenceData(resource.experiment_id);
    },
    onError: (error) => message.error(errorMessage(error)),
    onSettled: onActionSettled,
  });
  const deletePointResource = useMutation({
    mutationFn: deleteExperimentPointResource,
    onMutate: (resource) => onActionStart(resource, "delete"),
    onSuccess: (_, resource) => {
      message.success("视频引用已移除");
      invalidateVideoReferenceData(resource.experiment_id);
    },
    onError: (error) => message.error(errorMessage(error)),
    onSettled: onActionSettled,
  });
  return { publishPointResource, unpublishPointResource, deletePointResource };
}

export function useSavePointContentMutation({
  experimentId,
  point,
  message,
  onSaved,
}: {
  experimentId?: string;
  point: ExperimentVideoPoint | null;
  message: MessageApi;
  onSaved: (point: ExperimentVideoPoint | null, experimentId?: string) => void;
}) {
  const { invalidateVideoReferenceData } = useExperimentDataInvalidation();
  return useMutation({
    mutationFn: async (values: PointContentFormValues) => {
      if (!experimentId || !point) {
        throw new Error("请先选择实验点位");
      }
      await saveExperimentPointContent(experimentId, point.point_key, buildPointContentRequest(values));
      return saveExperimentPointRelatedLinks(experimentId, point.point_key, buildPointRelatedLinksRequest(values));
    },
    onSuccess: (payload) => {
      message.success("点位内容已保存");
      const updated = payload.points.find((item) => item.point_key === point?.point_key) || null;
      onSaved(updated, experimentId);
      invalidateVideoReferenceData(experimentId);
    },
    onError: (error) => message.error(errorMessage(error)),
  });
}

export function useChangePointPublicationMutation({
  experimentId,
  point,
  message,
  onChanged,
}: {
  experimentId?: string;
  point: ExperimentVideoPoint | null;
  message: MessageApi;
  onChanged: (point: ExperimentVideoPoint | null, experimentId?: string) => void;
}) {
  const { invalidateVideoReferenceData } = useExperimentDataInvalidation();
  return useMutation({
    mutationFn: (action: "publish" | "unpublish" | "archive") => {
      if (!experimentId || !point) {
        throw new Error("请先选择实验点位");
      }
      return changeExperimentPointPublication(experimentId, point.point_key, buildPointPublicationRequest(action));
    },
    onSuccess: (payload) => {
      message.success("点位发布状态已更新");
      const updated = payload.points.find((item) => item.point_key === point?.point_key) || null;
      onChanged(updated, experimentId);
      invalidateVideoReferenceData(experimentId);
    },
    onError: (error) => message.error(errorMessage(error)),
  });
}
