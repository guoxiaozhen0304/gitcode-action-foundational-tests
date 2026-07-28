# SEC-NAME-01-004
- **标题**: 与系统变量同名的用户自定义值绝不应覆盖 job 环境中的平台注入值
- **维度**: 安全性
- **优先级**: P1
- **评级**: 断言一致（2026-07-28 优化后重评）

## 修复内容
原步骤仅 echo 描述文字（两条 job_env 抽象断言 UNVERIFIABLE）。改为真实判定：比较 $ATOMGIT_ENV 是否被用户 env 遮蔽为 /tmp/fixture-shadow-path，被遮蔽输出 SYSTEM_VAR_SHADOWED_BAD 并 exit 1，否则 SYSTEM_VAR_PRESERVED_OK；断言全部确定化。

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain SYSTEM_VAR_PRESERVED_OK | ✅ GENUINE | 真实环境变量比对后输出 |
| 2 | run_logs | negative | must_not_contain SYSTEM_VAR_SHADOWED_BAD | ✅ GENUINE | 被遮蔽时输出并 exit 1 |
