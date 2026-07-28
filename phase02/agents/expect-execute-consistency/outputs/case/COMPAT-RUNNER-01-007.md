# COMPAT-RUNNER-01-007
- **标题**: Runner 预装工具链规格清单与实测全面对账
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
对ubuntu镜像Runner上java/mvn/gradle/node/go/kubectl/aws-cli的预装状态逐项探测，与官方预装清单对账。

## 做了什么
step1执行 `java -version`/`mvn -version`/`gradle -version`（含 || echo "XXX_MISSING"）；step2执行 `node --version`/`go version`/`kubectl version`/`aws --version` + `echo "AUDIT_DONE"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive must_contain | "AUDIT_DONE" | COVERED | step2中echo "AUDIT_DONE"直接覆盖(R1 GENUINE) |
| 2 | run_logs | positive llm | "逐项比对预装清单；文档列出但实测MISSING记为缺陷" | COVERED | 每个工具探测为真实命令(GENUINE R1)，输出在日志中；LLM辅助比对 |
| 3 | run_logs | negative llm | "不应出现文档列出但实测缺失而未登记" | COVERED | negative断言对账覆盖完整性；R5 LLM_DEPENDENT |
