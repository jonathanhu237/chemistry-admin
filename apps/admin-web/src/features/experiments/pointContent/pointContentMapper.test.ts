import { describe, expect, it } from "vitest";
import type { ExperimentVideoPoint } from "../../../api/experiments";
import {
  buildPointContentRequest,
  buildPointPublicationRequest,
  buildPointRelatedLinksRequest,
  hydratePointContentFormValues,
} from "./pointContentMapper";

describe("point content request builders", () => {
  it("keeps equation and text principle modes mutually exclusive", () => {
    expect(
      buildPointContentRequest({
        point_title: "Na2S2O3 + HCl",
        principle_mode: "equation",
        principle_equation: "Na2S2O3 + 2 HCl = 2 NaCl + S↓ + SO2↑ + H2O",
        principle_text: "should not be primary",
        phenomenon_explanation: "生成硫和二氧化硫。",
        safety_note: "通风橱操作。",
      }),
    ).toEqual({
      point_title: "Na2S2O3 + HCl",
      principle_mode: "equation",
      principle_equation: "Na2S2O3 + 2 HCl = 2 NaCl + S↓ + SO2↑ + H2O",
      principle_text: "",
      phenomenon_explanation: "生成硫和二氧化硫。",
      safety_note: "通风橱操作。",
    });

    expect(
      buildPointContentRequest({
        point_title: "文字原理",
        principle_mode: "text",
        principle_equation: "H2 + Cl2 = 2 HCl",
        principle_text: "氯气具有氧化性。",
      }),
    ).toMatchObject({
      principle_mode: "text",
      principle_equation: "",
      principle_text: "氯气具有氧化性。",
      phenomenon_explanation: "",
      safety_note: "",
    });
  });

  it("builds related link and publication payloads without touching video resources", () => {
    expect(
      buildPointRelatedLinksRequest({
        point_title: "source",
        principle_mode: "text",
        links: [
          { target: "EXP_1::point-a", relation_type: "manual", label: "相邻实验", sort_order: 2 },
          { target: "EXP_1::point-b", relation_type: "default_override", hidden: true },
          { target: "" },
        ],
      }),
    ).toEqual({
      links: [
        {
          target_experiment_id: "EXP_1",
          target_point_key: "point-a",
          relation_type: "manual",
          hidden: false,
          sort_order: 2,
          label: "相邻实验",
        },
        {
          target_experiment_id: "EXP_1",
          target_point_key: "point-b",
          relation_type: "default_override",
          hidden: true,
          sort_order: 2,
          label: null,
        },
      ],
    });
    expect(buildPointPublicationRequest("publish")).toEqual({ action: "publish" });
  });

  it("hydrates point form values from existing content and related links", () => {
    const point: ExperimentVideoPoint = {
      point_key: "point-a",
      point_title: "点位 A",
      source: "manual",
      resources: [],
      resource_count: 0,
      published_count: 0,
      content: {
        principle_mode: "equation",
        principle_equation: "H2 + Cl2 = 2 HCl",
        principle_text: null,
        phenomenon_explanation: "产生白雾。",
        safety_note: "避免强光直射。",
        content_status: "draft",
      },
      related_links: [
        {
          target_experiment_id: "EXP_2",
          target_point_key: "point-b",
          relation_type: "default_override",
          hidden: true,
          label: null,
        },
      ],
    };

    expect(hydratePointContentFormValues(point)).toMatchObject({
      point_title: "点位 A",
      principle_mode: "equation",
      principle_equation: "H2 + Cl2 = 2 HCl",
      principle_text: "",
      links: [{ target: "EXP_2::point-b", relation_type: "default_override", hidden: true, sort_order: 1, label: "" }],
    });
  });
});
