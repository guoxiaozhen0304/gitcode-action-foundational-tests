# inputs/gitcode-api/ （**必需**）— 已补充 ✅

GitCode **v5 全平台 API** 参考手册 + v8 Actions API 历史参考。agent 基于此文档组装 API 调用参数，辅助第二部分测试执行。

## 内容

- **[openapi.json](openapi.json)** — **v5 全平台 API OpenAPI 定义（推荐主参考）**
  - 覆盖：仓库、MR、Issues、Packages、用户、权限、Actions 等全模块
  - Base URL: `https://gitcode.com`
  - 认证: OAuth2 Bearer `Authorization: Bearer <token>`
  - 2026-08-18 补充

- **[api-reference.md](api-reference.md)** — 20 个 v8 Actions API 端点历史参考（已逐步迁移至 v5）
  - Base URL: `https://api.gitcode.com`（旧地址）
  - 认证: OAuth2.0 `access_token` query parameter（旧方式）
  - 2026-07-20

## 消费方

- **case-writer agent**: 编译 YAML 时，为 API 可验证的断言标注可用的 API 端点
- **第二部分 harness**: 执行时直接依据本文档组装 API 调用（`api_runner.py` 默认读取 v5）

## 状态

- v5 全平台 API: ✅ 已补充（`openapi.json` / 2026-08-18）
- v8 Actions API: ⚠️ 历史保留（`api-reference.md` / 2026-07-20，逐步迁移中）
