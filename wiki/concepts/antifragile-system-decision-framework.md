---
tags: [domain/system-design, domain/strategy, type/concept]
type: concept
status: seed
created: 2026-06-08
knowledge_stage: stored
evidence_level: single-source
---

# 抗脆弱系统决策框架

> 抗脆弱系统决策框架的核心不是预测迷雾，而是把系统设计成即使预测失败也能存活、调整并复利。
> (Source: [[src-20260608-minimal-investing-military-theory-research#^ki-shallow-deep-risk]], [[src-20260608-bernstein-military-antifragile-synthesis#^ki-survival-first]]) WARNING: Single source

## Core Mechanism

```text
承认无知与迷雾
  -> 定义生存底线与风险预算
  -> 构建去中心化蜂群架构
  -> 用机械规则再平衡资源
  -> 降低 OODA 与交易摩擦
  -> 让时间、概率、组织学习产生复利
```

该框架把投资、军事、企业和 Agent 系统放进同一个设计问题：在高不确定、强摩擦、可能对抗的环境里，系统先保护不归零，再通过低损耗循环积累优势。 (Source: [[src-20260608-bernstein-military-antifragile-synthesis#^ki-fog-friction-first-principle]], [[src-20260608-minimal-investing-military-theory-research#^ki-lanchester-compound]]) WARNING: Single source

## Classifications / Comparisons

| Layer | Investment reading | Military reading | Agent/system-design reading |
|---|---|---|---|
| Environment | 市场随机性、交易成本 | 战争迷雾、摩擦 | 输入污染、上下文噪音、工具故障 |
| Survival | 避免永久性资本损失 | 避免建制毁灭 | 限权、隔离、回滚、风险预算 |
| Architecture | 广泛指数化 | 分布式蜂群、多域协同 | [[decentralized-swarm-resilience-architecture|去中心化蜂群韧性架构]] |
| Discipline | 股债现金再平衡 | 预备队调度、奇正相生 | [[mechanical-rebalancing-discipline|机械化再平衡纪律]] |
| Iteration | 低成本长期持有 | OODA 节奏 | [[ooda-friction-minimization-loop|OODA 降摩擦循环]] |

## Implications / Applications

- 设计系统时先问“失败会不会杀死全局”，再问“如何提高收益或速度”；这对应 [[fog-friction-risk-budget|迷雾摩擦风险预算]]。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-risk-budget]]) WARNING: Single source
- 优先选择低耦合、可替换、可降级的结构，而不是依赖单一高手、单一模型、单一资产或单一服务。 (Source: [[src-20260608-minimal-investing-military-theory-research#^ki-swarm-no-hero-node]]) WARNING: Single source
- 把纪律写成规则、阈值、预算和自动化检查；越需要临场意志力的策略，越容易被摩擦和情绪击穿。 (Source: [[src-20260608-bernstein-military-antifragile-synthesis#^ki-mechanical-rebalancing]]) WARNING: Single source

## Source Boundary

当前页面只能证明“三份本地材料共同提出了一个跨域类比框架”。它不能证明伯恩斯坦原著、军事理论原典或 Agent 架构研究已经支持这些迁移结论。后续需要用 `verify-before-claim` 或外部一手材料复核。

## Connections

- [[fog-friction-risk-budget|迷雾摩擦风险预算]]：提供生存优先与风险分类入口。
- [[decentralized-swarm-resilience-architecture|去中心化蜂群韧性架构]]：提供结构层设计原则。
- [[mechanical-rebalancing-discipline|机械化再平衡纪律]]：提供执行层规则。
- [[agent-era-antifragile-system-design-playbook|Agent 时代抗脆弱系统设计 Playbook]]：把本框架转成可执行 SOP。
- [[william-bernstein|William Bernstein]]、[[carl-von-clausewitz|Carl von Clausewitz]]、[[john-boyd|John Boyd]]、[[sun-tzu|Sun Tzu]]、[[frederick-lanchester|Frederick Lanchester]]：来源材料使用的关键理论锚点。

---

## 演化时间线

- **2026-06-08**：根据三份本地综合材料创建初始版本，保留 single-source 风险。
