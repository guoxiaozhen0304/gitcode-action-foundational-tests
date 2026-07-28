# COMP-EXPR-01-055
- **标题**: hashFiles 函数边界行为
- **维度**: completeness
- **评级**: 断言一致

## 想测什么
hashFiles 返回 64 位十六进制 SHA256 值，多文件组合计算，不匹配路径返回空。

## 做了什么
1. step `Single file hash`：`H="${{ hashFiles('package.json') }}"`，echo 并正则校验 64 位 hex
2. step `Multi pattern hash`：`H="${{ hashFiles('src/**', 'package.json') }}"`，echo 并正则校验
3. step `No match hash`：`H="${{ hashFiles('nonexistent.xyz') }}"`，echo 并检查是否为空

## 逐断言判定
| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_logs | positive | must_contain: SINGLE_HEX64=yes | COVERED | ${{ hashFiles('package.json') }} 表达式 + bash 正则校验 |
| 2 | run_logs | positive | must_contain: MULTI_HEX64=yes | COVERED | ${{ hashFiles('src/**', 'package.json') }} 表达式 + 正则校验 |
| 3 | run_logs | positive | must_contain: NONE_EMPTY=yes | COVERED | hashFiles('nonexistent.xyz') 返回空，[ -z "$H" ] 校验 |
