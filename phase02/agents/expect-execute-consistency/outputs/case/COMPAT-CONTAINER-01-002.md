# COMPAT-CONTAINER-01-002

- **标题**: container 自定义镜像被拒绝时应给出替代指引
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 job 使用自定义 container image（myregistry.com）时平台拒绝并给出替代方案。

## 做了什么
job 声明 container.image: myregistry.com/build-env:v1 和 options。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | validation_error | negative | llm_assisted | LLM_DEPENDENT | 需人工判定报错说明自定义镜像不被支持 |
| 2 | error_message | positive | llm_assisted | LLM_DEPENDENT | 需人工判定报错给出替代方案 |
