# USE-DIR-01-001
- **标题**: workflow 放置于 .gitcode/workflows/ 下可正常触发
- **维度**: usability
- **评级**: 断言一致

## 想测什么
.gitcode/workflows/ 下的 workflow 文件被正常识别并触发运行。

## 做了什么
step `echo "workflow triggered from .gitcode/workflows/"`。断言检查 run_status。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals:COMPLETED | COVERED | 平台 run_status，GENUINE |
