---
tags: [domain/agent-systems, domain/system-design, type/sop]
type: sop
status: seed
created: 2026-06-08
knowledge_stage: stored
evidence_level: single-source
---

# Agent 时代抗脆弱系统设计 Playbook

> 这个 playbook 把“承认无知、优先生存、去中心化蜂群、机械化再平衡、OODA 降摩擦、学习复利”转成 Agent 系统设计步骤。
> (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-risk-budget]], [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-learning-compound]]) WARNING: Single source

## Trigger

当需要设计或重构一个多 Agent、自动化工具链、微服务系统或高不确定项目时，先运行本 SOP，再进入具体架构图或代码实现。

## Inputs

- System objective.
- Expected environment uncertainty.
- Critical assets and actions.
- Maximum acceptable loss per subsystem.
- Available verification gates and rollback paths.

## Steps

1. 承认迷雾：列出输入污染、上下文错误、工具失败、权限误用和外部环境变化。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-risk-budget]]) WARNING: Single source
2. 定义风险预算：为每个 Agent、服务或工具调用设定最大损失、权限边界和停止条件。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-risk-budget]]) WARNING: Single source
3. 拆成蜂群节点：把 Observe、Orient、Decide、Act、Verify、Write-back 分成可替换组件，避免单一 Agent 全权控制。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-swarm-architecture]]) WARNING: Single source
4. 写入再平衡规则：定义何时降权、下线、限流、切换模型、切换工具或要求人工复核。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-rebalancing]]) WARNING: Single source
5. 降低 OODA 摩擦：收敛工具链、模板、指标和动作频率，让每次循环都可观测、可回滚、可记录。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-ooda-minimalism]]) WARNING: Single source
6. 写回复利：把成功路径、失败模式、测试、策略和治理规则写回 wiki、SOP、代码或日志。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-learning-compound]]) WARNING: Single source

## Controls

| Control | Minimum standard |
|---|---|
| Permission boundary | 每个 Agent/服务只拿完成职责所需的最小权限 |
| Blast radius | 单个节点失败不应导致全局不可恢复损失 |
| Verification | 高风险动作必须有 fresh evidence 或人工复核 |
| Rebalance | 权重、预算、权限和上线状态有周期或事件触发规则 |
| Write-back | 每次有效循环产生可检索记录 |

## Verification

- 所有高风险外部事实用 `verify-before-claim` 复核。
- 架构图或实现必须能指出每个节点的权限、失败路径和回滚路径。
- 至少连接 [[antifragile-system-decision-framework|抗脆弱系统决策框架]]、[[fog-friction-risk-budget|迷雾摩擦风险预算]]、[[decentralized-swarm-resilience-architecture|去中心化蜂群韧性架构]]、[[mechanical-rebalancing-discipline|机械化再平衡纪律]] 和 [[ooda-friction-minimization-loop|OODA 降摩擦循环]]。

## Connections

- [[antifragile-system-decision-framework|抗脆弱系统决策框架]]：上位决策逻辑。
- [[decentralized-swarm-resilience-architecture|去中心化蜂群韧性架构]]：架构层实现。
- [[mechanical-rebalancing-discipline|机械化再平衡纪律]]：运行时资源治理。
- [[agent-understanding-framework|Agent Understanding Framework]]：现有 Agent OS/技能系统映射。

---

## 演化时间线

- **2026-06-08**：根据 Agent 时代系统设计 playbook source note 创建初始 SOP。
