import { Button, Checkbox, Form, InputNumber, Select, Space } from "antd";
import type { DefaultOptionType } from "antd/es/select";
import { DeleteOutlined, PlusOutlined } from "@ant-design/icons";

export function RelatedLinksEditor({ pointTargetOptions }: { pointTargetOptions: DefaultOptionType[] }) {
  return (
    <Form.List name="links">
      {(fields, { add, remove }) => (
        <Space orientation="vertical" size={10} className="full">
          {fields.map((field) => (
            <div className="related-link-editor-row" key={field.key}>
              <Form.Item name={[field.name, "target"]} rules={[{ required: true, message: "请选择目标点位" }]}>
                <Select options={pointTargetOptions} placeholder="选择当前实验中的相关点位" />
              </Form.Item>
              <Form.Item name={[field.name, "relation_type"]}>
                <Select
                  options={[
                    { value: "manual", label: "人工链接" },
                    { value: "default_override", label: "默认链接覆盖" },
                  ]}
                />
              </Form.Item>
              <Form.Item name={[field.name, "sort_order"]}>
                <InputNumber min={1} />
              </Form.Item>
              <Form.Item name={[field.name, "hidden"]} valuePropName="checked">
                <Checkbox>隐藏</Checkbox>
              </Form.Item>
              <Button danger icon={<DeleteOutlined />} onClick={() => remove(field.name)}>
                删除
              </Button>
            </div>
          ))}
          <Button icon={<PlusOutlined />} onClick={() => add({ relation_type: "manual", hidden: false, sort_order: fields.length + 1 })}>
            添加相关点位
          </Button>
        </Space>
      )}
    </Form.List>
  );
}
