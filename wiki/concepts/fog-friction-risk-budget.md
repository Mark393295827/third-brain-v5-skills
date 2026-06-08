---
tags: [domain/risk, domain/system-design, type/concept]
type: concept
status: seed
created: 2026-06-08
knowledge_stage: stored
evidence_level: single-source
---

# 迷雾摩擦风险预算

> 迷雾摩擦风险预算要求系统先承认观察不完整、执行有损耗，再把每个失败模式限制在不会杀死全局的边界内。
> (Source: [[src-20260608-bernstein-military-antifragile-synthesis#^ki-fog-friction-first-principle]], [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-risk-budget]]) WARNING: Single source

## Core Mechanism

```text
迷雾：看不清真实状态
  + 摩擦：执行持续损耗
  -> 预测可靠性下降
  -> 先定义最大可承受损失
  -> 用隔离、冗余、预备队、验证门保护生存
```

在该框架中，“风险预算”不是收益优化后的附属参数，而是架构设计的起点：如果某个子系统失败会导致全局死亡，就必须先限权、隔离或重构。 (Source: [[src-20260608-minimal-investing-military-theory-research#^ki-shallow-deep-risk]], [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-risk-budget]]) WARNING: Single source

## Classifications / Comparisons

| Risk layer | Meaning | Wrong reaction | Design response |
|---|---|---|---|
| Shallow risk | 短期波动、局部失败、可恢复损失 | 过度交易、频繁改战略 | 承受波动，保持纪律 |
| Deep risk | 永久性资本损失、建制毁灭、全局失控 | 把尾部风险当噪音 | 限权、分散、现金/预备队、复核 |
| Friction | 费用、税、认知负荷、工具失败 | 增加复杂度追求控制感 | 极简规则、低换手、自动检查 |
| Fog | 信息不完整、虚假信号、输入污染 | 迷信预测模型 | source boundary、verification gate |

## Implications / Applications

- 投资组合中，波动不是唯一风险；通胀、通缩、没收、地缘毁灭等深层风险需要不同防线。 (Source: [[src-20260608-minimal-investing-military-theory-research#^ki-shallow-deep-risk]]) WARNING: Single source
- Agent 系统中，prompt injection、上下文投毒、工具误用都应被看作 Observe/Orient 阶段的迷雾污染，而不是单纯 prompt 质量问题。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-risk-budget]]) WARNING: Single source
- 企业或技术架构中，风险预算应回答“局部失败是否可隔离”，而不是只回答“平均状态是否高效”。 (Source: [[src-20260608-agent-era-antifragile-system-design-playbook#^ki-agent-swarm-architecture]]) WARNING: Single source

## Source Boundary

该页把三份本地材料中的风险语言编译为系统设计概念；具体风险类别、金融结论和安全模式都需要进一步一手来源验证。

## Connections

- [[antifragile-system-decision-framework|抗脆弱系统决策框架]]：总框架。
- [[decentralized-swarm-resilience-architecture|去中心化蜂群韧性架构]]：风险预算的结构实现。
- [[mechanical-rebalancing-discipline|机械化再平衡纪律]]：风险暴露的运行时调度。
- [[agent-era-antifragile-system-design-playbook|Agent 时代抗脆弱系统设计 Playbook]]：Agent 应用流程。

---

## 演化时间线

- **2026-06-08**：创建初始版本，用来区分浅层波动、深层风险、迷雾和摩擦。

