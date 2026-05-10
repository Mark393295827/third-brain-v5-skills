---
name: agent-teams-command
description: Ender's Game approach to commanding Claude Code Agent Teams. Strategic multi-agent orchestration with Karpathy Agentic Engineering principles — plan, act, observe, iterate. L1-L5 commander progression.
---

# 安德的游戏：Agent Teams 指挥系统

> 这不是一个"功能"——这是一个**指挥系统**。基于 Karpathy Agentic Engineering 的系统性工程方法，将 Claude Code Agent Teams 从零散工具升级为完整的作战体系。

---

## Karpathy Agentic Engineering 框架映射

```
你 (Commander) = Process Scheduler
Team Lead      = CPU Core
Teammates      = Parallel Processes
Task List      = Shared Memory / IPC
Context Window = RAM (每个 agent 独立)
Tools          = System Calls
QA Loop        = Error Correction / Interrupt Handler
```

---

## 指挥体系架构

```
┌─────────────────────────────────────────────────────────────┐
│                    舰队指挥系统                                │
├─────────────────────────────────────────────────────────────┤
│  Phase 0: 战略评估 (Plan)   — 任务分解 + 兵力配置              │
│  Phase 1: 侦察 (Act)       — 多路并行探索                     │
│  Phase 2: 分析 (Observe)   — 交叉验证 + QA 循环               │
│  Phase 3: 执行 (Iterate)   — 迭代优化直到达标                  │
│  Phase 4: 复盘 (Learn)     — session-learn + 战后报告          │
└─────────────────────────────────────────────────────────────┘
```

---

## 指挥链 (Chain of Command)

```
你 ──→ Team Lead ──→ Teammates
 ↓         ↓            ↓
战略层    战术层        执行层
```

### 三层决策模型

| 层 | 角色 | 职责 | Karpathy 对应 |
|:--:|------|------|---------------|
| **战略层** | 你 (Ender) | 设定目标、分配资源、关键决策 | Process Scheduler |
| **战术层** | Team Lead | 任务分解、agent 协调、质量监控 | Main Agent Loop |
| **执行层** | Teammates | 具体执行、工具调用、返回结果 | Worker Processes |

---

## L1: 新兵 — 系统激活

### 初始配置
```json
// .claude/settings.local.json — 激活舰队指挥系统
{
  "experimental.agentTeams": true,
  "teammateMode": "auto"
}
```

```bash
claude --version  # 要求 ≥ v2.1.32
```

### 系统验证 (Plan→Act→Observe)
```
Plan:    验证 Agent Teams 是否可用
Act:     创建一个 3-agent 团队完成简单任务
Observe: 观察多色面板是否正常亮起
Iterate: 如果失败，检查配置和版本
```

### 首次出勤
```
Create a team of 3 teammates using Sonnet.
1. Front-end developer
2. Back-end developer
3. QA agent
Build me a landing page.
```

---

## L2: 班长 — 理解系统

### Agentic Engineering 核心概念

```
Agent Teams = 多进程并行系统
Sub-agents  = 单线程子进程
```

| 架构模式 | Sub-agents | Agent Teams |
|----------|-----------|-------------|
| Context | 独立进程，结果返回主进程 | 完全独立进程 |
| IPC | 仅向主进程报告 | **进程间直接通信** |
| 调度 | 主进程管理 | **共享内存 + 自调度** |
| Token 成本 | 低 | 高（但质量更高） |

### Karpathy 系统性工程检查清单

```
□ 每个 agent 有明确的系统边界 (Own Territory)
□ 任务列表作为共享内存管理
□ QA 循环作为错误纠正机制
□ Plan→Act→Observe 迭代
□ 资源监控 (Token 成本)
```

---

## L3: 战术专家 — 高效执行

### 标准作战命令 (Karpathy Plan→Act→Observe 模板)

```
GOAL: [战略目标 — 设定上下文，如同加载 system prompt]

ORDERS: Create a team of [N] teammates using [MODEL].

─── TEAMMATE 1 ─── 代号: [NAME] — 角色: [ROLE]
  TASK: [具体任务]
  OWNERSHIP: [文件/模块所有权]
  DEPENDENCY: 完成后通知 [TEAMMATE]
  
─── TEAMMATE 2 ─── 代号: [NAME] — 角色: [ROLE]
  TASK: [具体任务]
  OWNERSHIP: [文件/模块所有权]
  DEPENDENCY: 等待 [TEAMMATE] 完成

─── TEAMMATE 3 ─── 代号: [NAME] — 角色: QA
  TASK: 验证所有输出
  OWNERSHIP: test/
  DEPENDENCY: 等待所有 teammate 完成

DELIVERABLES:
1. [交付物 1]
2. [交付物 2]
3. QA 报告

QUALITY GATES:
- [ ] 所有测试通过
- [ ] QA 无 critical 问题
- [ ] 文件所有权不冲突
```

### 三大系统铁律

| # | 原则 | 工程意义 | 违反后果 |
|:-|------|---------|---------|
| 1 | **Own Territory** | 每个模块有明确属主 | 文件覆盖、逻辑冲突 |
| 2 | **Direct Messaging** | 进程间 IPC 通信 | 依赖阻塞、串行化 |
| 3 | **Wait-for-Dependencies** | 同步点管理 | 数据不一致、竞态条件 |

### 指挥界面操作

```
In-process 模式:
  Shift+Down = 切换进程上下文
  Escape     = 发送中断信号 (SIGINT)
  Ctrl+T     = 查看进程表 (task list)

Split-panes 模式 (tmux):
  每个进程独立终端
  颜色编码: 红(BE)/绿(FE)/蓝(QA)/黄(研究)
```

---

## L4: 指挥官 — 高级系统工程

### 作战计划审批 (Plan Approval Gate)

> 系统工程中的"设计评审"阶段。

```text
Spawn an architect teammate to refactor the auth module.
Require plan approval before they make any changes.
```

```
Teammate (Plan Mode) → 提交设计方案
    ↓
Lead → 设计评审
    ├── 通过 → 进入执行阶段
    └── 拒绝 → 修改后重新评审
```

**评审标准** (可编程的质量门控):
```
"Only approve plans that include test coverage"        → 测试覆盖率门控
"Reject plans that modify the database schema"          → 架构保护门控
"Every plan must have a rollback strategy"              → 回滚策略门控
```

### Hooks: 系统事件钩子

> 类似 Karpathy 工具调用中的 hook 机制——在关键系统事件时触发回调。

```json
{
  "hooks": {
    "TeammateIdle":   "python scripts/check-idle.py",    // 进程空闲 → 重新调度
    "TaskCreated":    "python scripts/validate-task.py",  // 创建任务 → 验证合理性
    "TaskCompleted":  "python scripts/verify-quality.py"  // 完成任务 → 质量检查
  }
}
```

### 多阶段作战 (Multi-Phase Pipeline)

> 系统工程的典型模式：串行阶段中的并行子任务。

```
PHASE 0 — 规划 (Plan)
  3 个 researcher 并行探索不同方向
  ↓ 同步点: 所有方向完成

PHASE 1 — 分析 (Observe)
  Critic 审查所有发现
  ↓ 同步点: 一致结论

PHASE 2 — 执行 (Act)
  Builder 执行验证后的方案
  ↓ 同步点: 执行完成

PHASE 3 — QA (Iterate)
  全面测试 + 修复循环
  ↓ 达标后退出
```

### 舰队资源管理

```
最优规模: 3-5 agents (超过 → 调度开销 > 并行收益)
模型选择: Sonnet (默认) | Opus (复杂推理) | Haiku (简单任务)
Token 预算: 每个 agent 独立 context window
清理协议: Lead 必须执行 cleanup (否则资源泄漏)
```

### 清理协议 (Resource Cleanup)

```text
1. "Ask [teammate] to shut down"     → 发送终止信号
2. 等待确认                           → 优雅关闭
3. 重复直到所有 teammate 关闭         → 所有进程终止
4. "Clean up the team"                → 释放共享资源
```

---

## L5: 传奇指挥官 — 经典战役 (完整工程案例)

### 战役 1: 全栈系统开发

```text
GOAL: 开发全栈应用 (REST API + React)，可在 localhost 运行。

ORDERS: Create a team of 3 teammates using Sonnet.

─── TEAMMATE 1 (代号: GEPARD/BACKEND) ───
  TASK: FastAPI + SQLite + REST endpoints
  OWNERSHIP: backend/
  DEPENDENCY: 完成后通知 FALCON

─── TEAMMATE 2 (代号: FALCON/FRONTEND) ───
  TASK: React frontend + API 集成
  OWNERSHIP: frontend/
  DEPENDENCY: 等待 GEPARD 的 API 规范

─── TEAMMATE 3 (代号: SENTINEL/QA) ───
  TASK: E2E 测试 + API 测试
  OWNERSHIP: tests/
  DEPENDENCY: 等待所有 teammate 完成

QUALITY GATES:
- [ ] 所有测试通过
- [ ] API 响应时间 <200ms
- [ ] 前端无控制台错误
```

### 战役 2: 技术决策研究

```text
GOAL: 评估 PostgreSQL → MongoDB 迁移可行性。

ORDERS: Create a team of 3 teammates using Opus.

─── TEAMMATE 1 (代号: OWL/DATABASE) ───
  TASK: 查询模式分析 + 性能基准测试
  OWNERSHIP: research/performance/

─── TEAMMATE 2 (代号: BEAVER/MIGRATION) ───
  TASK: 迁移工具评估 + 停机时间分析
  OWNERSHIP: research/migration/

─── TEAMMATE 3 (代号: FOX/CRITIC) ───
  TASK: 挑战前两个队友的结论，识别隐藏风险
  OWNERSHIP: research/risks/
  DEPENDENCY: 等待 OWL + BEAVER 完成
```

### 战役 3: 安全审计与修复

```text
GOAL: 发现并修复 auth 模块的所有安全漏洞。

ORDERS: Create a team of 2 teammates using Sonnet.

─── TEAMMATE 1 (代号: EAGLE/AUDITOR) ───
  TASK: OWASP Top 10 扫描 + 代码审计
  OWNERSHIP: security/audit/
  DEPENDENCY: 完成后提交问题列表给 BADGER

─── TEAMMATE 2 (代号: BADGER/FIXER) ───
  TASK: 修复所有发现的安全问题
  OWNERSHIP: src/auth/
  DEPENDENCY: 等待 EAGLE 的问题列表
```

---

## Karpathy Agentic Engineering 质量门控

### 系统性工程检查清单

```
[Phase 0: Plan]
□ 任务已分解为可并行执行的子任务
□ 每个子任务有明确属主和边界
□ 依赖关系已建模

[Phase 1: Act]
□ Agent 已按计划并行启动
□ 文件所有权无冲突
□ 进程间通信正常

[Phase 2: Observe]
□ QA 循环已执行
□ 问题已反馈给对应 agent
□ 修复后重新验证

[Phase 3: Iterate]
□ 质量达标 → 退出循环
□ 未达标 → 继续迭代
□ 超过迭代上限 → 升级给指挥官

[Phase 4: Learn]
□ 战后报告已生成
□ 教训已记录到 wiki
□ 下次战役可以借鉴
```

### 故障诊断矩阵

| 症状 | 根因分析 | 系统级解决方案 |
|------|---------|--------------|
| Agent 文件覆盖 | 没有文件所有权协议 | 强制 Own Territory |
| 任务死锁 | 依赖循环 | 简化依赖图，避免环形依赖 |
| Token 爆炸 | agent 数量 > 10 | 控制规模 3-5 |
| Context 不足 | 初始指令缺少上下文 | Goal 中提供完整 system prompt |
| 资源泄漏 | Lead 未执行 cleanup | 严格执行清理协议 |

---

## 演化时间线

- **2026-05-10**：创建。基于 Karpathy Agentic Engineering 框架的 Agent Teams 指挥系统。L1-L5 指挥官成长路径。3 场经典工程战役。
