# COMPAT-CTX-01-001

- **标题**: 使用 github.ref 上下文应报错或求值为空
- **维度**: 兼容性
- **评级**: 断言一致

---

## 想测什么
验证 ${{ github.ref }} 在 GitCode 平台不应被静默映射为 atomgit.ref。

## 做了什么
echo "github_ref=${{ github.ref }}"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | negative | llm_assisted | LLM_DEPENDENT | 需人工判定 github_ref 为空或不支持而失败 |
| 2 | error_message | nonfunctional | llm_assisted | LLM_DEPENDENT | 需人工判定报错提示替换为 atomgit.* |
