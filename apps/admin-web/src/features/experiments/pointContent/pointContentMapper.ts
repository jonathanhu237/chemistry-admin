import type { ExperimentVideoPoint } from "../../../api/experiments";

export type PointContentFormValues = {
  point_title: string;
  principle_mode: "equation" | "text";
  principle_equation?: string;
  principle_text?: string;
  phenomenon_explanation?: string;
  safety_note?: string;
  links?: Array<{
    target?: string;
    relation_type?: "manual" | "default_override";
    hidden?: boolean;
    sort_order?: number;
    label?: string;
  }>;
};

export type PointRelatedLinkPayload = {
  target_experiment_id: string;
  target_point_key: string;
  relation_type: "manual" | "default_override";
  hidden: boolean;
  sort_order: number;
  label: string | null;
};

function isPointRelatedLinkPayload(value: PointRelatedLinkPayload | null): value is PointRelatedLinkPayload {
  return value !== null;
}

export function hydratePointContentFormValues(point: ExperimentVideoPoint): PointContentFormValues {
  return {
    point_title: point.point_title,
    principle_mode: point.content?.principle_mode || "text",
    principle_equation: point.content?.principle_equation || "",
    principle_text: point.content?.principle_text || "",
    phenomenon_explanation: point.content?.phenomenon_explanation || "",
    safety_note: point.content?.safety_note || "",
    links: (point.related_links || []).map((link, index) => ({
      target: `${link.target_experiment_id}::${link.target_point_key}`,
      relation_type: link.relation_type === "default_override" ? "default_override" : "manual",
      hidden: Boolean(link.hidden),
      sort_order: link.sort_order || index + 1,
      label: link.label || "",
    })),
  };
}

export function buildPointContentRequest(values: PointContentFormValues): Record<string, unknown> {
  const principleMode = values.principle_mode || "text";
  return {
    point_title: values.point_title,
    principle_mode: principleMode,
    principle_equation: principleMode === "equation" ? values.principle_equation || "" : "",
    principle_text: principleMode === "text" ? values.principle_text || "" : "",
    phenomenon_explanation: values.phenomenon_explanation || "",
    safety_note: values.safety_note || "",
  };
}

export function buildPointRelatedLinksRequest(values: PointContentFormValues): { links: PointRelatedLinkPayload[] } {
  const links = (values.links || [])
    .map((link, index): PointRelatedLinkPayload | null => {
      const [targetExperimentId, targetPointKey] = String(link.target || "").split("::");
      if (!targetExperimentId || !targetPointKey) return null;
      return {
        target_experiment_id: targetExperimentId,
        target_point_key: targetPointKey,
        relation_type: link.relation_type || "manual",
        hidden: Boolean(link.hidden),
        sort_order: link.sort_order || index + 1,
        label: link.label || null,
      };
    })
    .filter(isPointRelatedLinkPayload);
  return { links };
}

export function buildPointPublicationRequest(action: "publish" | "unpublish" | "archive"): { action: "publish" | "unpublish" | "archive" } {
  return { action };
}
