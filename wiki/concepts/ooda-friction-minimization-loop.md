---
tags: [domain/decision-making, domain/agent-systems, type/concept]
type: concept
status: seed
created: 2026-06-08
knowledge_stage: stored
evidence_level: single-source
---

# OODA 降摩擦循环

> OODA 降摩擦循环强调速度来自减少无效观察、判断分叉和执行损耗，而不是盲目增加动作频率。
> (Source: [[src-20260608-minimal-investing-military-theory-research#^ki-ooda-low-friction]], [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-ooda-minimalism]]) WARNING: Single source

## Core Mechanism

```text
Observe：只采集少数高价值信号
  -> Orient：用稳定框架解释，而非临时预测
  -> Decide：从有限策略集中选择
  -> Act：小步、可回滚、可记录
  -> Write back：把结果固化为规则或记忆
```

该循环把 OODA 从“高频动作”重构为“低摩擦迭代”：复杂系统中的优势不一定来自更快出手，而可能来自更少噪音、更少工具分叉、更低成本和更稳定的写回机制。 (Source: [[src-20260608-bernstein-military-antifragile-synthesis#^ki-minimal-ooda]], [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-learning-compound]]) WARNING: Single source

## Classifications / Comparisons

| Friction source | Symptom | Minimalist countermeasure |
|---|---|---|
| Observation overload | 监控太多指标，无法判断 | 固定少数关键指标 |
| Orientation drift | 每次都重建解释框架 | 使用 [[antifragile-system-decision-framework|抗脆弱系统决策框架]] |
| Decision branching | 策略集无限扩张 | 预设 playbook 与阈值 |
| Action cost | 交易、部署、工具调用过多 | 小步、低成本、可回滚动作 |
| Learning leakage | 经验停留在会话里 | 写回 wiki、SOP、测试和日志 |

## Implications / Applications

- 投资中的低换手、低费用和固定再平衡可以被视为一种慢频但低摩擦的 OODA。 (Source: [[src-20260608-bernstein-military-antifragile-synthesis#^ki-minimal-ooda]]) WARNING: Single source
- Agent 系统中的高频工具调用可能只是噪音放大；真正的加速应来自标准化工具链、角色边界和可观测写回。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-ooda-minimalism]]) WARNING: Single source
- 每次循环结束都应形成新证据或新规则，否则系统没有复利，只有活动量。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-learning-compound]]) WARNING: Single source

## Source Boundary

该页不能证明 John Boyd 原始 OODA 理论或 AI 自动化研究的准确性，只记录本地材料中对 OODA 的系统设计迁移。

## Connections

- [[john-boyd|John Boyd]]：来源材料使用的 OODA 理论锚点。
- [[mechanical-rebalancing-discipline|机械化再平衡纪律]]：低摩擦循环中的规则化动作。
- [[agent-era-antifragile-system-design-playbook|Agent 时代抗脆弱系统设计 Playbook]]：该循环的 SOP 化应用。
- [[agent-understanding-framework|Agent Understanding Framework]]：强调写回和可复用系统记忆。

---

## 演化时间线

- **2026-06-08**：创建初始版本，把 OODA 解释为低摩擦、可写回的系统循环。

