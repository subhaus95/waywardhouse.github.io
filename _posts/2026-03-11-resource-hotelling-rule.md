---
layout: model
title: "The Hotelling Rule"
subtitle: "Why the Price of a Finite Resource Must Rise at the Rate of Interest"
series: "Economic Systems"
series_order: 16
cluster: "RE — Resource Economics"
date: 2026-03-11
image: /assets/images/resource-economics.png
categories: [modelling]
tags: [economic-geography, resource-economics, tag-hash-math, tag-hash-viz]
difficulty: 3
math: true
viz: true
math_core:
  - "Hotelling rule"
  - "Net present value"
  - "Optimal control"
  - "Royalty vs scarcity rent"
excerpt: "A resource owner faces a fundamental investment question: extract now, or wait? The Hotelling rule shows that in equilibrium, the price of any finite resource must rise at exactly the rate of interest — and this simple insight explains everything from Alberta's oil sands production decisions to the long-run trajectory of commodity prices."
---

In 1931, Harold Hotelling published a paper that remains one of the most elegant results in resource economics. The question he posed seems almost trivially simple: when should you extract a finite resource? Yet the answer — that the price must rise at exactly the rate of interest — has profound implications for how we understand oil, minerals, groundwater, and every other exhaustible resource on Earth.

Alberta sits at the heart of this problem. The Athabasca oil sands hold roughly 165 billion barrels of proved reserves — the third-largest oil reserve in the world. Every decision about how quickly to extract that bitumen, what royalty to charge, and what to do with the revenues is, implicitly or explicitly, a decision shaped by Hotelling's logic.

## The Fundamental Arbitrage

The core insight is an arbitrage argument. Suppose you own an oil well. You have two options:

1. **Extract today**, sell the oil at price $P_0$, invest the proceeds at interest rate $r$.
2. **Wait one year**, extract then, sell at price $P_1$.

For you to be indifferent between these options — for there to be no profitable arbitrage — the payoff must be equal:

$$P_0(1 + r) = P_1$$

Or in continuous time, the Hotelling rule:

$$\frac{dP}{dt} = r \cdot P$$

This is the fundamental no-arbitrage condition for exhaustible resources. If price rises faster than $r$, everyone waits — supply collapses, price rises even faster. If price rises slower than $r$, everyone extracts now — supply floods the market, price falls. The only stable equilibrium has price rising at exactly $r$.

The solution is exponential growth from an initial price $P_0$:

$$P(t) = P_0 \cdot e^{rt}$$

## Deriving the Rule Formally

The formal derivation uses optimal control theory. A resource owner has a finite stock $S_0$ and chooses an extraction path $q(t)$ to maximise the net present value of profits:

$$\max_{q(t)} \int_0^T \left[ P(t) - c \right] q(t) \, e^{-rt} \, dt$$

subject to:

$$\dot{S}(t) = -q(t), \quad S(t) \geq 0, \quad q(t) \geq 0$$

where $c$ is the (constant) marginal extraction cost and $S(t)$ is the remaining stock at time $t$.

The Hamiltonian for this problem is:

$$\mathcal{H} = \left[ P(t) - c \right] q(t) e^{-rt} + \lambda(t) \cdot (-q(t))$$

where $\lambda(t)$ is the costate variable — the shadow price of the resource stock, measured in present-value terms. The optimality conditions require:

$$\frac{\partial \mathcal{H}}{\partial q} = 0 \implies (P - c)e^{-rt} = \lambda$$

and the costate equation:

$$\dot{\lambda} = 0 \implies \lambda = \text{constant}$$

This means $(P - c)e^{-rt}$ must be constant, so the **net price** (price minus extraction cost) must rise at rate $r$:

$$\frac{d(P - c)}{dt} = r(P - c)$$

## Two Components of the Resource Price

This derivation reveals something crucial. The full price of a resource has **two components**:

$$P(t) = c + \rho(t)$$

where:
- $c$ = marginal extraction cost (the cost to lift one more barrel)
- $\rho(t)$ = **scarcity rent** (also called the royalty or Hotelling rent)

The scarcity rent is the shadow price of the finite stock — it compensates the owner for permanently depleting a non-renewable asset. It rises at rate $r$ over time. The extraction cost (if constant) does not rise.

**Alberta illustration:** The oil sands have a marginal extraction cost of roughly &#36;25–35 per barrel for SAGD operations, compared to roughly &#36;5–10 for conventional Alberta oil and &#36;2–5 for Middle Eastern conventional. This means:

- At &#36;80 WTI, an Alberta SAGD producer earns a scarcity rent of roughly &#36;45–55/bbl
- A Saudi producer earns a scarcity rent of roughly &#36;70–75/bbl — much larger
- High extraction costs compress the scarcity rent, which is why conventional producers have more to lose from depletion

The royalty charged by the Alberta government is supposed to capture some portion of this scarcity rent — the return that belongs, in principle, to the resource's public owners.

## The Backstop Technology

Extraction stops when the price reaches the **backstop technology** price — the cost of a substitute that can perfectly replace the resource. If oil can be replaced by synthetic fuel at &#36;150/bbl, then no one will pay more than &#36;150 for conventional oil, regardless of scarcity.

The backstop price $\bar{P}$ sets the terminal condition for the Hotelling path. The initial price $P_0$ is determined by:

$$P_0 = \bar{P} \cdot e^{-rT}$$

where $T$ is the time to exhaustion. This means the initial price and the depletion horizon are jointly determined — you cannot set one without the other.

For Alberta's oil sands, the backstop is arguably set by the carbon-adjusted cost of electric vehicles, hydrogen, and synthetic aviation fuel. As these costs fall, $\bar{P}$ falls, and the entire Hotelling price path shifts down. This is one reason why "stranded asset" discussions have intensified since 2015.

## Interest Rates and Extraction Speed

One of the most practically important implications of the Hotelling rule is the relationship between interest rates and extraction speed.

When $r$ is high, the price must rise steeply — which means the initial price is low (to fit the exponential path under the backstop constraint). Low initial prices mean high early demand, fast extraction, rapid depletion.

When $r$ is low, the required price growth is shallow — the initial price can be higher, demand lower, extraction slower.

This explains why the decade of near-zero interest rates from 2010 to 2021 was, paradoxically, associated with lower incentives to rapidly extract — and why rising rates after 2022 changed extraction economics. Lower $r$ means patience is less costly; the Hotelling logic says wait.

<div data-viz="echarts" data-options='{"title": {"text": "Hotelling Price Paths Under Different Interest Rates", "subtext": "Illustrative; backstop at $150, extraction cost $20"}, "tooltip": {"trigger": "axis"}, "legend": {"data": ["High r (8%)", "Medium r (4%)", "Low r (2%)"], "bottom": 0}, "xAxis": {"type": "category", "name": "Year", "data": ["2025","2027","2029","2031","2033","2035","2037","2039","2041","2043","2045"]}, "yAxis": {"type": "value", "name": "Price (USD/bbl)", "min": 0, "max": 160}, "series": [{"name": "High r (8%)", "type": "line", "smooth": true, "data": [40, 47, 54, 64, 75, 87, 100, 116, 135, 150, 150], "lineStyle": {"width": 2}}, {"name": "Medium r (4%)", "type": "line", "smooth": true, "data": [68, 73, 78, 84, 90, 97, 104, 111, 119, 128, 137], "lineStyle": {"width": 2}}, {"name": "Low r (2%)", "type": "line", "smooth": true, "data": [90, 94, 97, 101, 105, 109, 113, 117, 122, 126, 131], "lineStyle": {"width": 2}}, {"name": "Backstop", "type": "line", "data": [150,150,150,150,150,150,150,150,150,150,150], "lineStyle": {"type": "dashed", "color": "#999"}, "itemStyle": {"color": "#999"}}]}'>
</div>

The chart shows three stylised Hotelling paths with different interest rates, all terminating at the same backstop price. High interest rates (blue) produce fast price growth from a low initial level — rapid early extraction. Low interest rates (green) produce slow price growth from a high initial level — more patient depletion.

## Does Oil Actually Follow the Hotelling Rule?

The empirical track record is mixed. Observed oil prices are far more volatile than any Hotelling path would predict — they whipsaw with geopolitical events, OPEC decisions, demand shocks, and financial crises. The 2014 price collapse from &#36;110 to &#36;45 in six months has no counterpart in Hotelling's smooth exponential.

What the rule gets right is the **long-run framework**. Over decades, resource prices do tend to reflect scarcity — they have risen in real terms for most finite commodities over the past century, broadly consistent with Hotelling's logic. The rule is best understood as a description of the gravity well that market prices orbit around, not a precise forecast of day-to-day prices.

## Price Decomposition: Oil Sands vs Conventional

The two-component price structure looks very different across resource types. When WTI is at &#36;60, &#36;80, or &#36;100, the split between extraction cost and scarcity rent is not the same for all producers.

<div data-viz="echarts" data-options='{"title": {"text": "Price Decomposition: Extraction Cost + Scarcity Rent", "subtext": "By producer type at three WTI price levels"}, "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}}, "legend": {"data": ["Extraction Cost", "Scarcity Rent"], "bottom": 0}, "xAxis": {"type": "category", "data": ["Oilsands\n$60", "Oilsands\n$80", "Oilsands\n$100", "Conventional\n$60", "Conventional\n$80", "Conventional\n$100", "Shale\n$60", "Shale\n$80", "Shale\n$100"]}, "yAxis": {"type": "value", "name": "USD/bbl"}, "series": [{"name": "Extraction Cost", "type": "bar", "stack": "total", "data": [30, 30, 30, 10, 10, 10, 40, 40, 40], "itemStyle": {"color": "#5470c6"}}, {"name": "Scarcity Rent", "type": "bar", "stack": "total", "data": [30, 50, 70, 50, 70, 90, 20, 40, 60], "itemStyle": {"color": "#91cc75"}}]}'>
</div>

The chart illustrates why conventional producers (Middle East, conventional Alberta) have much larger scarcity rents per barrel than oil sands or shale — and therefore more to lose from depletion. It also shows why at &#36;60 WTI, high-cost oil sands producers are near their break-even: the "scarcity rent" in that column is really almost entirely a return of capital, not economic rent.

## What This Means for Resource Policy

The Hotelling rule has direct policy implications:

**Royalty design:** If the scarcity rent is the portion that should accrue to Albertans as public resource owners, then royalties should track the net price $(P - c)$, not the gross price $P$. Flat percentage royalties on gross revenue systematically under-capture rent when prices are high and over-burden producers when prices are low.

**Depletion rate:** The optimal depletion rate depends on the interest rate, which is itself partially a policy variable. Alberta's low-royalty, fast-extraction approach implicitly accepts a high effective discount rate — prioritising current revenue over future resource wealth.

**Energy transition timing:** If the backstop price is falling — as electric vehicle costs decline and carbon prices rise — the Hotelling path shifts. Optimal extraction accelerates *now*, before the backstop arrives, not slows. This creates a political economy tension: the resource curse logic says go slow, the Hotelling logic says go fast before the window closes.

---

**Next in this cluster:** Model 17 — Supply Cost Curves and Break-Even Prices translates the Hotelling framework into the practical question of who actually extracts at each price level, and where Alberta's oil sands sit on the global cost curve.

## References

Alberta Energy Regulator. 2025. *Alberta Energy Outlook (ST98): Crude Bitumen Supply Costs*. <https://www.aer.ca/data-and-performance-reports/statistical-reports/alberta-energy-outlook-st98/crude-bitumen/crude-bitumen-supply-costs>

Alberta Energy Regulator. 2025. *Alberta Energy Outlook (ST98): Reserves*. <https://www.aer.ca/data-and-performance-reports/statistical-reports/alberta-energy-outlook-st98/reserves>

Government of Alberta. 2025. *Oil Sands Facts and Statistics*. <https://www.alberta.ca/oil-sands-facts-and-statistics>

Government of Alberta. 2025. *Oil Prices and Value*. <https://www.alberta.ca/oil-prices-and-value>

Hotelling, Harold. 1931. "The Economics of Exhaustible Resources." *Journal of Political Economy* 39 (2): 137–175. <https://doi.org/10.1086/254195>

International Energy Agency. 2021. *Net Zero by 2050: A Roadmap for the Global Energy Sector*. Paris: IEA. <https://www.iea.org/reports/net-zero-by-2050>

Norges Bank Investment Management. 2025. *The Fund*. <https://www.nbim.no/en/>

Pindyck, Robert S. 1978. "The Optimal Exploration and Production of Nonrenewable Resources." *Journal of Political Economy* 86 (5): 841–861. <https://doi.org/10.1086/260711>
