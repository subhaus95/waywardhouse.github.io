---
layout: model
title: "The Resource Curse"
subtitle: "Booms, Busts, and the Staples Trap"
series: "Economic Systems"
series_order: 19
cluster: "RE — Resource Economics"
date: 2026-03-11
categories: [modelling]
tags: [economic-geography, resource-economics, tag-hash-math, tag-hash-viz]
difficulty: 4
math: true
viz: true
math_core:
  - "Dutch disease"
  - "Staples theory"
  - "Volatility transmission"
  - "Diversification indices"
excerpt: "Resource-rich regions often grow more slowly than resource-poor ones. This paradox — the resource curse — operates through three interacting mechanisms: Dutch disease warps the exchange rate, boom-bust volatility disrupts investment, and the political economy of rent locks institutions into extraction dependency. Alberta is not immune."
---

There is something deeply counterintuitive about the resource curse. A region discovers it sits atop billions of barrels of oil, or a mountain of iron ore, or a vein of gold — and the conventional expectation is prosperity. Yet the empirical record is troubling. Angola, Nigeria, Venezuela, and dozens of other resource-rich nations have grown more slowly than resource-poor counterparts at similar income levels. Within Canada, the provinces most dependent on resource extraction have the most volatile GDP trajectories and the least diversified economic bases.

Understanding why requires three lenses: Dutch disease (the exchange rate mechanism), volatility transmission (the boom-bust amplification), and staples theory (the institutional lock-in). Together they constitute what economists call the resource curse — and while "curse" overstates a probabilistic tendency, the pattern is real enough to demand explanation.

## Dutch Disease: The Exchange Rate Channel

The Dutch disease mechanism was named after the experience of the Netherlands following large natural gas discoveries in the 1960s. Gas exports caused the guilder to appreciate, crushing Dutch manufacturing exports. The same dynamic operates wherever resource booms are large relative to the broader economy.

The transmission runs through four steps:

1. **Resource boom** → increased foreign exchange earnings from resource exports
2. **Appreciation** → the exchange rate strengthens as resource-currency inflows rise
3. **Tradeable sector squeeze** → manufacturing, agriculture, and other export sectors face reduced price competitiveness
4. **De-industrialisation** → labour and capital shift out of manufacturing into services and resources

The real exchange rate effect can be decomposed into a **spending effect** (domestic demand rises with resource income, pushing up non-tradeable prices) and a **resource movement effect** (factors of production physically move into the resource sector).

For Canada, the Canadian dollar's correlation with oil prices is well-documented. During the 2003–2014 commodity supercycle, the CAD rose from $0.63 USD to over $1.05 USD — a 67% appreciation. Over the same period, Ontario's manufacturing sector shed roughly 300,000 jobs. The counterfactual — what manufacturing employment would have been without the petrodollar — is contested, but the directional effect is clear.

The **Balassa-Samuelson-style** exchange rate model for a resource-exporting economy suggests the real exchange rate appreciation is:

$$\Delta q = \frac{\omega_X}{\omega_N} \cdot \Delta p_X$$

where $q$ is the real exchange rate, $p_X$ is the resource price, $\omega_X$ and $\omega_N$ are the shares of resource and non-resource exports in GDP. High resource dependence (large $\omega_X / \omega_N$) means larger exchange rate swings from any given resource price change.

## Staples Theory: The Canadian Lens

Harold Innis, the Canadian economic historian, developed **staples theory** in the 1930s to explain Canada's distinctive development pattern. His core observation: Canada's economy was built around successive export commodities — cod, fur, wheat, timber, minerals, oil — each of which created infrastructure, institutions, and skills aligned to extraction and export rather than to domestic value-added processing.

The **staples trap** is the long-run consequence. Each commodity cycle:

1. **Builds extraction infrastructure** — railways, pipelines, port facilities — optimised for getting the staple to tidewater
2. **Creates complementary industries** — equipment supply, financing, regulatory expertise — all serving extraction
3. **Attracts labour and capital** at wages and returns calibrated to the commodity cycle
4. **Shapes institutions** — land tenure, property rights, regulatory frameworks — that favour large extractive firms
5. **Locks in a growth model** — when the commodity busts, the economy lacks the alternative capabilities to pivot

For Alberta, the oil sands created world-class capabilities in bitumen extraction, upgrading, and heavy oil pipeline transport. But they generated minimal upstream technology development (most equipment is imported), limited downstream petrochemical processing (most bitumen leaves Alberta unrefined), and negligible knowledge spillovers to non-resource industries.

The **backward linkages** (inputs to the resource sector) were supplied largely by Texas, Ontario, and international suppliers. The **forward linkages** (processing the extracted resource) were captured by US refineries. Alberta's oil sands operate as a classic staple: raw material in, extraction rent out, with limited economic complexity generated in between.

## Volatility Transmission: The Boom-Bust Amplifier

Even if Dutch disease and staples effects are partially mitigated, resource dependence creates a **volatility problem**. Oil prices are among the most volatile commodity prices in the world — standard deviation of annual returns is roughly 30–40%, compared to 15–20% for equity markets. This volatility transmits through the economy in a chain of effects with different lags:

$$\underbrace{P_{\text{oil}}}_{\text{t}} \rightarrow \underbrace{R_{\text{royalty}}}_{\text{t}} \rightarrow \underbrace{G_{\text{spending}}}_{\text{t+1}} \rightarrow \underbrace{E_{\text{employment}}}_{\text{t+1 to t+2}} \rightarrow \underbrace{N_{\text{migration}}}_{\text{t+2 to t+4}} \rightarrow \underbrace{H_{\text{housing}}}_{\text{t+2 to t+5}}$$

Oil price → royalty revenues (immediate) → government spending (budget cycle lag) → employment (hiring cycle) → net migration (household relocation lag) → housing prices (construction supply lag).

The volatility **amplifies** at each stage because agents respond to the signal with momentum. Workers move to Alberta during booms, committing to mortgages; when the bust arrives, they cannot move quickly enough, creating housing price crashes, negative equity, and financial distress that deepens the recession.

The **volatility transmission regression** estimates the sensitivity at each step. A simple version:

$$\Delta \ln Y_{t} = \alpha + \beta \cdot \Delta \ln P_{\text{oil}, t} + \gamma \cdot \Delta \ln P_{\text{oil}, t-1} + \epsilon_t$$

where $Y_t$ is any downstream variable (government revenue, employment, etc.) and $\beta, \gamma$ capture contemporaneous and lagged responses. For Alberta GDP, estimates suggest $\beta \approx 0.3$: a 10% oil price fall reduces Alberta GDP growth by roughly 3 percentage points — a very high sensitivity for a province with a $400 billion economy.

<div data-viz="echarts" data-options='{"title": {"text": "Alberta GDP Growth vs WTI Oil Price (2000–2024)", "subtext": "Annual % change in Alberta real GDP vs WTI annual average price change"}, "tooltip": {"trigger": "axis"}, "legend": {"data": ["Alberta GDP Growth (%)", "WTI Price Change (%)"], "bottom": 0}, "xAxis": {"type": "category", "data": ["2000","2002","2004","2006","2008","2010","2012","2014","2016","2018","2020","2022","2024"]}, "yAxis": {"type": "value", "name": "Annual Change (%)", "min": -20, "max": 30}, "series": [{"name": "Alberta GDP Growth (%)", "type": "bar", "data": [5.2, 4.1, 5.8, 7.2, 0.5, 4.8, 4.3, 4.7, -3.7, 2.4, -8.2, 5.1, 2.8], "itemStyle": {"color": "#5470c6", "opacity": 0.7}}, {"name": "WTI Price Change (%)", "type": "line", "data": [57, -4, 33, 19, 38, 29, -1, -8, -46, 25, -23, 67, -11], "lineStyle": {"width": 2}, "itemStyle": {"color": "#ee6666"}}]}'>
</div>

The correlation is visible even in this simplified chart. The 2015–16 downturn (Alberta GDP −3.7%) followed the 2014 oil price collapse; the 2020 recession (−8.2%) combined COVID demand destruction with the oil price crash. Strong oil price years generally track Alberta economic booms.

## The Herfindahl-Hirschman Index: Measuring Concentration

The **Herfindahl-Hirschman Index (HHI)** measures economic concentration. Applied to export structure, it captures how diversified (or not) a regional economy is:

$$\text{HHI} = \sum_{i=1}^{N} s_i^2$$

where $s_i$ is the share of sector $i$ in total exports. HHI ranges from $1/N$ (perfectly equal across $N$ sectors) to 1 (complete monopoly). Higher HHI means greater concentration and higher vulnerability to sector-specific shocks.

Alberta's export HHI is dominated by energy. Energy goods account for roughly 85% of Alberta's merchandise exports — an HHI approaching 0.73. Compare this to Ontario (automotive, machinery, pharmaceuticals — HHI around 0.15) and British Columbia (forestry, mining, agricultural, software — HHI around 0.25).

<div data-viz="echarts" data-options='{"title": {"text": "Export Concentration (HHI) by Province", "subtext": "Higher HHI = more concentrated = more vulnerable to sector shocks"}, "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}}, "xAxis": {"type": "category", "data": ["Alberta", "Saskatchewan", "Newfoundland", "BC", "Manitoba", "Quebec", "Ontario"]}, "yAxis": {"type": "value", "name": "HHI (0–1)", "max": 0.85}, "series": [{"name": "Export HHI", "type": "bar", "data": [0.73, 0.52, 0.58, 0.25, 0.28, 0.18, 0.15], "itemStyle": {"color": {"type": "linear", "x": 0, "y": 0, "x2": 0, "y2": 1, "colorStops": [{"offset": 0, "color": "#ee6666"}, {"offset": 1, "color": "#fac858"}]}}, "label": {"show": true, "position": "top", "formatter": "{c}"}}]}'>
</div>

Alberta's HHI of 0.73 is roughly five times Ontario's — reflecting the degree to which the provincial economy is built around a single commodity. Saskatchewan's high HHI (0.52) reflects potash and grain concentration; Newfoundland (0.58) reflects offshore oil and fish.

## Historical Diversification Attempts in Alberta

Alberta has tried to diversify before:

**NovAtel (1980s):** The province invested in cellular telephone manufacturing through a Crown corporation subsidiary. NovAtel became a world leader in cellular handsets — and then haemorrhaged $566 million in bad loans to US dealers before the province sold it at a $611 million loss. A diversification attempt that succeeded technologically and failed commercially.

**MagCan (1980s):** A magnesium smelter in High River — another provincially backed industrial development project — closed after cost overruns and low commodity prices.

**Kananaskis Centre:** Less an economic diversification play than a tourism investment.

The pattern in diversification attempts is consistent with what economic geography research predicts: **relatedness matters**. Diversification is most successful when it builds on existing capabilities — knowledge, supply chains, institutions, labour skills. Alberta's oil sector creates strong relatedness to oil-field services technology, environmental monitoring, industrial automation, and energy transition technologies (carbon capture, hydrogen). It creates weak relatedness to software, finance, life sciences, or consumer electronics.

The academic literature (Hidalgo, Hausmann, Balland) suggests that the optimal diversification path for Alberta is not to leap to unrelated industries but to climb the **capability ladder** within energy — moving from bitumen extraction to energy technology development, from pipeline management to grid management, from reservoir modelling to carbon storage modelling.

## Can the Curse Be Broken?

The resource curse is a tendency, not a fate. Botswana (diamonds), Chile (copper), and Norway (oil) have all managed resource wealth without classic resource curse symptoms. What distinguishes them?

1. **Strong institutions before the boom** — property rights, rule of law, and bureaucratic quality were established before resource revenues created rent-seeking incentives
2. **Fiscal rules** — explicit constraints on spending resource revenues, forcing saving or debt reduction
3. **Exchange rate management** — mechanisms to prevent excessive appreciation (capital controls, sovereign fund offshore investment)
4. **Investment in human capital** — resource revenues directed toward education and R&D that create the capabilities for post-resource diversification

Alberta scored reasonably well on institutions before its oil boom but weakly on fiscal rules and fiscal saving. The Heritage Fund decision — stopping deposits in 1987 — is the pivotal moment when Alberta chose the consumption path over the investment path.

---

**Next in this cluster:** Model 20 — The Integrated Resource System synthesises all four cluster models into a complete systems view of Alberta from wellhead to Heritage Fund, traces three scenarios through 2040, and maps the energy transition overlay onto the Hotelling depletion framework.
