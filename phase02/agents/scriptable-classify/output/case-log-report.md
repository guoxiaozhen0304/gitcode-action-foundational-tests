# Scriptable-Classify Cases: Test Log Report

**Total:** 129 | **Tested (has log):** 74 | **Untested (no log):** 55

## Rule 1: schedule trigger (12) — tested: 0, untested: 12

| # | Case ID | Log |
|---|---------|-----|
| 1 | `COMP-BOUND-01-085` | **NO LOG** |
| 2 | `COMP-SCHEDULE-01-001` | **NO LOG** |
| 3 | `COMP-SCHEDULE-01-002` | **NO LOG** |
| 4 | `COMP-SCHEDULE-01-003` | **NO LOG** |
| 5 | `COMP-TRIG-01-075` | **NO LOG** |
| 6 | `COMPAT-SCHEDULE-01-001` | **NO LOG** |
| 7 | `COMPAT-SCHEDULE-01-002` | **NO LOG** |
| 8 | `COMPAT-SCHEDULE-01-003` | **NO LOG** |
| 9 | `COMPAT-SCHEDULE-01-004` | **NO LOG** |
| 10 | `REL-SCHED-01-058` | **NO LOG** |
| 11 | `USE-DOC-01-003` | **NO LOG** |
| 12 | `USE-SCHED-01-001` | **NO LOG** |

## Rule 2: complex target (8) — tested: 5, untested: 3

| # | Case ID | Log |
|---|---------|-----|
| 1 | `COMP-CACHE-01-001` | `failure/2026-07-24/COMP-CACHE-01-001.log` |
| 2 | `COMP-RERUN-01-001` | **NO LOG** |
| 3 | `COMP-SUMMARY-01-001` | `failure/2026-07-24-valid297-final2/result/COMP-SUMMARY-01-001.log.txt` |
| 4 | `SEC-ARTF-01-001` | **NO LOG** |
| 5 | `SEC-ARTF-01-003` | **NO LOG** |
| 6 | `SEC-MASK-01-002` | `failure/2026-07-24/SEC-MASK-01-002.log` |
| 7 | `SEC-SIDE-01-002` | `failure/2026-07-24/SEC-SIDE-01-002.log` |
| 8 | `USE-MD-01-001` | `failure/2026-07-24-valid297-final2/result/USE-MD-01-001.log.txt` |

## Rule 2b: fault injection (10) — tested: 3, untested: 7

| # | Case ID | Log |
|---|---------|-----|
| 1 | `REL-CLUSTER-01-001` | **NO LOG** |
| 2 | `REL-FAULT-01-031` | `failure/2026-07-24/REL-FAULT-01-031.log` |
| 3 | `REL-FAULT-01-032` | `failure/2026-07-24/REL-FAULT-01-032.log` |
| 4 | `REL-FAULT-01-033` | `failure/2026-07-24/REL-FAULT-01-033.log` |
| 5 | `REL-FAULT-01-034` | **NO LOG** |
| 6 | `REL-FAULT-01-035` | **NO LOG** |
| 7 | `REL-FAULT-01-036` | **NO LOG** |
| 8 | `REL-FAULT-01-037` | **NO LOG** |
| 9 | `REL-FAULT-01-038` | **NO LOG** |
| 10 | `REL-FAULT-01-039` | **NO LOG** |

## Rule 4: timing (33) — tested: 7, untested: 26

| # | Case ID | Log |
|---|---------|-----|
| 1 | `COMP-ACT-01-003` | **NO LOG** |
| 2 | `COMP-TIMEOUT-01-001` | `failure/2026-07-24/COMP-TIMEOUT-01-001.log` |
| 3 | `REL-API-01-065` | **NO LOG** |
| 4 | `REL-ARTPERF-01-053` | `failure/2026-07-24/REL-ARTPERF-01-053.log` |
| 5 | `REL-ARTPERF-01-053-V2` | `failure/2026-07-24/REL-ARTPERF-01-053-V2.log` |
| 6 | `REL-CACHEPERF-01-054` | **NO LOG** |
| 7 | `REL-CANCEL-01-029` | **NO LOG** |
| 8 | `REL-CANCELREL-01-061` | **NO LOG** |
| 9 | `REL-CONC-01-001` | `failure/2026-07-24/REL-CONC-01-001.log` |
| 10 | `REL-CPU-01-022` | **NO LOG** |
| 11 | `REL-FAIR-01-044` | **NO LOG** |
| 12 | `REL-FLOOD-01-037` | **NO LOG** |
| 13 | `REL-IMAGE-01-052` | **NO LOG** |
| 14 | `REL-IMAGE-01-052-V2` | **NO LOG** |
| 15 | `REL-LATENCY-01-050` | **NO LOG** |
| 16 | `REL-LATENCY-01-050-V2` | **NO LOG** |
| 17 | `REL-LOGPERF-01-051` | **NO LOG** |
| 18 | `REL-LOGPERF-01-051-V2` | **NO LOG** |
| 19 | `REL-LOGPERF-01-052` | **NO LOG** |
| 20 | `REL-LONG-01-043` | **NO LOG** |
| 21 | `REL-MATRIX-01-039` | `failure/2026-07-24/REL-MATRIX-01-039.log` |
| 22 | `REL-MATRIX-01-040` | **NO LOG** |
| 23 | `REL-NEEDS-01-026` | **NO LOG** |
| 24 | `REL-NETFAULT-01-062` | **NO LOG** |
| 25 | `REL-PRESSURE-01-055` | **NO LOG** |
| 26 | `REL-PROJLIMIT-01-067` | **NO LOG** |
| 27 | `REL-PROJLIMIT-01-068` | **NO LOG** |
| 28 | `REL-REG-01-001` | **NO LOG** |
| 29 | `REL-SCHED-01-057` | **NO LOG** |
| 30 | `REL-STATE-01-058` | **NO LOG** |
| 31 | `REL-STATE-01-059` | **NO LOG** |
| 32 | `REL-TIMEOUT-01-007` | `failure/2026-07-24/REL-TIMEOUT-01-007.log` |
| 33 | `REL-TIMEOUT-01-009` | `failure/2026-07-24/REL-TIMEOUT-01-009.log` |

## Rule 5: UI (3) — tested: 1, untested: 2

| # | Case ID | Log |
|---|---------|-----|
| 1 | `USE-BADGE-01-001` | **NO LOG** |
| 2 | `USE-LOG-01-001` | `failure/2026-07-24/USE-LOG-01-001.log` |
| 3 | `USE-SEARCH-01-001` | **NO LOG** |

## Hardcoded (63) — tested: 58, untested: 5

| # | Case ID | Log |
|---|---------|-----|
| 1 | `COMP-ARTIFACT-01-001` | `failure/2026-07-24-valid297-final2/result/COMP-ARTIFACT-01-001.log.txt` |
| 2 | `COMP-ARTIFACT-01-002` | `failure/2026-07-24/COMP-ARTIFACT-01-002.log` |
| 3 | `COMP-PERMS-01-001` | `failure/2026-07-24/COMP-PERMS-01-001.log` |
| 4 | `COMP-PERMS-01-002` | `failure/2026-07-24/COMP-PERMS-01-002.log` |
| 5 | `COMP-PERMS-01-003` | `failure/2026-07-24-valid297-final2/result/COMP-PERMS-01-003.log.txt` |
| 6 | `COMP-PR-01-001` | `failure/2026-07-24-valid297-final2/result/COMP-PR-01-001.log.txt` |
| 7 | `COMP-PR-01-003` | `failure/2026-07-24-valid297-final2/result/COMP-PR-01-003.log.txt` |
| 8 | `COMP-RERUN-01-002` | **NO LOG** |
| 9 | `COMP-RERUN-01-003` | **NO LOG** |
| 10 | `COMP-SECRET-01-001` | `failure/2026-07-24/COMP-SECRET-01-001.log` |
| 11 | `COMP-TIMEOUT-01-002` | `failure/2026-07-24/COMP-TIMEOUT-01-002.log` |
| 12 | `COMPAT-CONTAINER-01-001` | `failure/2026-07-25-01/result/COMPAT-CONTAINER-01-001.log.txt` |
| 13 | `COMPAT-DEPR-01-002` | `failure/2026-07-25-01/result/COMPAT-DEPR-01-002.log.txt` |
| 14 | `COMPAT-EXPR-01-002` | `failure/2026-07-24/COMPAT-EXPR-01-002.log` |
| 15 | `COMPAT-EXPR-01-003` | `failure/2026-07-24/COMPAT-EXPR-01-003.log` |
| 16 | `COMPAT-INPUTS-01-001` | `failure/2026-07-24-valid297-final2/result/COMPAT-INPUTS-01-001.log.txt` |
| 17 | `COMPAT-MATRIX-01-003` | `failure/2026-07-25-01/result/COMPAT-MATRIX-01-003.log.txt` |
| 18 | `COMPAT-MATRIX-01-004` | `failure/2026-07-25-01/result/COMPAT-MATRIX-01-004.log.txt` |
| 19 | `COMPAT-OUTCOME-01-002` | `failure/2026-07-24/COMPAT-OUTCOME-01-002.log` |
| 20 | `COMPAT-OUTCOME-01-003` | `failure/2026-07-24-valid297-final2/result/COMPAT-OUTCOME-01-003.log.txt` |
| 21 | `COMPAT-PERM-01-001` | `failure/2026-07-24/COMPAT-PERM-01-001.log` |
| 22 | `COMPAT-PR-01-006` | `failure/2026-07-25-01/result/COMPAT-PR-01-006.log.txt` |
| 23 | `COMPAT-VARS-01-006` | `failure/2026-07-24-valid297-final2/result/COMPAT-VARS-01-006.log.txt` |
| 24 | `REL-ART-01-041` | `failure/2026-07-24/REL-ART-01-041.log` |
| 25 | `REL-ARTCONC-01-063` | `failure/2026-07-24/REL-ARTCONC-01-063.log` |
| 26 | `REL-BIGRUNNER-01-066` | `failure/2026-07-24-valid297-final2/result/REL-BIGRUNNER-01-066.log.txt` |
| 27 | `REL-CANCEL-01-028` | `failure/2026-07-24/REL-CANCEL-01-028.log` |
| 28 | `REL-CONTINUE-01-030` | `failure/2026-07-24/REL-CONTINUE-01-030.log` |
| 29 | `REL-K8S-01-045` | `failure/2026-07-24/REL-K8S-01-045.log` |
| 30 | `REL-MATRIX-01-026` | `failure/2026-07-24-valid297-final2/result/REL-MATRIX-01-026.log.txt` |
| 31 | `REL-MATRIX-01-038` | `failure/2026-07-24/REL-MATRIX-01-038.log` |
| 32 | `REL-NEEDS-01-025` | `failure/2026-07-24/REL-NEEDS-01-025.log` |
| 33 | `REL-PREEMPT-01-005` | **NO LOG** |
| 34 | `REL-QUEUE-01-003` | `failure/2026-07-24/REL-QUEUE-01-003.log` |
| 35 | `REL-RERUN-01-011` | `failure/2026-07-24/REL-RERUN-01-011.log` |
| 36 | `REL-RERUN-01-012` | **NO LOG** |
| 37 | `REL-RERUN-01-013` | **NO LOG** |
| 38 | `REL-RUNNER-01-049-V2` | `failure/2026-07-24-valid297-final2/result/REL-RUNNER-01-049-V2.log.txt` |
| 39 | `REL-YAMLCACHE-01-060` | `failure/2026-07-24/REL-YAMLCACHE-01-060.log` |
| 40 | `SEC-BASE-01-001` | `failure/2026-07-24-valid297-final2/result/SEC-BASE-01-001.log.txt` |
| 41 | `SEC-BASE-01-002` | `failure/2026-07-24-valid297-final2/result/SEC-BASE-01-002.log.txt` |
| 42 | `SEC-FORK-01-001` | `failure/2026-07-24-valid297-final2/result/SEC-FORK-01-001.log.txt` |
| 43 | `SEC-FORK-01-002` | `failure/2026-07-24-valid297-final2/result/SEC-FORK-01-002.log.txt` |
| 44 | `SEC-MASK-01-001` | `failure/2026-07-24/SEC-MASK-01-001.log` |
| 45 | `SEC-MASK-01-005` | `failure/2026-07-24/SEC-MASK-01-005.log` |
| 46 | `SEC-NAME-01-001` | `failure/2026-07-24/SEC-NAME-01-001.log` |
| 47 | `SEC-NAME-01-002` | `failure/2026-07-24/SEC-NAME-01-002.log` |
| 48 | `SEC-PERM-01-003` | `failure/2026-07-24/SEC-PERM-01-003.log` |
| 49 | `SEC-PERM-01-004` | `failure/2026-07-24/SEC-PERM-01-004.log` |
| 50 | `SEC-PRTGT-01-001` | `failure/2026-07-24-valid297-final2/result/SEC-PRTGT-01-001.log.txt` |
| 51 | `SEC-PRTGT-01-002` | `failure/2026-07-24-valid297-final2/result/SEC-PRTGT-01-002.log.txt` |
| 52 | `SEC-TOKEN-01-001` | `failure/2026-07-24-valid297-final2/result/SEC-TOKEN-01-001.log.txt` |
| 53 | `SEC-TOKEN-01-002` | `failure/2026-07-24-valid297-final2/result/SEC-TOKEN-01-002.log.txt` |
| 54 | `USE-ANNOT-01-002` | `failure/2026-07-24-valid297-final2/result/USE-ANNOT-01-002.log.txt` |
| 55 | `USE-CONC-01-001` | `failure/2026-07-24/USE-CONC-01-001.log` |
| 56 | `USE-CTX-01-001` | `failure/2026-07-24/USE-CTX-01-001.log` |
| 57 | `USE-CTX-01-002` | `failure/2026-07-24/USE-CTX-01-002.log` |
| 58 | `USE-DISP-01-002` | `failure/2026-07-24/USE-DISP-01-002.log` |
| 59 | `USE-ENV-01-002` | `failure/2026-07-24/USE-ENV-01-002.log` |
| 60 | `USE-EXPR-01-001` | `failure/2026-07-24/USE-EXPR-01-001.log` |
| 61 | `USE-INPT-01-002` | `failure/2026-07-24/USE-INPT-01-002.log` |
| 62 | `USE-OS-01-001` | `failure/2026-07-24/USE-OS-01-001.log` |
| 63 | `USE-SECNAME-01-001` | `failure/2026-07-24/USE-SECNAME-01-001.log` |
