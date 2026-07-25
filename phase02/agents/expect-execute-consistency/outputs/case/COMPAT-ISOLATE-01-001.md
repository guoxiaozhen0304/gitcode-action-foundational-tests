# COMPAT-ISOLATE-01-001

- 标题: Runner 环境隔离——跨 job 文件隔离
- 维度: 兼容性 | 优先级: P1
- 评级: 断言一致

---

## 1. 想测什么（规格）

用例 ID:   COMPAT-ISOLATE-01-001
维度标签:   [compatibility, reliability]
维度:      兼容性
优先级:    P1
溯源意图:  INTENT-COMPAT-028
参照来源:  inputs/gitcode-spec/runner-management/selecting-runner-labels.md; inputs/platform-config/instance-config.md
母意图:    —
标题:      Runner 环境隔离——跨 job 文件隔离

前置条件:
  - 平台提供多 job 工作流执行能力
  - Runner 为官方托管资源池或等效隔离环境

操作步骤:
  1. 在 job A 中于 workspace 和 /tmp 写入唯一标记文件
  2. 在 job B 中尝试读取 job A 写入的标记文件
  3. 验证 job B 无法访问 job A 的文件残留

预期结果:
  - job B 无法读取到 job A 在 workspace 或 /tmp 中写入的文件
  - 每个 job 获得独立的文件系统视图
  - 隔离行为与 GitHub Actions 的 job 级隔离语义一致

验证点:
  - [负向] job B 中不存在 job A 的 workspace 标记文件
  - [负向] job B 中不存在 job A 的 /tmp 标记文件
  - [正向] 系统为每个 job 提供独立执行环境

清理:      fixture


## 2. 实际做了什么（实现）

| # | 步骤名 | 关键内容 | 实质逻辑 |
|---|--------|------|:---:|
| 1 | (TC) write workspace marker | run: echo "ISOLATION_MARKER_$(date +%s)" > workspace_marker.txt
 | 是 |
| 2 | (TC) write tmp marker | run: echo "ISOLATION_MARKER_TMP_$(date +%s)" > /tmp/isolation_marker.txt
 | 是 |
| 3 | (TC) output marker names | run: echo "workspace_marker=workspace_marker.txt" >> "$ATOMGIT_OUTPUT"
echo "tmp_marker=/tmp/isolation_marker.txt" >> "$ATOMGIT_OUTPUT"
 | 是 |
| 4 | (TC) verify workspace isolation | run: if ls workspace_marker.txt 2>/dev/null; then
  echo "ISOLATION_BROKEN_WORKSPACE"
  exit 1
else
  echo "WORKSPACE_ISOLATED_OK"
fi
 | 是 |
| 5 | (TC) verify tmp isolation | run: if ls /tmp/isolation_marker.txt 2>/dev/null; then
  echo "ISOLATION_BROKEN_TMP"
  exit 1
else
  echo "TMP_ISOLATED_OK"
fi
 | 是 |

<details><summary>完整 workflow YAML</summary>

```yaml
on:
  workflow_dispatch:
jobs:
  job-write:
    name: Write isolation markers
    runs-on: [ubuntu-latest, x64, small]
    steps:
      - name: (TC) write workspace marker
        run: |
          echo "ISOLATION_MARKER_$(date +%s)" > workspace_marker.txt
      - name: (TC) write tmp marker
        run: |
          echo "ISOLATION_MARKER_TMP_$(date +%s)" > /tmp/isolation_marker.txt
      - name: (TC) output marker names
        run: |
          echo "workspace_marker=workspace_marker.txt" >> "$ATOMGIT_OUTPUT"
          echo "tmp_marker=/tmp/isolation_marker.txt" >> "$ATOMGIT_OUTPUT"
  job-verify:
    name: Verify file isolation
    runs-on: [ubuntu-latest, x64, small]
    needs: job-write
    steps:
      - name: (TC) verify workspace isolation
        run: |
          if ls workspace_marker.txt 2>/dev/null; then
            echo "ISOLATION_BROKEN_WORKSPACE"
            exit 1
          else
            echo "WORKSPACE_ISOLATED_OK"
          fi
      - name: (TC) verify tmp isolation
        run: |
          if ls /tmp/isolation_marker.txt 2>/dev/null; then
            echo "ISOLATION_BROKEN_TMP"
            exit 1
          else
            echo "TMP_ISOLATED_OK"
          fi

```
</details>

## 3. 触发与运行环境

| 字段 | 值 |
|------|----|
| 触发事件 | workflow_dispatch |
| 触发身份 | maintainer |
| Repo Fixture | default |
| Secrets | N/A |

## 4. 规格 vs 实现对照

| 验证点 | 覆盖? | 说明 |
|------|:---:|------|
| [负向] job B 中不存在 job A 的 workspace 标记文件 | ✅ COVERED | negative assertion in YAML assertions |
| [负向] job B 中不存在 job A 的 /tmp 标记文件 | ✅ COVERED | negative assertion in YAML assertions |
| [正向] 系统为每个 job 提供独立执行环境 | ✅ COVERED | steps have real logic |

### 问题

无

---
