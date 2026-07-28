# COMP-ARTIFACT-01-001

- **标题**: artifact 可在同 workflow 的 job 间正确传递
- **维度**: 完备性
- **评级**: 断言一致

---

## 想测什么
验证 artifact 通过 `upload-artifact` / `download-artifact` 在同一个 workflow 的不同 job 之间正确传递，内容一致。

## 做了什么
job1 创建 `dist/app.txt`（内容 `hello artifact`）并 upload-artifact；job2 通过 `needs: build` 依赖下载 artifact 后 `cat` 文件内容验证。

## 逐断言判定

| # | 目标 | 类型 | 期望 | 判定 | 说明 |
|---|------|------|------|------|------|
| 1 | run_status | positive | equals: success | COVERED | 整个 pipeline（上传→下载→验证）成功，校验有意义 |
| 2 | run_logs | positive | contains: hello artifact | COVERED | verify job 中 `cat dist/app.txt` 直接输出文件内容 `hello artifact` |
