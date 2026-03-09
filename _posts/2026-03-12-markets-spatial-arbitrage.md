---
layout: model
title: "Spatial Arbitrage and the Law of One Price"
subtitle: "When Prices Converge, When They Don't, and What Infrastructure Has to Do With It"
series: "Economic Systems"
series_order: 22
cluster: "MK — Markets and Price Formation"
date: 2026-03-12
image: /assets/images/commodity-markets.png
categories: [modelling]
tags: [economic-geography, commodity-markets, tag-hash-math, tag-hash-viz]
difficulty: 3
math: true
viz: true
math_core:
  - "Spatial price equilibrium"
  - "Arbitrage condition"
  - "Transfer costs"
  - "Price band theorem"
excerpt: "Alberta natural gas is chemically identical to Louisiana natural gas. Yet AECO in Alberta persistently trades $1.00–$2.00 per GJ below Henry Hub in Louisiana. The difference is not quality — it is pipeline capacity. When arbitrageurs cannot physically move the gas to where it is worth more, the price gap persists indefinitely. This is the spatial arbitrage constraint in its purest form: a quantified dollar value attached to a geographic bottleneck."
---

In 1952, Paul Samuelson published a paper that seems almost too obvious to be worth publishing. He proved that in a competitive world with transport costs, trade flows from low-price to high-price regions until the price difference equals the cost of moving the good between them. Any larger gap is arbitraged away by traders buying cheap and selling dear. Any smaller gap means no trade is profitable.

This Samuelson condition — sometimes called spatial price equilibrium — is the foundation of all commodity market geography. It explains which markets are connected, what price differences are permanent versus temporary, and crucially, what a persistent price anomaly tells us about the physical infrastructure that is supposed to connect two markets.

## The Law of One Price and Why It Fails

The Law of One Price (LOP) states that in competitive markets, identical goods trade at the same price everywhere, once adjusted for transport costs and quality differences. The intuition is straightforward: if the same good trades at $100 in City A and $120 in City B, with transport costing $5, traders will buy in A and sell in B, capturing $15 profit. This arbitrage continues until the price difference collapses to exactly $5.

The formal condition is:

$$P_B \leq P_A + T_{AB}$$

where $P_A$ is the price in the lower-priced market, $P_B$ is the price in the higher-priced market, and $T_{AB}$ is the per-unit transport cost from A to B. If this condition holds, no arbitrage profit is available. If $P_B > P_A + T_{AB}$, arbitrage is profitable and trade will occur.

The **price band theorem** extends this: the prices in two connected regions can only differ by at most the transfer cost $T_{AB}$ in either direction. Prices are bounded within the band $[P_A - T_{AB},\ P_A + T_{AB}]$. Within this band, prices can differ freely. Outside it, they cannot — the market mechanism enforces the constraint.

LOP fails — or more precisely, does not apply — in several real circumstances:

**Transport constraints:** If pipelines or rail are full, trade cannot increase even when the price differential exceeds transport costs. The physical constraint overrides the economic incentive. Prices diverge arbitrarily.

**Quality differences:** WCS and WTI are not the same good. Quality adjustments make direct LOP comparison misleading — you must adjust for processing economics before comparing.

**Market power:** If a single company controls the relevant pipeline, it can charge transport fees that maintain price differentials above the competitive level. The constraint is not physics but market power.

**Regulatory barriers:** Export licensing, tariffs, or border restrictions prevent arbitrage even when trade would otherwise be profitable.

Understanding which type of failure is present matters enormously for policy. A transport infrastructure constraint calls for investment in capacity. A market power problem calls for regulation. A regulatory barrier calls for trade negotiation. The price signal looks similar in all cases, but the interventions are completely different.

## The Samuelson Condition in Continuous Space

In the simplest spatial model, price varies continuously across geography. Let $p(x)$ be the price at location $x$ and $t(x,y)$ be the transport cost between locations $x$ and $y$. In equilibrium:

$$p(y) - p(x) \leq t(x, y) \quad \text{for all } x, y \text{ where trade flows from } x \text{ to } y$$

When this holds with equality, $x$ exports to $y$ and the price difference exactly covers transport costs. When it holds strictly ($p(y) - p(x) < t(x,y)$), there is no trade between $x$ and $y$ — the price difference does not justify the transport cost.

The equilibrium conditions determine which regions export, which import, and which are self-sufficient — and at what prices. The Samuelson formulation is equivalent to a linear programming problem: minimise total transport costs subject to satisfying demand at every location from available supply. The shadow prices on the demand constraints are the equilibrium regional prices.

This is the formal structure underlying all spatial commodity market analysis. The model is solved computationally for real markets, but the intuition is unchanged: prices form to minimise the total cost of moving goods from where they are produced to where they are consumed.

## AECO vs Henry Hub: Infrastructure as Price Signal

The AECO-Henry Hub basis differential is the most important spatial price relationship in Canadian energy economics. AECO is the delivery point for natural gas at the Empress hub on the Alberta-Saskatchewan border — the pricing point for Alberta's gas production. Henry Hub is the delivery point in Erath, Louisiana — the NYMEX futures settlement point and the dominant North American gas benchmark.

Pipeline-quality natural gas is, by definition, a standardised commodity. Methane is methane. There is no quality differential between AECO gas and Henry Hub gas — they meet the same pipeline specifications. Any price difference is purely spatial: the cost of moving gas from Alberta to the Gulf Coast.

The physical path from AECO to Henry Hub requires crossing several regulatory and capacity bottlenecks: the Northern Border Pipeline into the US Midwest, the Vector Pipeline into the Chicago hub, and various connections south and east to Henry Hub. The nominal transport cost for this journey is roughly $1.20–$1.50/GJ.

The **observed** AECO-Henry Hub differential has averaged $1.50–$2.50/GJ over the past decade — often exceeding the nominal transport cost by $0.50–$1.00/GJ. This excess differential has a simple explanation: export pipeline capacity from Alberta is intermittently full.

When the NGTL (Nova Gas Transmission Line) system within Alberta is congested, or when the border-crossing pipelines are at capacity, additional gas cannot physically move south regardless of how profitable the arbitrage appears. The price gap widens beyond the transport cost and stays there until demand within Alberta falls (shoulder seasons) or additional capacity is commissioned.

<div data-viz="echarts" data-options='{"title": {"text": "AECO vs Henry Hub Natural Gas: Monthly Prices 2015–2024", "subtext": "CAD/GJ (AECO) and USD/MMBtu (Henry Hub, shown for comparison) — the persistent basis differential"}, "tooltip": {"trigger": "axis", "axisPointer": {"type": "cross"}}, "legend": {"data": ["Henry Hub (USD/MMBtu)", "AECO (CAD/GJ)", "Basis Differential"], "bottom": 0}, "xAxis": {"type": "category", "data": ["Jan 2015","Jan 2016","Jan 2017","Jan 2018","Jan 2019","Jan 2020","Jan 2021","Jan 2022","Jul 2022","Jan 2023","Jan 2024"]}, "yAxis": [{"type": "value", "name": "Price (USD or CAD)", "max": 10}, {"type": "value", "name": "Basis Differential (USD/GJ)", "max": 4, "position": "right"}], "series": [{"name": "Henry Hub (USD/MMBtu)", "type": "line", "smooth": true, "data": [3.0, 2.6, 3.3, 3.2, 2.6, 1.9, 2.6, 4.7, 8.8, 2.7, 2.2], "lineStyle": {"width": 2}, "itemStyle": {"color": "#5470c6"}}, {"name": "AECO (CAD/GJ)", "type": "line", "smooth": true, "data": [2.4, 1.8, 2.1, 1.2, 0.9, 1.5, 2.0, 3.8, 6.5, 2.2, 1.6], "lineStyle": {"width": 2}, "itemStyle": {"color": "#91cc75"}}, {"name": "Basis Differential", "type": "bar", "yAxisIndex": 1, "data": [0.6, 0.8, 1.2, 2.0, 1.7, 0.4, 0.6, 0.9, 2.3, 0.5, 0.6], "itemStyle": {"color": "#ee6666", "opacity": 0.7}}]}'>
</div>

The chart reveals the structural nature of the problem. AECO consistently trades below Henry Hub, with the differential widening during periods of high Alberta production (winter heating demand in the US draws on Alberta gas, but the pipes may not have room for more) and narrowing during pipeline outages or maintenance when the constraint reverses.

The brief period in 2022 when both prices spiked and the differential actually compressed reflects the global LNG demand surge after Russia's invasion of Ukraine, which tightened all North American gas markets simultaneously. The constraint disappeared temporarily because demand was high enough to pull all available Alberta gas exports.

## Quantifying the Infrastructure Constraint

When a price differential persists above the competitive transport cost, the excess differential is a direct measure of the dollar cost of the infrastructure constraint. We can calculate this precisely.

Let:
- $\delta = \bar{P}_{\text{HH}} - \bar{P}_{\text{AECO}}$ = observed average price differential
- $t = $ competitive transport cost (what the pipeline tariff would be in a competitive market)
- $\epsilon = \delta - t$ = excess differential attributable to the capacity constraint
- $Q_{\text{Alberta}}$ = Alberta gas production volume (in GJ/year)

The **annual revenue loss from the constraint** is:

$$\text{Revenue Loss} = \epsilon \cdot Q_{\text{Alberta}}$$

Using approximate 2015–2023 averages:
- $\delta \approx \$1.50/\text{GJ}$
- $t \approx \$1.20/\text{GJ}$
- $\epsilon \approx \$0.30–\$0.80/\text{GJ}$ (varies year to year)
- $Q_{\text{Alberta}} \approx 15.5 \text{ Bcf/day} \approx 5,660 \text{ Bcf/year} \approx 5.98 \times 10^{12} \text{ GJ/year}$

At $\epsilon = \$0.50/\text{GJ}$:

$$\text{Revenue Loss} = \$0.50 \times 5.98 \times 10^{12} \approx \$3.0 \text{ billion/year}$$

This is not a small number. It is larger than Alberta's annual post-secondary education budget. It is the annual cost Alberta's gas producers pay — in foregone revenue — for the absence of adequate export pipeline capacity. That cost flows entirely to consumers of Alberta's gas (US utilities who buy it cheap) rather than to Alberta producers or the Alberta government.

The LNG Canada project in Kitimat, BC (Phase 1 capacity: 1.8 Bcf/day, coming online 2025) was expected to reduce this differential by opening a Pacific export route. Whether it does so depends on whether NGTL capacity to the coast is adequate and whether Asian gas prices are high enough to justify Pacific routing over the US market.

## The Scatter: Price Bands in Practice

The price band theorem predicts that observed price differentials across commodity corridors should cluster near the transport cost, with no observations exceeding it in a world of free trade. In reality, we observe a distribution that spans from zero (when markets are momentarily integrating) to well above the nominal transport cost (when constraints bind).

<div data-viz="echarts" data-options='{"title": {"text": "Transfer Cost vs Observed Price Differential: 15 Commodity Corridors", "subtext": "Each point is a commodity-corridor pair — points above the 45° line indicate a binding transport constraint"}, "tooltip": {"formatter": "function(p){return p.data[2]+'<br/>Transfer cost: $'+p.data[0]+'/unit<br/>Observed diff: $'+p.data[1]+'/unit'}"}, "xAxis": {"type": "value", "name": "Nominal Transfer Cost (USD/unit)", "min": 0, "max": 5}, "yAxis": {"type": "value", "name": "Observed Price Differential (USD/unit)", "min": 0, "max": 6}, "series": [{"name": "At-or-below cost (integrated)", "type": "scatter", "data": [[0.5,0.4,"AECO-Chicago gas (2023)"],[1.2,1.0,"WTI-Brent crude (2021)"],[0.3,0.2,"Chicago-Gulf wheat"],[0.8,0.6,"Pacific NW-Japan LNG (2023)"],[1.5,1.3,"Duluth-Chicago iron ore"],[0.4,0.3,"Appalachian-Henry Hub gas"]], "symbolSize": 12, "itemStyle": {"color": "#91cc75"}}, {"name": "Above cost (constrained)", "type": "scatter", "data": [[1.2,2.0,"AECO-Henry Hub gas (2018)"],[0.8,3.5,"WCS-WTI crude (Nov 2018)"],[1.5,2.2,"Alberta-California gas (2017)"],[1.0,1.8,"AECO-Henry Hub gas (2019)"],[1.2,1.9,"Montney gas-Henry Hub (2022)"],[0.9,1.7,"Western Canada-Chicago gas (2016)"]], "symbolSize": 12, "itemStyle": {"color": "#ee6666"}}, {"name": "45° line (no-arbitrage boundary)", "type": "line", "data": [[0,0],[5,5]], "lineStyle": {"type": "dashed", "color": "#999"}, "symbol": "none"}]}'>
</div>

The scatter plots two populations: corridors where trade is unconstrained (green, clustered at or below the 45-degree line) and corridors where infrastructure constraints bind (red, above the 45-degree line). Every red point represents a situation where the market is pricing in a constraint — where traders are aware that arbitrage is profitable but physically impossible.

The Alberta-US gas corridors cluster in the red zone during constraint periods. The WCS-WTI point for November 2018 is almost off the chart — a $40/bbl differential on an $8/bbl transport cost, reflecting an acute pipeline crisis.

## What Price Signals Tell Infrastructure Planners

The spatial arbitrage framework has a direct policy application: a persistent price differential above the competitive transport cost is a market signal that additional infrastructure would generate positive returns.

If the AECO-Henry Hub basis is $0.80/GJ above the transport cost, and if additional pipeline capacity costs $0.40/GJ (amortised capital and operating cost), then every GJ of new capacity generates $0.40 of net surplus. The value of new infrastructure is directly readable from the price signal.

This is the economic case for Trans Mountain Expansion, LNG Canada, and Coastal GasLink: persistent price differentials that exceed the cost of the infrastructure required to close them. The counterargument — that these differentials will narrow as oil demand falls — is the energy transition risk: if global oil demand falls fast enough, the infrastructure will be built into a declining market and may not recover its capital costs before the differential disappears.

The price signal tells you the current value. It cannot tell you the future value. Infrastructure investment is a bet that current constraints will persist long enough to justify the capital. The energy transition makes that a more uncertain bet than it was in 2010.

---

**Next in this cluster:** Model 23 — Futures Markets as Geographic Instruments examines how forward prices encode not just time preferences but geographic constraints — and how the futures curve carries information about infrastructure risk, storage scarcity, and the market's expectations about transport capacity.
