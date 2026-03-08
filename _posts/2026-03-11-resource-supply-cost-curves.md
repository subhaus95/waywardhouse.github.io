---
layout: model
title: "Supply Cost Curves and Break-Even Prices"
subtitle: "What It Actually Costs to Produce Oil — and Who Survives a Price Crash"
series: "Economic Systems"
series_order: 17
cluster: "RE — Resource Economics"
date: 2026-03-11
categories: [modelling]
tags: [economic-geography, resource-economics, tag-hash-math, tag-hash-viz]
difficulty: 3
math: true
viz: true
math_core:
  - "Marginal cost curves"
  - "Break-even analysis"
  - "Levelised cost"
  - "Supply stack"
excerpt: "Not all oil is created equal. The global supply cost curve — the 'supply stack' — arranges every barrel of the world's extractable oil in order of what it costs to produce. Alberta's oil sands sit near the expensive end, which means understanding who shuts down first during a price crash requires knowing where you stand on the stack."
---

When the oil price collapsed from $110 to $45 between June and December 2014, the immediate question in Calgary was: who keeps pumping? The answer depends entirely on where each producer sits on the global supply cost curve — the ranked list of every barrel of extractable oil in the world, ordered from cheapest to most expensive.

This curve is not just an academic tool. It determines which projects get sanctioned, which shut in during downturns, which generate economic rents for governments and shareholders, and which are stranded when the energy transition reshapes demand. Understanding it is prerequisite to understanding Alberta's place in the global energy economy.

## The Logic of the Supply Stack

The supply stack is an application of the standard economic concept of a marginal cost curve, adapted for the specific structure of the oil industry. The horizontal axis measures cumulative production capacity (in million barrels per day), and the vertical axis measures the break-even price for each tranche of supply.

The shape is roughly upward-sloping: the cheapest barrels (Middle Eastern conventional, on-shore legacy fields) are at the left; the most expensive (oil sands mining, Arctic, deepwater frontier) are at the right. The market-clearing price is where demand intersects this supply stack — and the difference between the clearing price and each producer's break-even is their economic rent.

But "break-even price" is not a single number. It depends critically on what costs you include:

**Operating cost (OPEX):** The cash cost to produce one incremental barrel — labour, energy, chemicals, maintenance. This is the floor below which producers shut in immediately.

**Full-cycle cost:** OPEX plus capital cost recovery, royalties, transportation, and a normal return on invested capital. This is the threshold below which no rational investor would sanction a *new* project — but an existing project with sunk capital may continue operating as long as it covers OPEX.

**Levelised cost of supply (LCOS):** The constant price at which the NPV of the project equals zero over its lifetime. The most useful metric for comparing projects on a consistent basis:

$$\text{LCOS} = \frac{\sum_{t=0}^{T} \frac{C_t}{(1+r)^t}}{\sum_{t=0}^{T} \frac{Q_t}{(1+r)^t}}$$

where $C_t$ is total cost in year $t$, $Q_t$ is production in year $t$, and $r$ is the discount rate.

## The Global Cost Hierarchy

The approximate full-cycle break-even ranges by major supply category (2024 estimates, USD/bbl WTI-equivalent):

| Supply Source | OPEX | Full-Cycle Break-Even |
|---|---|---|
| Middle East conventional | $2–5 | $10–25 |
| Russia onshore conventional | $5–10 | $20–35 |
| US shale (Permian core) | $15–25 | $35–50 |
| US shale (non-core) | $25–35 | $45–60 |
| Alberta conventional | $8–15 | $30–45 |
| Alberta SAGD (in-situ bitumen) | $20–30 | $45–65 |
| Deepwater (Gulf of Mexico, Brazil) | $15–25 | $50–70 |
| Alberta oil sands mining | $35–50 | $65–85 |
| Arctic / ultra-deepwater | $40–60 | $80–120 |

Alberta spans a wide range — conventional oil is competitive with US shale, while oil sands mining sits near the top of the global cost curve. This heterogeneity within a single jurisdiction is unusual.

<div data-viz="echarts" data-options='{"title": {"text": "Global Oil Supply Stack (Illustrative)", "subtext": "Cumulative capacity vs full-cycle break-even, 2024"}, "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}, "formatter": "{b}: ${c}/bbl break-even"}, "xAxis": {"type": "category", "name": "Cumulative Capacity (Mbd)", "data": ["ME Conv\n(20 Mbd)", "Russia\n(10 Mbd)", "Alta Conv\n(3 Mbd)", "US Shale\nCore (8 Mbd)", "Alta SAGD\n(2 Mbd)", "Deepwater\n(5 Mbd)", "US Shale\nNon-core (4 Mbd)", "Alta Mining\n(1.5 Mbd)", "Arctic\n(1 Mbd)"]}, "yAxis": [{"type": "value", "name": "Break-even (USD/bbl)", "min": 0, "max": 130}, {"type": "value", "name": "Break-even Range", "show": false}], "series": [{"name": "Min Break-even", "type": "bar", "stack": "stack", "itemStyle": {"color": "transparent"}, "data": [10, 20, 30, 35, 45, 50, 45, 65, 80]}, {"name": "Break-even Range", "type": "bar", "stack": "stack", "data": [15, 15, 15, 15, 20, 20, 15, 20, 40], "itemStyle": {"color": "#5470c6", "opacity": 0.8}, "label": {"show": false}}, {"name": "WTI Price ($75)", "type": "line", "markLine": {"data": [{"yAxis": 75, "label": {"formatter": "WTI $75", "position": "end"}, "lineStyle": {"color": "#ee6666", "width": 2, "type": "dashed"}}]}}]}'>
</div>

The supply stack chart shows break-even ranges (the bar spans minimum to maximum break-even within each category). At $75 WTI, Alberta SAGD operations are near break-even on a full-cycle basis, while Alberta mining and Arctic supply are underwater. Middle Eastern conventional producers earn enormous rents.

## The Critical Distinction: OPEX vs Full-Cycle

The difference between operating cost and full-cycle cost creates a well-known dynamic in commodity markets: producers keep pumping below their full-cycle break-even, because the capital is already sunk.

Consider an Alberta SAGD operation that cost $2 billion to build. Its full-cycle break-even (including capital recovery) is $60/bbl. Its OPEX is $25/bbl. When WTI falls to $40:

- The project loses money on a full-cycle basis: $40 − $60 = −$20/bbl
- But it still generates positive cash flow net of operating costs: $40 − $25 = +$15/bbl
- Rational decision: **keep pumping** — stopping would sacrifice $15/bbl of contribution to fixed and sunk costs

This logic explains why oil production does not immediately collapse when prices fall. Producers shut in only when price falls below OPEX — the true floor. For SAGD operations, that floor is around $20–25/bbl; for oil sands mining, around $35–50/bbl (because energy costs, diluent, and processing are all higher).

The break-even condition for continuing to operate is:

$$P \cdot (1 - \text{royalty rate}) - \text{OPEX} - \text{transport} > 0$$

Setting this to zero and solving for $P$ gives the **operating break-even price** — the true shut-in threshold.

## The WCS Discount: Alberta's Triple Penalty

Alberta oil does not sell at WTI. It sells at Western Canadian Select (WCS), which is:

1. **Quality-discounted** — heavy oil requires more refining; refiners pay less
2. **Transport-discounted** — landlocked producers pay pipeline tolls to reach tidewater
3. **Differentially priced** — WCS reflects Canadian supply/demand dynamics, which can diverge sharply from WTI

The **netback** to a producer is:

$$\text{Netback} = P_{\text{WTI}} - \text{quality discount} - \text{transport cost} - \text{WCS differential}$$

In periods of pipeline constraint (as in 2018), the WCS discount widened to $50/bbl — meaning Alberta producers received only $20 when WTI was $70. This completely inverted the economics of high-cost projects and triggered emergency discussions about rail transport and pipeline capacity.

The netback framework means Alberta's effective position on the global supply stack is *worse* than its nominal break-even costs suggest. A project with a $55/bbl full-cycle cost may only net $45 when transport and quality discounts are applied — making it uneconomic even at $60 WTI.

## Alberta SAGD Break-Even Components Over Time

The break-even for Alberta SAGD operations is not static. Capital costs, energy prices, royalty rates, and transport costs have all shifted over the past fifteen years.

<div data-viz="echarts" data-options='{"title": {"text": "Alberta SAGD Break-Even Components (2010–2024)", "subtext": "Full-cycle cost decomposition, USD/bbl"}, "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}}, "legend": {"data": ["Capital Cost Recovery", "OPEX", "Royalties", "Transport / WCS Discount", "Return on Capital"], "bottom": 0}, "xAxis": {"type": "category", "data": ["2010","2012","2014","2016","2018","2020","2022","2024"]}, "yAxis": {"type": "value", "name": "USD/bbl", "max": 80}, "series": [{"name": "Capital Cost Recovery", "type": "bar", "stack": "total", "data": [18, 22, 25, 20, 18, 15, 16, 17], "itemStyle": {"color": "#5470c6"}}, {"name": "OPEX", "type": "bar", "stack": "total", "data": [14, 16, 18, 18, 17, 16, 19, 22], "itemStyle": {"color": "#91cc75"}}, {"name": "Royalties", "type": "bar", "stack": "total", "data": [6, 8, 10, 4, 5, 3, 8, 7], "itemStyle": {"color": "#fac858"}}, {"name": "Transport / WCS Discount", "type": "bar", "stack": "total", "data": [8, 9, 10, 12, 18, 10, 11, 12], "itemStyle": {"color": "#ee6666"}}, {"name": "Return on Capital", "type": "bar", "stack": "total", "data": [8, 9, 10, 8, 7, 6, 7, 8], "itemStyle": {"color": "#73c0de"}}]}'>
</div>

Several features stand out. Transport costs spiked in 2018 (the pipeline constraint crisis). Royalties dropped sharply in 2016 and 2020 (bust years, when the pre-payout royalty tiers kicked in). OPEX has risen post-2020, partly from energy cost inflation. Capital cost recovery peaked in the mid-2010s as the construction boom completed.

## Implications for Policy and Investment

The supply cost curve framework has direct implications for Alberta's resource policy:

**Investment sanctioning:** New projects are only sanctioned when the long-run expected price exceeds the full-cycle LCOS, including a risk premium. At $65 WTI, no new oil sands mining project is economic on a full-cycle basis — which is why no major mining expansion has been sanctioned since 2014.

**Price floor policy:** The OPEX floor determines when the government faces a catastrophic revenue collapse (producers shut in) vs a gradual decline. Understanding the $20–25/bbl SAGD OPEX floor helps budget planners model downside scenarios.

**Pipeline capacity:** The WCS discount analysis shows that transport infrastructure is not a mere logistics issue — it is a direct determinant of whether Alberta's oil is competitive on global markets. The differential between WTI and WCS can determine whether the entire tail of the supply stack is viable.

**Energy transition exposure:** As global demand falls with electrification, the demand curve shifts left — intersecting the supply stack at a lower price. High-cost Alberta supply is at the right end of the stack, meaning it is disproportionately exposed. The question is whether current producers can recover capital before the intersection moves past them.

---

**Next in this cluster:** Model 18 — Royalty Regimes and Resource Rents examines how governments design the fiscal systems that capture (or fail to capture) the economic rent sitting above each producer's break-even on the supply stack.
