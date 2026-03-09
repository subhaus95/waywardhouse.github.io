---
layout: model
title: "Canadian Trade Corridors"
subtitle: "How Canada's Goods Actually Move: Rail, Road, and the Dominance of Windsor-Detroit"
series: "Economic Systems"
series_order: 7
cluster: "TR — Trade and Transport"
date: 2026-03-09
image: /assets/images/trade-corridors.png
categories: [modelling]
tags:
  - trade-corridors
  - canada
  - rail
  - trucking
  - windsor-detroit
  - pacific-gateway
  - transport-geography
  - alberta
difficulty: 3
math: true
viz: true
leaflet: true
math_core: ["Flow assignment", "origin-destination matrices", "corridor capacity", "Wardrop equilibrium"]
description: >
  A quantitative geography of Canadian freight corridors — how goods actually
  move from origin to destination across the three primary corridor systems,
  the mathematics of flow assignment and user equilibrium, and the structural
  vulnerability created by Windsor-Detroit's dominance.
excerpt: >
  A corridor is not just a road or a rail line. It is the bundle of
  infrastructure, terminal capacity, customs facilities, and commercial services
  that make freight movement possible at scale. Canada has three primary corridor
  systems, and they are not equal: Windsor-Detroit alone carries roughly a quarter
  of all Canada-US trade by value, and it is served by a single privately-owned
  bridge.
toc: true
---

## 1. The Question

How does freight actually move in Canada? The gravity model from T1 tells us
how much trade should occur between any two locations, given their sizes and
the distance between them. But the gravity model is silent on routing: it
predicts volumes, not paths. This essay asks the infrastructure question behind
the trade statistics: which physical routes carry Canada's goods, at what
capacity, and what happens to the system when a key link is disrupted?

The distinction between routes and corridors is important. A corridor is not
simply a road or a railway. It is the bundle of physical infrastructure, terminal
capacity, border crossing facilities, customs processing capability, and
commercial services — trucking companies, freight brokers, logistics providers,
warehousing — that collectively make freight movement possible at scale. Two
geographically identical routes can have vastly different corridor capacity
depending on this bundle of complementary assets. Understanding Canadian freight
movement means understanding corridors, not just roads and rails.

---

## 2. The Three Corridor Systems

Canada's freight geography is organised around three primary corridor systems.
Each connects a set of Canadian origins to a set of destinations — primarily
in the United States, but also to international maritime connections for global
trade. The three systems are geographically distinct, serve different commodity
mixes, and face different structural constraints.

### Pacific Gateway

The Pacific Gateway connects the Port of Vancouver and the Port of Prince Rupert
on the British Columbia coast to the Canadian prairies and beyond via the
CN and CP national rail networks. Vancouver handled approximately 3.3 million
twenty-foot equivalent units (TEUs) of container traffic in 2023, making it
by far Canada's largest container port. Prince Rupert, though smaller at
870,000 TEUs in 2023, is growing rapidly and has structural advantages over
Vancouver: it is 2.4 shipping days closer to Shanghai, and its CN rail connection
runs directly to Chicago without traversing the congested Vancouver-area rail
network.

Together the two Pacific Gateway ports handle approximately 35% of Canada's
container trade. The corridor's primary commodity flows in one direction
are consumer goods, manufactured products, and machinery from Asia; outbound
flows include Prairie grain, potash, coal, and increasingly, Canadian
manufactured goods. The corridor's critical infrastructure constraints are
the mountain passes through which rail must traverse the Rockies and the
Coastal Mountains — a geographic constraint that limits the number of rail
lines and makes the corridor vulnerable to weather events and rock slides.

### Mid-Continent: Windsor-Detroit

The mid-continent corridor, centred on the Windsor-Detroit crossing, is the
most economically significant freight route in Canada. The Ambassador Bridge
alone — a single privately-owned span across the Detroit River connecting
Windsor, Ontario to Detroit, Michigan — carries approximately CAD$146 billion
per year in two-way trade, accounting for roughly 25% of all Canada-US trade by
value. The crossing is the primary artery for automotive supply chains, which
dominate the Ontario-Michigan manufacturing relationship and involve the same
parts crossing the border multiple times during assembly.

The Windsor-Detroit crossing's dominance reflects the logic of the gravity
model applied to industrial geography. The US automotive manufacturing heartland
— centred on Detroit but extending to Ohio, Indiana, and Kentucky — is within
a few hundred kilometres of Windsor and the surrounding Ontario manufacturing
cluster. Proximity reduces logistics costs, enables just-in-time delivery, and
allows tight coordination across the border. The result is an extraordinarily
dense corridor of high-frequency, time-sensitive freight movement that
is deeply integrated into North American manufacturing.

### Atlantic Corridor

The Atlantic corridor connects the Port of Halifax on the Nova Scotia coast and
the Port of Montreal on the St. Lawrence River to eastern Canada and the US
Northeast. Halifax handled 535,000 TEUs in 2023; Montreal handled 1.57 million
TEUs, making it Canada's second-largest container port by volume. The Atlantic
corridor's geographic advantage is proximity to European markets — Halifax is
approximately two days closer to northern European ports than Montreal, and
several days closer than Pacific Gateway ports — and proximity to the US
Northeast, which is Canada's second-largest export destination after the US
Midwest.

The corridor serves Atlantic Canadian provinces, Quebec, and Ontario for European
trade, and provides an alternative to Pacific Gateway routing for some Prairie
grain and resource exports destined for European markets. Rail connections from
Montreal and Halifax to the interior are operated by CN and CP, though landside
distances are greater than for Pacific Gateway routing to the same Prairie origins.

---

## 3. The Mathematics of Flow Assignment

### Origin-destination matrices

The starting point for corridor flow analysis is the origin-destination (O-D)
matrix: a matrix $T$ where entry $T_{ij}$ represents the volume of freight
(in tonnes, TEUs, or dollars) moving from origin $i$ to destination $j$ over
a defined time period. For Canadian freight, origins might be provinces or
major cities; destinations might be US states, ports, or major inland hubs.

The O-D matrix is estimated from shipper surveys, customs records, waybill
data from railways, and weigh station records from trucking. It is never
measured directly with complete accuracy. Statistics Canada's annual freight
survey provides the most comprehensive Canadian O-D data, augmented by
Transport Canada's border crossing statistics and the railways' own traffic data.

### Wardrop's principles of user equilibrium

Once the O-D matrix is estimated, the question is how to assign those flows
to the actual network of routes and corridors. The dominant framework is
Wardrop's first principle of user equilibrium (1952):

> In user equilibrium, all routes between a given origin-destination pair that
> are actually used have equal generalised cost; no unused route has a lower
> cost than any used route.

Formally, let $c_r$ be the generalised cost (time plus money, weighted by the
shipper's value of time) on route $r$ between O-D pair $(i,j)$, and let $x_r$
be the flow on that route. User equilibrium requires:

$$c_r(x) = \lambda_{ij} \quad \forall r \text{ with } x_r > 0$$
$$c_r(x) \geq \lambda_{ij} \quad \forall r \text{ with } x_r = 0$$

where $\lambda_{ij}$ is the minimum cost between $i$ and $j$ in equilibrium.
This is a fixed-point condition: the costs depend on the flows (through
congestion), and the flows depend on the costs (through shipper routing choices).

### The Beckmann formulation

Beckmann, McGuire, and Winsten (1956) showed that Wardrop user equilibrium is
equivalent to the solution of an optimisation problem. Define the link cost
function $t_a(x_a)$ giving the travel time on link $a$ as a function of the
flow $x_a$ on that link. The Beckmann objective is:

$$\min \sum_{a} \int_0^{x_a} t_a(\omega) \, d\omega$$

subject to flow conservation at each node and non-negativity constraints.
This is a convex programme when $t_a(\cdot)$ is increasing (congestion increases
with flow), and its solution is the user equilibrium flow pattern.

The Beckmann formulation makes the assignment problem tractable: standard
convex optimisation algorithms can find the equilibrium flow pattern given
a network, an O-D matrix, and link cost functions. Transport planners use
this framework to evaluate infrastructure investments, identify bottlenecks,
and simulate the effects of corridor disruptions.

---

## 4. Corridor Trade Volumes: The Data

<div data-viz="echarts" style="height:380px" data-options='{
  "title": {"text": "Canada-US Trade by Major Crossing or Corridor (2023)", "subtext": "Estimated two-way trade value, CAD$ billions", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "grid": {"left": "4%", "right": "8%", "bottom": "5%", "containLabel": true},
  "xAxis": {"type": "value", "name": "CAD$ billions"},
  "yAxis": {
    "type": "category",
    "data": ["Pacific Highway BC", "St. Lawrence marine", "Other crossings", "Sarnia-Port Huron", "Niagara crossings", "Pacific Gateway rail", "Windsor-Detroit road"],
    "axisLabel": {"fontSize": 11}
  },
  "series": [{
    "type": "bar",
    "label": {"show": true, "position": "right", "formatter": "{c}B"},
    "data": [
      {"value": 25,  "itemStyle": {"color": "#bfdbfe"}},
      {"value": 40,  "itemStyle": {"color": "#93c5fd"}},
      {"value": 50,  "itemStyle": {"color": "#7dd3fc"}},
      {"value": 60,  "itemStyle": {"color": "#3b82f6"}},
      {"value": 80,  "itemStyle": {"color": "#2563eb"}},
      {"value": 100, "itemStyle": {"color": "#16a34a"}},
      {"value": 146, "itemStyle": {"color": "#1e3a8a"}}
    ]
  }]
}'></div>

*Windsor-Detroit's dominance is structural, not incidental: it reflects the geographic concentration of North American automotive manufacturing on both sides of a narrow river. Pacific Gateway rail volumes reflect container imports from Asia moving to Canadian and US interior markets.*

---

## 5. The Network: Corridor Geography

<div data-leaflet id="corridors-map" style="height:420px" data-lat="48" data-lng="-88" data-zoom="4" data-tiles="carto" data-markers='[{"lat":49.28,"lng":-123.12,"label":"Pacific Gateway — 3.3M TEUs (Vancouver)"},{"lat":54.31,"lng":-130.32,"label":"Prince Rupert — 870K TEUs, fastest growing"},{"lat":42.31,"lng":-83.04,"label":"Windsor-Detroit — CAD$146B/yr"},{"lat":42.97,"lng":-82.40,"label":"Sarnia-Port Huron — CAD$60B/yr"},{"lat":43.10,"lng":-79.07,"label":"Niagara crossings — CAD$80B/yr"},{"lat":45.50,"lng":-73.57,"label":"Montreal Port — 1.57M TEUs"},{"lat":44.64,"lng":-63.57,"label":"Halifax — 535K TEUs"},{"lat":53.55,"lng":-113.49,"label":"Edmonton — Prairie freight hub"},{"lat":49.90,"lng":-97.14,"label":"Winnipeg — Mid-continent hub"}]'></div>

*The three corridor systems are geographically separate: Pacific Gateway on the west coast, Atlantic on the east, and the mid-continent Windsor-Detroit crossing in the south. Note the absence of a major crossing between Sarnia and Niagara — Windsor dominates the Great Lakes crossing geography.*

---

## 6. The Windsor-Detroit Bottleneck

The Ambassador Bridge is a private infrastructure asset owned by the Moroun
family of Michigan, who have held the crossing since 1979. It is approximately
2.4 kilometres long, carries four traffic lanes, and operates around the clock.
By the measure of economic value crossing per linear metre of infrastructure,
it is likely the most economically significant bridge in the world.

That concentration creates structural vulnerability. The Freedom Convoy protest
of February 2022 blockaded the Ambassador Bridge for six days. During those six
days, automotive plants on both sides of the border began halting production
lines as parts inventory ran out. The just-in-time delivery systems that make
modern automotive assembly economical — in which parts arrive hours before they
are needed on the production line — have essentially zero buffer for multi-day
border disruptions. The estimated economic cost of the six-day blockade was
CAD$300-400 million per day, concentrated in the automotive sector. A single
protest at a single bridge cost an estimated CAD$1.8-2.4 billion in total.

The Gordie Howe International Bridge, under construction throughout 2024 and
approaching completion, addresses this vulnerability. The new crossing is a
public-private partnership between the governments of Canada and Michigan,
funded through a combination of federal contributions and toll revenue financing,
at an estimated total cost of CAD$5.7 billion. It adds six lanes of crossing
capacity — doubling the effective Windsor-Detroit corridor throughput — and is
owned publicly rather than privately, eliminating the single-owner bottleneck
that created both the Freedom Convoy vulnerability and three decades of capacity
constraints on one of the world's most economically important trade routes.

### The 2025 tariff impact on the corridor

The 2025 US tariffs on Canadian goods hit Windsor-Detroit disproportionately
hard, for a reason that is specific to the automotive supply chain structure.
A typical automotive part crosses the Canada-US border five to seven times
during the assembly process — moving between component suppliers, sub-assembly
plants, and final assembly facilities on both sides of the border. Under a
25% tariff regime, each crossing incurs a 25% levy. A part that crosses five
times faces, in aggregate, a cost structure equivalent to a tariff far exceeding
25% of the original component value. Estimates of the total annual cost to the
Canadian automotive sector range from CAD$8 billion to CAD$15 billion, depending
on the assumptions made about pass-through rates and supply chain reconfiguration.

---

## 7. Pacific Gateway Growth

<div data-viz="echarts" style="height:360px" data-options='{
  "title": {"text": "Pacific Gateway Container Throughput Growth (2010–2023)", "subtext": "TEUs (thousands). Note 2020 dip from COVID-19 supply chain disruption.", "left": "center"},
  "tooltip": {"trigger": "axis"},
  "legend": {"data": ["Vancouver Port", "Prince Rupert"], "bottom": 0},
  "grid": {"left": "3%", "right": "4%", "bottom": "10%", "containLabel": true},
  "xAxis": {"type": "category", "data": ["2010","2012","2014","2016","2018","2020","2022","2023"]},
  "yAxis": {"type": "value", "name": "TEUs (thousands)"},
  "series": [
    {
      "name": "Vancouver Port",
      "type": "line",
      "smooth": true,
      "symbol": "circle",
      "itemStyle": {"color": "#1e40af"},
      "areaStyle": {"opacity": 0.08},
      "data": [1800, 2100, 2500, 2900, 3100, 2800, 3400, 3300]
    },
    {
      "name": "Prince Rupert",
      "type": "line",
      "smooth": true,
      "symbol": "circle",
      "itemStyle": {"color": "#16a34a"},
      "areaStyle": {"opacity": 0.08},
      "data": [300, 380, 450, 500, 620, 700, 850, 870]
    }
  ]
}'></div>

*Prince Rupert grew by roughly 190% between 2010 and 2023, compared to Vancouver's 83%. The rate of growth reflects Prince Rupert's geographic advantage (2.4 days closer to Shanghai), expanding Fairview container terminal capacity, and CN's direct Chicago rail service. Unlike most ports, Prince Rupert saw minimal throughput decline during COVID, reflecting its position as a preferred alternative when Vancouver congestion peaked.*

---

## 8. Tariff Impact by Corridor

<div data-viz="echarts" style="height:300px" data-options='{
  "title": {"text": "2025 Tariff Impact — Cost Index by Corridor and Commodity", "subtext": "Baseline (pre-tariff) = 100. Higher = greater cost burden from 25% tariff. Auto parts cross border 5–7x during assembly.", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "legend": {"data": ["Without tariff (baseline)", "With 25% tariff"], "bottom": 0},
  "grid": {"left": "3%", "right": "4%", "bottom": "14%", "containLabel": true},
  "xAxis": {"type": "category", "data": ["Auto parts\n(Windsor)", "Agri exports\n(Pacific/Atlantic)", "Steel/Aluminum\n(Multiple)", "Consumer goods\n(Pacific)"]},
  "yAxis": {"type": "value", "name": "Cost index (baseline=100)", "min": 0, "max": 200},
  "series": [
    {
      "name": "Without tariff (baseline)",
      "type": "bar",
      "itemStyle": {"color": "#2563eb"},
      "label": {"show": true, "position": "top"},
      "data": [100, 100, 100, 100]
    },
    {
      "name": "With 25% tariff",
      "type": "bar",
      "itemStyle": {"color": "#dc2626"},
      "label": {"show": true, "position": "top"},
      "data": [175, 105, 125, 115]
    }
  ]
}'></div>

*Auto parts face by far the largest tariff burden because supply chains are structured around multiple border crossings per component. Each crossing incurs the 25% levy, compounding the effective cost. Agricultural exports to non-US markets are largely unaffected (indexed to 105, reflecting minor routing cost changes). Steel and aluminum face a direct 25% tariff, reflected in the 125 index.*

---

## 9. What the Corridor Analysis Tells Us

The three-corridor structure of Canadian freight geography has a central
implication: the system is geographically concentrated in ways that create
specific vulnerabilities. The Pacific Gateway is constrained by mountain terrain.
The Atlantic corridor is constrained by distance from interior origin points.
And the mid-continent corridor is constrained, above all, by the Windsor-Detroit
crossing — a privately-owned bridge across a narrow river that carries a quarter
of all Canada-US trade by value.

Wardrop's user equilibrium framework explains why freight concentrates at
Windsor-Detroit even though it creates vulnerability. Shippers routing freight
from Ontario to the US Midwest face a choice: the Ambassador Bridge at
Windsor, or longer routes through Sarnia or Niagara. The Ambassador Bridge
route has lower generalised cost for most Ontario-to-US-Midwest trips. In
equilibrium, freight concentrates on the lower-cost route. The result is an
economically rational outcome that creates a single-point structural risk —
precisely the kind of outcome that infrastructure policy needs to address through
investment in capacity at alternative crossings, not through attempts to override
market-driven routing.

The Gordie Howe International Bridge addresses exactly this: it does not
try to redirect freight away from Windsor, it adds capacity at Windsor so that
the corridor's structural advantage can be realised without single-bridge
vulnerability. The CAD$5.7 billion cost, spread over a corridor that carries
CAD$146 billion per year in trade, represents an infrastructure investment cost
of approximately 3.9% of annual corridor value — a straightforward case for
public investment in strategic infrastructure.

---

*Next in this cluster: [T3 — Port Economics](/canada-port-economics/)*
