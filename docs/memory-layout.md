# memory-layout.md · 记忆目录规范

> 版本 v0.1（2026-08-13）· 对应 ARCHITECTURE.md 第 3 节。

## 目录结构

```
~/.sea/（或 $SEA_HOME）
├── memory/
│   ├── scratch/   # L1 工作记忆：会话内的临时想法（低保留，30 天滚动清理）
│   ├── logs/      # L2 情景记忆：每次任务/会话的摘要日志（按日期命名，按主题归档）
│   └── kb/        # L3 语义记忆：提炼后的规则/事实/方法论（高保留，人工确认才写）
├── skills/        # 技能文件（SKILL.md / markdown 规则）
├── task-log.md    # 任务记录流（蒸馏的原料）
└── config.json    # 配置（分层阈值 / 版本）
```

## 文件命名

- 每日文件：`memory-YYYY-MM-DD.md`（同层同日追加写入）
- task-log：单文件追加

## 保留策略

| 层 | 保留 | 清理方式 |
|---|---|---|
| L1 scratch | 低（30 天） | 滚动清理 |
| L2 logs | 中 | 按主题归档 |
| L3 kb | 永久 | 人工确认才写入，不自动删 |

## 分层 ↔ 框架五层

见 memory-system/memory-layers.md「四层 ↔ 五层对照」：运行时三级（scratch/logs/kb）管"文件存哪"，框架五层管"内容记什么"，蒸馏 = 把 L2 logs 提炼进 L3 kb 的过程。
