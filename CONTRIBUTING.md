# Contributing to self-evolving-agent

感谢你对"越用越懂你的记忆系统"感兴趣！这个项目由一个 16 岁学生用 AI 协作构建，所有反馈都是它进化的原料。

## 你可以怎么参与

- **提 Issue**：报 bug、提功能建议、讨论方法论
- **提 PR**：修 bug、补文档、加测试
- **讨论**：在 Issue 区提问（"这个框架怎么用在我的场景？"）

## Issue 指南

- **Bug 报告**：用模板，附环境（Python 版本/系统）+ 复现步骤 + 实际 vs 期望输出
- **功能建议**：说明使用场景 + 为什么需要
- 中文或英文都可以，不要求专业术语

## 开发环境

```bash
git clone https://github.com/3loveljw2/self-evolving-agent.git
cd self-evolving-agent
uv sync            # 或 pip install -e .
uv run pytest      # 跑测试（10 个用例）
```

## 提交规范

- 提交信息用 [Conventional Commits](https://www.conventionalcommits.org/)：`feat:` / `fix:` / `docs:` / `test:` / `ci:`
- 改动必须保证 `pytest` 全绿
- 新增功能建议带测试

## 代码风格

- Python ≥3.11，全类型注解
- 中文/英文注释均可，变量名用英文
- 最小依赖原则：优先标准库

## 双轨许可

- 代码（`src/`、`tests/`）：MIT
- 文档（`.md`）：CC BY 4.0

## 待做方向（Roadmap）

- `sea distill`：经验蒸馏命令（软著流程后放出）
- `sea skill`：技能管理
- 欢迎在 Issue 区讨论优先级！
