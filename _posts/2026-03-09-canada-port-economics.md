---
layout: model
title: "Port Economics"
subtitle: "Throughput, Hinterland, and the Geography of Canada's Gateway Competition"
series: "Economic Systems"
series_order: 8
cluster: "TR — Trade and Transport"
date: 2026-03-09
image: /assets/images/trade-corridors.png
categories: [modelling]
tags:
  - ports
  - canada
  - vancouver
  - prince-rupert
  - montreal
  - halifax
  - container-shipping
  - throughput
  - economic-geography
difficulty: 3
math: true
viz: true
leaflet: true
math_core: ["Throughput functions", "queuing theory", "inventory in transit", "hinterland capture"]
description: >
  A quantitative account of Canadian port economics — how throughput is
  measured and produced, how queuing theory explains congestion, how
  hinterland geography determines port competition, and why Prince Rupert's
  geographic advantage translates into economic advantage at certain distances.
excerpt: >
  A port is a node with two sets of edges: maritime connections to global
  shipping lanes, and landside connections to the domestic hinterland. Its
  competitive position depends on both. Canada's four major ports — Vancouver,
  Montreal, Prince Rupert, and Halifax — occupy different positions in this
  geography, and the competition between them for hinterland capture is
  reshaping Canadian freight flows.
toc: true
---

## 1. The Question

What determines how much traffic a port captures, and from which geographic
hinterland? Why is Prince Rupert — a small city of 12,000 people on the
northern British Columbia coast — one of the fastest-growing container ports
in North America? And why do shippers in Saskatchewan sometimes choose
Vancouver over Montreal for routing goods to European markets, even though
Montreal is geographically closer?

These questions belong to the economics of port competition, which is a
branch of transport economics with a specific mathematical structure. Ports
compete not on price alone — container handling rates are relatively transparent
and competitive — but on the total generalised cost of moving a container from
its origin to its destination, including the maritime leg, port handling time,
and the landside rail or road movement to or from the interior. The port that
minimises total generalised cost for a given origin-destination pair wins that
flow. The geographic locus of shippers indifferent between two competing ports
— where the total costs are exactly equal — is the port's competitive boundary,
and the region inside that boundary is its hinterland.

---

## 2. Canada's Port Hierarchy

Canada's container port system is organised around four major gateways, each
serving a distinct geographic catchment and connected to different maritime
trade lanes.

### Vancouver: Roberts Bank, Centerm, Vanterm

Vancouver handled approximately 3.3 million TEUs in 2023, making it by far
Canada's largest container port. The port complex is actually three separate
terminals on the southern British Columbia coast: the Roberts Bank terminal
complex (including the Deltaport and Westshore bulk terminals), Centerm, and
Vanterm. Together they handle Asian trade dominated by consumer electronics,
manufactured goods, vehicles, and machinery inbound, and Prairie grain, potash,
coal, lumber, and other bulk and break-bulk commodities outbound.

Vancouver's landside connectivity is provided by both CN and CP, giving it
the competitive advantage of rail network redundancy that Prince Rupert lacks.
Two competing railways create pricing competition on the landside leg, and two
networks provide routing alternatives when one is disrupted. Vancouver's
disadvantage is its geography: it sits at the southern end of a coastal mountain
corridor that constrains rail capacity and creates bottlenecks when volume peaks.
It is also further from Shanghai and other major Asian ports than Prince Rupert —
a disadvantage that compounds with container shipping rates on longer voyages.

### Prince Rupert: Fairview Container Terminal

Prince Rupert handled 870,000 TEUs in 2023, and the trajectory is steeply upward.
The Fairview Container Terminal opened in 2007 with initial capacity of 500,000
TEUs and has been expanded several times. A Phase 2 expansion approved in 2023
will bring capacity to approximately 1.8 million TEUs when complete.

The economic case for Prince Rupert rests on a specific arithmetic. The port
is 2.4 sailing days closer to Shanghai than Vancouver. On a containership with
an operating cost of approximately USD$1,800 per day, 2.4 days of sailing equals
USD$4,320 saved per voyage. A Panamax vessel carrying approximately 4,000 TEUs
would yield a per-TEU maritime cost advantage of roughly USD$1.08 — or
approximately CAD$1.50 at typical exchange rates. For certain commodity flows
where time value is not paramount, this maritime cost advantage more than offsets
Prince Rupert's slightly longer landside rail transit to major inland destinations.

CN's direct rail connection from Prince Rupert to Chicago runs approximately
4.5 days compared to 4 days from Vancouver — a 0.5-day landside disadvantage
that partially but not completely offsets the 2.4-day maritime advantage. For
most Pacific container flows, Prince Rupert's net total-cost advantage is
positive and growing as terminal capacity expands and CN's service frequency
increases.

### Montreal: Inland Port on the St. Lawrence

Montreal handled 1.57 million TEUs in 2023, making it Canada's second-largest
container port. Its distinctive characteristic is its inland location — the
port sits at kilometre 1,600 of the St. Lawrence Seaway, approximately 1,600
kilometres from open ocean. Deep-draught ocean vessels can reach Montreal
directly, making it a true inland ocean port.

Montreal serves Ontario and Quebec for European trade, and provides a
competitive alternative to Halifax for Atlantic Canada shippers. Its rail
connections run westward to Toronto and beyond via both CN and CP, and
the port's proximity to the Ontario manufacturing base — considerably closer
than Halifax — gives it a landside cost advantage for central Canadian origins
and destinations.

### Halifax: Atlantic Gateway and European Proximity

Halifax handled 535,000 TEUs in 2023 from two terminals: Halterm and
Fairview Cove. Halifax's competitive advantage is proximity to Europe:
it is approximately 2 days closer to northern European ports than Montreal,
and many days closer than Pacific Gateway ports. For Atlantic Canadian
shippers sending goods to Europe, Halifax is the obvious choice. For Ontario
and Prairie shippers, the calculus is more complex: the shorter maritime leg
to Europe must be weighed against the longer landside rail movement from
interior origins to Halifax.

---

## 3. Throughput Economics

### Berth productivity

The fundamental metric of port productivity is the number of container moves
per crane-hour. A container move is the loading or unloading of one TEU from
a vessel. World-class productivity at major Asian ports (Busan, Shanghai,
Singapore) runs at 35 to 40 moves per crane-hour. North American ports
typically operate at lower rates, partly due to labour agreements, partly due
to older equipment, and partly due to different vessel size mixes.

Vancouver averages approximately 28 moves per crane-hour across its terminals.
Prince Rupert's Fairview terminal, with newer equipment and a more streamlined
labour agreement, achieves approximately 32. The difference may sound small,
but at scale it is significant: at 28 vs 32 moves per crane-hour, across
multiple cranes operating around the clock, the productivity differential
translates into meaningful differences in vessel turnaround time and annual
throughput capacity.

### The throughput function

Port throughput capacity — the maximum number of TEUs a port can handle in
a year — is determined by the product of several factors:

$$T_{max} = n_{berths} \times n_{cranes} \times m_{ph} \times h_{op}$$

where $n_{berths}$ is the number of berths capable of handling container
vessels, $n_{cranes}$ is the number of ship-to-shore cranes per berth (typically
2-4), $m_{ph}$ is the moves per crane-hour, and $h_{op}$ is the annual operating
hours (typically around 7,000-8,000 for a round-the-clock operation with
maintenance downtime). Container dwell time — the average time a container
spends in the port between vessel unloading and landside pickup — also affects
effective throughput: high dwell reduces yard space available for incoming
containers and constrains overall throughput below the theoretical maximum.

---

## 4. Queuing Theory and Port Congestion

### The M/M/1 model applied to ports

Ship arrivals at a port can be modelled as a Poisson process with rate $\lambda$
(ships per day), where the Poisson assumption captures the random, approximately
memoryless nature of vessel arrivals under typical operating conditions. Vessel
service (berth occupancy time) follows an approximately exponential distribution
with rate $\mu$ (vessels processed per day per berth). The single-server
M/M/1 queuing model — or its multi-server M/M/c extension for ports with
multiple berths — provides the foundational analytics.

The key quantity is the server utilisation:

$$\rho = \frac{\lambda}{\mu}$$

When $\rho < 1$, the port can handle the incoming vessel traffic on average and
the queue remains bounded. The expected waiting time in the queue before
entering service is:

$$W_q = \frac{\rho}{\mu(1 - \rho)}$$

This expression has a crucial property: as $\rho \to 1$, $W_q \to \infty$.
Congestion grows explosively as utilisation approaches 100%. A port running at
80% utilisation has manageable queues; the same port running at 90% has queues
roughly twice as long; at 95%, roughly five times as long. The non-linearity
of queuing congestion is why ports invest in capacity well before they appear
to be "full" — and why the supply chain crisis of 2021-22 was so severe when
it hit.

### The Vancouver 2021-22 crisis

During the 2021-22 global supply chain disruption, the Port of Vancouver
experienced a utilisation rate approaching $\rho \approx 0.92$ — close
enough to saturation that the queuing formula predicts severe congestion.
Average vessel waiting time before berth access rose from the normal 1-2 days
to 8-12 days. Container dwell times in the port yard extended from a normal
4-5 days to 12-15 days, further reducing effective throughput and creating
a feedback loop: high dwell used yard space, reducing crane productivity,
increasing vessel wait times, which further delayed container pickup.

The crisis illustrated both the non-linearity of queuing congestion and
the systemic nature of port bottlenecks. The proximate cause was a surge
in import demand following pandemic restrictions. But the structural cause
was that Pacific Gateway infrastructure had been running at high utilisation
for several years, with limited buffer capacity. Prince Rupert, with lower
initial utilisation and newer facilities, experienced considerably less
disruption than Vancouver during the same period — a demonstration that
geographic redundancy in port infrastructure has measurable economic value
when the primary gateway becomes saturated.

---

## 5. Port Throughput: Historical Trends

<div data-viz="echarts" style="height:340px" data-options='{
  "title": {"text": "Pacific Gateway: Prince Rupert vs Vancouver TEU Throughput", "subtext": "TEUs (thousands). Grey band = COVID supply chain disruption period.", "left": "center"},
  "tooltip": {"trigger": "axis"},
  "legend": {"data": ["Vancouver", "Prince Rupert"], "bottom": 0},
  "grid": {"left": "3%", "right": "4%", "bottom": "10%", "containLabel": true},
  "xAxis": {"type": "category", "data": ["2010","2012","2014","2016","2018","2019","2020","2021","2022","2023"]},
  "yAxis": {"type": "value", "name": "TEUs (thousands)"},
  "series": [
    {
      "name": "Vancouver",
      "type": "line",
      "smooth": true,
      "symbol": "circle",
      "itemStyle": {"color": "#1e40af"},
      "areaStyle": {"opacity": 0.06},
      "data": [2000, 2200, 2500, 2900, 3100, 3100, 2800, 3400, 3500, 3300],
      "markArea": {
        "itemStyle": {"color": "rgba(156,163,175,0.15)"},
        "data": [[{"xAxis": "2020"}, {"xAxis": "2021"}]],
        "label": {"show": true, "position": "insideTop", "color": "#6b7280", "formatter": "COVID disruption"}
      }
    },
    {
      "name": "Prince Rupert",
      "type": "line",
      "smooth": true,
      "symbol": "circle",
      "itemStyle": {"color": "#16a34a"},
      "areaStyle": {"opacity": 0.06},
      "data": [300, 380, 450, 500, 620, 680, 700, 820, 860, 870]
    }
  ]
}'></div>

*Prince Rupert grew nearly 190% from 2010 to 2023, compared to Vancouver's 65%. Unlike Vancouver, Prince Rupert saw minimal throughput decline during COVID, partly because its lower pre-crisis utilisation left more buffer capacity.*

---

## 6. Port Hinterland Geography

<div data-leaflet id="port-hinterland-map" style="height:400px" data-lat="50" data-lng="-95" data-zoom="3" data-tiles="carto" data-markers='[{"lat":49.28,"lng":-123.12,"label":"Vancouver — 3.3M TEU 2023"},{"lat":54.31,"lng":-130.32,"label":"Prince Rupert — 870K TEU, fastest-growing"},{"lat":45.50,"lng":-73.57,"label":"Montreal — 1.57M TEU, inland port"},{"lat":44.64,"lng":-63.57,"label":"Halifax — 535K TEU, Atlantic gateway"},{"lat":41.85,"lng":-87.65,"label":"Chicago — key inland destination"},{"lat":49.90,"lng":-97.14,"label":"Winnipeg — Prairie freight hub"},{"lat":53.55,"lng":-113.49,"label":"Edmonton — Prairie origin"}]'></div>

*The geographic logic of hinterland competition: Vancouver and Prince Rupert compete for Prairie and Ontario freight to Asia; Montreal and Halifax compete for eastern Canadian freight to Europe. The hinterland boundary between Pacific and Atlantic gateways for grain exports from Saskatchewan shifts depending on the relative cost of CN rail to the two coasts.*

---

## 7. Asia-Pacific Transit Time to Chicago

<div data-viz="echarts" style="height:300px" data-options='{
  "title": {"text": "Asia-Pacific Shipping + Inland Rail to Chicago", "subtext": "Days by route. Prince Rupert ocean advantage partially offset by longer inland distance.", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}, "formatter": "function(params){var total=0;params.forEach(function(p){total+=p.value});return params[0].name+\"<br/>Total: \"+total+\" days\";}"},
  "legend": {"data": ["Ocean transit (days)", "Inland rail (days)"], "bottom": 0},
  "grid": {"left": "4%", "right": "8%", "bottom": "12%", "containLabel": true},
  "xAxis": {"type": "value", "name": "Days", "max": 22},
  "yAxis": {"type": "category", "data": ["LA / Long Beach\n→ Chicago", "Vancouver\n→ Chicago", "Prince Rupert\n→ Chicago"]},
  "series": [
    {
      "name": "Ocean transit (days)",
      "type": "bar",
      "stack": "total",
      "itemStyle": {"color": "#1e40af"},
      "label": {"show": true, "position": "inside", "formatter": "{c}d ocean"},
      "data": [14, 12, 10]
    },
    {
      "name": "Inland rail (days)",
      "type": "bar",
      "stack": "total",
      "itemStyle": {"color": "#16a34a"},
      "label": {"show": true, "position": "inside", "formatter": "{c}d rail"},
      "data": [4, 4, 4.5]
    }
  ]
}'></div>

*Prince Rupert's 2-day ocean advantage over Vancouver is partially offset by its 0.5-day longer inland rail to Chicago. Net advantage to Prince Rupert: approximately 1.5 days total, with an additional maritime cost saving from fewer vessel operating days.*

---

## 8. The Hinterland Competition Model

The hinterland boundary between two competing ports $A$ and $B$ is the set of
origin points where the total generalised cost of routing through port $A$
equals the total generalised cost of routing through port $B$:

$$C_A(o) = C_B(o)$$

where $C_A(o)$ is the total cost (maritime + port handling + landside transport)
for a shipper at origin $o$ routing through port $A$. The boundary is a
curve in geographic space; all origins on one side prefer port $A$, all
origins on the other prefer port $B$.

For Vancouver vs Prince Rupert, the boundary for Asia-Pacific container flows
sits somewhere in the Canadian prairies, shifting east as Prince Rupert's
capacity expands and CN's service frequency improves. As the boundary moves
east, Prince Rupert captures more Prairie origins that previously defaulted to
Vancouver. This is the commercial geography of port competition: not a sudden
shift but a gradual boundary migration driven by infrastructure investment and
service quality improvement.

The hinterland concept also explains why port infrastructure investment is
strategic: a new terminal or improved rail service at port $A$ shifts the
boundary in port $A$'s favour, capturing hinterland from port $B$ and generating
revenue to justify the investment. Port competition is, in this sense, a
geographic game played with infrastructure as the primary instrument.

---

*Next in this cluster: [T4 — Modal Split and Freight Economics](/canada-freight-modal-split/)*
