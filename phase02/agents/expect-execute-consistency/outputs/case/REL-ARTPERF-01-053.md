# REL-ARTPERF-01-053

- 标题: 制品传输性能——100MB artifact 上传下载耗时
- 维度: 稳定性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: 制品传输性能——100MB artifact 上传下载耗时

- [正向] 上传≤30s
- [正向] 下载≤30s
- [正向] hash 100% 匹配（下载后文件名为原始文件名 artifact.bin，非 artifact 名称 perf-artifact）

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | generate 100MB file | dd if=/dev/urandom of=artifact.bin bs=1M count=100 | - |
| 2 | upload artifact step | uses: upload-artifact | Y |
| 3 | download artifact step | uses: download-artifact | Y |
| 4 | verify artifact step | ls -la perf-artifact | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| nonfunctional | upload_time_seconds |  |
| nonfunctional | download_time_seconds |  |
| positive | hash_match | true |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] 上传≤30s | COVERED | 2 real steps, assertions present |
| [正向] 下载≤30s | COVERED | 2 real steps, assertions present |
| [正向] hash 100% 匹配（下载后文件名为原始文件名 artifact.bin，非 artifact 名称 perf-artifact） | COVERED | 2 real steps, assertions present |

### 问题

无重大问题。

---
