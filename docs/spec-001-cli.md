# spec-001-cli.md · sea CLI 规格（P0）

> 版本 v0.1（2026-08-13）· 状态：Implemented（P0）
> 对应 ARCHITECTURE.md 的 P0 最小闭环：init / add / status / read。

## 命令总览

```
sea init                 # 创建记忆目录布局（幂等）
sea add <text> [--level L] [--show]   # 追加记忆（自动分层）
sea status               # 查看各层文件统计
sea read <level>         # 打印某层全部条目
sea version              # 版本号
```

## 参数与行为

| 命令 | 参数 | 说明 | 退出码 |
|---|---|---|---|
| `init` | — | 创建 `~/.sea/` 结构（memory/{scratch,logs,kb}/ + skills/ + task-log.md + config.json） | 0 |
| `add` | `text`（位置参数，必填）<br>`--level/-l`（可选：scratch/logs/kb，强制分层）<br>`--show`（打印检测到的层级） | 空文本 → 错误退出 2；非法 level → 退出 2 | 0 / 2 |
| `status` | — | 未 init → 提示并退出 1 | 0 / 1 |
| `read` | `level`（位置参数，必填） | 非法 level → 退出 2 | 0 / 2 |

## 分层规则（P0 启发式）

```
规则性内容（含 # 标题/规则/原则/铁律/必须/禁止 等词，长度 ≥30）→ kb
含日期 / 任务 / 记录 / 完成 词 → logs
其余 → scratch
```

## 环境

- `SEA_HOME` 环境变量覆盖默认 `~/.sea/`（测试用）
- 运行时依赖：typer + rich（+ 标准库）
- Python ≥3.11

## 实现

- 源码：`src/sea/`（config.py / cli.py / memory/store.py / memory/layering.py）
- 测试：`tests/test_memory.py`（7 个用例：分层规则/自动分层/强制分层/非法层级/空输入/读写回环/统计）
- 安装：`pip install -e .` 后 `sea` 命令可用

## 后续（P1/P2，软著流程后）

- `sea distill`：扫描 task-log → 聚类 → 蒸馏草稿（产出需人工确认才写入 kb）
- `sea skill update`：蒸馏结果合并进技能文件
- `guard` 边界守护模块（脱敏/隐私过滤）
