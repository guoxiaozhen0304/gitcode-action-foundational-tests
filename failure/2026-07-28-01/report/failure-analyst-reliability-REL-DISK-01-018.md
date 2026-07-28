## 失败分诊 · REL-DISK-01-018 · Runner 磁盘边界——small runner 写入 49 GB 应成功

**判定结果**: FAIL
**失败断言**: assertions[0] (job_status, positive) — 期望 job_status == COMPLETED，实际 disk boundary test=FAILED

**根因初判**: 产品bug

**责任人**: 平台方 — 官方托管 Runner small (2核8G) 规格文档声明磁盘 50 GB，实际可用磁盘远小于声明值

**证据**:

- **Job 日志全量**（12 行）:
  ```
  [2026/07/28 13:17:02.610 GMT+08:00] [INFO] Job(1531651699410604032_1531651699385438215) duration check: true
  No shell specified, using platform default: default-bash
  ::debug::Script file created: /home/slave1/runner/workers/0.0.4.4.version/_temp/e616ac63-2042-41af-9463-1f912d640acc.sh
  ::debug::Executing: bash -e /home/slave1/runner/workers/0.0.4.4.version/_temp/e616ac63-2042-41af-9463-1f912d640acc.sh
  fallocate: fallocate failed: No space left on device
  dd: error writing 'testfile': No space left on device
  36189+0 records in
  36188+0 records out
  37946486784 bytes (38 GB, 35 GiB) copied, 317.101 s, 120 MB/s
  ::error::Process exited with code 1
  ```
  - `fallocate -l 49G testfile`：直接失败，报 `No space left on device`——预分配即判定磁盘不足。
  - `dd` 回退路径：仅写入 36,188 个 1MB block（~37.9 GB），在第 36,189 个 block 写入时报 `No space left on device` 退出。
  - 结论：small Runner 的实际可用磁盘空间约为 35-38 GiB（~38 GB），远低于文档声明的 50 GB。

- **预期行为**（Phase 01 文本用例 `phase01/runs/2026-07-27-01/cases/text/REL-DISK-01-018.md`，优先级 P1，维度 stability）:
  - 操作步骤 1: "触发 runs-on=[ubuntu-latest,x64,small] 的 workflow，job 顺序写入 49 GB 文件"
  - 预期结果: "job 状态=success" / "df 显示剩余约 1 GB"
  - 验证点 [正向]: "job 状态=success"
  - 验证点 [负向]: "不应在 49 GB 时报磁盘满"

- **实际行为**:
  - 写入到约 37.9 GB 时磁盘满，job 以 exit code 1 失败。
  - 49 GB 写入目标完全未达到——实际可写入量仅目标的 ~77%。

- **对照 GitCode 规格**:
  - `phase01/inputs/gitcode-spec/core-concepts/runner-and-environment.md` 第 21-28 行「资源规格详表」：small 规格的磁盘列明确标注为 **50 GB**。
    ```
    | `small` | 2 | 8 | 50 | 常规构建与测试（**默认**） |
    ```
  - 测试 YAML 中 `runs-on: [ubuntu-latest, x64, small]` 与规格示例写法完全一致——文档确凿承诺 small Runner 提供 50 GB 磁盘空间。
  - 测试 YAML 中 `fallocate -l 49G` 写入 49 GB（仅占文档承诺 50 GB 的 98%），是该规格下的合理边界测试。

**置信度**: 高（日志直接显示 `No space left on device` 错误 + dd 仅写入 37.9 GB 的实际字节数；规格第 25 行明确标注 small=50GB 磁盘；49 GB 写入请求是 50 GB 承诺下的合理边界）

**影响**:
- **阻塞性**: 🔴阻塞 — 磁盘空间不足直接导致 job 失败，阻止任何涉及 >38 GB 磁盘 I/O 的工作负载
- **静默性**: 🟡可察觉 — job 报 `No space left on device` 错误，用户能感知失败，但错误信息未提示"磁盘容量与文档不符"
- **影响面**: 🟡同维度 — 影响所有依赖 small Runner 磁盘 ≥50 GB 承诺的重 I/O 用例（大文件构建、数据密集型测试、大型缓存恢复）
- **综合**: 阻塞——small Runner 磁盘实际可用 ~38 GB 而非文档承诺的 50 GB，49 GB 边界测试直接因磁盘满而失败，用户按文档规划磁盘用量会踩坑
- **是否有规避手段**: 是 — 用户可升级到 medium（100 GB）或 large（200 GB）规格，但会增加成本和等待时间

**建议**:
- 确认 small Runner 节点的实际磁盘空间：是物理磁盘只有 40 GB（文档写错），还是磁盘有 50 GB 但 OS/runner-agent/preinstalled-tools 占用了过多空间导致可用不足（需在文档中标注"可用空间"而非"总磁盘"）
- 若实际磁盘确实不足 50 GB，需同步更新文档中的磁盘列数值，或调整 runner 镜像减少预装工具占用
- 相关用例: 所有依赖 small Runner 磁盘 = 50 GB 承诺的容量边界用例
