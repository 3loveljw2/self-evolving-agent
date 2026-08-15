# Changelog

本文件记录 sea（self-evolving-agent CLI）的版本变更。格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/) + [Semantic Versioning](https://semver.org/lang/zh-CN/)。

## [Unreleased]

### Added
- （规划）`sea distill`：经验蒸馏命令（核心模块，本地留存）
- （规划）`sea skill`：技能管理命令

## [0.1.0] - 2026-08-15

### Added
- `sea init`：创建本地记忆目录结构（`memory/{scratch,logs,kb}/` + `skills/` + `task-log.md` + `config.json`）
- `sea add`：追加记忆条目，自动分层（L1 scratch / L2 logs / L3 kb），支持 `--level` 强制指定与 `--show` 显示判定层级
- `sea status`：显示各层级记忆文件统计
- `sea read`：按层级读取记忆内容
- **双语分层规则**：中文与英文关键词均支持（规则类 → kb，任务/日期类 → logs）
- **测试套件**：10 个用例（分层规则/强制层级/非法层级/空输入/读写回环/英文用例），覆盖边界与异常路径
- **CI 流水线**：GitHub Actions（Python 3.11 / 3.12 双版本，`uv sync` + `pytest`）

### 技术说明
- 语言：Python ≥3.11，Typer CLI + Rich 输出
- 存储：本地 Markdown 文件（记忆即文件——可读、可 diff、可 git 版本化）
- 设计依据：`ARCHITECTURE.md`（P0 最小闭环：init/add/status/read）
- 许可：代码 MIT / 文档 CC BY 4.0（双轨）

[Unreleased]: https://github.com/3loveljw2/self-evolving-agent/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/3loveljw2/self-evolving-agent/releases/tag/v0.1.0
