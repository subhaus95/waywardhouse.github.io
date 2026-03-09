---
layout: model
title: "Commodity Price Formation"
subtitle: "How Global Markets Set the Price a Producer Actually Receives"
series: "Economic Systems"
series_order: 21
cluster: "MK — Markets and Price Formation"
date: 2026-03-12
image: /assets/images/commodity-markets.png
categories: [modelling]
tags: [economic-geography, commodity-markets, tag-hash-math, tag-hash-viz]
difficulty: 3
math: true
viz: true
math_core:
  - "Benchmark pricing"
  - "Quality differentials"
  - "Basis and netback"
  - "Price discovery"
excerpt: "A Texas Permian producer and an Alberta oil sands producer both sell into a WTI-priced world. When WTI trades at $75, the Texan receives close to $75. The Albertan receives $53. The $22 difference is not random — it is the systematic product of quality penalties, transport tariffs, and diluent costs. Understanding commodity price formation means understanding why identical headline prices produce radically different wellhead receipts."
---

When you read that WTI crude traded at $75 per barrel yesterday, you are reading a price that almost nobody actually received. WTI is a benchmark — a reference point, a financial abstraction, a futures contract settled in Cushing, Oklahoma. The price a producer receives depends on who they are, where their oil came from, what quality it is, how they got it to market, and which refinery ultimately processed it.

This model starts with benchmarks — how they are formed and what they measure — then works outward through quality differentials, transportation adjustments, and the netback calculation to arrive at the number that actually matters: the wellhead price that determines whether a project is economic.

## Benchmark Crudes and How They Are Made

A benchmark crude is a crude oil whose price serves as a reference for pricing other crudes. Three crudes dominate global pricing:

**West Texas Intermediate (WTI):** Light, sweet crude (API gravity ~39°, sulphur ~0.24%) delivered at Cushing, Oklahoma. Priced on the NYMEX futures exchange. The dominant benchmark for North American crudes.

**Brent:** A blend of crudes from the North Sea (Brent, Forties, Oseberg, Ekofisk, Troll — the "BFOET" basket). Light and sweet (API ~38°, sulphur ~0.37%). Priced on ICE Futures Europe. The dominant benchmark for Atlantic Basin and international trade — most of the world's oil is priced off Brent.

**Dubai/Oman:** Medium sour crude (API ~31°, sulphur ~2%) priced in Dubai. The reference benchmark for Middle Eastern crude sold into Asia. Reflects the heavier, sourer crude stream that makes up most of what Asian refineries actually process.

Each benchmark is a physical delivery mechanism — you can actually take delivery of WTI at Cushing or Brent at a North Sea terminal — anchored to real supply and demand, not purely financial. The futures price converges to the physical spot price at expiry because any divergence creates an arbitrage opportunity.

Natural gas has its own benchmarks: Henry Hub in Louisiana (the delivery point for NYMEX natural gas futures and the North American reference), AECO in Alberta (the Canadian benchmark, persistently trading below Henry Hub), and TTF in the Netherlands (the European reference, which became highly volatile after the 2022 Russian supply shock).

Metals benchmarks are set on the London Metal Exchange (LME), with contracts for copper, aluminium, nickel, zinc, and others settled against LME spot prices.

## Price Discovery: How the Benchmark Price Is Set

Price discovery is the process through which a market aggregates dispersed information — about current supply, expected future supply, demand conditions, inventories, geopolitical risk — into a single observable price.

For commodities, price discovery happens through three overlapping mechanisms:

**Futures markets** are the primary mechanism. Thousands of buyers, sellers, hedgers, and speculators continuously trade contracts for delivery at future dates. The futures price reflects the market's collective expectation of the supply-demand balance at that delivery date. Liquidity is high; information is incorporated rapidly. WTI futures on NYMEX are among the most liquid financial instruments in the world.

**Spot markets** for physical cargoes adjust around the futures price. When a tanker of North Sea crude trades, the negotiated price is typically "Dated Brent plus or minus X dollars" — the benchmark provides the base, and the differential reflects the specific cargo's quality, delivery timing, and counterparty preferences.

**Formula pricing** is used for most physical oil trade. A national oil company selling a cargo to an Asian refinery does not negotiate an absolute price — it sets a formula: "Oman/Dubai benchmark, plus $1.50/bbl, delivery CIF Chiba." The refinery agrees to pay whatever Oman/Dubai averages during the bill of lading month, plus the agreed premium. This shifts price risk to the market rather than requiring negotiation on an uncertain future price.

The result is that the benchmark price is publicly visible and continuously updated, while physical traders negotiate differentials to the benchmark that reflect quality, location, and timing. Almost no physical crude changes hands at exactly the benchmark price.

## Quality Differentials: Why Heavy Sour Trades at a Discount

Not all crude is equal. The two key quality dimensions are API gravity (a measure of density, where higher is lighter) and sulphur content (lower is "sweeter"). Refineries are designed to process specific crude slates, and the more complex the refinery, the more it can handle heavier, sourer grades.

The economics of the quality differential:

- **Light sweet crude** (high API, low sulphur) is cheaper to refine — it requires less processing to produce high-value products like gasoline and diesel. Refineries can process it without expensive upgrading equipment.
- **Heavy sour crude** (low API, high sulphur) requires hydrocracking, hydrotreating, and other expensive secondary processes. Refineries that can handle it have spent hundreds of millions on this equipment and demand a discount on the feedstock to justify the investment.

The Western Canada Select (WCS) differential to WTI is the most watched quality differential in Canadian energy markets. WCS is a blend of bitumen and diluent — heavy (API ~20°), high-sulphur (~3.5%). It trades at a persistent discount to WTI reflecting both quality and location:

$$\text{WCS Price} = \text{WTI Price} - \Delta_{\text{quality}} - \Delta_{\text{location}}$$

Historically, the WCS-WTI differential has averaged $14–20/bbl, widening dramatically when export pipelines are constrained (reaching $50/bbl in late 2018 when Enbridge Line 3 was delayed and Trans Mountain was running at capacity).

<div data-viz="echarts" data-options='{"title": {"text": "WTI, Brent, and WCS Weekly Prices 2019–2024", "subtext": "USD/bbl — showing the persistent WCS discount and the 2020 COVID collapse"}, "tooltip": {"trigger": "axis", "axisPointer": {"type": "cross"}}, "legend": {"data": ["WTI", "Brent", "WCS"], "bottom": 0}, "xAxis": {"type": "category", "data": ["Jan 2019","Jul 2019","Jan 2020","Apr 2020","Jul 2020","Jan 2021","Jul 2021","Jan 2022","Apr 2022","Jul 2022","Jan 2023","Jul 2023","Jan 2024","Jul 2024"]}, "yAxis": {"type": "value", "name": "USD/bbl", "min": -10, "max": 110}, "series": [{"name": "WTI", "type": "line", "smooth": true, "data": [52, 57, 60, -5, 40, 52, 71, 85, 103, 95, 78, 75, 72, 78], "lineStyle": {"width": 2}, "itemStyle": {"color": "#5470c6"}}, {"name": "Brent", "type": "line", "smooth": true, "data": [60, 64, 67, 18, 44, 56, 74, 90, 108, 100, 83, 80, 77, 83], "lineStyle": {"width": 2}, "itemStyle": {"color": "#91cc75"}}, {"name": "WCS", "type": "line", "smooth": true, "data": [35, 40, 44, -10, 28, 38, 55, 66, 84, 73, 57, 55, 50, 58], "lineStyle": {"width": 2}, "itemStyle": {"color": "#ee6666"}, "areaStyle": {"opacity": 0.08}}]}'>
</div>

The chart makes the structural penalty visible: even in bull markets, WCS lags WTI by a roughly constant margin. The differential is not cyclical noise — it is a permanent feature of being a landlocked heavy sour producer. In the COVID collapse of April 2020, WCS briefly went deeply negative because storage at Hardisty was full, pipelines were at capacity, and producers could not shut in fast enough.

## The Netback Calculation

The netback is the price the producer actually receives at the wellhead after all deductions between the benchmark and the production point. It is the only price that matters for investment decisions.

$$\text{Netback} = P_{\text{benchmark}} - \Delta_{\text{quality}} - T_{\text{transport}} - C_{\text{diluent}} - C_{\text{processing}}$$

where:
- $P_{\text{benchmark}}$ is the relevant benchmark price (WTI, Brent, etc.)
- $\Delta_{\text{quality}}$ is the quality discount (heavy/sour penalty)
- $T_{\text{transport}}$ is the pipeline or rail tariff from the production point to the market hub
- $C_{\text{diluent}}$ is the cost of the diluent required to move bitumen by pipeline (bitumen is too viscous to flow — it must be blended with condensate or synthetic crude)
- $C_{\text{processing}}$ is any upgrading or tolling cost

For a worked example using 2024 representative prices:

**Texas Permian producer (WTI-quality, Midland):**

$$\text{Netback}_{\text{Permian}} = \$75.00 - \$0 - \$3.50 - \$0 = \$71.50/\text{bbl}$$

The Permian producer pays a small transport fee to get to Cushing or the Gulf Coast but incurs no quality discount (WTI-quality light sweet crude).

**Alberta oil sands producer (bitumen, Athabasca):**

$$\text{Netback}_{\text{Athabasca}} = \$75.00 - \$14.00 - \$8.00 - \$5.50 = \$47.50/\text{bbl (bitumen equivalent)}$$

The $27.50/bbl gap between the Permian and Alberta netbacks — at the same WTI benchmark — is entirely infrastructure and geology. The Alberta producer is selling a fundamentally different product over a fundamentally more constrained supply chain.

<div data-viz="echarts" data-options='{"title": {"text": "WTI to Alberta Bitumen Netback: Waterfall Decomposition", "subtext": "USD/bbl, representative 2024 values — where the price goes between benchmark and wellhead"}, "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}}, "xAxis": {"type": "category", "data": ["WTI Benchmark", "Quality Discount\n(WCS-WTI)", "Trans Mountain\nTariff", "Diluent Cost\n(net)", "= Bitumen\nNetback", "Permian\nNetback (ref.)"]}, "yAxis": {"type": "value", "name": "USD/bbl", "min": 0, "max": 85}, "series": [{"name": "Price Component", "type": "bar", "data": [75, -14, -8, -5.5, 47.5, 71.5], "itemStyle": {"color": ["#5470c6","#ee6666","#ee6666","#ee6666","#91cc75","#73c0de"]}, "label": {"show": true, "position": "top", "formatter": "{c}"}}]}'>
</div>

The waterfall makes the penalty structure concrete. The quality discount is the largest single component — it reflects the refinery economics of upgrading heavy sour crude. Transport is the second largest — it reflects Alberta's landlocked geography and limited pipeline access. The diluent cost is real but recoverable (diluent returns in the condensate stream), making it a net cost only if condensate prices are high.

## Market Segmentation and the Limits of Arbitrage

A key implication of the netback analysis is that markets are not seamlessly integrated. The textbook assumption of a Law of One Price — identical goods trade at identical prices everywhere — only holds when trade is frictionless. When transport has a cost (a tariff, a pipeline fee, an ocean freight rate), identical goods can trade at different prices in different geographies simultaneously without creating a profitable arbitrage opportunity.

The no-arbitrage condition between two markets A and B is:

$$|P_A - P_B| \leq T_{AB}$$

where $T_{AB}$ is the transfer cost between them. If $|P_A - P_B| > T_{AB}$, it is profitable to buy in the cheap market and sell in the expensive one — the arbitrage trade will occur until the price gap is eliminated. If $|P_A - P_B| \leq T_{AB}$, the price difference is within the transport band and no arbitrage is profitable.

This is why WCS can trade $14–20/bbl below WTI without triggering arbitrage that closes the gap: the transfer cost (the pipeline tariff, quality upgrading cost, and market access constraint) exceeds the price differential. The price difference is not a market failure — it is the market correctly pricing geography and quality.

When transport is constrained and no additional capacity exists, the price gap can widen beyond the normal transport cost — because there is no physical mechanism to arbitrage the differential even when it would be profitable to do so. This is what happened in late 2018: the WCS discount widened to $50/bbl not because the economic logic changed, but because pipelines were full and no additional oil could physically move to close the gap.

Understanding commodity price formation is understanding this system: benchmarks set the reference, quality adjustments and transport costs set the differential, and the netback is what actually arrives at the producer's account. The benchmark price is the starting point of a calculation, not the answer.

---

**Next in this cluster:** Model 22 — Spatial Arbitrage and the Law of One Price examines the formal economics of price convergence: when markets integrate, when constraints prevent integration, and how to calculate the dollar cost of a pipeline bottleneck as a price signal.
