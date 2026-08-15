# Self-Evolving Agent · 越用越懂你的系统

> **给 AI 一个会自我进化的记忆系统——它越用越懂你，而不是每次从零开始。**

一个可部署的基准框架：让任何人在本地给 AI Agent 搭一套**持续自生长的系统**——记忆分层、经验蒸馏、技能进化、边界守护。你不需要懂复杂架构，照着模板填，AI 就会开始"记住你、变聪明、越用越顺手"。

![badge](https://img.shields.io/badge/核心-自我进化-brightgreen) ![badge](https://img.shields.io/badge/形态-基准框架-blue) ![badge](https://img.shields.io/badge/适用-任何AI-Agent-orange) ![CI](https://github.com/3loveljw2/self-evolving-agent/actions/workflows/ci.yml/badge.svg)

---

## 为什么需要它

普通 AI 对话是"失忆的"：每次开新会话，它不认识你、忘了上次的决定、重复问同样的问题。你所有的使用经验、踩过的坑、做过的决策，都浪费了。

**Self-Evolving Agent 解决这个问题**——它给 AI 搭一套"大脑"：

```
你使用 → AI 记录 → 经验沉淀 → 蒸馏成方法论 → 技能进化 → 下次更懂你
   ↑                                                     │
   └───────────────── 越用越强的循环 ←──────────────────┘
```

---

## 快速上手（30 分钟搭好）

```bash
# 1. 克隆框架
git clone https://github.com/3loveljw2/self-evolving-agent.git

# 2. 复制模板，填入你的信息
cd self-evolving-agent
cp templates/*.md my-agent/          # 锚点模板/画像模板/任务记录模板...

# 3. 按 templates/ 各模板文件内说明的顺序填写（每份模板都有填写说明）
#    ├── anchor.md          ← 系统入口（恢复上下文用）
#    ├── constitution.md    ← 行为准则（边界/铁律）
#    ├── profile.md         ← 你的画像（角色/习惯/偏好）
#    ├── memory.md          ← 长期记忆（项目/决策/待办）
#    └── task-log.md        ← 任务记录（每次任务留痕）

# 4. 告诉你的 AI：每次对话先读 anchor.md 恢复上下文
# 5. 开始用——系统开始自生长
```

---

## 正在变成可执行形态（v0.1 → P0 已可运行）

本框架 = **基准框架（模板+方法论）+ 可运行 CLI**。最小可执行形态 `sea` 的 **P0 已实现并可运行**：

> **`sea` CLI**：管理本地 Markdown 记忆——`sea init` → `sea add`（自动分层 L1/L2/L3）→ `sea status` → `sea read`。本地优先、记忆即文件、最小依赖（typer + rich）。
>
> ```bash
> pip install -e .   # 或：pip install .（见 pyproject.toml）
> sea init && sea add "2026-08-13 完成 P0" --show && sea status
> ```

架构设计见 **[ARCHITECTURE.md](ARCHITECTURE.md)**；CLI 规格见 **[docs/spec-001-cli.md](docs/spec-001-cli.md)**。蒸馏（`sea distill`）与边界守护（`guard`）模块按软著流程推进后放出。

---

## 系统架构（五层）

```
┌─────────────────────────────────────────────┐
│  ① 系统层（soul/profile/memory）             │  ← 每次对话自动注入
│     人格设定 · 用户画像 · 长期记忆             │
├─────────────────────────────────────────────┤
│  ② 知识库层（固化层）                         │  ← 权威、持久、可检索
│     锚点入口 · 宪法准则 · 方法论 · 技能库      │
├─────────────────────────────────────────────┤
│  ③ 笔记层（活跃层）                          │  ← 动态、追加、轻量
│     待办清单 · 学习日志 · 每日记录            │
├─────────────────────────────────────────────┤
│  ④ 技能层（可进化）                          │  ← 越用越强的核心
│     Skill 定义 · 经验档案 · 蒸馏机制          │
├─────────────────────────────────────────────┤
│  ⑤ 边界层（守护）                            │  ← 主权/隐私/数据卫生
│     敏感信息隔离 · 权限分级 · 回滚机制        │
└─────────────────────────────────────────────┘
```

---

## 核心机制：经验蒸馏（自我进化的引擎）

```
每次任务完成
    │
    ├─ 写任务记录（问题/正确路径/错误路径）
    │
    ▼
任务档案累积（满 N 条）
    │
    ├─ 触发蒸馏：读全部档案 → 提炼共性 → 分类
    │     （操作类→SOP / 质量类→审查标准 / 工具类→环境文档）
    │
    ▼
蒸馏产物 → 合并进技能 → 版本 +1 → 下次直接用
    │
    └─ 循环：新的经验继续累积 → 系统持续进化
```

**效果**：你的 AI 每完成一批任务就"升级"一次——审查更严、踩坑更少、交付更快。10 轮蒸馏后，它积累的是**你的真实经验**，这是任何通用模型给不了的。

---

## 目录

```
self-evolving-agent/
├── README.md                  # 本文件
├── architecture/
│   ├── five-layers.md         # 五层架构详解
│   └── data-flow.md           # 数据流向（知识库↔笔记↔系统层）
├── memory-system/
│   └── memory-layers.md       # 记忆分层设计（系统/知识库/笔记/经验/边界）
├── distillation/
│   └── mechanism.md           # 蒸馏机制详解
├── boundary/
│   ├── privacy.md             # 隐私与数据卫生
│   └── sovereignty.md         # 主权设计（决策权归属）
├── skill-evolution/
│   ├── skill-design.md        # Skill 怎么设计
│   └── versioning.md          # 版本管理与回滚
├── templates/                 # 可直接套用的模板
│   ├── anchor.md
│   ├── constitution.md
│   ├── profile.md
│   ├── memory.md
│   └── task-log.md
└── LICENSE                    # CC BY 4.0
```

---

## 边界声明（重要）

- 本框架只提供**骨架、方法、模板**——不含任何人的个人数据
- 你在本地填入自己的信息，数据**只属于你**
- 框架设计原则：**敏感信息永不外传、决策权永远在人、系统可回滚**

---

## 谁适合用

- 想让 AI "记住你"的普通用户
- 用 AI 做长期项目（学习/写作/研究/创作）的人
- AI Agent 开发者（借鉴记忆与进化设计）

---

⭐ 如果这个框架对你有用，点个 star——让更多人拥有"越用越懂自己"的 AI。

## 与现有方案对比（2026-08）

| 方案 | 形态 | 存储 | 蒸馏可审计 | 本地优先 | 关键差异 |
|---|---|---|---|---|---|
| **self-evolving-agent（本项目）** | 基准框架（模板+方法论+CLI） | 纯 Markdown 文件 | ✅ 写入长期记忆必须人工确认 | ✅ 数据不出本机 | 五层架构 + 记忆即文件 + 蒸馏防污染 |
| MemGPT / Letta | Agent 记忆框架（可自托管，server 架构为主） | 数据库/服务端 | ❌ 自动 | 部分（可自托管但非文件优先） | 侧重上下文分层管理，非本地文件优先（[GitHub](https://github.com/letta-ai/letta)） |
| Mem0 | 记忆库（托管/自建） | 向量存储 | ❌ 自动嵌入 | 部分 | 自动嵌入为主，人不可读（[GitHub](https://github.com/mem0ai/mem0)） |
| Claude / Cursor 原生记忆 | 供应商内置 | 供应商云端 | ❌ | ❌ | 供应商锁定，不可迁移（[Anthropic](https://docs.anthropic.com/)） |
| 第二脑/笔记流方法论 | 个人知识管理方法 | 笔记软件 | — | ✅ | 为"人记笔记"设计，不是给 AI 的记忆系统（[Building a Second Brain](https://www.buildingasecondbrain.com/)） |

**一句话定位**：它们解决"AI 记不记得住"，我们额外解决"记忆可读、可审计、不污染、不锁死"——给 AI 的记忆，同时是你随时能翻开看、能 git、能带走的文件。

## License

**Dual license**: code (`src/`, `tests/`, `pyproject.toml`) is [MIT](https://opensource.org/licenses/MIT); documentation and methodology docs (`.md` files) are [CC BY 4.0](LICENSE).
