import { Alert, Button, Divider, Form, Input, Modal, Segmented, Space } from "antd";
import type { FormInstance } from "antd";

import type { ExperimentVideoPoint } from "../../../api/experiments";
import type { PointContentFormValues } from "./pointContentMapper";
import { RelatedLinksEditor } from "./RelatedLinksEditor";

type MutationLike<T> = {
  isPending: boolean;
  mutate: (value: T) => void;
};

export function PointContentModal({
  contentPoint,
  form,
  pointTargetOptions,
  savePointContent,
  changePointPublication,
  onClose,
}: {
  contentPoint: ExperimentVideoPoint | null;
  form: FormInstance<PointContentFormValues>;
  pointTargetOptions: Array<{ value: string; label: string }>;
  savePointContent: MutationLike<PointContentFormValues>;
  changePointPublication: MutationLike<"publish" | "unpublish" | "archive">;
  onClose: () => void;
}) {
  return (
    <Modal
      title={contentPoint ? `编辑点位：${contentPoint.point_title}` : "编辑点位内容"}
      open={Boolean(contentPoint)}
      width={860}
      onCancel={onClose}
      footer={[
        <Button key="cancel" onClick={onClose}>
          关闭
        </Button>,
        <Button key="archive" danger disabled={!contentPoint} loading={changePointPublication.isPending} onClick={() => changePointPublication.mutate("archive")}>
          归档内容
        </Button>,
        <Button key="unpublish" disabled={!contentPoint} loading={changePointPublication.isPending} onClick={() => changePointPublication.mutate("unpublish")}>
          撤回发布
        </Button>,
        <Button key="save" loading={savePointContent.isPending} onClick={() => form.submit()}>
          保存草稿
        </Button>,
        <Button key="publish" type="primary" disabled={!contentPoint} loading={changePointPublication.isPending} onClick={() => changePointPublication.mutate("publish")}>
          发布并同步搜索
        </Button>,
      ]}
    >
      <Form form={form} layout="vertical" onFinish={(values) => savePointContent.mutate(values)}>
        <Space orientation="vertical" size={14} className="full">
          {contentPoint?.validation?.errors.length ? (
            <Alert type="warning" showIcon title="发布前需要补全内容" description={contentPoint.validation.errors.join("；")} />
          ) : null}
          <Form.Item name="point_title" label="点位标题" rules={[{ required: true, message: "请输入点位标题" }]}>
            <Input maxLength={200} />
          </Form.Item>
          <Form.Item name="principle_mode" label="实验原理类型" rules={[{ required: true }]}>
            <Segmented
              options={[
                { value: "equation", label: "化学方程式" },
                { value: "text", label: "文字描述" },
              ]}
            />
          </Form.Item>
          <Form.Item noStyle shouldUpdate={(prev, next) => prev.principle_mode !== next.principle_mode}>
            {({ getFieldValue }) =>
              getFieldValue("principle_mode") === "equation" ? (
                <Form.Item name="principle_equation" label="化学方程式" rules={[{ required: true, message: "请输入化学方程式" }]}>
                  <Input placeholder="Na2S2O3 + 2 HCl = 2 NaCl + S↓ + SO2↑ + H2O" />
                </Form.Item>
              ) : (
                <Form.Item name="principle_text" label="实验原理文字描述" rules={[{ required: true, message: "请输入实验原理文字描述" }]}>
                  <Input.TextArea rows={3} maxLength={500} showCount className="fixed-textarea" />
                </Form.Item>
              )
            }
          </Form.Item>
          <Form.Item name="phenomenon_explanation" label="现象解释" rules={[{ required: true, message: "请输入现象解释" }]}>
            <Input.TextArea rows={4} maxLength={800} showCount className="fixed-textarea" />
          </Form.Item>
          <Form.Item name="safety_note" label="安全提示" rules={[{ required: true, message: "请输入安全提示" }]}>
            <Input.TextArea rows={4} maxLength={800} showCount className="fixed-textarea" />
          </Form.Item>
          <Divider>相关实验链接</Divider>
          <RelatedLinksEditor pointTargetOptions={pointTargetOptions} />
        </Space>
      </Form>
    </Modal>
  );
}
