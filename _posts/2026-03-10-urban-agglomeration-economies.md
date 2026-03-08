---
layout: model
title: "Agglomeration Economies"
subtitle: "Why Firms Cluster and What It Costs When They Don't"
series: "Economic Systems"
series_order: 12
cluster: "UE — Urban Economic Systems"
date: 2026-03-10
categories: [modelling]
tags: [economic-geography, urban-economics, tag-hash-math, tag-hash-viz]
difficulty: 3
math: true
viz: true
math_core:
  - "Production functions"
  - "Wage-density elasticity"
  - "Localisation vs urbanisation"
excerpt: "Cities are not just concentrations of people — they are productivity machines. Workers in large dense cities earn 4–8% more than identical workers in small cities, not because they work harder but because density itself raises productivity. This essay derives why, measures how much, and asks what Calgary's energy-sector concentration implies about resilience."
---

In 2014, when oil prices collapsed from over $100 to under $50 a barrel, Calgary's unemployment rate rose from roughly 4% to 9% within eighteen months. Edmonton's rose too, but more slowly and by less. Montreal and Toronto barely registered the shock. This asymmetry was not an accident of geography or policy — it was a predictable consequence of how differently these cities had organised their economic bases. Calgary had clustered, deeply and deliberately, into a single sector. That clustering had made it extraordinarily productive in good times. The same clustering made it fragile.

To understand why, we need to distinguish two things that both look like clustering but work through entirely different mechanisms. **Localisation economies** are productivity gains that come from being near other firms in the *same* industry. **Urbanisation economies** are productivity gains that come from being in a *large and diverse* city, regardless of industry. Alfred Marshall identified the first in 1890; Jane Jacobs articulated the second in 1969. The distinction matters enormously for economic policy — and for interpreting what happened to Calgary.

---

## 1. Marshall's Three Sources of Localisation

Marshall observed that firms in the same industry benefit from co-locating through three distinct channels:

**Labour market pooling.** When many firms in the same industry cluster together, they create a thick local labour market. Workers can move between firms easily; firms can hire quickly when they grow and shed workers who find alternative employment nearby when they contract. Both parties benefit from lower search costs and better matches. The result is higher average productivity — better worker-firm fit — and lower wage variance.

**Input sharing.** Specialised suppliers locate near their customers. A cluster of oil and gas firms in Calgary supports a dense ecosystem of engineering consultants, equipment suppliers, software vendors, and financial services that would not be viable in a smaller market. Each individual firm benefits from access to these specialised inputs at lower cost and shorter lead times. The suppliers also achieve scale economies they could not reach serving a dispersed market.

**Knowledge spillovers.** Workers who share a local labour market also share knowledge. They talk at conferences, move between firms, and observe each other's practices. Ideas spread through informal contact. This is why Silicon Valley retains its technology advantage: the density of engineering talent means that knowledge generated anywhere in the cluster diffuses rapidly, reducing duplication and accelerating innovation. Patent citation data confirms that knowledge spillovers decay sharply with distance — an invention in one part of a city is far more likely to be cited by a nearby inventor than by one in another city.

---

## 2. Jacobs and Urbanisation Economies

Jane Jacobs argued that the most important driver of urban productivity was not industry-level clustering but city-level diversity. In her account, new ideas emerge from the *recombination* of knowledge across different industries. A city where engineers, artists, biologists, and financiers interact produces innovations that no single-industry cluster can. New York's fashion industry benefits from proximity to advertising, media, and finance. London's finance sector benefits from proximity to law, technology, and design.

Urbanisation economies increase with total city size and economic diversity. They predict that the largest and most diverse cities — Toronto, Montreal, Vancouver — will be more productive and more innovative, even after controlling for industry composition. Localisation economies, by contrast, predict that specialised cities will outperform diversified ones *within* their sector.

The empirical challenge is separating the two. Both predict a positive relationship between density and productivity, but they have different policy implications. If localisation dominates, specialised clusters are the right strategy. If urbanisation dominates, diversified growth is more valuable.

---

## 3. The Wage-Density Relationship

The cleanest empirical test of agglomeration economies is the wage-density elasticity. The idea is straightforward: if agglomeration raises productivity, wages should be higher in denser places, even after controlling for worker characteristics. The relationship is typically estimated as:

$$\ln(w_i) = \alpha + \beta \ln(\text{density}_j) + \mathbf{X}_i \gamma + \varepsilon_i$$

where $w_i$ is the wage of worker $i$, $\text{density}_j$ is the employment density of the city or zone where they work, $\mathbf{X}_i$ is a vector of individual controls (education, experience, occupation), and $\beta$ is the **wage-density elasticity** — the percentage increase in wages associated with a doubling of density.

Across dozens of studies of North American and European cities, $\hat{\beta}$ typically falls in the range $0.04$ to $0.08$. That is: doubling employment density is associated with a 4–8% wage premium. At first glance this seems modest. But consider the difference in density between a small city of 100,000 and a metropolitan area of 5,000,000. A ten-fold difference in density implies a wage premium of $\beta \cdot \ln(10) \approx 0.06 \cdot 2.3 \approx 14\%$ — before controlling for industry composition or worker selection.

The challenge for causal identification is that high-ability workers sort into dense cities. The wage premium in Toronto relative to Lethbridge partly reflects the skill of the people who chose to move there, not only the productivity boost from density itself. Identifying the pure agglomeration effect requires instruments for density — historical population levels, geographic constraints, or the density of railroads in 1900 — or longitudinal data tracking the same workers as they move between cities.

---

## 4. Location Quotient: Measuring Specialisation

To measure whether a city is specialised in a given industry — and therefore likely to benefit from localisation economies — economists use the **Location Quotient** (LQ):

$$LQ_{i,c} = \frac{e_{i,c} / E_c}{e_{i,n} / E_n}$$

where $e_{i,c}$ is employment in industry $i$ in city $c$, $E_c$ is total employment in city $c$, $e_{i,n}$ is national employment in industry $i$, and $E_n$ is total national employment.

An $LQ > 1$ means the city is more specialised in industry $i$ than the national average — the city has a relative concentration that suggests export orientation. An $LQ < 1$ means the city is underrepresented in that industry relative to the national norm.

Calgary's LQ in mining, oil and gas extraction exceeds 8 — meaning the city is more than eight times as specialised in energy as the national average. This extreme specialisation drives both its exceptional productivity during oil booms and its exceptional fragility during busts.

---

## 5. The Net-Benefit Curve: Agglomeration vs Congestion

Agglomeration generates benefits, but density also generates costs: congestion on roads and transit, higher housing prices, higher wages for non-tradable services (restaurants, retail), and pollution. The net agglomeration benefit is the difference between productivity gains and these congestion costs.

Formally, if $A(N)$ is the agglomeration benefit and $C(N)$ is the congestion cost, both functions of city size $N$, the net benefit is:

$$NB(N) = A(N) - C(N)$$

Empirically, $A(N)$ is concave — diminishing marginal returns to scale. $C(N)$ is convex — congestion costs accelerate as the city grows. The optimal city size $N^*$ satisfies:

$$A'(N^*) = C'(N^*)$$

Most estimates place North American cities well below $N^*$, implying that further densification would raise net welfare. The persistent undersupply of housing in Toronto and Vancouver — enforced by zoning — keeps density below the social optimum and suppresses agglomeration gains.

---

## 6. Calgary vs Toronto: Specialised vs Diversified Agglomeration

<div data-viz="echarts" data-options='{
  "title": {"text": "City-Size vs Wage Premium: Canadian CMAs", "left": "center", "subtext": "Stylised — log scale on x-axis"},
  "tooltip": {"trigger": "item", "formatter": "{b}: {c}% premium"},
  "xAxis": {
    "type": "log",
    "name": "CMA Employment (thousands, log scale)",
    "nameLocation": "middle",
    "nameGap": 35,
    "min": 50,
    "max": 4000
  },
  "yAxis": {
    "type": "value",
    "name": "Estimated Wage Premium vs National Median (%)",
    "nameLocation": "middle",
    "nameGap": 50,
    "min": -5,
    "max": 30
  },
  "series": [
    {
      "type": "scatter",
      "symbolSize": 12,
      "data": [
        {"name": "Toronto", "value": [3200, 26]},
        {"name": "Vancouver", "value": [1400, 18]},
        {"name": "Montreal", "value": [2100, 12]},
        {"name": "Calgary", "value": [830, 22]},
        {"name": "Edmonton", "value": [620, 14]},
        {"name": "Ottawa", "value": [730, 16]},
        {"name": "Winnipeg", "value": [420, 4]},
        {"name": "Quebec City", "value": [350, 2]},
        {"name": "Hamilton", "value": [280, 1]},
        {"name": "Saskatoon", "value": [160, -1]},
        {"name": "Regina", "value": [130, -2]},
        {"name": "Halifax", "value": [220, 0]},
        {"name": "Kelowna", "value": [100, -3]},
        {"name": "Lethbridge", "value": [60, -4]}
      ],
      "label": {"show": true, "formatter": "{b}", "position": "right", "fontSize": 11},
      "itemStyle": {"color": "#5c8ee0"}
    }
  ]
}'></div>

Calgary sits above the trend line: its wage premium exceeds what its size alone would predict. This is the signature of localisation economies — sector-specific productivity gains from energy cluster density that push wages above the urbanisation-only benchmark. Toronto's premium reflects diversified urbanisation: a mix of finance, technology, professional services, and creative industries that generates broad-based productivity gains.

<div data-viz="echarts" data-options='{
  "title": {"text": "Location Quotient by Industry: Calgary vs Toronto vs Vancouver", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "legend": {"data": ["Calgary", "Toronto", "Vancouver"], "bottom": 0},
  "xAxis": {
    "type": "category",
    "data": ["Energy & Mining", "Finance & Insurance", "Technology", "Government", "Health & Social", "Retail", "Construction"],
    "axisLabel": {"rotate": 25, "fontSize": 11}
  },
  "yAxis": {
    "type": "value",
    "name": "Location Quotient",
    "nameLocation": "middle",
    "nameGap": 45,
    "min": 0,
    "max": 5
  },
  "series": [
    {
      "name": "Calgary",
      "type": "bar",
      "data": [4.8, 1.6, 1.0, 0.7, 0.8, 0.9, 1.4],
      "itemStyle": {"color": "#e05c5c"}
    },
    {
      "name": "Toronto",
      "type": "bar",
      "data": [0.2, 2.8, 1.9, 0.9, 1.1, 1.0, 0.8],
      "itemStyle": {"color": "#5c8ee0"}
    },
    {
      "name": "Vancouver",
      "type": "bar",
      "data": [0.3, 1.1, 1.7, 1.0, 1.2, 1.1, 1.2],
      "itemStyle": {"color": "#6dba6d"}
    }
  ]
}'></div>

Calgary's energy LQ of ~4.8 dwarfs any other specialisation in any of the three cities. Toronto's finance LQ of ~2.8 reflects a significant cluster but one embedded in a far more diversified economy. Vancouver is the most balanced of the three — moderate LQs across technology, finance, and construction, consistent with Jacobs-style urbanisation rather than Marshall-style localisation.

---

## 7. Resilience Implications

The contrast matters for how each city responds to shocks. When Calgary's energy sector contracts — as it did in 2015–16 and again in 2020 — the localisation economies that boosted productivity in good times become channels of contagion. Energy firms shed workers; the specialised suppliers who depend on them lose revenue; the thick local labour market becomes a pool of structurally unemployed engineers and geoscientists whose skills are not easily transferred to other sectors.

Toronto's 2008–09 recession hit the financial sector hard, but the city's diversification meant that technology, healthcare, and government employment provided a partial offset. The diversified agglomeration model is more resilient, at the cost of somewhat lower sector-specific productivity peaks.

Alberta's provincial government has grappled explicitly with this tradeoff. The diversification agenda — attracting technology companies, expanding the post-secondary sector, developing renewable energy — is an attempt to shift Calgary's LQ profile toward something more like Vancouver's. The challenge is that localisation economies are self-reinforcing: the energy cluster is productive precisely because it is concentrated, and dismantling that concentration reduces the very advantages that made it attractive.

---

## 8. Limits of the Framework

The wage-density elasticity captures average productivity effects. It misses the distribution: agglomeration benefits accrue unevenly across workers. High-skill workers capture the majority of the productivity premium; low-skill workers in service industries may see little wage gain from density while bearing high housing costs. The net welfare effect of agglomeration for a low-income worker in Vancouver or Toronto may be negative despite the city-wide productivity gains.

The framework also treats agglomeration as a smooth, continuous effect of density. In practice, agglomeration effects are lumpy and path-dependent. A city that fails to achieve the critical mass needed to attract a specialised supplier ecosystem may be stuck in a low-productivity equilibrium despite its geographic and demographic potential.

---

Next in this cluster: **Zipf's Law and the City Size Distribution** (Model 13) steps back from individual cities to ask: why do national city systems organise into a predictable rank-size hierarchy, and where does Canada — with its near-equal Edmonton-Calgary pair — fit that pattern?
