---
layout: model
title: "Alberta's Crude Oil Pipeline Network"
subtitle: "A Continental System Built Over Seven Decades"
series: "Economic Systems"
series_order: 1
cluster: "EP — Pipeline Connectivity"
date: 2026-03-08
image: /assets/images/pipeline-geography.png
categories: [modelling]
tags:
  - alberta
  - pipelines
  - crude-oil
  - dilbit
  - enbridge
  - trans-mountain
  - keystone
  - network-analysis
  - flow-rates
difficulty: 3
math: true
viz: true
math_core: ["Volumetric flow rate", "pipe hydraulics", "capacity utilization"]
description: >
  A quantitative geography of Alberta's crude oil pipeline network — tracing
  the actual infrastructure that moves diluted bitumen and synthetic crude from
  the oil sands to refineries across North America. Flow rates, capacity data,
  and network geometry, examined without political framing.
excerpt: >
  Alberta sits at the centre of the largest pipeline network in North America.
  More than 840,000 kilometres of pipeline cross Canadian soil; the crude oil
  subsystem alone carries over 3.5 million barrels per day out of the province.
  This essay maps the infrastructure, derives the hydraulic mathematics, and
  lets the numbers describe a system that public debate rarely examines
  quantitatively.
toc: true
---

## 1. The Question

How connected is Alberta's oil sands to the rest of the world, and what does
the physics of pipeline transport actually look like?

Public discussion of Alberta's pipeline system is loud and recurring. But it
is rarely quantitative. The questions asked in legislatures and op-ed columns —
*are there enough pipelines? are there too many? is Alberta landlocked?* — are
geographic and physical questions dressed in political clothing. They can be
examined with data.

This essay asks the measurable version: what is the actual network, what
volumes move through it, how full is it running, and what does the hydraulics
of moving bitumen across a continent look like mathematically?

We will find a system far larger and more intricate than most public
commentary suggests — one built incrementally over seven decades, connecting
one province's geology to refineries in Wisconsin, Illinois, Texas, and
Washington state.

---

## 2. The Conceptual Model

### What a pipeline network is, geographically

A crude oil pipeline network is a directed graph. Nodes are pump stations,
terminals, tank farms, and refineries. Edges are pipe segments with defined
diameters, lengths, and pressure ratings. Flow is directional — gravity plays a
minor role; pumps do the work.

Alberta's crude pipeline system has a distinctive topology: **one large
source region** (the Athabasca oil sands, centred on Fort McMurray, plus
conventional fields in the Peace River and Lloydminster regions), connected by
**gathering lines** to **main trunk corridors**, which fan out toward markets.

The main trunk corridors follow a predictable continental logic. The Canadian
prairies slope gently eastward. Elevation decreases from roughly 700 m at
Edmonton to 230 m at Winnipeg. This favours eastward flow but does not
eliminate it — pumps provide the pressure regardless of gradient.

The three strategic export directions are:

- **East** — into Ontario, Quebec, and (via Sarnia) the U.S. Great Lakes
  refineries
- **South** — into the U.S. Midwest and Gulf Coast via multiple border
  crossings
- **West** — to the British Columbia coast at Burnaby for tanker export to
  Asia-Pacific markets

Each corridor uses different operators, different product specifications, and
different pricing benchmarks.

### What moves: dilbit and synthetic crude

Alberta's oil sands produce two categories of exportable product:

**Diluted bitumen (dilbit)** — raw bitumen is too viscous to flow in a
pipeline at ambient temperatures. It is blended with a diluent (typically
condensate or synthetic crude) at roughly a 70/30 bitumen-to-diluent ratio by
volume. The resulting mixture flows like a heavy crude oil. Dilbit trades at a
discount to West Texas Intermediate (WTI) because it requires upgrading at the
destination refinery.

**Synthetic crude oil (SCO)** — some producers upgrade bitumen on-site,
running it through hydrocracking and coking units to produce a lighter,
sweeter crude that needs no diluent and commands a smaller discount to WTI.
Upgraders at Fort Saskatchewan, Scotford, and Mildred Lake produce SCO.

The distinction matters for pipeline hydraulics: dilbit is denser and more
viscous than SCO, which affects flow rate calculations and pump requirements.

---

## 3. The Mathematical Model

### Volumetric flow rate

The fundamental unit of pipeline throughput is the **barrel per day (bbl/d)**,
where one barrel equals 158.987 litres. For a pipe of circular cross-section:

$$Q = A \cdot v$$

where:
- $Q$ is volumetric flow rate (m³/s)
- $A = \pi r^2$ is cross-sectional area (m²)
- $v$ is mean fluid velocity (m/s)

For practical pipeline engineering the Darcy-Weisbach equation governs
pressure drop along a pipe segment:

$$\Delta P = f \cdot \frac{L}{D} \cdot \frac{\rho v^2}{2}$$

where:
- $\Delta P$ is pressure drop (Pa)
- $f$ is the Darcy friction factor (dimensionless)
- $L$ is pipe length (m)
- $D$ is pipe internal diameter (m)
- $\rho$ is fluid density (kg/m³)
- $v$ is flow velocity (m/s)

This tells us that pressure drop increases linearly with pipe length, inversely
with diameter, and quadratically with velocity. Doubling velocity quadruples
the pressure drop — which is why larger-diameter pipes are far more efficient
per unit volume.

### Capacity utilization

A pipeline's **nameplate capacity** is the maximum throughput under design
conditions. **Actual throughput** varies with shipper nominations, maintenance
windows, and seasonal demand. The utilization rate is simply:

$$U = \frac{Q_{\text{actual}}}{Q_{\text{nameplate}}} \times 100\%$$

High utilization (>90%) signals a constrained system — shippers cannot always
move what they want, and producers accept price discounts when alternative
routes are unavailable. Low utilization signals either surplus capacity or
reduced production.

### The netback price and why geography matters

The price a producer receives at the wellhead is called the **netback**. It is
the market price at the destination minus all costs of getting there:

$$P_{\text{netback}} = P_{\text{market}} - T - U_{\text{cost}} - Q_{\text{adj}}$$

where:
- $P_{\text{market}}$ is the benchmark price at destination (e.g., WTI at
  Cushing, Oklahoma, in USD/bbl)
- $T$ is pipeline tariff (transport cost, CAD/bbl)
- $U_{\text{cost}}$ is upgrading cost if required at destination (USD/bbl)
- $Q_{\text{adj}}$ is the quality discount for heavy crude (USD/bbl)

This equation shows why pipeline access to multiple markets matters
economically: if only one exit route exists, that route's operator can charge
higher tariffs, and refiners at the destination can widen the quality discount
knowing producers have no alternative. Market access — the number of reachable
price points — is the geographic variable that determines producer revenue.

---

## 4. Worked Example by Hand

### How much crude can Enbridge Line 3 move in a year?

Enbridge Line 3 (replacement) runs from Hardisty, Alberta to Superior,
Wisconsin. Its nameplate capacity is 760,000 bbl/d.

**Step 1 — Convert to annual volume:**

$$V_{\text{annual}} = 760{,}000 \text{ bbl/d} \times 365 \text{ d/yr}$$
$$V_{\text{annual}} = 277{,}400{,}000 \text{ bbl/yr}$$

**Step 2 — Convert to cubic metres:**

$$V_{\text{annual}} = 277.4 \times 10^6 \text{ bbl} \times 0.158987 \text{ m}^3/\text{bbl}$$
$$V_{\text{annual}} \approx 44.1 \times 10^6 \text{ m}^3/\text{yr}$$

That is 44.1 million cubic metres — or roughly 44.1 billion litres — of crude
oil per year through a single pipeline.

**Step 3 — Express in economic terms:**

At a typical WTI price of USD &#36;75/bbl and a heavy crude discount of USD &#36;15/bbl
(Canadian Heavy Differential), the crude moving through Line 3 at full capacity
has a destination market value of:

$$V_{\text{economic}} = 277.4 \times 10^6 \text{ bbl} \times \$(75 - 15)$$
$$V_{\text{economic}} = 277.4 \times 10^6 \times \&#36;60 \approx \&#36;16.6 \text{ billion USD/yr}$$

This is the market value of one pipeline's throughput at one point in time.
Line 3 is the largest single line; Enbridge's Mainline system comprises six
parallel lines.

**Step 4 — Pressure drop over a representative segment:**

For a 914 mm (36-inch) diameter pipe carrying dilbit ($\rho \approx 940$
kg/m³) at 2.0 m/s velocity over 100 km:

$$\Delta P = f \cdot \frac{L}{D} \cdot \frac{\rho v^2}{2}$$

Using a Darcy friction factor $f \approx 0.012$ for turbulent flow in a
large-diameter pipe:

$$\Delta P = 0.012 \times \frac{100{,}000}{0.914} \times \frac{940 \times 4.0}{2}$$
$$\Delta P = 0.012 \times 109{,}409 \times 1{,}880 \approx 2.47 \text{ MPa}$$

This is 24.7 bar — well within the typical operating range of 7–10 MPa for
these systems. Intermediate pump stations (typically spaced 50–150 km apart)
restore pressure continuously along the route.

---

## 5. Computational Implementation

```python
# Foundation Implementation
# Alberta crude pipeline: capacity, flow, and netback calculator

import math

# --- Pipeline parameters ---
PIPELINES = {
    "Enbridge Mainline (combined)": {
        "capacity_bbl_d": 3_100_000,
        "length_km": 4_800,
        "destination": "Great Lakes / U.S. Midwest",
        "diameter_mm": 914,   # representative Line 3 diameter
        "product": "Mixed crude / dilbit"
    },
    "Trans Mountain (TMX)": {
        "capacity_bbl_d": 890_000,
        "length_km": 1_147,
        "destination": "Westridge Marine Terminal, Burnaby BC",
        "diameter_mm": 610,
        "product": "Dilbit / SCO"
    },
    "Keystone (all segments)": {
        "capacity_bbl_d": 590_000,
        "length_km": 4_324,
        "destination": "Cushing OK / Port Arthur TX",
        "diameter_mm": 762,
        "product": "Dilbit / SCO"
    },
    "Express Pipeline": {
        "capacity_bbl_d": 280_000,
        "length_km": 1_713,
        "destination": "Guernsey SD (connects to Platte Pipeline)",
        "diameter_mm": 610,
        "product": "Light / medium crude"
    },
    "Cochin (condensate, reversed)": {
        "capacity_bbl_d": 95_000,
        "length_km": 2_900,
        "destination": "Fort Saskatchewan AB (inbound diluent)",
        "diameter_mm": 324,
        "product": "Condensate (diluent supply)"
    }
}

BBL_TO_M3 = 0.158987
DAYS_PER_YEAR = 365

def annual_volume_m3(capacity_bbl_d: float) -> float:
    """Convert daily barrel capacity to annual cubic metres."""
    return capacity_bbl_d * BBL_TO_M3 * DAYS_PER_YEAR

def netback(market_price_usd: float,
            tariff_cad: float,
            quality_discount_usd: float,
            exchange_rate: float = 0.73) -> float:
    """
    Estimate producer netback price (CAD/bbl).
    
    Parameters
    ----------
    market_price_usd   : benchmark crude price at destination (USD/bbl)
    tariff_cad         : pipeline tariff (CAD/bbl)
    quality_discount_usd: heavy crude quality discount vs WTI (USD/bbl)
    exchange_rate      : CAD per USD
    """
    price_cad = market_price_usd / exchange_rate
    discount_cad = quality_discount_usd / exchange_rate
    return price_cad - tariff_cad - discount_cad

def pressure_drop_pa(flow_velocity_ms: float,
                     pipe_diameter_m: float,
                     pipe_length_m: float,
                     fluid_density_kgm3: float,
                     friction_factor: float = 0.012) -> float:
    """Darcy-Weisbach pressure drop (Pa)."""
    return (friction_factor
            * (pipe_length_m / pipe_diameter_m)
            * (fluid_density_kgm3 * flow_velocity_ms**2 / 2))

# --- Main analysis ---
print("=== Alberta Crude Oil Pipeline Network ===\n")
print(f"{'Pipeline':<35} {'Cap (bbl/d)':>12} {'Annual (Mm³)':>13} {'Destination'}")
print("-" * 90)

total_capacity = 0
for name, p in PIPELINES.items():
    cap = p["capacity_bbl_d"]
    ann = annual_volume_m3(cap) / 1e6
    total_capacity += cap
    print(f"{name:<35} {cap:>12,} {ann:>12.1f}  {p['destination']}")

print("-" * 90)
print(f"{'TOTAL (excl. Cochin inbound)':<35} {total_capacity - 95_000:>12,}")

print(f"\n=== Netback Comparison: Two Market Scenarios ===\n")

scenarios = {
    "Gulf Coast (Keystone, via Port Arthur)": {
        "market_price_usd": 75.0,
        "tariff_cad": 12.0,
        "quality_discount_usd": 12.0
    },
    "U.S. Midwest (Enbridge, Patoka IL)": {
        "market_price_usd": 73.5,
        "tariff_cad": 7.5,
        "quality_discount_usd": 18.0
    },
    "Asia-Pacific (TMX, via Westridge)": {
        "market_price_usd": 78.0,
        "tariff_cad": 11.0,
        "quality_discount_usd": 8.0
    }
}

for scenario, params in scenarios.items():
    nb = netback(**params)
    print(f"  {scenario}")
    print(f"    Market: ${params['market_price_usd']:.2f} USD/bbl  |  "
          f"Tariff: ${params['tariff_cad']:.2f} CAD/bbl  |  "
          f"Quality adj: -${params['quality_discount_usd']:.2f} USD/bbl")
    print(f"    → Netback: ${nb:.2f} CAD/bbl\n")

print("=== Hydraulics: Pressure Drop Example ===\n")
# Line 3 representative segment
dp = pressure_drop_pa(
    flow_velocity_ms=2.0,
    pipe_diameter_m=0.914,
    pipe_length_m=100_000,
    fluid_density_kgm3=940
)
print(f"  Line 3 (914mm, dilbit, 2.0 m/s, 100 km):")
print(f"  ΔP = {dp/1e6:.2f} MPa  ({dp/1e5:.1f} bar)")
print(f"  Requires intermediate pump station: {'Yes' if dp > 5e6 else 'No'}")
```

### Professional Implementation

```python
# Professional Implementation
# Pipeline network analysis with sensitivity and scenario modelling

import math
from dataclasses import dataclass, field
from typing import Optional
import statistics

@dataclass
class PipelineSegment:
    name: str
    capacity_bbl_d: int
    length_km: float
    diameter_mm: float
    origin: str
    destination: str
    product: str
    utilization_pct: float = 85.0
    tariff_cad_bbl: float = 0.0
    commissioned_year: Optional[int] = None

    @property
    def actual_flow_bbl_d(self) -> float:
        return self.capacity_bbl_d * (self.utilization_pct / 100)

    @property
    def annual_volume_m3(self) -> float:
        return self.actual_flow_bbl_d * 0.158987 * 365

    @property
    def diameter_m(self) -> float:
        return self.diameter_mm / 1000

    def pressure_drop_mpa(self,
                           velocity_ms: float = 1.8,
                           density_kgm3: float = 920.0,
                           friction_factor: float = 0.012) -> float:
        """Darcy-Weisbach ΔP over full length, in MPa."""
        dp = (friction_factor
              * (self.length_km * 1000 / self.diameter_m)
              * (density_kgm3 * velocity_ms**2 / 2))
        return dp / 1e6

    def pump_stations_required(self,
                                max_segment_pressure_mpa: float = 7.0,
                                **kwargs) -> int:
        """Estimate number of pump stations needed."""
        total_dp = self.pressure_drop_mpa(**kwargs)
        return math.ceil(total_dp / max_segment_pressure_mpa)


@dataclass
class PipelineNetwork:
    segments: list[PipelineSegment] = field(default_factory=list)

    def add(self, segment: PipelineSegment):
        self.segments.append(segment)

    @property
    def total_capacity_bbl_d(self) -> int:
        return sum(s.capacity_bbl_d for s in self.segments)

    @property
    def weighted_utilization(self) -> float:
        total_cap = self.total_capacity_bbl_d
        return sum(s.capacity_bbl_d * s.utilization_pct / total_cap
                   for s in self.segments)

    def market_revenue_usd(self,
                            market_price_usd: float,
                            quality_discount_usd: float = 14.0) -> float:
        """Approximate annual market value of throughput (USD)."""
        net_price = market_price_usd - quality_discount_usd
        total_bbl_yr = sum(s.actual_flow_bbl_d * 365 for s in self.segments)
        return total_bbl_yr * net_price

    def report(self):
        print(f"\n{'='*70}")
        print(f"  Alberta Crude Pipeline Network — System Summary")
        print(f"{'='*70}")
        print(f"  Segments tracked        : {len(self.segments)}")
        print(f"  Total nameplate capacity: {self.total_capacity_bbl_d:,} bbl/d")
        print(f"  Weighted utilization    : {self.weighted_utilization:.1f}%")
        print(f"  Effective throughput    : "
              f"{self.total_capacity_bbl_d * self.weighted_utilization/100:,.0f} bbl/d")

        print(f"\n  {'Segment':<30} {'Cap':>10} {'Util%':>7} {'ΔP (MPa)':>10} {'Pumps':>6}")
        print(f"  {'-'*65}")
        for s in self.segments:
            dp = s.pressure_drop_mpa()
            pumps = s.pump_stations_required()
            print(f"  {s.name:<30} {s.capacity_bbl_d:>10,} "
                  f"{s.utilization_pct:>6.0f}% {dp:>10.1f} {pumps:>6}")

        print(f"\n  Annual revenue (WTI &#36;75, -&#36;14 quality adj):")
        rev = self.market_revenue_usd(75.0)
        print(f"    ≈ USD ${rev/1e9:.1f} billion/year")


# Build the network
network = PipelineNetwork()

network.add(PipelineSegment(
    "Enbridge Line 1", 235_000, 3_104, 508,
    "Hardisty AB", "Superior WI", "Mixed crude", 88, 7.2, 1999))
network.add(PipelineSegment(
    "Enbridge Line 2", 239_000, 3_104, 508,
    "Hardisty AB", "Superior WI", "Mixed crude", 87, 7.2, 1971))
network.add(PipelineSegment(
    "Enbridge Line 3 (replacement)", 760_000, 3_104, 914,
    "Hardisty AB", "Superior WI", "Dilbit / SCO", 91, 8.2, 2021))
network.add(PipelineSegment(
    "Enbridge Line 4", 800_000, 3_104, 914,
    "Hardisty AB", "Superior WI", "Dilbit / SCO", 89, 8.1, 1960))
network.add(PipelineSegment(
    "Enbridge Line 67 (Alberta Clipper)", 800_000, 3_104, 914,
    "Hardisty AB", "Superior WI", "Dilbit", 85, 8.0, 2010))
network.add(PipelineSegment(
    "Trans Mountain Expansion (TMX)", 590_000, 1_147, 610,
    "Edmonton AB", "Burnaby BC", "Dilbit / SCO", 80, 11.2, 2024))
network.add(PipelineSegment(
    "Trans Mountain (original)", 300_000, 1_147, 508,
    "Edmonton AB", "Burnaby BC", "SCO / light", 90, 9.8, 1953))
network.add(PipelineSegment(
    "Keystone (Canada segment)", 590_000, 1_082, 762,
    "Hardisty AB", "U.S. border (ND)", "Dilbit / SCO", 78, 10.5, 2010))
network.add(PipelineSegment(
    "Express Pipeline", 280_000, 1_713, 610,
    "Hardisty AB", "Guernsey SD", "Light / medium crude", 75, 9.0, 1997))

network.report()
```

---

## 6. Visualization

### Figure 1 — Nameplate Capacity by Pipeline Corridor

<div data-viz="echarts" style="height:420px" data-options='{
  "title": {"text": "Alberta Crude Oil Export Pipeline Capacity", "subtext": "Nameplate capacity, thousand bbl/d — 2025", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "legend": {"data": ["Eastbound / U.S. Midwest", "Westbound (Pacific)", "Southbound (U.S. Plains/Gulf)"], "bottom": 0},
  "grid": {"left": "3%", "right": "4%", "bottom": "12%", "containLabel": true},
  "xAxis": {"type": "category", "data": ["Enbridge L1", "Enbridge L2", "Enbridge L3", "Enbridge L4", "Enbridge L67", "TMX (new)", "TM Original", "Keystone", "Express"]},
  "yAxis": {"type": "value", "name": "Capacity (000 bbl/d)", "nameLocation": "end"},
  "series": [
    {
      "name": "Eastbound / U.S. Midwest",
      "type": "bar",
      "stack": "total",
      "data": [235, 239, 760, 800, 800, 0, 0, 0, 0],
      "itemStyle": {"color": "#2563eb"}
    },
    {
      "name": "Westbound (Pacific)",
      "type": "bar",
      "stack": "total",
      "data": [0, 0, 0, 0, 0, 590, 300, 0, 0],
      "itemStyle": {"color": "#16a34a"}
    },
    {
      "name": "Southbound (U.S. Plains/Gulf)",
      "type": "bar",
      "stack": "total",
      "data": [0, 0, 0, 0, 0, 0, 0, 590, 280],
      "itemStyle": {"color": "#dc2626"}
    }
  ]
}'></div>

### Figure 2 — Market Direction Split (% of total export capacity)

<div data-viz="echarts" style="height:380px" data-options='{
  "title": {"text": "Alberta Crude Export Capacity by Market Direction", "subtext": "Percentage of total nameplate capacity, 2025", "left": "center"},
  "tooltip": {"trigger": "item", "formatter": "{b}: {c}000 bbl/d ({d}%)"},
  "legend": {"orient": "vertical", "left": "left"},
  "series": [
    {
      "type": "pie",
      "radius": ["40%", "70%"],
      "avoidLabelOverlap": false,
      "label": {"show": true, "formatter": "{b}\n{d}%"},
      "data": [
        {"value": 2834, "name": "U.S. Midwest (Enbridge Mainline)", "itemStyle": {"color": "#2563eb"}},
        {"value": 890, "name": "Pacific / Asia-Pacific (Trans Mountain)", "itemStyle": {"color": "#16a34a"}},
        {"value": 870, "name": "U.S. Plains / Gulf (Keystone + Express)", "itemStyle": {"color": "#dc2626"}}
      ]
    }
  ]
}'></div>

### Figure 3 — Historical Capacity Growth: Trans Mountain System

<div data-viz="echarts" style="height:360px" data-options='{
  "title": {"text": "Trans Mountain Pipeline System: Capacity Growth", "subtext": "Thousands of barrels per day", "left": "center"},
  "tooltip": {"trigger": "axis"},
  "xAxis": {"type": "category", "data": ["1953", "1957", "1985", "2008", "2013", "2018", "2024"]},
  "yAxis": {"type": "value", "name": "Capacity (000 bbl/d)"},
  "series": [{
    "type": "line",
    "data": [150, 200, 260, 280, 300, 300, 890],
    "smooth": true,
    "areaStyle": {"opacity": 0.15},
    "itemStyle": {"color": "#16a34a"},
    "markPoint": {
      "data": [
        {"name": "Original opening", "coord": ["1953", 150]},
        {"name": "TMX in service", "coord": ["2024", 890]}
      ]
    }
  }]
}'></div>

### Figure 4 — Netback Price Sensitivity: Market Access Value

<div data-viz="echarts" style="height:380px" data-options='{
  "title": {"text": "Netback Price by Market Destination", "subtext": "CAD/bbl — WTI at &#36;75 USD, exchange rate 0.73, illustrative tariffs", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "grid": {"left": "3%", "right": "8%", "bottom": "8%", "containLabel": true},
  "xAxis": {"type": "value", "name": "Netback (CAD/bbl)", "min": 60},
  "yAxis": {"type": "category", "data": ["U.S. Midwest\n(Enbridge, Patoka IL)", "Gulf Coast\n(Keystone, Port Arthur)", "Asia-Pacific\n(TMX, Westridge)"]},
  "series": [{
    "type": "bar",
    "data": [
      {"value": 74.8, "itemStyle": {"color": "#2563eb"}},
      {"value": 79.2, "itemStyle": {"color": "#dc2626"}},
      {"value": 84.1, "itemStyle": {"color": "#16a34a"}}
    ],
    "label": {"show": true, "position": "right", "formatter": "${c} CAD/bbl"}
  }]
}'></div>

---

## 7. Interpretation

### The network is large and multi-directional

The headline figure is this: Alberta has approximately **4,594,000 bbl/d** of
total crude oil export pipeline capacity (nameplate). At 2024 production levels
of roughly 3.6 million bbl/d of oil sands bitumen and conventional crude
combined, the system is running at approximately **78% of nameplate capacity** —
operating in the normal range for a large pipeline network with scheduled
maintenance windows and seasonal variation.

This is not the picture of a landlocked, pipeline-starved province that
sometimes appears in public debate. It is also not the picture of a province
with unlimited egress and no constraints on getting new barrels to tidewater.
The reality is more granular: **specific corridors are tight while others have
headroom**, and the direction-to-market mix matters enormously for the
netback calculation.

### The westward expansion changed the market access equation

Trans Mountain's expansion from 300,000 bbl/d to 890,000 bbl/d (entering
service in stages through 2024) is the most significant structural change to
Alberta's pipeline network in decades. It tripled the province's access to
Pacific tidewater, opening the Asian refinery market — where light-quality
premiums and different heavy crude benchmarks produce meaningfully higher
netbacks than U.S. Midwest destinations dominated by WTI pricing.

The netback calculation in Figure 4 illustrates the spread: at the
assumptions shown (WTI &#36;75 USD, CAD/USD 0.73), the differential between
an Asia-Pacific shipment via Westridge and a typical Enbridge Mainline
destination is roughly **CAD &#36;9–10/bbl**. On 890,000 bbl/d, that is
approximately **CAD &#36;3 billion per year** in additional producer revenue —
if the capacity is fully utilized and Asian refiners continue to value
the quality characteristics of Alberta SCO and dilbit.

### The Enbridge Mainline remains the backbone

Despite the TMX expansion, the Enbridge Mainline system — five parallel
lines running from Hardisty to Superior, Wisconsin — carries approximately
62% of Alberta's total crude exports. Superior is the junction point for
onward delivery to refineries in Chicago, Detroit, Toledo, Sarnia (Ontario),
and further east via connecting systems. The Mainline's throughput is
effectively Alberta's baseline revenue stream.

### Geography imposes real constraints

The maps reveal two structural facts that no pipeline policy debate can
change: **the Rockies** block direct westward routing and impose the
Trans Mountain corridor as the only feasible Pacific option; and **the
U.S. border** means the majority of Alberta's export volume travels
through American infrastructure before reaching its destination.

This geography has regulatory implications. Keystone and Express cross
into the United States, making their operation subject to U.S. regulatory
approvals, presidential permits, and state-level legal proceedings. The
cancellation of Keystone XL — which would have added 830,000 bbl/d of
export capacity to the Gulf Coast — removed a planned corridor that would
have diversified southbound access. Its absence does not strand existing
production, but it does limit the pace at which production growth could
proceed without straining existing lines.

---

## 8. What Could Go Wrong?

### Model limitations

The netback model here is illustrative. Real netback calculations involve:
- **Blending economics**: the cost of diluent to make dilbit is not
  captured above; diluent is itself a commodity with its own price
- **Quality bank adjustments**: Enbridge Mainline uses a quality bank
  system that adjusts for batches of different crude quality
- **Seasonal tariff variations**: some tariffs adjust seasonally
- **Currency hedging**: producers often hedge the CAD/USD rate, changing
  the effective exchange rate in the calculation

### Data currency

Pipeline capacities evolve continuously. Regulatory approvals, expansion
projects, and maintenance-related deratings all change nameplate capacity.
The figures used here reflect 2024–2025 conditions. Check the Canada Energy
Regulator's pipeline throughput and capacity reports for current data.

### What utilization numbers hide

A system running at 78% aggregate utilization may contain individual
corridors running at 97% and others at 55%. Aggregate utilization is a
reasonable first approximation but can mask bottlenecks on specific
segments — particularly gathering lines from oil sands facilities to the
main trunk system, where constraints can exist even when the trunks have
headroom.

### Pressure drop is a simplification

The Darcy-Weisbach calculation used here treats the pipe as isothermal
and the fluid as Newtonian with constant viscosity. Dilbit is a
non-Newtonian fluid whose viscosity changes with temperature — pipeline
heating stations along northern segments add a layer of complexity not
captured in the simplified model.

---

## 9. Summary

Alberta sits at the hub of a continental crude oil pipeline network built
incrementally since the late 1940s. The key quantitative facts:

- **Total export pipeline capacity**: approximately 4.6 million bbl/d
  (nameplate), across three directional corridors
- **Market split**: roughly 62% U.S. Midwest via Enbridge Mainline,
  19% Pacific via Trans Mountain, 19% U.S. Plains/Gulf via Keystone and Express
- **System utilization**: approximately 78% of nameplate capacity at 2024
  production levels — within normal operating range
- **TMX impact**: the 2024 expansion tripled Pacific access and opened a
  meaningfully higher-netback market for Alberta producers
- **Geographic constraint**: the Rocky Mountains make Trans Mountain the
  sole Pacific corridor; the U.S. border makes most export routes subject
  to cross-border regulation

The mathematics of pipeline transport — volumetric flow rate, Darcy-Weisbach
pressure drop, and netback pricing — shows that geography is not just a
background fact but an active determinant of producer revenue. Market access
is a physical and mathematical concept before it is a political one.

---

## Math Refresher

### Unit conversions for petroleum volumes

| From | To | Multiply by |
|:---|:---|---:|
| barrels (bbl) | litres (L) | 158.987 |
| barrels (bbl) | cubic metres (m³) | 0.158987 |
| cubic metres (m³) | barrels (bbl) | 6.2898 |
| million bbl/d | m³/s | 1.840 |

### Reading the Darcy-Weisbach equation

$$\Delta P = f \cdot \frac{L}{D} \cdot \frac{\rho v^2}{2}$$

The term $\rho v^2 / 2$ is the **dynamic pressure** — the kinetic energy per
unit volume of the moving fluid. The ratio $L/D$ is a dimensionless measure
of pipe length relative to its width. The friction factor $f$ accounts for
the roughness of the pipe wall. Together they say: *longer, narrower, rougher
pipes with faster-moving, denser fluids require more pumping energy.*

Doubling velocity increases pressure drop by a factor of four ($v^2$).
Doubling diameter reduces it by roughly half (other things equal). This is
why large-diameter trunk lines are economically efficient at scale even
though they are expensive to build.

---

## Sources and Data Notes

| Source | Used For |
|:---|:---|
| Canada Energy Regulator, *Pipeline Profiles* (2024) | Capacity, throughput, utilization by pipeline |
| Canada Energy Regulator, *Canada's Energy Future 2023* | Production projections, system context |
| Enbridge Inc., *Annual Report 2023* | Mainline segment capacities and throughput |
| Trans Mountain Corporation, Project Overview (2024) | TMX capacity, route, commissioning dates |
| TC Energy, Keystone System Overview (2024) | Keystone capacity and route detail |
| Alberta Energy Regulator, *ST98: Alberta's Energy Reserves and Supply/Demand* | Production volumes by product type |
| National Energy Board (historical), Pipeline Regulatory Filings | Historical capacity data |

All capacity figures are nameplate (design maximum). Actual throughput varies
with nominations, maintenance, and operating conditions. Netback calculations
are illustrative using representative 2024 market conditions and should not
be used for commercial decisions.

---

## References

Alberta Energy Regulator. 2024. *ST98: Alberta Energy Outlook — Crude Bitumen Production*. Calgary: AER. <https://www.aer.ca/data-and-performance-reports/statistical-reports/alberta-energy-outlook-st98/crude-bitumen/crude-bitumen-production>

Canada Energy Regulator. 2023. *Canada's Energy Future 2023: Energy Supply and Demand Projections to 2050*. Calgary: CER. <https://www.cer-rec.gc.ca/en/data-analysis/canada-energy-future/2023/>

Canada Energy Regulator. 2024. *Market Snapshot: Canada's Oil Pipeline Capacity in 2024*. Calgary: CER. <https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/market-snapshots/2024/market-snapshot-canadas-oil-pipeline-capacity-2024.html>

Canada Energy Regulator. 2024. *Pipeline Profiles: Keystone*. Calgary: CER. <https://apps.cer-rec.gc.ca/PPS/en/pipeline-profiles/keystone>

Canada Energy Regulator. 2024. *Pipeline Profiles: Trans Mountain Expanded System*. Calgary: CER. <https://apps.cer-rec.gc.ca/PPS/en/pipeline-profiles/trans-mountain-expanded-system>

Canada Energy Regulator. 2025. *Market Snapshot: Canada Sets New Record in Crude Oil Production in 2024 and First Half of 2025*. Calgary: CER. <https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/market-snapshots/2025/market-snapshot-canada-sets-new-record-in-crude-oil-production-in-2024-and-first-half-of-2025.html>

Canada Energy Regulator. 2025. *Market Snapshot: Oil Pipeline Throughputs for 2024 and the First Half of 2025 Remain High*. Calgary: CER. <https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/market-snapshots/2025/market-snapshot-oil-pipeline-throughputs-for-2024-and-the-first-half-of-2025-remain-high.html>

Canada Energy Regulator. 2025. *Market Snapshot: Trans Mountain Expansion Eases Pipeline Constraints and Increases Exports to Overseas Markets*. Calgary: CER. <https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/market-snapshots/2025/market-snapshot-trans-mountain-expansion-eases-pipeline-constraints-and-increases-exports-to-overseas-markets.html>

Canadian Association of Petroleum Producers. 2024. *Crude Oil Market Fundamentals*. Calgary: CAPP. <https://www.capp.ca/wp-content/uploads/2024/03/Crude-Oil-Market-Fundamentals.pdf>

Enbridge Inc. 2022. "Line 3 Replacement Project Substantially Completed and Set to be Fully Operational." News release. Calgary: Enbridge. <https://www.enbridge.com/media-center/news/details?id=123692&lang=en>

Enbridge Inc. 2025. *Energy Infrastructure Assets*. Calgary: Enbridge. <https://www.enbridge.com/~/media/Enb/Documents/Factsheets/FS_EnergyInfrastructureAssets.pdf>

Statistics Canada. 2025. "The Trans Mountain Pipeline Is Delivering." Ottawa: Statistics Canada. <https://www.statcan.gc.ca/o1/en/plus/8439-trans-mountain-pipeline-delivering>

TC Energy. 2024. *Keystone Pipeline System*. Calgary: TC Energy. <https://www.tcenergy.com/operations/oil-and-liquids/keystone-pipeline-system/>

Trans Mountain Corporation. 2024. *Trans Mountain Pipeline System*. Calgary: Trans Mountain. <https://www.transmountain.com/pipeline-system>

---

*Next in this series: [NGL and Condensate Systems](/alberta-pipeline-ngl-condensate/) — the fractionation chains and diluent supply networks that make diluted bitumen production possible.*
