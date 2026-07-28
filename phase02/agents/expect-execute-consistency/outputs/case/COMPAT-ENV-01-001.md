# COMPAT-ENV-01-001

- **标题**: ATOMGIT_SHA 环境变量应正确返回触发提交 SHA
- **维度**: 兼容性
- **评级**: 部分不符

---

## 想测什么
验证 ATOMGIT_SHA 环境变量返回当前触发事件的提交 SHA。

## 做了什么
echo "atomgit_sha=$ATOMGIT_SHA"。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | TRIVIAL | 仅有 echo 步骤，无条件失败路径，必然成功 |
| 2 | run_logs | positive | llm_assisted | LLM_DEPENDENT | 需人工判定 atomgit_sha 含有效 40 位十六进制 SHA |
