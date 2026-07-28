# REL-CONC-01-002
- **标题**: concurrency.max=6 配置应被系统拒绝
- **维度**: reliability
- **评级**: 断言一致
## 想测什么
创建 concurrency.max=6 的 workflow（超出允许范围），验证 YAML 校验失败/保存被拒，不应静默截断为 5。
## 做了什么
YAML 定义 concurrency max:6（非法值），sleep 10。平台应对不合规 YAML 在校验阶段拒绝。
## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | yaml_validation | positive | equals rejected | COVERED | YAML 包含非法配置 max:6 → 平台校验拒绝 → 对应文本"YAML 校验失败或保存被拒"，按校准 8 malformed YAML platform reject → COVERED |
| 2 | run_status | negative | equals should_not_start | COVERED | YAML 负向断言不应 start，对应文本"不应静默截断为 5" |
