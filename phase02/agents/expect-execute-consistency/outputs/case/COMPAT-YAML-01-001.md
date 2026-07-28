# COMPAT-YAML-01-001
- **标题**: YAML 1.1 on 键布尔陷阱与 env 中 yes/no/on/off 字面量
- **维度**: 兼容性
- **评级**: 断言一致

## 想测什么
验证顶层 `on` 键不被YAML 1.1解析为布尔true导致workflow静默不触发，以及env中`on`字面值的类型行为。

## 做了什么
workflow配置 `on: push: branches: [main]` + `env: {DEBUG_FLAG: on}`，push触发，step输出 `echo "DEBUG_FLAG=[$DEBUG_FLAG]"` + `echo "ON_KEY_OK"`。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|---|---|---|---|---|
| 1 | run_logs | positive must_contain | "ON_KEY_OK" | COVERED | echo直接覆盖(R1 GENUINE)，该标记证明workflow被正常触发执行 |
| 2 | run_list | negative llm | "push后不应出现workflow静默不触发" | COVERED | ON_KEY_OK出现即证明触发成功；若run_list中无记录则证明静默不触发缺陷 |
| 3 | run_logs | positive llm | "DEBUG_FLAG取值(字符串on或布尔翻转值)与GitHub比对" | COVERED | $DEBUG_FLAG为env环境变量(GENUINE R1)；[$DEBUG_FLAG]在日志中可见实际取值 |
