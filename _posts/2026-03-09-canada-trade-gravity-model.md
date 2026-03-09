---
layout: model
title: "The Gravity Model of Trade"
subtitle: "Distance, Mass, and the Economic Geography of Canada's Bilateral Trade"
series: "Economic Systems"
series_order: 6
cluster: "TR — Trade and Transport"
date: 2026-03-09
image: /assets/images/trade-corridors.png
categories: [modelling]
tags:
  - trade
  - gravity-model
  - canada
  - alberta
  - border-effect
  - distance-decay
  - ols-regression
  - economic-geography
difficulty: 3
math: true
viz: true
math_core: ["Gravity equation", "log-linear OLS regression", "distance decay", "border effect"]
description: >
  A quantitative account of the gravity model of trade — how economic mass and
  geographic distance together predict bilateral trade volumes — applied to
  Canada's relationship with the United States, with attention to provincial
  variation and Alberta's specific position in the framework.
excerpt: >
  The Canada-US bilateral trade relationship is the largest in the world, worth
  roughly CAD&#36;1.4 trillion in goods in 2023. But that aggregate number conceals
  enormous provincial variation. Ontario trades nearly twice what Alberta does.
  The gravity model of international trade — one of the most empirically robust
  relationships in all of economics — explains why, and quantifies the role of
  distance, economic mass, and borders in shaping who trades with whom.
toc: true
---

## 1. The Question

Why does Canada trade so much with the United States and so much less with
equally large economies elsewhere? Why does Ontario account for the largest
share of Canada-US trade when Alberta produces more resource wealth per capita?
And why, even after three decades of liberalised trade under first the Canada-US
Free Trade Agreement and then NAFTA and CUSMA, do provinces still trade many
times more with each other than with equivalent US states?

These are not rhetorical questions. They have quantitative answers, derived from
one of the most durable empirical regularities in economics: the gravity model
of trade. The model is named for its structural resemblance to Newton's law of
universal gravitation. Just as the gravitational force between two objects
increases with their masses and decreases with the square of the distance between
them, trade between two economies increases with their sizes and decreases with
the distance between them. The mathematics is simple. The empirical performance
is remarkable. And the residuals — the deviations from the model's predictions —
are among the most informative quantities in economic geography.

This essay derives the gravity equation, fits it to Canada-US provincial trade
data, and examines three specific puzzles: the magnitude of the border effect,
Alberta's position in the gravity framework, and what the 2025 US tariff regime
implies for bilateral flows when viewed through a model that has been calibrated
over decades.

---

## 2. The Gravity Equation

### The basic model

The gravity model of bilateral trade in its simplest form states that trade
between two countries (or regions) $i$ and $j$ is proportional to the product
of their economic masses and inversely proportional to the distance between them:

$$T_{ij} = G \cdot \frac{M_i^\alpha \cdot M_j^\beta}{d_{ij}^\gamma}$$

where $T_{ij}$ is the value of bilateral trade, $M_i$ and $M_j$ are the economic
masses of the trading partners (typically measured by GDP), $d_{ij}$ is the
distance between them, and $G$ is a constant capturing all other factors held
fixed. The exponents $\alpha$, $\beta$, and $\gamma$ are estimated from data.

The model looks like physics, and it borrows physics' notation deliberately —
but it was not derived from first principles. It emerged empirically. Jan
Tinbergen proposed it in 1962 as a description of observed trade patterns, and
it has been repeatedly validated across datasets, time periods, and levels of
geographic aggregation since. The typical finding is $\alpha \approx \beta
\approx 0.9$ (slightly less than proportional to GDP) and $\gamma \approx 1.1$
(distance reduces trade somewhat more than proportionally). More recent studies
using modern gravity frameworks and structural estimation tend to find slightly
higher distance elasticities, in the range of 1.0 to 1.5, depending on the
commodity composition and time period.

### Log-linearisation and OLS estimation

The multiplicative form of the gravity equation can be transformed into an
additive (linear) form by taking natural logarithms of both sides:

$$\ln T_{ij} = \ln G + \alpha \ln M_i + \beta \ln M_j - \gamma \ln d_{ij} + \varepsilon_{ij}$$

This is now a standard ordinary least squares (OLS) regression equation. The
dependent variable is the log of bilateral trade; the explanatory variables are
the logs of the economic masses and the log of distance. The error term
$\varepsilon_{ij}$ captures all variation not explained by mass and distance.

The log-linear form has a useful interpretation. Each coefficient is an
elasticity: $\alpha$ is the percentage increase in trade associated with a
1% increase in exporter GDP; $\gamma$ is the percentage decrease in trade
associated with a 1% increase in distance. The regression can be estimated with
standard software on any dataset that provides bilateral trade values, partner
GDPs, and inter-partner distances.

### Augmented gravity: the border dummy

The basic model can be augmented with additional variables. The most important
augmentation for the Canada-US case is a border dummy variable $B_{ij}$, which
equals 1 if $i$ and $j$ are in the same country and 0 if they are in different
countries:

$$\ln T_{ij} = \ln G + \alpha \ln M_i + \beta \ln M_j - \gamma \ln d_{ij} + \delta B_{ij} + \varepsilon_{ij}$$

The coefficient $\delta$ on the border dummy captures the border effect: the
additional reduction in trade caused by crossing an international border, above
and beyond what distance alone would predict. When $\delta > 0$, same-country
pairs trade more than the gravity model would predict from mass and distance
alone. The border effect is typically expressed as a multiplier: $e^\delta$,
the factor by which within-country trade exceeds what the model would predict
for equivalent international pairs.

---

## 3. Canada-US Trade: The Provincial Picture

Canada and the United States together account for the world's largest bilateral
trade relationship by value. In 2023, Canadian goods exports to the United States
reached approximately CAD&#36;630 billion, with imports of roughly CAD&#36;470 billion
in goods returning northward, for a two-way goods trade total approaching
CAD&#36;1.4 trillion. This is larger than any other bilateral goods trade pair in
the world, exceeding even US-China and US-Mexico relationships when measured
in value terms.

But the provincial distribution of this trade is anything but uniform, and the
unevenness is precisely what the gravity model predicts and explains. Ontario,
with the largest provincial GDP and the shortest distance to the US manufacturing
heartland, accounts for by far the largest share of Canada-US goods trade.
Alberta, with the second-largest GDP but much greater distance from major US
consumer and manufacturing markets, accounts for substantially less — and even
that understates the divergence, because Alberta's largest export to the US,
crude oil, moves predominantly via pipeline and is classified separately from
goods trade in standard trade statistics.

The chart below shows estimated Canada-US goods trade by province for 2023,
based on provincial trade statistics and federal trade data disaggregated by
origin. These are goods-trade figures; they exclude pipeline crude oil and natural
gas from Alberta, which are accounted for in energy trade statistics under
different commodity classifications.

<div data-viz="echarts" style="height:380px" data-options='{
  "title": {"text": "Canada-US Goods Trade by Province (2023)", "subtext": "Estimated two-way goods trade, CAD$ billions. Excludes pipeline crude and natural gas.", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "grid": {"left": "4%", "right": "8%", "bottom": "5%", "containLabel": true},
  "xAxis": {"type": "value", "name": "CAD$ billions"},
  "yAxis": {"type": "category", "data": ["PEI","NL","NS","MB","NB","SK","BC","QC","AB","ON"], "axisLabel": {"fontSize": 12}},
  "series": [{
    "type": "bar",
    "label": {"show": true, "position": "right", "formatter": "{c}B"},
    "data": [
      {"value": 3,   "itemStyle": {"color": "#bfdbfe"}},
      {"value": 12,  "itemStyle": {"color": "#93c5fd"}},
      {"value": 15,  "itemStyle": {"color": "#7dd3fc"}},
      {"value": 28,  "itemStyle": {"color": "#60a5fa"}},
      {"value": 18,  "itemStyle": {"color": "#4db8ff"}},
      {"value": 45,  "itemStyle": {"color": "#3b82f6"}},
      {"value": 90,  "itemStyle": {"color": "#2563eb"}},
      {"value": 120, "itemStyle": {"color": "#1d4ed8"}},
      {"value": 175, "itemStyle": {"color": "#1e40af"}},
      {"value": 310, "itemStyle": {"color": "#1e3a8a"}}
    ]
  }]
}'></div>

*Ontario's dominance reflects both GDP size and geographic proximity to Detroit, Buffalo, and the US manufacturing corridor. Alberta's figure of CAD&#36;175B substantially understates total US-bound flows — crude oil pipeline exports add another CAD&#36;130B+ that does not appear in goods-trade statistics.*

---

## 4. The Border Effect

The most famous finding in the empirical gravity literature on Canada-US trade
is John McCallum's 1995 result, published in the American Economic Review under
the title "National Borders Matter." McCallum used data from 1988 — the year the
Canada-US Free Trade Agreement came into force — and found that Canadian provinces
traded, on average, 22 times more with each other than with equivalent US states
at the same distance and with comparable economic sizes.

This is the border effect. Twenty-two-fold. At a time when Canada and the United
States had already agreed to eliminate tariffs, when the two economies shared
language (mostly), legal traditions, currency convertibility, and cultural
familiarity. The border still reduced trade by a factor of twenty-two, relative
to equivalent within-country flows.

The border effect operates through multiple channels. Different regulatory
regimes mean that products certified for one market must be recertified for
the other. Different legal systems create transaction costs in contract
enforcement. Currency risk, even when managed, imposes hedging costs. Customs
procedures impose delays and documentation costs even when duties are zero.
Supply chains, marketing networks, and distribution systems have historically
developed separately on each side. Trust, familiarity, and business relationships
take time to build across borders. Each of these is a modest friction. In
aggregate they are substantial.

Since McCallum's 1995 finding, subsequent research has tracked a gradual decline
in the border effect. The full implementation of NAFTA, deeper business
integration, the explosion of internet-facilitated trade relationships, and
continued regulatory harmonisation reduced the measured border effect from
roughly 22x in 1995 to approximately 8-10x by the early 2020s. This is still
a large number — the border still matters enormously, even in one of the world's
most integrated bilateral relationships — but the trajectory was downward.

The 2025 imposition of broad US tariffs on Canadian goods represents the first
major policy-induced reversal of this trend in three decades. Tariffs raise the
cost of international trade directly, reduce the competitiveness of border-crossing
relative to domestic alternatives, and disrupt the just-in-time supply chains
that have been built on the assumption of frictionless crossing. The estimated
border effect multiplier is expected to rise — the chart below shows the
historical trajectory and projects the 2025 reversal.

<div data-viz="echarts" style="height:320px" data-options='{
  "title": {"text": "Canada-US Border Effect Multiplier Over Time", "subtext": "How many times more provinces trade with each other vs equivalent US states at same distance", "left": "center"},
  "tooltip": {"trigger": "axis"},
  "grid": {"left": "3%", "right": "4%", "bottom": "10%", "containLabel": true},
  "xAxis": {"type": "category", "data": ["1988\npre-FTA", "1995\nMcCallum", "2001", "2008", "2014", "2020", "2023", "2025\ntariffs"]},
  "yAxis": {"type": "value", "name": "Border effect multiplier", "min": 0},
  "series": [{
    "name": "Border effect multiplier",
    "type": "line",
    "smooth": true,
    "symbol": "circle",
    "symbolSize": 8,
    "itemStyle": {"color": "#1e40af"},
    "areaStyle": {"opacity": 0.15, "color": "#1e40af"},
    "data": [30, 22, 18, 14, 11, 9, 8, 12],
    "markLine": {
      "symbol": "none",
      "lineStyle": {"color": "#16a34a", "type": "dashed", "width": 2},
      "label": {"formatter": "Frictionless border = 1", "position": "insideEndTop"},
      "data": [{"yAxis": 1}]
    },
    "markPoint": {
      "data": [
        {"name": "McCallum (1995)", "coord": ["1995\nMcCallum", 22]},
        {"name": "2025 reversal", "coord": ["2025\ntariffs", 12]}
      ],
      "itemStyle": {"color": "#dc2626"},
      "label": {"formatter": "{b}"}
    }
  }]
}'></div>

*The 2025 tariff spike reverses three decades of integration. A multiplier of 12 means that, controlling for economic size and distance, provinces still trade twelve times more with each other than with equivalent US states. The green dashed line at y=1 represents a theoretically frictionless border — a level no real border in the world has ever achieved.*

---

## 5. Alberta in the Gravity Framework

When we apply the gravity model to Canadian provincial trade data and plot each
province's actual US trade against the model's prediction (derived from GDP and
distance), Alberta appears as a notable underperformer. Its actual goods-trade
volume with the United States is substantially below what the gravity model would
predict given Alberta's GDP and distance to US markets.

This apparent anomaly has several explanations, each of which illuminates a
different aspect of the gravity model's assumptions.

First and most importantly, the standard goods-trade statistics exclude pipeline
flows. Alberta's crude oil exports to the United States — roughly CAD&#36;130 billion
per year — move via pipeline and are classified as energy trade rather than goods
trade. Natural gas pipeline exports add another CAD&#36;25 billion or so. When these
are included, Alberta's total economic exchange with the United States is
substantially larger and aligns much more closely with gravity model predictions.
The apparent underperformance is largely a statistical artefact of commodity
classification conventions.

Second, distance still matters even controlling for this. Alberta's major
population and economic centres — Edmonton and Calgary — are approximately
2,000 to 4,000 kilometres from the US manufacturing heartland in Detroit,
Chicago, and the US Northeast. Ontario's major centres are 400 to 800 kilometres
from those same markets. The gravity model predicts that this distance difference
alone produces a substantial trade volume difference even at identical GDPs.

Third, Alberta's export structure is concentrated in commodities — energy,
agriculture, potash, lumber — that move through specific commodity trade
channels rather than through the generalised goods-trade statistics that the
gravity model was originally calibrated on. The gravity model performs best
when trade is diversified across many commodity classes. For highly specialised
commodity exporters, the model captures less of the variation.

<div data-viz="echarts" style="height:360px" data-options='{
  "title": {"text": "Provincial GDP vs US Goods Trade — Gravity Scatter", "subtext": "Log-log axes. Red dashed line = gravity model prediction. Points below the line underperform gravity prediction.", "left": "center"},
  "tooltip": {"trigger": "item", "formatter": "{b}: GDP ${c[0]}B, US trade ${c[1]}B"},
  "grid": {"left": "5%", "right": "5%", "bottom": "10%", "containLabel": true},
  "xAxis": {"type": "log", "name": "Provincial GDP (CAD$B)", "nameLocation": "middle", "nameGap": 30, "min": 30, "max": 1100},
  "yAxis": {"type": "log", "name": "US Goods Trade (CAD$B)", "nameLocation": "middle", "nameGap": 40, "min": 2, "max": 400},
  "series": [
    {
      "name": "Gravity prediction",
      "type": "line",
      "smooth": false,
      "symbol": "none",
      "lineStyle": {"color": "#dc2626", "type": "dashed", "width": 2},
      "data": [[30,3],[90,10],[960,310]],
      "label": {"show": false}
    },
    {
      "name": "Province",
      "type": "scatter",
      "symbolSize": 14,
      "itemStyle": {"color": "#1e40af", "opacity": 0.85},
      "label": {"show": true, "position": "right", "formatter": "{@[2]}"},
      "data": [
        [960, 310, "ON"],
        [450, 175, "AB"],
        [520, 120, "QC"],
        [400, 90,  "BC"],
        [100, 45,  "SK"],
        [90,  28,  "MB"],
        [55,  18,  "NB"],
        [50,  15,  "NS"],
        [40,  12,  "NL"],
        [38,  3,   "PEI"]
      ]
    }
  ]
}'></div>

*Alberta (AB) falls below the gravity prediction line, but this reflects the exclusion of pipeline crude oil and gas from goods-trade statistics. Quebec (QC) also underperforms somewhat, reflecting its export structure and distance effects. Saskatchewan (SK) overperforms relative to its GDP due to high-value agricultural and potash exports to specific US destinations.*

---

## 6. The Alberta Pipeline Correction

The donut chart below shows the composition of Alberta's total economic flows
to the United States, disaggregated by export channel. The majority, by value,
moves through pipeline systems that do not appear in standard goods-trade
statistics. This has direct implications for how Alberta appears in gravity
model analyses: the province is not an underperformer by economic geography —
it is an economy whose primary export mode is systematically excluded from the
datasets on which gravity models are typically calibrated.

<div data-viz="echarts" style="height:340px" data-options='{
  "title": {"text": "Alberta Exports to US by Channel (CAD$B/yr, estimated)", "subtext": "Pipeline categories are excluded from standard goods-trade statistics — explaining Alberta gravity model underperformance", "left": "center"},
  "tooltip": {"trigger": "item", "formatter": "{b}: CAD${c}B ({d}%)"},
  "legend": {"orient": "vertical", "right": 10, "top": "center"},
  "series": [{
    "type": "pie",
    "radius": ["42%", "68%"],
    "center": ["38%", "55%"],
    "label": {"formatter": "{d}%"},
    "data": [
      {"value": 130, "name": "Crude oil — pipeline",           "itemStyle": {"color": "#1e3a8a"}},
      {"value": 25,  "name": "Natural gas — pipeline",         "itemStyle": {"color": "#2563eb"}},
      {"value": 20,  "name": "Agricultural products",          "itemStyle": {"color": "#16a34a"}},
      {"value": 15,  "name": "Petrochemicals and NGL",         "itemStyle": {"color": "#f59e0b"}},
      {"value": 10,  "name": "Other goods",                    "itemStyle": {"color": "#6b7280"}}
    ]
  }]
}'></div>

*Pipeline exports (crude oil + natural gas) account for roughly 77% of Alberta's total exports to the United States by value. These flows move through entirely separate trade statistics and infrastructure channels, and are invisible to gravity model analyses based on goods-trade data alone.*

Understanding this disaggregation is essential for interpreting any gravity model
result involving Alberta. The province is not trading less with the United States
than its economic size would predict; it is trading differently — through
commodity pipelines rather than trucks and railways crossing border crossings
that appear in trade statistics. The gravity model's prediction is approximately
correct when all trade channels are included; the apparent anomaly disappears
when the commodity classification conventions are understood.

This distinction also matters for the 2025 tariff analysis. Pipeline crude oil
and natural gas do not face the same tariff regime as goods crossing land borders.
The US administration's 2025 tariff orders specifically targeted goods trade at
border crossings; energy imports via pipeline were initially treated separately
under a different tariff schedule. Alberta's apparent exposure to the 2025 tariffs
is therefore substantially lower than Ontario's or Quebec's when measured as
a fraction of total US-bound economic flows — though the economic linkages are
complex enough that indirect effects through energy pricing and supply chain
disruption affect all provinces.

---

## 7. What the Model Tells Us

The gravity model of trade is not a causal model. It does not explain why
distance reduces trade or why GDP increases it; it describes that these
relationships hold empirically with remarkable stability across a wide range
of contexts. Its value is precisely in this stability: when an observation
deviates significantly from the gravity prediction, something interesting is
happening that warrants investigation.

For Canada, the border effect is the most important deviation. For Alberta,
the pipeline classification gap is the most important. For the 2025 tariff
episode, the gravity model provides a baseline: we can estimate, from the
observed relationship between trade barriers and trade volumes, roughly how much
a given increase in bilateral trade costs should reduce trade flows. The
coefficient $\gamma$ on distance, which proxies for all trade costs that scale
with the friction of crossing space, suggests that a 25% tariff imposed as an
ad valorem cost on goods trade is equivalent to a substantial increase in
effective distance — enough to predict a measurable reduction in the
Canada-US border effect's denominator and an increase in the overall multiplier.

The gravity model was built on peacetime data from decades of gradual trade
liberalisation. It has never been calibrated on a data point as sharp as a
25% tariff imposed suddenly on the world's largest bilateral trading relationship.
What it can tell us, with some confidence, is that the direction of the effect
is unambiguous: tariffs reduce trade, the reduction is approximately proportional
to the tariff level, and the adjustment works through both volume reductions and
price changes. The precise magnitude remains to be seen in the data when 2025
and 2026 provincial trade statistics become available.

---

*Next in this cluster: [T2 — Canadian Trade Corridors](/canada-trade-corridors/)*

---

## References

Anderson, James E., and Eric van Wincoop. 2003. "Gravity with Gravitas: A Solution to the Border Puzzle." *American Economic Review* 93 (1): 170–192. <https://doi.org/10.1257/000282803321455214>

Global Affairs Canada. 2023. *Canada's State of Trade 2023: Inclusive Trade*. Ottawa: Government of Canada. <https://www.international.gc.ca/transparency-transparence/state-trade-commerce-international/2023.aspx?lang=eng>

McCallum, John. 1995. "National Borders Matter: Canada-U.S. Regional Trade Patterns." *American Economic Review* 85 (3): 615–623. <https://ideas.repec.org/a/aea/aecrev/v85y1995i3p615-23.html>

Statistics Canada. 2024. "Canadian International Merchandise Trade: Annual Review 2023." *The Daily*, May 9, 2024. Ottawa: Statistics Canada. <https://www150.statcan.gc.ca/n1/daily-quotidien/240509/dq240509a-eng.htm>

Statistics Canada. 2024. *Canadian International Merchandise Trade by Province and Country, and by Product Sections, Customs-Based, Annual*. Table 12-10-0173-01. Ottawa: Statistics Canada. <https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1210017301>

Statistics Canada. 2024. *Focus on Canada and the United States: Trade*. Ottawa: Statistics Canada. <https://www.statcan.gc.ca/en/topics-start/canada-united-states/trade>

Tinbergen, Jan. 1962. "An Analysis of World Trade Flows." In *Shaping the World Economy: Suggestions for an International Economic Policy*, edited by Jan Tinbergen, 262–293. New York: Twentieth Century Fund. (No public URL available.)
