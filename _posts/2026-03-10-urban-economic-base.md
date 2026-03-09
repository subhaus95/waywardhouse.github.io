---
layout: model
title: "The Urban Economic Base"
subtitle: "Export Employment, Multipliers, and What Actually Drives a City's Economy"
series: "Economic Systems"
series_order: 14
cluster: "UE — Urban Economic Systems"
date: 2026-03-10
image: /assets/images/urban-economics.png
categories: [modelling]
tags: [economic-geography, urban-economics, tag-hash-math, tag-hash-viz]
difficulty: 3
math: true
viz: true
math_core:
  - "Economic base multiplier"
  - "Location quotient"
  - "Input-output basics"
excerpt: "When oil prices fell in 2015, Calgary lost roughly 40,000 direct energy-sector jobs. But total employment fell by far more than that — because every energy job supports multiple local service jobs. Economic base theory explains this amplification, derives the multiplier mathematically, and shows why Calgary's multiplier makes it unusually sensitive to commodity price cycles."
---

In late 2015, as the oil price shock worked its way through the Calgary economy, the city's food banks reported a 25% increase in usage. Coffee shops in the Beltline closed. Fitness studios in Eau Claire emptied out. Real estate listings multiplied. None of this was caused directly by oil — most of these businesses had nothing to do with petroleum. They were casualties of the economic base multiplier: the amplification mechanism that turns a contraction in one sector into a citywide recession.

Economic base theory offers a simple but powerful framework for understanding this dynamic. It divides urban employment into two categories: **basic** (or export-oriented) employment that serves markets outside the city, and **non-basic** (or local service) employment that serves the city's own residents. Basic employment is the engine. Non-basic employment is the drivetrain that translates engine output into wheel motion — and amplifies it.

The insight is old. Harold Hoyt formalised it in the 1930s, building on earlier work by Frederick Law Olmsted Jr. But it remains the starting point for any analysis of how urban economies respond to external shocks.

---

## 1. The Core Framework

Divide all employment in a city into basic employment $B$ and non-basic employment $N$. Total employment is:

$$E = B + N$$

The non-basic sector serves the basic sector's workers and their households. Assume that each basic worker generates a constant level of local spending, which in turn supports a fixed amount of non-basic employment. Define $k$ as the proportion of income spent locally on non-basic goods and services. In the simplest version, $N$ is proportional to $B$:

$$N = \frac{k}{1-k} \cdot B$$

Total employment is then:

$$E = B + \frac{k}{1-k} \cdot B = \frac{1}{1-k} \cdot B$$

The **economic base multiplier** is:

$$m = \frac{E}{B} = \frac{1}{1-k}$$

If $k = 0.5$ (half of income is spent locally), $m = 2$: each basic job supports one non-basic job, for a total multiplier of 2. For a typical Canadian CMA, multipliers tend to fall between 2 and 3, with larger and more self-sufficient metropolitan areas having higher multipliers.

---

## 2. The Multiplier Derivation

The multiplier can also be derived as an infinite geometric series. Suppose basic employment increases by $\Delta B$. This generates income for basic workers, who spend a fraction $k$ locally, creating non-basic employment. Those non-basic workers also spend a fraction $k$ locally, creating a second round of employment, and so on.

$$\Delta E = \Delta B + k\Delta B + k^2 \Delta B + k^3 \Delta B + \cdots$$

$$\Delta E = \Delta B \cdot \sum_{n=0}^{\infty} k^n = \Delta B \cdot \frac{1}{1-k}$$

This is the same multiplier $m = 1/(1-k)$. The series converges provided $0 < k < 1$, which is satisfied as long as some fraction of income leaks out of the local economy (into savings, imports, and taxes).

The larger the leakage, the smaller the multiplier. Small cities with limited local economic diversity have high leakage — residents must import many goods and services from outside — producing low multipliers. Large, diversified metros like Toronto have more local spending opportunities and less leakage, producing higher multipliers.

Calgary's multiplier is elevated above what its size alone would predict because the energy sector generates very high average wages, which in turn support disproportionate local spending on housing, professional services, and retail. High average income means each basic worker generates more local spending than the national average.

---

## 3. Identifying the Basic Sector: The Location Quotient Method

The critical empirical challenge is identifying which employment is basic and which is non-basic. The most widely used method is the Location Quotient, introduced in Model 12:

$$LQ_{i,c} = \frac{e_{i,c} / E_c}{e_{i,n} / E_n}$$

If $LQ_{i,c} > 1$, industry $i$ is overrepresented in city $c$ relative to the national average. The excess employment — the amount above the national average share — is presumed to serve export markets and is counted as basic employment:

$$B_{i,c} = \max\left(0,\; e_{i,c} - e_{i,n} \cdot \frac{E_c}{E_n}\right)$$

For industries with $LQ < 1$, all employment is non-basic by assumption (the city imports what it doesn't produce locally). For industries with $LQ > 1$, basic employment equals the excess over what would be expected if the city were simply serving its own population.

Total basic employment is the sum of $B_{i,c}$ across all industries, and the multiplier is $m = E_c / B_c$.

---

## 4. Calgary's Location Quotients

<div data-viz="echarts" data-options='{
  "title": {"text": "Location Quotients: Calgary by Industry", "left": "center", "subtext": "LQ > 1 = export-oriented; LQ < 1 = import-dependent"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "xAxis": {
    "type": "value",
    "name": "Location Quotient",
    "nameLocation": "middle",
    "nameGap": 30,
    "min": 0,
    "max": 6
  },
  "yAxis": {
    "type": "category",
    "data": [
      "Education",
      "Health & Social",
      "Retail Trade",
      "Government",
      "Construction",
      "Transport & Warehousing",
      "Prof. & Scientific Services",
      "Finance & Insurance",
      "Energy, Mining & Oil & Gas"
    ],
    "axisLabel": {"fontSize": 11}
  },
  "series": [
    {
      "name": "LQ",
      "type": "bar",
      "data": [0.72, 0.81, 0.95, 0.68, 1.35, 1.12, 1.48, 1.58, 4.85],
      "itemStyle": {
        "color": {
          "type": "linear",
          "x": 0, "y": 0, "x2": 1, "y2": 0,
          "colorStops": [
            {"offset": 0, "color": "#5c8ee0"},
            {"offset": 1, "color": "#e05c5c"}
          ]
        }
      },
      "label": {"show": true, "position": "right", "formatter": "{c}"}
    }
  ],
  "markLine": {
    "data": [{"xAxis": 1, "lineStyle": {"type": "dashed", "color": "#888"}}]
  }
}'></div>

Energy, Mining and Oil & Gas has an LQ of nearly 5: Calgary's concentration is almost five times the national average, meaning roughly 80% of energy employment serves export markets. Finance and Insurance (LQ ~1.58) and Professional & Scientific Services (LQ ~1.48) are also export-oriented — Calgary's financial sector largely serves the energy industry, and its professional services sector (engineering consultancies, legal firms, environmental assessors) similarly derives much of its revenue from outside the city.

Government, Health, and Education all have LQs below 1, confirming that Calgary under-provides public services relative to its size — reflecting Alberta's historically lean public sector and the fact that Edmonton hosts most provincial government functions.

---

## 5. Edmonton vs Calgary: Complementary Base Structures

<div data-viz="echarts" data-options='{
  "title": {"text": "Basic vs Non-Basic Employment Share: Calgary, Edmonton, Toronto", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "legend": {"data": ["Basic Employment", "Non-Basic Employment"], "bottom": 0},
  "xAxis": {
    "type": "category",
    "data": ["Calgary", "Edmonton", "Toronto"]
  },
  "yAxis": {
    "type": "value",
    "name": "Share of Total Employment (%)",
    "nameLocation": "middle",
    "nameGap": 45,
    "min": 0,
    "max": 100
  },
  "series": [
    {
      "name": "Basic Employment",
      "type": "bar",
      "stack": "total",
      "data": [42, 35, 31],
      "itemStyle": {"color": "#e05c5c"},
      "label": {"show": true, "position": "inside", "formatter": "{c}%"}
    },
    {
      "name": "Non-Basic Employment",
      "type": "bar",
      "stack": "total",
      "data": [58, 65, 69],
      "itemStyle": {"color": "#5c8ee0"},
      "label": {"show": true, "position": "inside", "formatter": "{c}%"}
    }
  ]
}'></div>

Calgary has a higher share of basic employment than Edmonton or Toronto. This is consistent with its narrow export specialisation: energy employment is strongly basic (high LQ), and Calgary's economy is dominated by it. Edmonton's basic share is intermediate — government and education are less export-oriented than energy, pulling down the basic fraction. Toronto has the smallest basic share; its large non-basic sector reflects its role as a service hub for its own dense metropolitan population.

The multiplier calculation follows:

- Calgary: $m = 1/0.58 \approx 1.72$ (basic employment is 42% of total)
- Edmonton: $m = 1/0.65 \approx 1.54$
- Toronto: $m = 1/0.69 \approx 1.45$

These are simplified estimates from the LQ method; more careful input-output analysis tends to produce higher multipliers because it accounts for supply chain linkages not captured by employment ratios alone.

---

## 6. Oil Price Shocks and Multiplier Amplification

The 2015–16 oil price shock illustrates the multiplier in action. Calgary's direct energy employment fell by an estimated 35,000–45,000 jobs. With a multiplier of approximately 1.7–2.0, the implied total employment impact is:

$$\Delta E = m \cdot \Delta B \approx 1.8 \times (-40{,}000) = -72{,}000 \text{ jobs}$$

Calgary's total employment did fall by roughly 60,000–75,000 over the 2015–2017 period, broadly consistent with the multiplier prediction. The non-basic losses — in retail, construction, food services, and professional support — were nearly as large as the direct energy losses. This is precisely what the theory predicts and precisely why the economic pain spread far beyond the oil patch itself.

The asymmetry between Calgary and Edmonton during this period also reflects their base structure. Edmonton's export base is more diversified (government, health, education, and a significant petrochemical manufacturing component). Government employment is also less sensitive to commodity prices. Edmonton's multiplier amplified a smaller initial shock, producing a milder total contraction.

---

## 7. Limitations of Economic Base Theory

Economic base theory is a useful first-order framework but has well-documented limitations.

**The basic/non-basic boundary is fuzzy.** Healthcare is classified as non-basic (LQ below 1 in Calgary), but the University of Alberta Hospital and the University of Calgary generate research revenues and attract patients from across Alberta and beyond. The LQ method treats all healthcare as local service even when some of it is genuinely export-oriented.

**The theory is static.** The multiplier is a comparative-statics result: it describes the new equilibrium after the shock has fully worked through. It does not model the speed of adjustment, the path of employment over time, or the sectoral sequence of adjustment.

**Import substitution is ignored.** The theory assumes that non-basic sectors do not grow independently by replacing imported goods and services. In practice, a growing local economy may develop new industries that substitute for imports, increasing the multiplier over time — the mechanism Jane Jacobs emphasised in *The Economy of Cities*.

**Basic does not always mean export.** Tourism, post-secondary education, healthcare, and retirement services all attract income from outside the local economy without appearing in export trade statistics. The LQ method misses these unless the sector has a nationally high share in the local economy.

Despite these limitations, the economic base multiplier provides the essential link between changes in a city's export sector and the total employment response — and it makes the Calgary-oil price story legible in a way that sector-by-sector accounting does not.

---

Next in this cluster: **The Integrated Urban System** (Model 15) synthesises bid-rent, agglomeration, Zipf's Law, and the economic base into a single causal framework — and applies it to Calgary as a complete worked example of how all four mechanisms interact.
