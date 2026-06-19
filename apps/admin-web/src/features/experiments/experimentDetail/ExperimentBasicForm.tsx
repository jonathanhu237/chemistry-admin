import { Button, Card, Form, Input, Select } from "antd";
import type { FormInstance } from "antd";

type SaveMutation = {
  isPending: boolean;
  mutate: (values: { title: string; summary?: string; status: string; chapter_ids: string[] }) => void;
};

export function ExperimentBasicForm({
  form,
  save,
  chapterOptions,
}: {
  form: FormInstance;
  save: SaveMutation;
  chapterOptions: Array<{ value: string; label: string }>;
}) {
  return (
    <Card title="基础信息" className="experiment-basic-card">
      <Form form={form} layout="vertical" onFinish={(values) => save.mutate(values)}>
        <Form.Item name="title" label="实验名称" rules={[{ required: true, message: "请输入实验名称" }]}>
          <Input />
        </Form.Item>
        <Form.Item name="summary" label="实验说明">
          <Input.TextArea rows={4} maxLength={300} showCount className="fixed-textarea" />
        </Form.Item>
        <div className="compact-form-grid">
          <Form.Item name="status" label="发布状态" rules={[{ required: true }]}>
            <Select
              options={[
                { value: "draft", label: "草稿" },
                { value: "published", label: "已发布" },
                { value: "archived", label: "已归档" },
              ]}
            />
          </Form.Item>
          <Form.Item name="chapter_ids" label="理论章节" rules={[{ required: true, message: "请选择至少一个章节" }]}>
            <Select mode="multiple" options={chapterOptions} placeholder="选择章节" maxTagCount="responsive" />
          </Form.Item>
        </div>
        <Button type="primary" htmlType="submit" loading={save.isPending}>
          保存实验信息
        </Button>
      </Form>
    </Card>
  );
}
