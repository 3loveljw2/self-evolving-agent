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

架构设计见 **[ARCHITECTURE.md](ARCHITECTURE.md)**；CLI 规格见 **[docs/spec-001-cli.md](docs/spec-001-cli.md)**。蒸馏（`sea distill`）与边界守护（`guard`）为框架核心模块，按知识产权策略本地留存（GitHub 创作时间线作为著作权证据），后续择机发布。

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
├── src/sea/                # sea CLI 源码（P0，已开源）
│   ├── cli.py              # Typer 入口：init / add / status / read
│   ├── config.py           # 记忆目录配置（~/.sea）
│   └── memory/             # 分层存储（scratch / logs / kb）
├── tests/                  # 10 个测试（双语分层 / 边界 / 异常）
├── docs/                   # 规格文档（spec-001-cli / memory-layout）
├── architecture/           # 架构设计（五层 / 数据流）
├── distillation/           # 蒸馏机制（核心模块 · 本地留存）
├── boundary/               # 边界守护（核心模块 · 本地留存）
├── memory-system/          # 记忆分层设计
├── skill-evolution/        # 技能进化机制
├── templates/              # 模板（anchor / memory / task-log …）
├── .github/workflows/      # CI（Python 3.11 / 3.12 矩阵）
├── CHANGELOG.md            # 版本记录（Keep a Changelog）
├── CONTRIBUTING.md         # 贡献指南
├── LICENSE                 # CC BY 4.0（文档）
├── llms.txt                # AI 可索引
└── pyproject.toml          # 包配置（代码 MIT）
```

## License

**Dual license**: code (`src/`, `tests/`, `pyproject.toml`) is [MIT](https://opensource.org/licenses/MIT); documentation and methodology docs (`.md` files) are [CC BY 4.0](LICENSE).
