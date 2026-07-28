# COMP-SCRIPT-01-081

- **标题**: 仓库内脚本执行与路径验证
- **维度**: 完备性
- **评级**: 部分不符

---

## 想测什么
验证 run 支持执行仓库内相对路径脚本，脚本标准输出被捕获到日志。

## 做了什么
Step 1: `echo "inline_script_ok"`（字面量 echo）。Step 2: `./scripts/hello.sh || echo "script_fallback"`（真实脚本执行 + fallback）。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain inline_script_ok | TRIVIAL | assertion 仅检查 step 1 的字面量 echo，无 ${{ }}、无 real 命令 |
