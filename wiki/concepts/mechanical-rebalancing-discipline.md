---
tags: [domain/decision-making, domain/system-design, type/concept]
type: concept
status: seed
created: 2026-06-08
knowledge_stage: stored
evidence_level: single-source
---

# 机械化再平衡纪律

> 机械化再平衡纪律把资源调度写成可执行规则，使系统在狂热时降风险、在恐慌时释放预备队，而不是被情绪接管。
> (Source: [[src-20260608-bernstein-military-antifragile-synthesis#^ki-mechanical-rebalancing]], [[src-20260608-minimal-investing-military-theory-research#^ki-rebalancing-qizheng]]) WARNING: Single source

## Core Mechanism

```text
预设目标权重 / 阈值
  -> 观察偏离
  -> 触发调仓或调权
  -> 高估/过载节点降权
  -> 低估/欠配节点补给
  -> 系统回到风险预算
```

再平衡的系统意义是把“风险暴露管理”从临场判断改为机械化纪律；它不保证最高收益，但降低了人性、噪音和局部胜利导致全局过度暴露的概率。 (Source: [[src-20260608-minimal-investing-military-theory-research#^ki-rebalancing-qizheng]], [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-rebalancing]]) WARNING: Single source

## Classifications / Comparisons

| Setting | Rebalanced resource | Trigger | Purpose |
|---|---|---|---|
| Investment | 股票、债券、现金权重 | 周期或阈值偏离 | 恢复风险预算 |
| Military metaphor | 突击部队、防御部队、预备队 | 战线过度延伸或受挫 | 奇正相生、保存建制 |
| Enterprise | 业务线预算、人力、管理注意力 | ROI、风险、相关性偏离 | 避免被热点绑架 |
| Agent systems | Agent 调用预算、权限、模型、工具 | 错误率、成本、收益、风险偏离 | 降权危险节点，补给稳定节点 |

## Implications / Applications

- 再平衡必须在事前定义，不应在压力最大时临时发明规则。 (Source: [[src-20260608-bernstein-military-antifragile-synthesis#^ki-mechanical-rebalancing]]) WARNING: Single source
- Agent 系统的再平衡可以包括降低高风险 Agent 权限、减少调用预算、切换模型或要求人工复核。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-rebalancing]]) WARNING: Single source
- 再平衡只在 [[fog-friction-risk-budget|迷雾摩擦风险预算]] 明确时有意义；没有目标暴露，就无法判断何时偏离。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-risk-budget]]) WARNING: Single source

## Source Boundary

该页把投资再平衡迁移为通用资源治理规则；具体调仓周期、阈值和投资收益影响不在本页证明范围内。

## Connections

- [[antifragile-system-decision-framework|抗脆弱系统决策框架]]：再平衡是其执行层。
- [[decentralized-swarm-resilience-architecture|去中心化蜂群韧性架构]]：再平衡的对象。
- [[ooda-friction-minimization-loop|OODA 降摩擦循环]]：再平衡需要低摩擦触发和执行。
- [[sun-tzu|Sun Tzu]]：来源材料用“奇正相生”解释反周期调度。

---

## 演化时间线

- **2026-06-08**：创建初始版本，把投资再平衡转成系统运行纪律。

