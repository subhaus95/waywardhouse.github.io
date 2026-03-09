---
layout: model
title: "Futures Markets as Geographic Instruments"
subtitle: "How Forward Prices Encode Infrastructure Risk, Storage Scarcity, and Time"
series: "Economic Systems"
series_order: 23
cluster: "MK — Markets and Price Formation"
date: 2026-03-12
image: /assets/images/commodity-markets.png
categories: [modelling]
tags: [economic-geography, commodity-markets, tag-hash-math, tag-hash-viz]
difficulty: 4
math: true
viz: true
math_core:
  - "Cost of carry model"
  - "Contango and backwardation"
  - "Convenience yield"
  - "Basis risk"
excerpt: "On April 20, 2020, the WTI May futures contract settled at negative &#36;37.63 per barrel. Oil had never had a negative price before. What actually happened was not mysterious — it was the cost-of-carry model working exactly as designed, in a world where every storage tank near Cushing, Oklahoma was full. The futures market was pricing a geographic constraint: there was nowhere to put the oil, so the market paid people to take it away."
---

A futures contract is, on its surface, a straightforward instrument: an agreement to buy or sell a specific quantity of a commodity at a specific price on a specific future date. But the price of that contract encodes something far richer than a simple forecast of where spot prices will be. It encodes the cost of holding inventory, the value of having physical supply on hand during uncertain times, the geographic specificity of delivery obligations, and the market's collective assessment of how supply and demand will balance at a specific location on a specific date.

This model unpacks that structure. We start with the cost-of-carry model — the theoretical foundation — then work through contango, backwardation, and convenience yield as economic phenomena, before arriving at the geographic application: how basis differentials between delivery points encode spatial information that can be read as an infrastructure signal.

## The Cost-of-Carry Model

If you can store a commodity costlessly and borrow money freely, the futures price must equal the spot price plus the cost of financing the inventory:

$$F(t, T) = S(t) \cdot e^{r(T-t)}$$

where $F(t, T)$ is the futures price at time $t$ for delivery at time $T$, $S(t)$ is the current spot price, $r$ is the continuously compounded risk-free interest rate, and $(T - t)$ is time to delivery in years.

The intuition: you can replicate the futures contract by buying the commodity today (paying $S$), storing it until $T$, and delivering it. The cost of this replication strategy determines the futures price. Any higher futures price creates an arbitrage: sell the futures, buy spot, store, deliver — riskless profit.

When storage has a cost $u$ per unit time (warehouse fees, insurance, pipeline booking fees), the formula becomes:

$$F(t, T) = S(t) \cdot e^{(r + u)(T-t)}$$

And when holding physical inventory provides a benefit — the **convenience yield** $y$ — because having inventory available reduces operating risk or avoids costly production shutdowns during supply disruptions, the formula is:

$$F(t, T) = S(t) \cdot e^{(r + u - y)(T-t)}$$

The convenience yield $y$ is the implicit return to holding physical inventory, above and beyond financial returns. It is not directly observable — it is calculated as the residual that makes the cost-of-carry equation balance given the observed futures price.

## Contango: When Storage Is Plentiful

When $r + u > y$ — when financing and storage costs exceed the convenience yield — futures prices exceed the spot price. This condition is called **contango**:

$$F(t, T) > S(t)$$

Contango says: it is more expensive to hold the commodity for future delivery than to buy it now. The forward curve slopes upward — later delivery months are progressively more expensive.

Economically, contango is a signal of surplus. Storage is available, the market does not feel an urgent need for physical inventory, and the futures price must carry enough premium to incentivise holders to store rather than sell immediately. Contango creates a "storage trade": buy spot, sell futures at a premium, earn the spread as a return for providing storage services.

Contango is the normal condition for most commodities most of the time. WTI futures are typically in a modest contango of 2–5% per year in the front months — roughly reflecting financing costs with minimal convenience yield.

## Backwardation: When Scarcity Bites

When $y > r + u$ — when the convenience yield exceeds carrying costs — spot prices exceed futures prices. This is **backwardation**:

$$F(t, T) < S(t)$$

The forward curve slopes downward — later delivery months are cheaper than prompt delivery. Backwardation signals tightness: physical supply is scarce enough that having inventory on hand is extremely valuable. The market is effectively saying: "We need oil *now* and will pay a premium for prompt delivery."

The convenience yield spikes during supply disruptions because the cost of *not* having inventory — having to shut down a refinery or break a delivery contract — can be enormous. In backwardated markets, it is difficult to execute the storage trade (buy spot, sell futures) because the futures price is below spot — the trade loses money unless you can earn the convenience yield, which by definition accrues only to physical holders of the commodity.

The post-Ukraine 2022 energy market was deeply backwardated across oil, gas, and coal. WTI spot traded &#36;20–30/bbl above 12-month futures at points in mid-2022. This was the market screaming that physical supply right now was extraordinarily scarce.

## April 20, 2020: When Contango Broke the Market

The most dramatic demonstration of the cost-of-carry model in modern commodity history occurred on April 20, 2020. The WTI May futures contract — which expired on April 21, with delivery in May at Cushing, Oklahoma — settled at **negative &#36;37.63 per barrel**.

This was not irrational. It was the cost-of-carry model operating exactly as designed, but in an extreme environment.

The mechanism: COVID lockdowns had collapsed oil demand globally. Storage tanks at Cushing (the WTI delivery point) were near capacity. The May contract required physical delivery at Cushing. Holders of long May contracts who did not want to take physical delivery needed to roll to June — but the June contract was trading at $+20/bbl, and there was essentially no one willing to take physical delivery at Cushing in May because there was nowhere to put the oil.

The cost of taking delivery and finding storage — negative &#36;37.63/bbl — was the market's price for one month of storage at Cushing under conditions of near-complete capacity exhaustion. The cost-of-carry model had always predicted that if $u$ (storage cost) became extremely high, futures prices could fall below spot prices — or even below zero. In 2020, $u$ effectively became infinite for a brief period, and the formula delivered a negative price.

The June contract did not go negative because by June, some storage capacity had freed up. The market structure reveals the geographic precision of futures pricing: the May price was about Cushing in May. Not Houston. Not Rotterdam. Not Alberta. Cushing, in May, with full tanks.

## The Forward Curve as State Variable

The shape of the futures curve carries information about the current and expected future supply-demand balance. We can read it as a continuous state variable:

$$\text{Slope} = \frac{dF}{dT} = F \cdot (r + u - y)$$

When the slope is positive (contango): $(r + u) > y$, storage is plentiful, no urgency. When the slope is negative (backwardation): $y > (r + u)$, physical supply is tight.

The term structure across all maturities encodes the market's expectation of how the supply-demand balance evolves over time. A curve that is backwardated at the front but switches to contango at 12 months is saying: "The market is tight now, but we expect it to ease within a year."

<div data-viz="echarts" data-options='{"title": {"text": "WTI Futures Curve Shape: Three Market States", "subtext": "Spot to 24 months forward — contango (2020 surplus), backwardation (2022 post-Ukraine), flat (2023 normalisation)"}, "tooltip": {"trigger": "axis"}, "legend": {"data": ["Contango (Apr 2020)", "Backwardation (Jul 2022)", "Flat (Sep 2023)"], "bottom": 0}, "xAxis": {"type": "category", "data": ["Spot","1M","2M","3M","6M","9M","12M","18M","24M"]}, "yAxis": {"type": "value", "name": "USD/bbl", "min": 0, "max": 130}, "series": [{"name": "Contango (Apr 2020)", "type": "line", "smooth": true, "data": [15, 22, 25, 27, 30, 32, 33, 35, 36], "lineStyle": {"width": 2}, "itemStyle": {"color": "#5470c6"}, "markPoint": {"data": [{"type": "min", "name": "Spot low"}]}}, {"name": "Backwardation (Jul 2022)", "type": "line", "smooth": true, "data": [105, 100, 96, 93, 87, 83, 80, 76, 73], "lineStyle": {"width": 2}, "itemStyle": {"color": "#ee6666"}}, {"name": "Flat (Sep 2023)", "type": "line", "smooth": true, "data": [88, 87, 86, 85, 83, 82, 81, 80, 79], "lineStyle": {"width": 2}, "itemStyle": {"color": "#91cc75"}}]}'>
</div>

The three curves tell three different stories about the world. The 2020 contango curve has an enormous slope — storing oil for 24 months at the April 2020 spot price and delivering it into a futures contract was worth &#36;21/bbl, reflecting the extraordinary cost of storage. The 2022 backwardation curve falls steeply — the market in July 2022 was pricing in supply relief over time, as LNG and non-Russian sources ramped up. The 2023 flat curve reflects relative market equilibrium: carrying costs and convenience yields roughly balanced.

## Geographic Basis: Two Delivery Points, One Forward Curve

The futures market for WTI settles at Cushing. The spot market for AECO gas settles at the Alberta-Saskatchewan border. The futures market for Henry Hub settles in Louisiana. Each is a distinct market with its own forward curve, and the relationship between their curves encodes both spatial information (transport cost between the locations) and temporal information (storage and carrying costs).

**The basis** between two delivery points at the same delivery date is:

$$\text{Basis}(t, T) = F_{\text{HH}}(t, T) - F_{\text{AECO}}(t, T)$$

For identical quality commodities, this basis should equal the competitive transport cost from AECO to Henry Hub. If it exceeds the transport cost, a capacity constraint is embedded in the forward prices — the market is pricing in the expectation that the constraint will persist through the delivery date $T$.

This is the geographic instrument interpretation: the AECO-Henry Hub futures basis is a market forecast of the transport constraint. When it exceeds the pipeline tariff, the futures market is predicting that capacity will be insufficient at delivery. When it equals the tariff, it predicts free flow. Reading the forward basis is reading the market's assessment of infrastructure adequacy — at every future date.

## Basis Risk: The Alberta Producer's Hedging Problem

An Alberta oil producer wants to hedge price risk — to lock in a future price for their production. The natural hedge is to sell WTI futures on NYMEX, since WTI is the benchmark that drives most price negotiations.

But the Alberta producer does not sell WTI. They sell WCS — and WCS trades at a persistent discount to WTI. The WCS-WTI differential (the basis) has historically averaged &#36;14–20/bbl, but it is itself volatile. In 2018, it widened to &#36;50/bbl. In 2020, it briefly went to near parity as WTI collapsed faster than WCS could follow.

**Basis risk** is the risk that the differential between the price you are hedging and the price you are receiving changes in an unexpected direction. Even if you have perfectly hedged your WTI exposure, you retain full exposure to the WCS-WTI differential as unhedged basis risk.

The total price risk for an Alberta oil producer is:

$$\text{WCS Price} = \text{WTI Price} - \text{Differential}$$
$$\text{WCS Price Risk} = \text{WTI Price Risk} + \text{Differential Risk}$$

A WTI futures hedge eliminates WTI price risk. It does not touch differential risk. The differential itself must be separately hedged — using WCS-specific derivative instruments that have historically been less liquid and more expensive than WTI futures.

<div data-viz="echarts" data-options='{"title": {"text": "WCS-WTI Differential vs Trans Mountain Utilisation 2016–2024", "subtext": "Showing that pipeline utilisation rate is the primary driver of differential widening"}, "tooltip": {"trigger": "axis", "axisPointer": {"type": "cross"}}, "legend": {"data": ["WCS-WTI Differential (USD/bbl)", "Trans Mountain Utilisation (%)"], "bottom": 0}, "xAxis": {"type": "category", "data": ["Q1 2016","Q3 2016","Q1 2017","Q3 2017","Q1 2018","Q3 2018","Q4 2018","Q1 2019","Q3 2019","Q1 2020","Q3 2020","Q1 2021","Q3 2021","Q1 2022","Q3 2022","Q1 2023","Q3 2023","Q1 2024"]}, "yAxis": [{"type": "value", "name": "USD/bbl Differential", "min": 0, "max": 55, "inverse": false}, {"type": "value", "name": "Pipeline Utilisation (%)", "min": 50, "max": 105, "position": "right"}], "series": [{"name": "WCS-WTI Differential (USD/bbl)", "type": "bar", "data": [18, 15, 14, 16, 22, 35, 49, 20, 15, 18, 12, 14, 16, 14, 13, 15, 17, 14], "itemStyle": {"color": "#ee6666", "opacity": 0.8}}, {"name": "Trans Mountain Utilisation (%)", "type": "line", "yAxisIndex": 1, "smooth": true, "data": [88, 85, 90, 92, 95, 98, 100, 92, 87, 82, 75, 80, 85, 88, 86, 84, 86, 78], "lineStyle": {"width": 2}, "itemStyle": {"color": "#5470c6"}}]}'>
</div>

The relationship is visible: when Trans Mountain operates near 100% utilisation, the WCS-WTI differential widens significantly — because there is no capacity margin to absorb additional production, and the market cannot arbitrage the differential through additional pipeline shipments. The Q4 2018 spike to nearly &#36;50/bbl occurred when Trans Mountain was simultaneously at capacity and regulatory uncertainty about the expansion project was at its peak, eliminating the expectation of new capacity.

## The Forward Curve as an Infrastructure Signal

Putting this together: the forward basis between AECO and Henry Hub futures, or between WCS and WTI futures, is a market forecast of how long a geographic constraint will persist. When the basis for delivery one year from now is as large as the basis for prompt delivery, the market is forecasting that the constraint does not resolve within one year. When the one-year basis is lower than the prompt basis, the market expects some relief.

This makes futures markets extraordinarily useful for infrastructure planning — not because they are always right, but because they aggregate the dispersed information of all market participants into a single observable price. The Trans Mountain Expansion project was justified, in part, by the persistent forward basis in WCS derivatives markets that signalled a multi-year transport constraint.

The limitation is that the market cannot distinguish between constraint types. A regulatory delay (reversible) and a geological constraint (irreversible) would both produce a widened basis. Reading the futures curve tells you the market's assessment of the constraint's persistence, but not its underlying cause.

Understanding that futures prices are not just time prices but geographic prices — that every futures contract embeds a location, a delivery point, a transport infrastructure assumption — changes how we read commodity market data. The WTI price is not "the oil price." It is the price of a specific grade of crude at a specific location in Oklahoma on a specific date, and the entire commodity price system is built around differentials from that single anchor.

---

**Next in this cluster:** Model 24 — Price Volatility and Its Geographic Consequences examines why commodity price swings hit landlocked, single-product regions harder than diversified coastal producers — and how to measure the amplification effect using GARCH models and revenue-at-risk analysis.

## References

Black, Fischer, and Myron Scholes. 1973. "The Pricing of Options and Corporate Liabilities." *Journal of Political Economy* 81 (3): 637–654. <https://doi.org/10.1086/260062>

Canada Energy Regulator. 2024. "Crude Oil Price Differential." Government of Canada. <https://www.cer-rec.gc.ca/en/data-analysis/energy-commodities/crude-oil-petroleum-products/crude-oil-price-differential/>

CME Group. 2025. "Light Sweet Crude Oil (WTI) Futures." NYMEX. <https://www.cmegroup.com/markets/energy/crude-oil/light-sweet-crude.html>

CME Group. 2020. "WTI Crude Oil Futures and the Events of April 20, 2020." CME Group Insights. <https://www.cmegroup.com/education/articles-and-reports/wti-crude-oil-futures-negative-prices.html>

Fama, Eugene F. 1984. "Forward and Spot Exchange Rates." *Journal of Monetary Economics* 14 (3): 319–338. <https://doi.org/10.1016/0304-3932(84)90046-1>

Gibson, Rajna, and Eduardo S. Schwartz. 1990. "Stochastic Convenience Yields and the Pricing of Oil Contingent Claims." *Journal of Finance* 45 (3): 959–976. <https://doi.org/10.1111/j.1540-6261.1990.tb05114.x>

ICE Futures Europe. 2025. "Brent Crude Futures." Intercontinental Exchange. <https://www.ice.com/products/219/Brent-Crude-Futures>

Kaldor, Nicholas. 1939. "Speculation and Economic Stability." *Review of Economic Studies* 7 (1): 1–27. <https://doi.org/10.2307/2967593>

Samuelson, Paul A. 1952. "Spatial Price Equilibrium and Linear Programming." *American Economic Review* 42 (3): 283–303. <https://www.jstor.org/stable/1907862>

Working, Holbrook. 1949. "The Theory of Price of Storage." *American Economic Review* 39 (6): 1254–1262. <https://www.jstor.org/stable/1816601>
