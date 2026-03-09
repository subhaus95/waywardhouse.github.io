---
layout: model
title: "Price Volatility and Its Geographic Consequences"
subtitle: "Why Resource Price Swings Hit Some Places Harder Than Others"
series: "Economic Systems"
series_order: 24
cluster: "MK — Markets and Price Formation"
date: 2026-03-12
image: /assets/images/commodity-markets.png
categories: [modelling]
tags: [economic-geography, commodity-markets, tag-hash-math, tag-hash-viz]
difficulty: 3
math: true
viz: true
math_core:
  - "Volatility measurement"
  - "Conditional volatility (GARCH)"
  - "Beta and correlation"
  - "Revenue at risk"
excerpt: "WTI crude oil has historical annualised volatility of roughly 35% — about twice the volatility of the S&P 500. But Alberta's wellhead netback has volatility significantly higher than WTI, because the WCS-WTI differential is itself volatile and correlated with oil price declines. When WTI falls, the differential widens at the same time. Landlocked heavy-oil producers face a double jeopardy: they receive less than benchmark when times are good, and they take larger losses than benchmark when times are bad."
---

Alberta's provincial government budget in fiscal year 2014–15 assumed WTI would average &#36;94/bbl. The actual average was &#36;81/bbl. The next year, it was &#36;53/bbl. The year after that, &#36;46/bbl. Over three years, the provincial government experienced a revenue shortfall of roughly &#36;30 billion relative to its planning assumptions — a consequence of commodity price volatility that was entirely predictable in its existence, if not its timing.

Volatility is not a peripheral feature of commodity markets. It is their central characteristic. Understanding why commodity prices are volatile, how volatility clusters and propagates, and why some geographies experience amplified volatility while others are shielded from it is essential for any serious analysis of resource-dependent economies.

## Measuring Volatility

Volatility is the annualised standard deviation of returns. For a daily price series $P_t$, the daily log return is:

$$r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)$$

The realised volatility over a rolling window of $N$ days is:

$$\hat{\sigma}_t = \sqrt{\frac{252}{N} \sum_{i=t-N+1}^{t} r_i^2}$$

where the factor 252 annualises from daily to annual frequency (252 trading days per year). This is the simplest estimator — the square root of the mean squared daily return, scaled to annual.

For WTI crude oil, historical realised volatility has averaged approximately 30–40% per year over the 2010–2024 period, with substantial variation: falling to 15–20% during stable price regimes and spiking to 80–100% during the 2020 COVID collapse and the 2022 Ukraine crisis. For comparison, the S&P 500 has averaged approximately 15–20% annual volatility over the same period.

Why are commodity prices so much more volatile than equity prices? Three structural reasons:

**Supply is inelastic in the short run.** You cannot instantly increase oil production when prices rise — wells take months to drill, pipelines take years to build. The price must adjust fully to balance supply and demand because supply cannot.

**Demand is also inelastic.** Industrial users and households cannot instantly switch fuels when oil prices rise — they adjust slowly. Both sides of the market are inflexible in the short run, so small supply or demand shocks produce large price moves.

**Storage is limited and heterogeneous.** Unlike financial assets, you cannot infinitely store oil. Storage capacity is finite and distributed (in tanks, pipelines, in-ground reserves), making the price system more sensitive to inventory shocks.

## GARCH: Volatility Clusters

The most important stylised fact about commodity price volatility is that **it clusters**: high-volatility periods tend to follow high-volatility periods, and low-volatility periods follow low-volatility periods. This is called volatility clustering, and it was formalised in the GARCH(1,1) model (Generalised Autoregressive Conditional Heteroscedasticity, Bollerslev 1986).

The GARCH(1,1) specification:

$$r_t = \mu + \epsilon_t, \quad \epsilon_t = \sigma_t z_t, \quad z_t \sim \mathcal{N}(0, 1)$$

$$\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2$$

where:
- $\sigma_t^2$ is the **conditional variance** — today's volatility given yesterday's information
- $\omega > 0$ is a long-run baseline variance
- $\alpha \epsilon_{t-1}^2$ is the **ARCH term** — how much yesterday's shock affects today's volatility ($\alpha$ is the "surprise" coefficient)
- $\beta \sigma_{t-1}^2$ is the **GARCH term** — how much yesterday's volatility persists into today ($\beta$ is the persistence coefficient)

For WTI crude, estimated GARCH(1,1) parameters are approximately $\alpha \approx 0.08$ and $\beta \approx 0.89$. The persistence $(\alpha + \beta) \approx 0.97$ — very close to 1, meaning volatility is highly persistent. A shock to volatility takes a long time to decay.

The long-run unconditional variance is:

$$\bar{\sigma}^2 = \frac{\omega}{1 - \alpha - \beta}$$

At $\alpha + \beta = 0.97$, the denominator is only 0.03 — small shocks to $\omega$ produce large changes in long-run volatility. This is why oil price regime changes (new OPEC policy, energy transition demand shift) have outsized effects on long-run price uncertainty.

<div data-viz="echarts" data-options='{"title": {"text": "WTI 30-Day Realised Volatility 2010–2024 with GARCH Overlay", "subtext": "Annualised volatility (%) — realised (bars) and GARCH(1,1) fitted conditional volatility (line)"}, "tooltip": {"trigger": "axis", "axisPointer": {"type": "cross"}}, "legend": {"data": ["Realised Volatility (30d)", "GARCH(1,1) Fitted"], "bottom": 0}, "xAxis": {"type": "category", "data": ["Jan 2010","Jan 2011","Jan 2012","Jan 2013","Jan 2014","Jan 2015","Jan 2016","Jan 2017","Jan 2018","Jan 2019","Jan 2020","Apr 2020","Jan 2021","Jan 2022","Jul 2022","Jan 2023","Jan 2024"]}, "yAxis": {"type": "value", "name": "Annualised Volatility (%)", "min": 0, "max": 120}, "series": [{"name": "Realised Volatility (30d)", "type": "bar", "data": [32, 28, 24, 18, 22, 45, 50, 28, 32, 38, 55, 112, 48, 38, 45, 30, 28], "itemStyle": {"color": "#5470c6", "opacity": 0.6}}, {"name": "GARCH(1,1) Fitted", "type": "line", "smooth": true, "data": [30, 26, 22, 20, 24, 38, 44, 28, 30, 35, 48, 88, 52, 40, 43, 32, 28], "lineStyle": {"width": 2}, "itemStyle": {"color": "#ee6666"}}]}'>
</div>

The chart makes volatility clustering visible: the 2015–16 period (OPEC supply war), the April 2020 COVID collapse (peak at over 100%), and the 2022 Ukraine shock all produced persistent elevated volatility — not single spikes but sustained periods of high conditional variance. The GARCH model tracks these clusters closely because it builds in the persistence structure.

## Transmission to Regional Economies

Price volatility does not stop at the commodity market. It transmits through a chain to regional economies, amplifying or dampening at each step.

The transmission chain from oil price volatility to Alberta employment volatility runs through five links:

1. **WTI price volatility** → **WCS netback volatility** (amplified because differential is also volatile)
2. **WCS netback volatility** → **upstream capital expenditure volatility** (amplified because investment decisions are nonlinear — projects are either sanctioned or cancelled)
3. **Capital expenditure volatility** → **employment volatility** (roughly proportional, with a lag)
4. **Employment volatility** → **population volatility** (migration responds to employment, with a longer lag)
5. **Population volatility** → **property price volatility** and **retail sales volatility** (cascading demand effects)

Each link involves a multiplier. The capex-to-employment multiplier for oil sands construction is typically estimated at 7–10 direct and indirect jobs per million dollars of investment. The employment-to-population multiplier reflects family migration decisions. By the time WTI price volatility has propagated to Fort McMurray property prices, the amplification factor can be 3–5 times the original price shock.

## The Double Jeopardy Problem

The key geographic amplification mechanism for Alberta is what can be called **double jeopardy**: the WCS-WTI differential is not independent of the WTI price. It is negatively correlated with it.

When WTI falls, the WCS-WTI differential tends to widen simultaneously. There are two reasons:

**Pipeline utilisation falls in absolute terms but pipeline capacity commitment does not.** When prices are low, producers curtail voluntary shipments, but take-or-pay contracts still fill much of the capacity. The effective available discretionary capacity falls, and any additional supply pushes the differential wider.

**Refinery incentives shift.** At high WTI prices, the economics of running expensive hydrocracking equipment to process heavy sour crude are favourable — the spread between heavy and light refined products is wide. At low WTI prices, refineries are less willing to pay for the complexity, and heavy sour differentials widen.

The combined effect on Alberta's wellhead netback is:

$$\text{WCS Netback} = \underbrace{P_{\text{WTI}}}_{\text{benchmark falls}} - \underbrace{\Delta_{\text{diff}}(P_{\text{WTI}})}_{\text{widens when benchmark falls}} - T_{\text{transport}}$$

The derivative with respect to WTI is:

$$\frac{d(\text{Netback})}{dP_{\text{WTI}}} = 1 - \frac{d\Delta_{\text{diff}}}{dP_{\text{WTI}}}$$

Historical data suggests $d\Delta_{\text{diff}}/dP_{\text{WTI}} \approx -0.3$ to $-0.5$ — a &#36;1 fall in WTI is typically associated with a &#36;0.30–&#36;0.50 widening in the WCS-WTI differential. This means the Alberta netback falls by &#36;1.30–&#36;1.50 for every &#36;1 fall in WTI. The amplification is real and persistent.

## Revenue at Risk

**Value at Risk (VaR)** is a standard financial risk measure: the loss that will be exceeded with probability $p$ over a given time horizon. Adapted to government commodity revenues, it becomes **Revenue at Risk (RaR)**: the shortfall in annual royalty revenue relative to the expected case, at the 5th percentile of the price distribution.

If annual royalty revenue $R$ is approximately log-normally distributed with mean $\mu_R$ and standard deviation $\sigma_R$, then the 5th percentile revenue is:

$$R_{5\%} = \exp\left(\ln(\mu_R) - 1.645 \cdot \sigma_R\right)$$

For Alberta government oil royalty revenues, historical parameters (2010–2024) are approximately:
- Mean annual royalty revenue: ~&#36;10 billion CAD
- Standard deviation: ~&#36;7 billion CAD
- Coefficient of variation: ~70%

This implies the 5th percentile revenue is approximately:

$$R_{5\%} = \exp(\ln(10) - 1.645 \times 0.7 \times \ln(10) / \ln(10)) \approx \&#36;2.5 \text{ billion}$$

At the 5th percentile, royalty revenues are about 25% of their mean — a catastrophic fiscal shock. This occurred in 2015–16 (&#36;2.8 billion in royalties) and again in 2020–21 (&#36;2.3 billion).

For fiscal planning purposes, the Alberta government should budget at or near the 5th percentile and treat any royalty revenue above that as a windfall to be directed to the Heritage Fund. In practice, Alberta has historically budgeted at or above the 50th percentile and been surprised by the downside.

## Alberta Revenue Beta

The **revenue beta** is the sensitivity of Alberta government revenues to WTI price changes — the Alberta-fiscal equivalent of the CAPM beta for equities.

From historical data, the estimated relationship is:

$$\Delta R_{\text{Alberta}} \approx \beta \cdot \Delta P_{\text{WTI}}$$

where $\beta$ is estimated at roughly 1.5–2.0 (in proportional terms): a 10% decline in WTI is historically associated with a 15–20% decline in total Alberta government revenues.

This high beta reflects the royalty dependence identified in the RE cluster: when oil prices fall, royalties collapse, but the government's spending obligations do not. The structural deficit created by a 20% revenue fall in a single year is not closable by normal fiscal adjustment.

<div data-viz="echarts" data-options='{"title": {"text": "Alberta Government Revenue: With vs Without Oil Royalties", "subtext": "Illustrating total revenue volatility reduction through fiscal diversification (CAD billion)"}, "tooltip": {"trigger": "axis"}, "legend": {"data": ["Total Revenue (historical)", "Non-royalty Revenue (stable base)", "Royalty Revenue (volatile)", "Diversified Target (royalties capped at 15%)"], "bottom": 0}, "xAxis": {"type": "category", "data": ["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024"]}, "yAxis": {"type": "value", "name": "CAD Billion", "min": 0, "max": 80}, "series": [{"name": "Non-royalty Revenue (stable base)", "type": "bar", "stack": "revenue", "data": [32, 34, 35, 36, 37, 33, 32, 34, 35, 36, 32, 35, 40, 43, 45], "itemStyle": {"color": "#5470c6"}}, {"name": "Royalty Revenue (volatile)", "type": "bar", "stack": "revenue", "data": [8, 9, 8, 7, 9, 3, 2, 5, 9, 5, 2, 8, 25, 16, 12], "itemStyle": {"color": "#ee6666", "opacity": 0.8}}, {"name": "Total Revenue (historical)", "type": "line", "data": [40, 43, 43, 43, 46, 36, 34, 39, 44, 41, 34, 43, 65, 59, 57], "lineStyle": {"width": 2, "type": "dashed"}, "itemStyle": {"color": "#333"}}, {"name": "Diversified Target (royalties capped at 15%)", "type": "line", "smooth": true, "data": [38, 40, 41, 42, 43, 38, 37, 40, 41, 41, 37, 40, 46, 49, 52], "lineStyle": {"width": 2}, "itemStyle": {"color": "#fac858"}}]}'>
</div>

The chart makes the stability case for fiscal diversification concrete. The royalty-inclusive revenue (stacked bars) swings from &#36;34 billion in bust years to &#36;65 billion in the 2022 boom — a &#36;31 billion range. A diversification strategy that caps the royalty contribution and directs excess to a stabilisation fund would produce a smoother, more predictable revenue profile (gold line) — with lower peak revenues but dramatically lower trough risks.

## Diversification as Volatility Management

The same mathematics that justify portfolio diversification in finance apply directly to regional economic structure. If a region's income comes from $N$ independent sectors each with volatility $\sigma$, the portfolio volatility is:

$$\sigma_{\text{portfolio}} = \frac{\sigma}{\sqrt{N}}$$

Diversification reduces volatility by the square root of the number of sectors. Moving from a single-sector (oil) economy to a two-sector economy (oil + non-oil) reduces volatility by a factor of $\sqrt{2} \approx 1.41$, all else equal.

The real world is messier — sectors are correlated, transitions are path-dependent, and capabilities built in oil sands engineering do not immediately transfer to software or finance. But the fundamental logic holds: diversification reduces the aggregate risk of the economic portfolio, even when individual sector returns are unchanged.

Alberta's high revenue beta — and the predictable fiscal crises that accompany oil price downturns — is not a natural disaster. It is the fiscal consequence of a policy choice to remain concentrated in a volatile commodity and to spend royalty revenues rather than save them as a buffer. The GARCH model tells us the clustering is structural. The beta tells us the amplification is systematic. The revenue-at-risk calculation tells us the downside is quantifiable. What changes these numbers is policy, not geology.

---

**Next in this cluster:** Model 25 — The Integrated Price System synthesises benchmarks, spatial arbitrage, forward pricing, and volatility into a single geographic framework — and closes the cluster with a scenario analysis of Alberta's price surface under three infrastructure futures to 2030.

## References

Alberta Treasury Board and Finance. 2015. *Budget 2015: A Plan for Jobs and the Economy*. Edmonton: Government of Alberta. <https://open.alberta.ca/publications/budget-2015>

Bollerslev, Tim. 1986. "Generalised Autoregressive Conditional Heteroscedasticity." *Journal of Econometrics* 31 (3): 307–327. <https://doi.org/10.1016/0304-4076(86)90063-1>

Canada Energy Regulator. 2024. "Crude Oil Price Differential." Government of Canada. <https://www.cer-rec.gc.ca/en/data-analysis/energy-commodities/crude-oil-petroleum-products/crude-oil-price-differential/>

Engle, Robert F. 1982. "Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation." *Econometrica* 50 (4): 987–1007. <https://doi.org/10.2307/1912773>

Fattouh, Bassam. 2011. "An Anatomy of the Crude Oil Pricing System." Oxford Institute for Energy Studies Working Paper WPM 40. <https://www.oxfordenergy.org/publications/an-anatomy-of-the-crude-oil-pricing-system/>

Government of Alberta. 2023. *Annual Report 2022–23: Treasury Board and Finance*. Edmonton: Government of Alberta. <https://open.alberta.ca/publications/treasury-board-and-finance-annual-report>

Peltzman, Sam. 2000. "Prices Rise Faster than They Fall." *Journal of Political Economy* 108 (3): 466–502. <https://doi.org/10.1086/262126>

Pindyck, Robert S. 2004. "Volatility and Commodity Price Dynamics." *Journal of Futures Markets* 24 (11): 1029–1047. <https://doi.org/10.1002/fut.20120>

World Bank. 2025. "Commodity Markets (Pink Sheet)." World Bank Group. <https://www.worldbank.org/en/research/commodity-markets>
