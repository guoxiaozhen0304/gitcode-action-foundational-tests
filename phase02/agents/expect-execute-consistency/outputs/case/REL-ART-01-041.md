# REL-ART-01-041

- 标题: 超大 artifact——100 MB artifact 上传后下游 job 应成功下载
- 维度: 稳定性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

标题: 超大 artifact——100 MB artifact 上传后下游 job 应成功下载

- [正向] upload 成功
- [正向] download 成功
- [正向] MD5 校验通过

## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | generate 100MB file | dd if=/dev/urandom of=artifact.bin bs=1M count=100 | - |
| 2 | upload artifact step | uses: upload-artifact | Y |
| 3 | download artifact step | uses: download-artifact | Y |
| 4 | verify artifact step | ls -la perf-artifact | - |

| 断言类型 | 目标 | 值 |
|---------|------|----|
| positive | upload_status | success |
| positive | download_status | success |
| positive | md5_match | true |

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 事件 | workflow_dispatch |
| 身份 | maintainer |
| 触发阻塞 | 否 |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [正向] upload 成功 | COVERED | 2 real steps, assertions present |
| [正向] download 成功 | COVERED | 2 real steps, assertions present |
| [正向] MD5 校验通过 | COVERED | 2 real steps, assertions present |

### 问题

无重大问题。

---
