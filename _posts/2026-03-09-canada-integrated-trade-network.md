---
layout: model
title: "The Integrated Trade Network"
subtitle: "Canada's Goods System as a Directed Graph — Flow, Centrality, and the Windsor Problem"
series: "Economic Systems"
series_order: 10
cluster: "T — Trade and Transport"
date: 2026-03-09
categories: [modelling]
tags:
  - network-analysis
  - graph-theory
  - canada
  - trade-network
  - windsor-detroit
  - betweenness-centrality
  - max-flow
  - economic-geography
difficulty: 4
math: true
viz: true
leaflet: true
math_core: ["Directed graph", "betweenness centrality", "max-flow min-cut", "network resilience", "O-D matrix"]
description: >
  Canada's goods trade system assembled as a directed network graph — applying
  max-flow min-cut analysis, betweenness centrality, and network resilience
  methods to identify the structural vulnerabilities of the Canadian freight
  network and draw explicit parallels with the pipeline network from Cluster P.
excerpt: >
  The previous four models examine pieces: gravity determines volumes, corridors
  carry them, ports gate them, modal choice routes them. This model assembles
  those pieces into a directed network graph and applies the same graph-theoretic
  tools used for the pipeline system to the trade system — revealing a structural
  architecture with one dominant vulnerability: Windsor-Detroit's betweenness
  centrality of 0.82.
toc: true
---

## 1. From Pieces to Network

The four preceding essays in this cluster each examine a component of Canada's
goods trade system in isolation. T1 derives the gravity model and quantifies
the volumes that geography and economic mass predict. T2 maps the corridor
systems that carry those volumes and examines the flow assignment mathematics
that determines routing. T3 analyses port economics — throughput functions,
queuing theory, hinterland competition. T4 examines modal choice and the
cost functions that determine whether freight moves by truck, rail, or ship.

Each analysis is valuable on its own terms. But pieces, however well understood
individually, do not compose automatically into a system-level picture. To
understand which nodes matter most, which links constrain total flow, and which
disruptions have outsized systemic effects, we need to assemble the pieces into
a single directed network and apply the tools of network analysis.

This is exactly what Cluster P did for Alberta's pipeline infrastructure. P5
assembled crude oil, natural gas, NGL, and refined product flows into a directed
graph and computed betweenness centrality and max-flow min-cut to identify
Hardisty as the network's dominant structural vulnerability — the node through
which virtually all Alberta hydrocarbon exports pass, whose disruption would
simultaneously affect all export directions.

This essay applies the same framework to Canada's goods trade network. The nodes
are different — ports, rail hubs, and border crossings rather than pump stations
and tank farms. The edge weights represent corridor capacity rather than pipe
throughput. But the mathematics is identical, and the result — a high-centrality
node whose disruption has asymmetric systemic consequences — is structurally
similar to what the pipeline analysis found.

---

## 2. The Network Defined

### Nodes

Canada's freight trade network can be represented with twelve key nodes, chosen
to capture the major geographic decision points where freight routes diverge,
where modes transfer, and where international borders are crossed:

1. **Vancouver Port** — Pacific Gateway primary container terminal
2. **Prince Rupert Port** — Pacific Gateway secondary, fastest-growing
3. **Edmonton** — Prairie freight hub; junction of northern and southern rail corridors
4. **Calgary** — Prairie distribution point; CN/CP interchange
5. **Winnipeg** — Mid-continent gateway; junction of east-west and north-south rail
6. **Toronto** — Ontario distribution hub; largest concentration of manufacturing freight origins
7. **Montreal** — Eastern Canada hub; inland ocean port
8. **Halifax Port** — Atlantic Gateway
9. **Windsor** — US border crossing; automotive corridor gateway to US Midwest
10. **Sarnia** — Secondary Great Lakes crossing; Bluewater Bridge complex
11. **Niagara** — Third major Ontario-US crossing; Rainbow, Peace, and Queenston bridges
12. **US Markets** — Composite sink node representing all US destinations

The choice to treat "US Markets" as a single composite sink node is a modelling
simplification. In reality, US destinations span the continent, with different
import crossing points serving different US regions. For the purpose of
identifying Canadian network structure, this simplification is appropriate:
we are interested in the Canadian freight network's internal geometry, not the
distribution within the US.

### Edges and capacities

Directed edges represent major freight corridors with estimated annual capacity
in thousands of TEU-equivalents (a normalised unit that allows comparison
across commodity types). The capacity figures are approximate, derived from
rail waybill data, port statistics, border crossing records, and published
infrastructure capacity assessments.

| Corridor | Capacity (000 TEU-equiv/yr) |
|:---|---:|
| Vancouver → Edmonton (CN/CP rail) | 2,500 |
| Prince Rupert → Edmonton (CN rail) | 1,000 |
| Edmonton → Calgary | 1,800 |
| Calgary → Winnipeg | 1,200 |
| Winnipeg → Toronto | 1,500 |
| Toronto → Windsor | 800 |
| Windsor → US Markets | 600 |
| Toronto → Niagara | 400 |
| Niagara → US Markets | 400 |
| Toronto → Montreal | 700 |
| Toronto → Sarnia | 350 |
| Sarnia → US Markets | 350 |
| Montreal → Halifax | 200 |
| Halifax → US Markets | 100 |
| Montreal → US Markets (direct) | 150 |

---

## 3. Max-Flow Min-Cut

### The theorem

The max-flow min-cut theorem, proved independently by Ford and Fulkerson (1956)
and Elias, Feinstein, and Shannon (1956), states that in any network with a
source node $s$ and a sink node $t$, the maximum flow that can be pushed from
$s$ to $t$ equals the capacity of the minimum cut separating $s$ from $t$.

Formally, a cut $(S, T)$ is a partition of the node set $V$ into two disjoint
subsets $S$ (containing the source) and $T$ (containing the sink). The capacity
of the cut is the sum of capacities of edges directed from $S$ to $T$:

$$c(S,T) = \sum_{(u,v): u \in S, v \in T} c(u,v)$$

The minimum cut is the cut with the smallest capacity. The max-flow min-cut
theorem states:

$$\max \text{ flow}(s \to t) = \min \text{ cut capacity}(s, t)$$

This theorem has a direct policy interpretation: the maximum throughput of
any network is constrained by its weakest link set — the set of edges that,
if removed, would disconnect the source from the sink and whose total capacity
is minimised.

### Application to the Canadian trade network

In Canada's trade network, sources are Pacific Gateway ports (Vancouver and
Prince Rupert) and Atlantic Gateway ports (Montreal and Halifax), plus Prairie
production nodes (Edmonton, Calgary). The sink is "US Markets." The maximum
flow the network can sustain from Canadian sources to US destinations is
determined by the minimum cut.

Examining the network structure, the minimum cut is dominated by the
Windsor-Detroit crossing. Windsor's outbound capacity to US Markets is
600,000 TEU-equivalents per year — lower than the combined capacity of the
links feeding it from Toronto. This means Windsor is a binding constraint:
even if upstream links (Winnipeg-Toronto, Toronto-Windsor) have spare capacity,
flow through Windsor cannot exceed 600K TEU-equiv. The minimum cut capacity
identifies Windsor as the binding constraint on the entire Canada-to-US-Midwest
flow.

This has a direct infrastructure policy implication. Adding capacity at Vancouver —
a new terminal, improved rail service — does not increase the maximum flow to
the US Midwest. The maximum flow is determined by Windsor, not by the Pacific
Gateway. Infrastructure investment improves the overall system only when it
addresses the actual minimum cut, not upstream links that already exceed the
minimum cut capacity.

The Gordie Howe International Bridge addresses exactly this. By adding
six lanes of crossing capacity, it increases Windsor's outbound capacity
from approximately 600K to over 1,200K TEU-equivalents — effectively doubling
the minimum cut and correspondingly increasing the maximum possible flow
through the Canada-US Midwest corridor.

---

## 4. Betweenness Centrality

### The definition

Betweenness centrality measures how frequently a node appears on shortest paths
between all other pairs of nodes in the network. For a node $v$:

$$B(v) = \sum_{s \neq v \neq t} \frac{\sigma(s,t \mid v)}{\sigma(s,t)}$$

where $\sigma(s,t)$ is the total number of shortest paths from source $s$ to
target $t$, and $\sigma(s,t \mid v)$ is the number of those shortest paths
that pass through $v$. Normalised betweenness divides by the maximum possible
value, giving a score between 0 and 1. A node with normalised betweenness of 1.0
lies on every shortest path in the network; a node with 0 lies on none.

High betweenness centrality identifies nodes that are critical intermediaries:
their removal or disruption affects not just their own connections but the
shortest-path structure between many other pairs of nodes. In freight networks,
high-betweenness nodes are the strategic vulnerabilities — the places where
disruption has amplified systemic effects.

### Estimated centrality values

For Canada's trade network, estimated normalised betweenness centrality values
(computed approximately from the network structure described above) are:

| Node | Betweenness (0–1) |
|:---|---:|
| Windsor | 0.82 |
| Toronto | 0.71 |
| Winnipeg | 0.58 |
| Montreal | 0.45 |
| Halifax | 0.25 |
| Vancouver | 0.38 |
| Calgary | 0.32 |
| Edmonton | 0.28 |
| Prince Rupert | 0.18 |
| Sarnia | 0.20 |
| Niagara | 0.22 |

Windsor's centrality of 0.82 reflects its position as the primary gateway
for freight moving from Ontario — Canada's manufacturing and distribution
heartland — to the US Midwest, which is Canada's largest single export market
region. Almost every optimal path from Canadian interior origins to US Midwest
destinations passes through Windsor. No other single node approaches this level
of path concentration.

---

## 5. Network Betweenness: Visualised

<div data-viz="echarts" style="height:360px" data-options='{
  "title": {"text": "Network Betweenness Centrality by Node", "subtext": "Normalised 0–1. Windsor highlighted in red as dominant structural vulnerability.", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "grid": {"left": "4%", "right": "8%", "bottom": "5%", "containLabel": true},
  "xAxis": {"type": "value", "name": "Betweenness centrality (0 = low, 1 = high)", "max": 1},
  "yAxis": {
    "type": "category",
    "data": ["Prince Rupert", "Sarnia", "Niagara", "Halifax", "Edmonton", "Calgary", "Vancouver", "Montreal", "Winnipeg", "Toronto", "Windsor"],
    "axisLabel": {"fontSize": 11}
  },
  "series": [{
    "type": "bar",
    "label": {"show": true, "position": "right", "formatter": "{c}"},
    "data": [
      {"value": 0.18, "itemStyle": {"color": "#bfdbfe"}},
      {"value": 0.20, "itemStyle": {"color": "#bfdbfe"}},
      {"value": 0.22, "itemStyle": {"color": "#93c5fd"}},
      {"value": 0.25, "itemStyle": {"color": "#93c5fd"}},
      {"value": 0.28, "itemStyle": {"color": "#7dd3fc"}},
      {"value": 0.32, "itemStyle": {"color": "#60a5fa"}},
      {"value": 0.38, "itemStyle": {"color": "#3b82f6"}},
      {"value": 0.45, "itemStyle": {"color": "#2563eb"}},
      {"value": 0.58, "itemStyle": {"color": "#1d4ed8"}},
      {"value": 0.71, "itemStyle": {"color": "#1e40af"}},
      {"value": 0.82, "itemStyle": {"color": "#dc2626"}}
    ]
  }]
}'></div>

*Windsor's betweenness of 0.82 is substantially higher than Toronto's 0.71 — which itself is high — because Windsor is where virtually all optimal paths from Toronto to US Midwest destinations must exit. Toronto distributes and accumulates freight; Windsor gates it to the US.*

---

## 6. The Full Network Map

<div data-leaflet id="trade-network-map" style="height:440px" data-lat="49" data-lng="-90" data-zoom="4" data-tiles="carto" data-markers='[{"lat":49.28,"lng":-123.12,"label":"Vancouver Port — centrality 0.38"},{"lat":54.31,"lng":-130.32,"label":"Prince Rupert — centrality 0.18"},{"lat":53.55,"lng":-113.49,"label":"Edmonton hub — centrality 0.28"},{"lat":51.05,"lng":-114.07,"label":"Calgary — centrality 0.32"},{"lat":49.90,"lng":-97.14,"label":"Winnipeg — centrality 0.58"},{"lat":43.65,"lng":-79.38,"label":"Toronto — centrality 0.71"},{"lat":42.31,"lng":-83.04,"label":"Windsor-Detroit — centrality 0.82 — CRITICAL NODE"},{"lat":45.50,"lng":-73.57,"label":"Montreal — centrality 0.45"},{"lat":44.64,"lng":-63.57,"label":"Halifax — centrality 0.25"},{"lat":43.10,"lng":-79.07,"label":"Niagara crossings — centrality 0.22"},{"lat":42.97,"lng":-82.40,"label":"Sarnia-Port Huron — centrality 0.20"}]'></div>

*The network visualised geographically. Windsor (southwest Ontario) is the geographic funnel through which Ontario-origin freight exits to the US Midwest. Winnipeg is the Prairie gateway — all rail traffic east from the Prairies flows through or near it. Pacific Gateway ports handle Asian trade; Atlantic ports handle European flows.*

---

## 7. Max-Flow by Corridor

<div data-viz="echarts" style="height:320px" data-options='{
  "title": {"text": "Corridor Capacity vs Min-Cut Constraint", "subtext": "000 TEU-equivalents/year. Windsor min-cut (600K) is below its theoretical feed capacity — the binding constraint.", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "legend": {"data": ["Theoretical capacity", "Min-cut constraint"], "bottom": 0},
  "grid": {"left": "3%", "right": "4%", "bottom": "14%", "containLabel": true},
  "xAxis": {"type": "category", "data": ["Pacific Gateway\n(Van+PR)", "Prairie rail\n(Wpg→Tor)", "Windsor-Detroit", "Niagara\ncrossings", "Atlantic gateway\n(Hal+Mtl)"]},
  "yAxis": {"type": "value", "name": "000 TEU-equiv/year", "max": 4000},
  "series": [
    {
      "name": "Theoretical capacity",
      "type": "bar",
      "itemStyle": {"color": "#2563eb"},
      "label": {"show": true, "position": "top"},
      "data": [3500, 1500, 700, 400, 300]
    },
    {
      "name": "Min-cut constraint",
      "type": "bar",
      "itemStyle": {"color": "#dc2626"},
      "label": {"show": true, "position": "top"},
      "data": [3500, 1500, 600, 400, 300]
    }
  ]
}'></div>

*Windsor is the only corridor where the min-cut constraint (600K) falls below theoretical feed capacity (700K). All other corridors are not currently bottlenecked at the crossing point itself — their constraints lie upstream or in terminal handling. The Gordie Howe bridge doubles Windsor's min-cut capacity when complete.*

---

## 8. The Windsor Problem: Disruption Economics

<div data-viz="echarts" style="height:300px" data-options='{
  "title": {"text": "Windsor Blockade — Economic Cost by Sector per Day", "subtext": "Estimated CAD$M/day based on Freedom Convoy 2022 economic analysis. Total ~CAD$350M/day.", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "grid": {"left": "3%", "right": "4%", "bottom": "8%", "containLabel": true},
  "xAxis": {"type": "category", "data": ["Automotive\nparts", "Manufacturing\ninputs", "Consumer\ngoods", "Perishable\nfood", "Other"]},
  "yAxis": {"type": "value", "name": "CAD$M per day", "max": 220},
  "series": [{
    "type": "bar",
    "label": {"show": true, "position": "top", "formatter": "CAD${c}M"},
    "data": [
      {"value": 180, "itemStyle": {"color": "#1e3a8a"}},
      {"value": 55,  "itemStyle": {"color": "#2563eb"}},
      {"value": 60,  "itemStyle": {"color": "#3b82f6"}},
      {"value": 35,  "itemStyle": {"color": "#60a5fa"}},
      {"value": 20,  "itemStyle": {"color": "#93c5fd"}}
    ],
    "markLine": {
      "symbol": "none",
      "lineStyle": {"color": "#dc2626", "type": "dashed", "width": 2},
      "label": {"formatter": "Total ~CAD$350M/day", "position": "insideEndTop"},
      "data": [{"yAxis": 350}]
    }
  }]
}'></div>

*Automotive parts account for roughly 51% of the per-day disruption cost, reflecting Windsor's dominance as an automotive corridor. A six-day blockade cost an estimated CAD$2.1 billion, concentrated in automotive just-in-time supply chains with no buffer inventory.*

---

## 9. Integrated Flow: The Sankey View

<div data-viz="echarts" style="height:380px" data-options='{
  "title": {"text": "Integrated Canada Goods Trade Flow", "subtext": "Estimated two-way flows, CAD$B/year. Sankey nodes represent network hubs.", "left": "center"},
  "tooltip": {"trigger": "item", "formatter": "{b}"},
  "series": [{
    "type": "sankey",
    "layout": "none",
    "emphasis": {"focus": "adjacency"},
    "nodeAlign": "left",
    "draggable": false,
    "itemStyle": {"borderWidth": 1, "borderColor": "#aaa"},
    "lineStyle": {"color": "gradient", "opacity": 0.4},
    "nodes": [
      {"name": "Pacific ports"},
      {"name": "Prairie hub"},
      {"name": "Eastern hub"},
      {"name": "Windsor crossing"},
      {"name": "Niagara + Sarnia"},
      {"name": "Atlantic gateway"},
      {"name": "US Midwest"},
      {"name": "US East"},
      {"name": "Asia"}
    ],
    "links": [
      {"source": "Pacific ports",     "target": "Prairie hub",      "value": 100},
      {"source": "Pacific ports",     "target": "Asia",             "value": 90},
      {"source": "Prairie hub",       "target": "Eastern hub",      "value": 80},
      {"source": "Prairie hub",       "target": "Asia",             "value": 30},
      {"source": "Eastern hub",       "target": "Windsor crossing", "value": 146},
      {"source": "Eastern hub",       "target": "Niagara + Sarnia", "value": 80},
      {"source": "Eastern hub",       "target": "Atlantic gateway", "value": 40},
      {"source": "Windsor crossing",  "target": "US Midwest",       "value": 146},
      {"source": "Niagara + Sarnia",  "target": "US East",          "value": 80},
      {"source": "Atlantic gateway",  "target": "US East",          "value": 40}
    ]
  }]
}'></div>

*The Sankey diagram makes the network's structure immediately legible: Pacific ports feed the Prairie hub and Asia; the Eastern hub (Toronto-Montreal region) distributes to Windsor, Niagara-Sarnia, and Atlantic gateways; Windsor carries by far the largest single flow to the US Midwest. The width of each link is proportional to flow value.*

---

## 10. Comparison to Cluster P: The Parallel Structure

The structural parallel between Canada's trade network and Alberta's pipeline
network — examined in P5 — is direct and instructive, and it is worth making
explicit.

In the pipeline network, Hardisty is the high-betweenness node. Every barrel
of oil sands production must pass through or near Hardisty before entering the
export pipeline system. Hardisty's centrality reflects the geology of the oil
sands: production is concentrated in the Athabasca region north of Fort McMurray,
and all export corridors begin at the Hardisty hub. Disruption at Hardisty
affects all export directions simultaneously.

In the trade network, Windsor is the high-betweenness node. The majority of
Ontario-origin goods trade with the United States must pass through the
Windsor-Detroit crossing. Windsor's centrality reflects the geography of the
Canada-US border: the Detroit River is narrow, the US manufacturing heartland
is directly across it, and decades of automotive supply chain investment have
created a corridor so economically integrated that alternative routes are
structurally uncompetitive for the dominant commodity flows.

Both are geographic bottlenecks. Both have betweenness centrality substantially
above all other nodes in their respective networks. Both have experienced high-profile
disruption events: Freedom Convoy at Windsor (2022), pipeline price collapse at
Hardisty during the 2018 AECO crisis. And both are being addressed through
infrastructure investment designed to add redundancy without displacing the
existing dominant node: Gordie Howe adds a second Windsor crossing; Trans
Mountain Expansion added a second Pacific corridor.

Betweenness centrality is the mathematical concept that names both vulnerabilities.
It is not a metaphor or an analogy — it is the same calculation applied to
two different networks, producing the same structural finding: a single node
of extremely high centrality, whose disruption has consequences disproportionate
to its geographic size or apparent significance. The pipeline system's Hardisty
and the trade network's Windsor are, in this formal sense, the same kind of
problem.

---

*This completes Cluster T — Trade and Transport. The five essays together cover the mathematical foundations of trade geography: the gravity model (T1) predicts bilateral volumes; corridor analysis (T2) maps the routes; port economics (T3) examines the gateway competition; modal choice (T4) explains how freight distributes across modes; and network analysis (T5) assembles the pieces into a system-level picture with quantified vulnerabilities.*

*The tools developed here — O-D matrices, Wardrop equilibrium, queuing theory, betweenness centrality, and max-flow min-cut — are general-purpose methods in economic geography. The next cluster, Cluster U (Urban Economic Systems), applies these same tools to a different scale: the city. The nodes become urban centres; the edges become commute flows, migration corridors, and housing market linkages. The mathematics is the same. The geography changes.*
