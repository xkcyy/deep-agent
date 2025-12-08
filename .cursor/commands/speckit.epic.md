---
description: Create or update a high-level epic document with Mermaid flows and specify-ready task slices.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. 解析用户输入为 epic 需求。若空则报错："No epic description provided".

2. 生成简短名称（2-4 词，action-noun 或名词短语，保留技术词），用于目录名：

   - 清洗：小写、非字母数字转“-”、去重连字符。

3. 创建 epic 目录与文件

   - 先获取最新分支信息：`git fetch --all --prune`（忽略错误）。
   - 运行 `.specify/scripts/powershell/create-new-epic.ps1 -Json "$ARGUMENTS"`，必要时加 `-ShortName "<short>"`，若需分支则加 `-CreateBranch`。
   - 脚本会在 `spec-epics/` 下创建 `E###-<short>` 目录，复制 `.specify/templates/epic-template.md` 到 `epic-spec.md`，并返回 JSON（EPIC_NAME / EPIC_DIR / EPIC_SPEC_FILE / BRANCH_NAME 等）。
   - 读取 JSON 输出，锁定 `epic-spec.md` 作为写入目标。

4. 写入高层 epic 文档（仅业务视角；不要系统集成视图、里程碑、风险）

   - 模板结构：
     - 摘要与成功标准：业务目标、KPI、范围/上线时间。
     - 业务蓝图：旅程/场景（3-7）、事件流（主干）、业务对象表（对象|核心属性|状态）。
     - 核心流程：分角色自然语言 + Mermaid `graph TD` 主路径（7-12 节点，可用 `subgraph` 区分角色）。
     - 能力分解与边界：3-7 个一级能力；Out-of-scope 列表。
     - 非功能关键点（业务紧耦合的合规/性能/可观测性/容错）。
     - speckit.specify 子任务清单：5-15 条，含目标、输入上下文（引用本文件段落编号）、输出物、验收、依赖、复杂度(0.5-2d)、并行组。
   - 长度控制：全稿 2-3 页；每节 3-7 项；句子短。流程过长可拆主干+子流程。

5. 验证与收敛

   - 范围封闭（In/Out-of-scope 清晰）。
   - Mermaid 覆盖主路径；无系统/集成/里程碑/风险版块残留。
   - 子任务可交付、粒度 0.5-2 天、依赖与并行组清晰。

6. 输出
   - 提示 epic 名称与文件路径：`EPIC_SPEC_FILE`
   - 提示可继续用 speckit.specify 针对子任务执行。
