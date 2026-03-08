---
layout: model
title: "Zipf's Law and the City Size Distribution"
subtitle: "Why the Largest City Is Twice the Second-Largest — and the Mathematics Behind It"
series: "Economic Systems"
series_order: 13
cluster: "UE — Urban Economic Systems"
date: 2026-03-10
categories: [modelling]
tags: [economic-geography, urban-economics, tag-hash-math, tag-hash-viz]
difficulty: 3
math: true
viz: true
math_core:
  - "Power laws"
  - "Rank-size rule"
  - "Log-log regression"
  - "Gibrat's Law"
excerpt: "In almost every country, if you rank cities by population and plot rank against size on a log-log scale, you get a straight line. This is Zipf's Law — one of the most robust regularities in all of social science. This essay derives it from first principles, fits it to Canadian data, and asks why Alberta's Edmonton-Calgary pair makes Canada an unusual case."
---

Open a table of world city populations and sort it by rank. Take any country with more than twenty substantial cities. Plot rank on the horizontal axis and population on the vertical axis, both on logarithmic scales. In almost every case, the points fall along a straight line with a slope of approximately $-1$. The second city has half the population of the first. The tenth has a tenth. The hundredth has a hundredth.

This is Zipf's Law, named after the linguist George Kingsley Zipf who observed it in word frequency distributions in 1949. It had already been noticed in city sizes by Auerbach in 1913 and was formalised as the "rank-size rule" by Zipf himself. The regularity is remarkable not because it holds perfectly — it does not — but because it holds approximately across countries with wildly different histories, geographies, political systems, and levels of development. Something deep in the process of city growth must be producing this pattern.

---

## 1. Zipf's Law: The Basic Statement

Let cities be ranked 1, 2, 3, ... by population in descending order. Let $P_r$ denote the population of the city at rank $r$ and $P_1$ the population of the largest city. Zipf's Law states:

$$P_r = \frac{P_1}{r}$$

Or in power-law form, for the generalised rank-size rule:

$$P_r = A \cdot r^{-\alpha}$$

where $A$ is a scaling constant and $\alpha$ is the **Pareto exponent**. Zipf's Law is the special case $\alpha = 1$.

Taking logs of both sides:

$$\ln P_r = \ln A - \alpha \ln r$$

This is a linear equation in $(\ln r, \ln P_r)$ space with slope $-\alpha$. Estimating $\alpha$ is therefore a matter of ordinary least squares regression on log-transformed data. If the estimated slope is close to $-1$, the city system follows Zipf's Law.

---

## 2. Derivation: Gibrat's Law Implies Zipf

Why would cities follow a power law? The most elegant answer comes from **Gibrat's Law of Proportionate Effect**, proposed by Robert Gibrat in 1931.

Gibrat's Law states that the growth rate of a city in any period is independent of its current size:

$$\frac{\Delta P_t}{P_t} = \varepsilon_t$$

where $\varepsilon_t$ is a random shock drawn independently of $P_t$. This is a multiplicative random walk: each period, the city's population is multiplied by $(1 + \varepsilon_t)$.

Taking logs: $\ln P_t = \ln P_0 + \sum_{s=1}^{t} \ln(1 + \varepsilon_s) \approx \ln P_0 + \sum_{s=1}^{t} \varepsilon_s$

By the central limit theorem, the sum of independent random variables converges to a normal distribution. So $\ln P_t$ is approximately normally distributed — meaning city population follows a **log-normal** distribution. This is close to a power law for the upper tail, and in the limit (as the variance of shocks accumulates over long time periods), the upper tail of the log-normal converges to a Pareto distribution with $\alpha \approx 1$.

More formally: if city growth follows a multiplicative random walk with a reflecting lower boundary (cities do not shrink below some minimum viable size), the stationary distribution is exactly Pareto, and the rank-size rule holds with $\alpha = 1$.

This provides the theoretical foundation. Cities grow randomly, but the statistical regularity that emerges — Zipf's Law — is a consequence of the central limit theorem applied to multiplicative processes, not of any intentional design.

---

## 3. Log-Log Regression

To test whether a city system follows Zipf's Law, we estimate:

$$\ln P_r = \beta_0 + \beta_1 \ln r + u_r$$

Under Zipf's Law, $\hat{\beta}_1 \approx -1$. A coefficient more negative than $-1$ (say, $-1.5$) implies a more unequal distribution — a primate city system where the largest city is disproportionately large. A coefficient less negative than $-1$ (say, $-0.7$) implies a more even distribution, with cities of similar sizes.

The log-linearisation also makes it straightforward to interpret deviations: cities that lie *above* the fitted line are larger than Zipf's Law predicts for their rank; cities that lie *below* it are smaller.

---

## 4. Canada's City Size Distribution

Canada's urban system has some distinctive features that make it an interesting test case for Zipf's Law.

The country has a small number of very large cities (Toronto at ~6.5 million, Montreal at ~4.3 million, Vancouver at ~2.7 million) and a long tail of medium and small cities. The top three are geographically dispersed: Toronto in the industrial heartland, Montreal in Quebec, Vancouver on the Pacific coast. This reflects regional political economy as much as pure market dynamics.

Below the top three, the distribution is remarkably even. Calgary and Edmonton both have roughly 1.3–1.4 million people — nearly tied for fourth and fifth. Winnipeg, Ottawa, and Quebec City cluster between 800,000 and 1.1 million. The Canadian city size distribution fits Zipf's Law reasonably well for ranks 1–3 but shows a more compressed middle than a pure Pareto distribution would predict.

<div data-viz="echarts" data-options='{
  "title": {"text": "Rank-Size Distribution: Top 30 Canadian CMAs", "left": "center", "subtext": "Log-log scale — slope ≈ −1 is Zipf's Law"},
  "tooltip": {
    "trigger": "item",
    "formatter": "{b}<br/>Rank: {c[0]}<br/>Population: {c[1]} thousand"
  },
  "xAxis": {
    "type": "log",
    "name": "Rank (log scale)",
    "nameLocation": "middle",
    "nameGap": 35,
    "min": 1,
    "max": 35
  },
  "yAxis": {
    "type": "log",
    "name": "Population (thousands, log scale)",
    "nameLocation": "middle",
    "nameGap": 55,
    "min": 80,
    "max": 8000
  },
  "series": [
    {
      "name": "Canadian CMAs",
      "type": "scatter",
      "symbolSize": 9,
      "data": [
        {"name": "Toronto", "value": [1, 6418]},
        {"name": "Montreal", "value": [2, 4314]},
        {"name": "Vancouver", "value": [3, 2737]},
        {"name": "Calgary", "value": [4, 1392]},
        {"name": "Edmonton", "value": [5, 1361]},
        {"name": "Ottawa", "value": [6, 1072]},
        {"name": "Winnipeg", "value": [7, 866]},
        {"name": "Quebec City", "value": [8, 839]},
        {"name": "Hamilton", "value": [9, 785]},
        {"name": "Kitchener", "value": [10, 590]},
        {"name": "London", "value": [11, 542]},
        {"name": "Halifax", "value": [12, 480]},
        {"name": "Oshawa", "value": [13, 415]},
        {"name": "Victoria", "value": [14, 408]},
        {"name": "Windsor", "value": [15, 336]},
        {"name": "Saskatoon", "value": [16, 330]},
        {"name": "Regina", "value": [17, 256]},
        {"name": "Sherbrooke", "value": [18, 230]},
        {"name": "St. John's", "value": [19, 214]},
        {"name": "Barrie", "value": [20, 210]},
        {"name": "Kelowna", "value": [21, 205]},
        {"name": "Abbotsford", "value": [22, 196]},
        {"name": "Sudbury", "value": [23, 174]},
        {"name": "Lethbridge", "value": [24, 118]},
        {"name": "Moncton", "value": [25, 160]},
        {"name": "Kingston", "value": [26, 172]},
        {"name": "Saguenay", "value": [27, 162]},
        {"name": "Trois-Rivières", "value": [28, 157]},
        {"name": "Guelph", "value": [29, 153]},
        {"name": "Brantford", "value": [30, 134]}
      ],
      "itemStyle": {"color": "#5c8ee0"},
      "label": {"show": false}
    },
    {
      "name": "Zipf Prediction",
      "type": "line",
      "smooth": true,
      "data": [[1,6418],[2,3209],[3,2139],[5,1284],[10,642],[15,428],[20,321],[30,214]],
      "lineStyle": {"type": "dashed", "color": "#e05c5c", "width": 2},
      "itemStyle": {"color": "#e05c5c"},
      "symbol": "none"
    }
  ]
}'></div>

The dashed line shows the Zipf prediction anchored to Toronto's population. Several features stand out. Toronto fits almost perfectly by construction. Montreal is slightly smaller than predicted. Vancouver is slightly larger. Calgary and Edmonton — almost equal in size — together approximate what Zipf predicts for a single fourth-ranked city. Below the top five, the distribution compresses relative to the Zipf prediction: Canadian medium cities are more equal in size than a pure power law implies.

<div data-viz="echarts" data-options='{
  "title": {"text": "Actual vs Zipf-Predicted Population: Top 10 Canadian CMAs", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "legend": {"data": ["Actual", "Zipf Prediction"], "bottom": 0},
  "xAxis": {
    "type": "category",
    "data": ["Toronto", "Montreal", "Vancouver", "Calgary", "Edmonton", "Ottawa", "Winnipeg", "Quebec City", "Hamilton", "Kitchener"],
    "axisLabel": {"rotate": 30, "fontSize": 11}
  },
  "yAxis": {
    "type": "value",
    "name": "Population (thousands)",
    "nameLocation": "middle",
    "nameGap": 55,
    "min": 0,
    "max": 7000
  },
  "series": [
    {
      "name": "Actual",
      "type": "bar",
      "data": [6418, 4314, 2737, 1392, 1361, 1072, 866, 839, 785, 590],
      "itemStyle": {"color": "#5c8ee0"}
    },
    {
      "name": "Zipf Prediction",
      "type": "bar",
      "data": [6418, 3209, 2139, 1605, 1284, 1070, 917, 802, 713, 642],
      "itemStyle": {"color": "#e05c5c", "opacity": 0.7}
    }
  ]
}'></div>

Montreal exceeds its Zipf prediction — it is the historical metropolis of Canada and retains a primate-city character in Quebec. Calgary and Edmonton together are roughly what Zipf predicts for the fourth-ranked city. Hamilton and Kitchener are substantially larger than predicted — reflecting their absorption into the Toronto metropolitan orbit.

---

## 5. Why Does Canada Deviate? Regional Political Economy

Pure Zipf's Law emerges from random multiplicative growth without institutional constraints. Canada's city system has been heavily shaped by institutions: federal bilingualism policies that reinforced Montreal, the National Policy that concentrated manufacturing in the Windsor-Quebec City corridor, natural resource booms that built Edmonton and Calgary, and interprovincial migration patterns that differ from the US.

The most notable deviation is the Alberta urban near-parity. Edmonton and Calgary are almost exactly the same size — highly unusual in a province of this scale. In most jurisdictions, economic geography produces a dominant regional city: Houston dominates Texas; Phoenix dominates Arizona; Perth dominates Western Australia. Alberta's energy economy created two cities with complementary functions — Calgary as the corporate headquarters and financial centre, Edmonton as the government capital and refining hub — that grew in parallel rather than in competition. This near-parity is what urban economists call an **urban system without a primate city**.

The primate city concept, formalised by Mark Jefferson in 1939, describes a city system where the largest city is disproportionately large relative to the rank-size prediction. Countries with primate city systems (France/Paris, Argentina/Buenos Aires, Thailand/Bangkok) tend to have highly centralised political systems and historically agrarian hinterlands. Canada's federal structure and regional power bases have prevented a single dominant city from emerging, keeping the distribution closer to Zipf's prediction even though the underlying growth process is not purely random.

---

## 6. Gibrat's Law in Practice

Empirical tests of Gibrat's Law for Canadian cities generally find support over long periods. Large cities and small cities have similar average growth rates. But there is substantial variation. Cities with favourable resource endowments (Fort McMurray, Saskatoon) can grow explosively over short windows. Cities losing their industrial base (Windsor, Sudbury) can stagnate or decline.

Over sufficiently long periods — decades rather than years — these idiosyncratic shocks wash out and the distribution returns to something close to Zipf. The law is a statement about the long-run statistical tendency of multiplicative random growth, not about the growth trajectory of any individual city.

---

## 7. Policy Implications

Zipf's Law has a somewhat fatalistic implication: the structure of the urban system is determined by deep statistical regularities, not by individual policy choices. No policy is going to make Lethbridge the size of Calgary. But the distribution is not immutable. Policy can shift the growth rate of particular cities, bend the rank-size relationship at specific points, or alter the slope of the Pareto exponent.

Canadian urban policy has generally not aimed to flatten the distribution. Immigration settlement patterns reinforce the dominance of Toronto and Vancouver. Federal transfers partly offset regional disparities but do not redistribute economic activity. Provincial capital status protects Edmonton and Ottawa from being purely subordinate to Calgary and Toronto respectively.

Understanding where a city sits relative to the Zipf prediction — above the line (larger than expected) or below it (smaller than expected) — helps diagnose whether a city is likely to grow toward its predicted size or whether structural factors have pushed it off the trajectory that market forces alone would produce.

---

Next in this cluster: **The Urban Economic Base** (Model 14) moves inside the city to ask: which industries actually drive growth, and how does a shock to the export sector — like an oil price collapse — amplify through the local economy via the multiplier effect?
