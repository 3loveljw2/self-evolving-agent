# ARCHITECTURE.md · self-evolving-agent

> 版本 v0.1（2026-08-13）· 状态：Proposed
> 本文档回答"这个框架怎么变成能跑的东西"——从纯方法论文档 → 最小可执行 CLI。
> 原则：先跑通最小闭环（读记忆 → 分层 → 蒸馏 → 更新 skill），再谈复杂。

## 0. 定位（电梯陈述）

**self-evolving-agent 是一个本地优先的 AI 记忆系统基准框架**——用一套会自我进化的 Markdown 记忆结构（分层/蒸馏/技能进化/边界守护），让任何 AI Agent 越用越懂它的主人。最小可执行形态：一个 Python CLI（`sea`），管理本地 Markdown 记忆文件。

## 1. 技术选型（ADR-001）

| 决策 | 选择 | 理由 |
|---|---|---|
| 形态 | **CLI 工具**（非 MCP/非 Web） | 人+Agent 双用、可脚本化、零依赖部署；MCP 包装留待生态分发需求出现后 |
| 语言 | Python ≥3.11 + Typer | 最小依赖、类型完备、跨平台 |
| 存储 | 本地 Markdown 文件（目录分层） | 记忆即文件——人可读、可 git 版本化、可迁移，符合"知识主权在本地"理念 |
| 依赖 | 仅 typer + rich（+ stdlib） | 最小攻击面、pip install 即用 |
| 构建 | uv（pyproject.toml + uv.lock） | 可复现、锁定传递树 |

## 2. 模块划分（5C）

```
self-evolving-agent/
├── src/sea/
│   ├── cli.py          # CLI 入口（Typer 子命令）
│   ├── config.py       # 路径/配置（默认 ~/.sea/）
│   ├── memory/         # ① 记忆分层模块
│   │   ├── store.py    #   读/写/追加 Markdown 记忆
│   │   └── layering.py #   L1 scratch / L2 logs / L3 kb 分层规则
│   ├── distill/        # ② 经验蒸馏模块
│   │   ├── scanner.py  #   扫描 task-log → 提取条目
│   │   └── cluster.py  #   聚类 → 提炼共性规则
│   ├── skill/          # ③ 技能管理模块
│   │   └── manager.py  #   列出/创建/更新 SKILL.md
│   └── guard/          # ④ 边界守护模块
│       └── policy.py   #   隐私/敏感信息过滤规则
├── tests/              # 镜像 src 结构
├── pyproject.toml
├── docs/
│   ├── spec-001-cli.md # 最小 CLI 规格（见下）
│   └── memory-layout.md# 记忆目录规范
└── examples/           # 示例记忆库（demo 用）
```

### 模块契约（接口先行）

| 模块 | 公开接口 | 输入 → 输出 | 异常 |
|---|---|---|---|
| memory.store | `add(entry, level)` / `read(level)` / `list()` | Markdown 文本 → 写入/读取分层文件 | `LevelError`（非法层级） |
| memory.layering | `classify(content)` | 文本 → 自动判断层级（L1/L2/L3） | 无 |
| distill.scanner | `scan(task_log_path)` | 日志文件 → 条目列表（含日期/主题/动作） | `FileNotFoundError` |
| distill.cluster | `cluster(entries, min_group=3)` | 条目列表 → 共性规则草稿 | 无 |
| skill.manager | `list()` / `create(name, content)` / `update(name, diff)` | 技能名 + 内容 → 技能文件操作 | `SkillExistsError` |
| guard.policy | `redact(text)` | 文本 → 脱敏文本（去除密钥/隐私） | 无 |

### 数据流（最小闭环）

```
sea init                 # 创建 ~/.sea/ 目录结构（memory/{scratch,logs,kb}/ + skills/）
  → sea add "今天发现：..."      # 追加记忆（自动分层）
  → sea distill --source task-log.md   # 扫描 + 聚类 → 输出蒸馏草稿
  → sea skill update trace-dig-method  # 蒸馏结果合并进技能文件
  → sea status             # 查看分层统计/最近蒸馏记录
```

## 3. 记忆目录规范（memory-layout 摘要）

```
~/.sea/
├── memory/
│   ├── scratch/   # L1 工作记忆：会话内的临时想法（低保留值，定期清理）
│   ├── logs/      # L2 情景记忆：每次任务/会话的摘要日志（按日期命名）
│   └── kb/        # L3 语义记忆：提炼后的规则/事实/方法论（高保留值）
├── skills/        # 技能文件（SKILL.md 或 markdown 规则）
├── task-log.md    # 任务记录流（蒸馏的原料）
└── config.json    # 配置（路径/分层阈值）
```

保留策略：L1 低保留（30 天滚动清理）、L2 中保留（按主题归档）、L3 永久（人工确认才写）。

## 4. 架构不变量

1. **记忆即文件**——所有状态存 Markdown，不引入数据库；任何时刻可读、可 diff、可 git
2. **蒸馏可审计**——distill 只产出"草稿"，写入 kb/skills 前必须人工或主代理确认（防记忆污染）
3. **本地优先**——无外部服务调用；用户数据不出本机（边界守护的底线）
4. **最小依赖**——运行时依赖 ≤3 个（typer/rich + stdlib），新增依赖需 ADR
5. **渐进披露**——CLI 帮助信息分三层：`sea --help`（概览）→ `sea distill --help`（子命令）→ `sea distill -v`（详细）

## 5. 分层落地计划

| 阶段 | 内容 | 验收 |
|---|---|---|
| P0（最小闭环） | memory.store + layering + cli init/add/status | `sea init && sea add "x" && sea status` 可跑通 |
| P1（蒸馏） | distill.scanner + cluster + skill.manager | `sea distill --source task-log.md` 产出可审草稿 |
| P2（边界） | guard.policy 脱敏 + 保留策略 | 密钥/隐私不出现在蒸馏输出 |
| P3（生态） | MCP 包装（可选） | 供 Claude/Cursor 直接调用 |

> 注意（软著红线）：P0-P3 的实现代码先完成软著申报，再公开开源；本文档为设计文档，不受限。

## 6. 相关文档

- `docs/spec-001-cli.md` —— CLI 命令规格（参数/退出码/错误信息）
- `docs/memory-layout.md` —— 记忆目录完整规范
- README.md —— 方法论文档（对外主入口）
