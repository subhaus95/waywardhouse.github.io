---
layout: model
title: "Modal Split and Freight Economics"
subtitle: "Why Freight Moves by Truck, Rail, or Ship — and What Changes When It Doesn't"
series: "Economic Systems"
series_order: 9
cluster: "TR — Trade and Transport"
date: 2026-03-09
image: /assets/images/trade-corridors.png
categories: [modelling]
tags:
  - modal-split
  - freight
  - rail
  - trucking
  - marine
  - canada
  - cn-cp-duopoly
  - logistics
  - transport-economics
difficulty: 3
math: true
viz: true
math_core: ["Total logistics cost", "break-even distance", "logit modal choice", "inventory in transit"]
description: >
  A quantitative treatment of freight modal choice — the cost functions
  governing truck, rail, and marine transport, the break-even distances at which
  mode switches occur, and what the 2025 US tariff regime implies for modal
  split across Canadian trade flows.
excerpt: >
  A shipper choosing how to move a tonne of goods from Calgary to Toronto faces
  a decision that is not simply about price per kilometre. It involves transit
  time, reliability, handling risk, minimum shipment size, frequency of service,
  and the cost of inventory sitting in motion. Modal split — the aggregate
  outcome of millions of such decisions — shapes the geography of freight
  infrastructure demand in ways that are predictable from cost functions.
toc: true
---

## 1. The Question

How does freight choose between truck, rail, and ship? And what does that
choice imply for infrastructure demand, commodity pricing, and the distributional
effects of trade disruption?

These are empirical questions with quantitative answers. Freight does not move
randomly; it moves according to cost. Each mode of transport has a characteristic
cost structure — a fixed component that is paid regardless of distance, and a
variable component that scales with distance. The mode with the lowest total cost
at any given distance wins the freight. The distance at which two modes have
equal total cost is the break-even distance, and it is one of the most important
parameters in freight transport planning.

The aggregate outcome of millions of individual shipper decisions — each choosing
the minimum-cost mode for their specific origin, destination, commodity, and
service requirements — is the modal split: the share of total freight (measured
in tonne-kilometres) carried by each mode. For Canada in 2023, that split is
approximately 44% rail, 37% truck, 12% pipeline, 6% marine, and 1% air.
Understanding why produces insight not just into freight economics but into
the geography of infrastructure investment, the competitive position of
Canadian commodity exporters, and the distributional effects of trade policy.

---

## 2. Cost Functions by Mode

### Truck: high variable, low terminal

Long-haul truckload (TL) transport in Canada costs approximately CAD$0.12 to
$0.18 per tonne-kilometre for full-truckload moves. The cost structure is
dominated by driver wages, fuel, and insurance — all of which scale with distance.
Terminal costs (loading, unloading, staging) are relatively low for truckload
moves, typically CAD$40 to $70 per truckload at each end of the journey.

Trucking's competitive advantages are service frequency (a truck can move as
soon as it is loaded, without waiting for a train assembly schedule), flexibility
in origin and destination (a truck can go anywhere there is a road, with no
terminal requirement), and reliability of transit time (absent congestion, truck
transit times are highly predictable). Its disadvantage is per-unit cost at
long distances: the high variable cost per tonne-kilometre makes truck
uncompetitive with rail beyond a threshold distance for most commodity classes.

### Rail: low variable, high terminal

Rail freight costs approximately CAD$0.03 to $0.05 per tonne-kilometre for bulk
carload traffic, and CAD$0.05 to $0.08 per tonne-kilometre for intermodal
containers. The cost structure is the inverse of trucking: variable costs are
low (rail is highly energy-efficient, with a typical locomotive hauling 400-500
truckload equivalents at a fraction of the fuel cost per tonne-kilometre), but
terminal costs are substantial. Loading a bulk commodity into a rail car at
origin, moving the car to the yard, assembling the train, and then unloading
at destination involves several days of terminal handling and costs
CAD$80 to $120 per carload at each end.

Rail's competitive advantages are cost efficiency at long distances and high
volume, making it the natural mode for Prairie grain, potash, coal, and forest
products moving thousands of kilometres to export terminals. Its disadvantages
are transit time (days longer than truck for equivalent distances), service
frequency (trains operate on fixed schedules, not on demand), and the origin
and destination requirements (freight must reach the railhead and be moved from
the destination railhead, adding dray costs for non-rail-served origins and
destinations).

### Marine: minimal variable, high terminal

Marine transport on the Great Lakes and coastal routes costs approximately
CAD$0.01 to $0.03 per tonne-kilometre — the lowest variable cost of any surface
mode. A bulk vessel operating on the Great Lakes can move several thousand tonnes
at extraordinary fuel efficiency. The catch is terminal cost and time: loading
a bulk vessel, moving it through the Seaway locks, and discharging at destination
involves several days of transit and substantial port handling costs, regardless
of the distance travelled.

Marine transport is competitive only for high-volume, low-time-sensitivity,
water-adjacent origins and destinations. Grain from Thunder Bay to eastern
Canadian or US Great Lakes ports is the archetypical application. Consumer goods
or manufacturing components, where transit time and frequency of service matter,
are almost never moved by marine on domestic routes.

### Air and pipeline

Air freight costs approximately CAD$2.50 to $5.00 per tonne-kilometre —
two to three orders of magnitude above rail. It is viable only for very high
value-to-weight goods (pharmaceuticals, electronics, luxury goods) where the
time saving justifies the cost premium.

Pipeline transport is not included in the standard modal split statistics
for goods trade, but it accounts for approximately 12% of Canadian freight
by tonne-kilometre when energy commodities are included. Pipeline variable costs
are extremely low (pumping energy only), with high fixed costs (construction and
maintenance of the pipe). For large-volume, continuous flows of homogeneous
liquids or gases over long distances, pipeline is essentially unrivalled in cost
efficiency.

---

## 3. Total Logistics Cost

### Beyond the freight rate

The freight rate per tonne-kilometre is only one component of the true cost of
moving goods. The full framework is total logistics cost (TLC), which includes:

$$TLC = \text{freight rate} \times \text{distance} + \text{terminal handling cost} + \text{inventory in transit cost}$$

The inventory in transit (IIT) component is often overlooked but can be decisive
for high-value goods. While a shipment is in motion, the shipper is effectively
holding inventory — capital tied up in goods that cannot yet be sold. The cost
of that tied-up capital is:

$$IIT = \frac{\text{commodity value} \times \text{annual interest rate} \times \text{transit days}}{365}$$

### Two worked examples

Consider a tonne of electronics valued at CAD$50,000, moving from Calgary to
Toronto — a distance of approximately 3,400 kilometres — at an annual interest
rate of 8%.

- **By truck** (2-day transit): $IIT = \$50,000 \times 0.08 \times 2 / 365 = \$21.92$/tonne
- **By rail** (4-day transit): $IIT = \$50,000 \times 0.08 \times 4 / 365 = \$43.84$/tonne
- **IIT difference**: CAD$21.92 per tonne in favour of truck.

But the freight rate difference is much larger. At $0.14/tonne-km by truck and
$0.065/tonne-km by rail over 3,400 km:

- **Truck freight rate**: $0.14 \times 3400 = \$476$/tonne
- **Rail freight rate**: $0.065 \times 3400 = \$221$/tonne
- **Freight rate difference**: CAD$255 per tonne in favour of rail.

Net of IIT, rail wins by approximately CAD$233 per tonne. Even for moderately
valuable electronics, rail is clearly cheaper for transcontinental distances.

Now consider a tonne of fresh produce valued at CAD$2,000, with the same
route and interest rate:

- **Truck IIT**: $\$2,000 \times 0.08 \times 2 / 365 = \$0.88$/tonne
- **Rail IIT**: $\$2,000 \times 0.08 \times 4 / 365 = \$1.75$/tonne
- **IIT difference**: CAD$0.87 per tonne — essentially negligible.

For perishables, transit time and reliability matter for quality reasons, not
capital cost reasons. Rail's 4-day transit creates spoilage risk, not financial
cost. This is why fresh produce moves predominantly by refrigerated truck even
at distances where rail would win on pure freight rate economics: reliability
of transit time and the absence of handling transfers during transit are worth
the freight rate premium.

---

## 4. Cost Comparison by Mode

<div data-viz="echarts" style="height:360px" data-options='{
  "title": {"text": "Freight Cost by Mode — CAD$/Tonne-Kilometre", "subtext": "Log scale. Typical long-haul rates; excludes terminal costs. Pipeline included for comparison.", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}, "formatter": "{b}: CAD${c}/tonne-km"},
  "grid": {"left": "3%", "right": "4%", "bottom": "8%", "containLabel": true},
  "xAxis": {"type": "category", "axisLabel": {"interval": 0, "fontSize": 11}, "data": ["Air", "Truck\n(short-haul)", "Truck\n(long-haul TL)", "Rail\n(intermodal)", "Rail\n(bulk)", "Marine\n(coastal)", "Marine\n(ocean)"]},
  "yAxis": {"type": "log", "name": "CAD$/tonne-km (log scale)", "min": 0.001},
  "series": [{
    "type": "bar",
    "label": {"show": true, "position": "top", "formatter": "{c}"},
    "data": [
      {"value": 3.50, "itemStyle": {"color": "#dc2626"}},
      {"value": 0.18, "itemStyle": {"color": "#f87171"}},
      {"value": 0.13, "itemStyle": {"color": "#fca5a5"}},
      {"value": 0.07, "itemStyle": {"color": "#60a5fa"}},
      {"value": 0.04, "itemStyle": {"color": "#2563eb"}},
      {"value": 0.02, "itemStyle": {"color": "#16a34a"}},
      {"value": 0.006,"itemStyle": {"color": "#15803d"}}
    ]
  }]
}'></div>

*Air freight is three orders of magnitude more expensive than ocean marine. Rail bulk at CAD$0.04/tonne-km is roughly 3x more expensive than coastal marine, but rail can reach inland origins and destinations where marine cannot. The log scale is necessary to display this range.*

---

## 5. Break-Even Distance Analysis

<div data-viz="echarts" style="height:380px" data-options='{
  "title": {"text": "Total Logistics Cost vs Distance — Mode Comparison", "subtext": "Includes terminal handling costs. Truck base = CAD$50 terminal; Rail = CAD$80 terminal; Marine = CAD$120 terminal.", "left": "center"},
  "tooltip": {"trigger": "axis"},
  "legend": {"data": ["Truck (TL)", "Rail (intermodal)", "Marine"], "bottom": 0},
  "grid": {"left": "3%", "right": "4%", "bottom": "12%", "containLabel": true},
  "xAxis": {"type": "value", "name": "Distance (km)", "min": 0, "max": 3000},
  "yAxis": {"type": "value", "name": "Total logistics cost (CAD$/tonne)", "min": 0, "max": 500},
  "series": [
    {
      "name": "Truck (TL)",
      "type": "line",
      "smooth": false,
      "symbol": "none",
      "itemStyle": {"color": "#dc2626"},
      "lineStyle": {"width": 3},
      "data": [[0,50],[200,78],[500,120],[800,162],[1000,190],[1500,260],[2000,330],[3000,470]],
      "markPoint": {
        "symbol": "pin",
        "data": [{"name": "Break-even truck/rail", "coord": [700, 125]}],
        "itemStyle": {"color": "#7c3aed"},
        "label": {"formatter": "Break-even\n~700 km"}
      }
    },
    {
      "name": "Rail (intermodal)",
      "type": "line",
      "smooth": false,
      "symbol": "none",
      "itemStyle": {"color": "#2563eb"},
      "lineStyle": {"width": 3},
      "data": [[0,80],[200,93],[500,112.5],[800,132],[1000,145],[1500,177.5],[2000,210],[3000,275]],
      "markPoint": {
        "symbol": "pin",
        "data": [{"name": "Break-even rail/marine", "coord": [1700, 154]}],
        "itemStyle": {"color": "#d97706"},
        "label": {"formatter": "Break-even\n~1700 km"}
      }
    },
    {
      "name": "Marine",
      "type": "line",
      "smooth": false,
      "symbol": "none",
      "itemStyle": {"color": "#16a34a"},
      "lineStyle": {"width": 3},
      "data": [[0,120],[500,130],[1000,140],[1500,150],[2000,160],[3000,180]]
    }
  ]
}'></div>

*The cross-over points are the break-even distances. Below ~700 km, truck's lower terminal cost outweighs its higher variable rate; above ~700 km, rail's lower variable rate wins. Marine only becomes competitive beyond ~1,700 km for non-time-sensitive goods with water-adjacent origins and destinations.*

---

## 6. The CN/CP Duopoly

Canada's rail freight system is operated by two national carriers: Canadian
National (CN) and Canadian Pacific Kansas City (CPKC, formed by the 2023 merger
of CP and Kansas City Southern). Together they carry approximately 95% of
Canadian rail freight by tonne-kilometre. The remaining 5% is carried by
regional and short-line operators, typically over short distances for local
industrial traffic.

The geographic division between CN and CP is not absolute, but it is
significant. CN's network is denser in eastern Canada and the western prairies,
with its main transcontinental line running north of Superior; CP's runs south.
Both serve the Prairie grain export market, providing the only real parallel
competition for bulk commodity shippers, and both serve major Pacific Gateway
port terminals at Vancouver and (CN only) Prince Rupert.

For many shipper-destination combinations, however, there is effectively only
one carrier option. A shipper in a small Prairie community served by only one
railway has no practical alternative — the cost of trucking to the competing
railway's nearest facility typically exceeds any freight rate savings. These
"captive shipper" situations are the structural condition that allows both
carriers to charge above-competitive rates on specific lanes: the Canadian
Transportation Agency has estimated that CN and CP charge roughly 20% to 40%
above their estimated long-run marginal costs on captive segments, including
much of the Prairie grain and potash export market.

The CPKC merger, which created the first single-line rail connection between
Canada, the United States, and Mexico, was approved by Canadian and US
regulators in 2023 with conditions designed to maintain competitive access for
shippers. The competitive implications are still unfolding: for some shippers,
the single-line service to Mexican markets is valuable; for captive Prairie
shippers, the merger's primary effect may be reduced competitive pressure
as the two national carriers no longer contest each other's captive lanes.

---

## 7. Canadian Freight Modal Split

<div data-viz="echarts" style="height:300px" data-options='{
  "title": {"text": "Canadian Freight by Mode — Tonne-Kilometre Share (2023)", "subtext": "Includes all domestic and international freight originating or terminating in Canada.", "left": "center"},
  "tooltip": {"trigger": "item", "formatter": "{b}: {c}% ({d}%)"},
  "legend": {"orient": "vertical", "right": 10, "top": "center"},
  "series": [{
    "type": "pie",
    "radius": ["42%", "68%"],
    "center": ["38%", "55%"],
    "label": {"formatter": "{b}\n{d}%"},
    "data": [
      {"value": 44, "name": "Rail",      "itemStyle": {"color": "#2563eb"}},
      {"value": 37, "name": "Truck",     "itemStyle": {"color": "#dc2626"}},
      {"value": 12, "name": "Pipeline",  "itemStyle": {"color": "#f59e0b"}},
      {"value": 6,  "name": "Marine",    "itemStyle": {"color": "#16a34a"}},
      {"value": 1,  "name": "Air",       "itemStyle": {"color": "#6b7280"}}
    ]
  }]
}'></div>

*Rail dominates by tonne-kilometre because it handles the enormous bulk volumes of Prairie grain, potash, coal, and forest products over transcontinental distances. Truck dominates by shipment count (not shown) because short-haul, small-shipment, and high-frequency freight moves by truck regardless of commodity.*

---

## 8. Tariff Impact on Modal Mix

The 2025 US tariffs affect modal split through two mechanisms: volume effects
and routing effects. Volume effects reduce total freight demand on all modes as
bilateral trade falls in response to higher costs. Routing effects shift the
geographic distribution of flows — some previously US-bound shipments are
redirected to domestic consumption or non-US export markets, changing which
corridors carry them and which modes are optimal.

The automotive sector illustrates the volume effect most starkly. Windsor-Detroit
corridor trucking is overwhelmingly automotive: parts, assemblies, and finished
vehicles crossing in both directions. As 25% tariffs make cross-border automotive
supply chains economically unviable for some producers, production volumes fall
or shift to US-only supply chains, reducing the freight demand that previously
moved by truck through Windsor. The modal mix within the automotive corridor
does not change much (trucks still carry automotive parts); the volume simply
falls.

Bulk commodities — Prairie grain, potash, lumber — face different dynamics.
Their primary US markets may shift to other destinations (Asia, Europe) as
US tariffs make some Canadian exporters uncompetitive in US markets. The
routing shift increases demand for Pacific Gateway rail (CN/CP to Vancouver
and Prince Rupert for Asian markets) while reducing demand for the truck-heavy
US-border movements that historically served US domestic grain, lumber, and
potash customers.

<div data-viz="echarts" style="height:340px" data-options='{
  "title": {"text": "Modal Split Shift Under 2025 Tariff Scenario", "subtext": "Truck percentage of mode mix by commodity. Volume reduction not shown — only modal share within remaining flows.", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "legend": {"data": ["2024 (% by truck)", "2025 estimate (% by truck)"], "bottom": 0},
  "grid": {"left": "3%", "right": "4%", "bottom": "14%", "containLabel": true},
  "xAxis": {"type": "category", "data": ["Automotive\nparts", "Prairie\ngrain", "Potash", "Lumber", "Consumer\ngoods"]},
  "yAxis": {"type": "value", "name": "% of freight volume by truck", "max": 100},
  "series": [
    {
      "name": "2024 (% by truck)",
      "type": "bar",
      "itemStyle": {"color": "#2563eb"},
      "label": {"show": true, "position": "top", "formatter": "{c}%"},
      "data": [85, 15, 5, 40, 55]
    },
    {
      "name": "2025 estimate (% by truck)",
      "type": "bar",
      "itemStyle": {"color": "#dc2626"},
      "label": {"show": true, "position": "top", "formatter": "{c}%"},
      "data": [60, 15, 5, 35, 50]
    }
  ]
}'></div>

*Automotive parts show the largest modal share shift: as US-bound automotive trade collapses under tariff pressure, some remaining flows re-route via rail to alternative assembly locations. Grain and potash show minimal change because they are already rail-dominated and their US market exposure is lower relative to total production volume.*

---

## 9. What the Modal Choice Analysis Tells Us

The break-even distance framework and the total logistics cost model together
provide a rigorous basis for understanding freight mode choice that goes
substantially beyond the intuition that "trucks are flexible, trains are cheap,
ships are slow." Each mode has a specific cost structure — terminal plus variable
— and the competitive boundary between modes shifts predictably with distance,
commodity value, and time sensitivity.

For Canadian freight policy, the most important implications are three. First,
the CN/CP duopoly creates real pricing power over captive shippers on specific
lanes, particularly for Prairie bulk commodities. This is not a theoretical
concern; it is documented in regulatory proceedings and shipper testimony to the
Canadian Transportation Agency. Policies that increase effective rail competition
— whether through competitive access rules, final-offer arbitration reform, or
revenue cap adjustments — have direct and quantifiable effects on the prices
Prairie producers receive for their commodities.

Second, the modal split is not a fixed characteristic of the freight system.
It responds to relative prices, infrastructure investments, and trade policy
changes in ways that are predictable from the cost functions. An infrastructure
investment that reduces rail terminal costs in a specific location shifts the
break-even distance and expands rail's competitive range. A tariff that reduces
cross-border automotive trade reduces Windsor-Detroit trucking demand without
necessarily affecting Prairie rail demand.

Third, the inventory in transit calculation shows that time sensitivity is
not simply a preference — it is a cost that can be calculated precisely for
any commodity with a known value. This has implications for trade policy analysis:
the cost of a 2-day border delay is not a vague "uncertainty cost" but a
specific dollar amount per tonne per day, calculable from commodity value and
the cost of capital.

---

*Next in this cluster: [T5 — The Integrated Trade Network](/2026/03/09/canada-integrated-trade-network/)*
