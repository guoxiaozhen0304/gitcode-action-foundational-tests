# COMP-EXPR-01-055

- **标题**: hashFiles 函数边界行为
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 `hashFiles` 对单文件、多文件、无匹配路径的输出格式（64 位 hex SHA256 / 空值）。

## 做了什么
step 使用 `${{ hashFiles('package.json') }}` 计算单文件 hash，bash `[[ =~ ^[0-9a-f]{64}$ ]]` 校验格式；用 `${{ hashFiles('src/**', 'package.json') }}` 计算多文件组合 hash；用 `${{ hashFiles('nonexistent.xyz') }}` 测试无匹配时的行为。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: SINGLE_HEX64=yes | COVERED | `hashFiles('package.json')` 实际计算 SHA256，bash 正则校验 64 位 hex 后输出 |
| 2 | run_logs | positive | must_contain: MULTI_HEX64=yes | COVERED | `hashFiles('src/**', 'package.json')` 组合计算，bash 正则校验后输出 |
| 3 | run_logs | positive | must_contain: NONE_EMPTY=yes | COVERED | `hashFiles('nonexistent.xyz')` 无匹配，bash `[ -z "$H" ]` 判断为空后输出 |
