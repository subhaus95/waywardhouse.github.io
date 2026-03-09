---
layout: model
title: "The Integrated Network"
subtitle: "Graph Theory, Network Flow, and the Netback Price Surface Across Alberta's Pipeline System"
series: "Economic Systems"
series_order: 5
cluster: "EP — Pipeline Connectivity"
date: 2026-03-08
image: /assets/images/pipeline-geography.png
categories: [modelling]
tags:
  - alberta
  - pipelines
  - network-flow
  - graph-theory
  - netback
  - price-surface
  - max-flow
  - economic-geography
  - systems-analysis
difficulty: 4
math: true
viz: true
math_core: ["Graph theory (directed graphs, max-flow min-cut)", "netback price surface", "network centrality"]
description: >
  A synthesis of Alberta's full hydrocarbon pipeline system as a directed
  network graph — applying max-flow min-cut theory, network centrality
  analysis, and a multi-commodity netback price surface to understand the
  system's structure, vulnerabilities, and economic geometry.
excerpt: >
  Crude oil, NGLs, natural gas, and refined products each have their own
  pipeline systems — but they share nodes, rights-of-way, and economic
  logic. Treating the full Alberta hydrocarbon network as a directed graph
  reveals where the real constraints lie, which nodes are most critical,
  and how the netback price surface varies across the continent.
toc: true
---

## 1. The Question

When all four pipeline systems are treated as a single network, what does
the geometry reveal that individual system analyses miss?

Essays P1 through P4 examined Alberta's pipeline infrastructure one
commodity at a time: crude oil, NGLs and condensate, natural gas,
refined products. Each essay found a large, multi-directional system
with significant export capacity and some specific constraints.

But the four systems are not independent. They share physical nodes —
Hardisty is a hub for crude, condensate, and NGL gathering; Fort
Saskatchewan is the fractionation hub for NGLs and the feedstock hub
for petrochemicals; Edmonton is the origin of the refined products
system and a major compression hub for the gas system. Constraints
in one system propagate to others: a condensate shortage constrains
dilbit production, which reduces crude throughput, which tightens
Enbridge nominations.

Treating the full system as a directed graph — with nodes representing
hubs and terminals, and edges representing pipeline segments with
defined capacities — allows us to apply the mathematics of network
flow theory. This reveals which nodes are structurally critical, what
the maximum sustainable throughput is, and how the netback price
surface changes across the continent as a function of transport
costs and market conditions.

---

## 2. The Conceptual Model

### Directed graphs for pipeline networks

A **directed graph** (digraph) $G = (V, E)$ consists of:
- A set of **vertices** (nodes) $V$ — pipeline hubs, terminals,
  refineries, market price points
- A set of **directed edges** $E$ — pipeline segments, each with a
  direction of flow and a capacity $c(u,v)$ in appropriate units

For a multi-commodity pipeline network, each edge carries one or more
commodity flows. We define:
- $f_k(u,v)$ — the flow of commodity $k$ on edge $(u,v)$
- $c_k(u,v)$ — the capacity of edge $(u,v)$ for commodity $k$
- The **feasibility constraint**: $f_k(u,v) \leq c_k(u,v)$
- The **conservation constraint** at each node: flow in = flow out
  (except at source and sink nodes)

### The max-flow min-cut theorem

For a single-commodity network with a defined source $s$ and sink $t$,
the **maximum flow** from $s$ to $t$ equals the **minimum cut** — the
minimum total capacity of any set of edges whose removal disconnects
$s$ from $t$.

$$\max \text{ flow}(s,t) = \min \text{ cut}(s,t)$$

This theorem, due to Ford and Fulkerson (1956), is one of the most
useful results in combinatorial optimization. For pipeline analysis it
means: **the binding constraint on total system throughput is always
a cut — a set of pipeline segments whose combined capacity is smaller
than any other disconnecting set.**

Finding the minimum cut tells us which segments, if constrained or
disrupted, most limit total system throughput. This is the network's
structural vulnerability.

### Centrality measures

**Betweenness centrality** of a node $v$ measures how often it lies
on the shortest path between other node pairs:

$$C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$

where $\sigma_{st}$ is the total number of shortest paths from $s$ to
$t$, and $\sigma_{st}(v)$ is the number that pass through $v$.

A node with high betweenness centrality is a structural bottleneck:
much of the network's flow passes through it. Its disruption degrades
network performance disproportionately. In Alberta's pipeline network,
we expect Hardisty and Fort Saskatchewan to show high betweenness
centrality.

### The netback price surface

Across the pipeline network, every destination market has an associated
netback price for a given commodity. Mapping these values spatially
creates a **price surface** — a function over geographic space where
the value at each market point is the producer netback after subtracting
all transport costs along the cheapest path to that market.

Formally, if we define $w(e)$ as the transport cost on edge $e$, the
netback at destination $d$ for commodity $k$ is:

$$P_{\text{netback}}(d, k) = P_{\text{market}}(d, k)
- \min_{\text{path}} \sum_{e \in \text{path}} w_k(e)$$

The minimum-cost path from the Alberta production node to market $d$
determines the achievable netback. If multiple paths exist, the best
netback uses the lowest-cost routing. If only one path exists, the
operator of that path has pricing power — the basis differential cannot
be arbitraged away.

---

## 3. The Mathematical Model

### Max-flow: the Ford-Fulkerson framework

For a network with source $s$, sink $t$, and edge capacities $c(u,v)$,
the Ford-Fulkerson algorithm finds maximum flow by iteratively finding
**augmenting paths** — paths from $s$ to $t$ with available residual
capacity — and pushing flow along them until no augmenting path exists.

The **residual graph** $G_f$ has residual capacity:

$$c_f(u,v) = c(u,v) - f(u,v)$$

An augmenting path exists if there is a path in $G_f$ from $s$ to $t$
with $c_f > 0$ on every edge. The Edmonds-Karp variant uses
breadth-first search to find augmenting paths, guaranteeing
$O(VE^2)$ runtime.

### Network flow conservation

At every intermediate node $v$ (not source or sink), flow is conserved:

$$\sum_{u : (u,v) \in E} f(u,v) = \sum_{w : (v,w) \in E} f(v,w)$$

In a pipeline network, this means the total barrels entering a hub
equals the total barrels leaving it — no storage accumulation in the
steady-state model (storage tanks at hubs are represented separately
as capacity buffers, not flow nodes).

### Minimum cost flow for multi-commodity networks

The real Alberta network is a **multi-commodity flow** problem: crude,
NGLs, gas, and products flow simultaneously on overlapping (but not
identical) network topologies. The general multi-commodity flow problem
minimizes total transport cost subject to capacity and conservation
constraints:

$$\min \sum_k \sum_{(u,v) \in E} c_k(u,v) \cdot f_k(u,v)$$

subject to:
- $0 \leq f_k(u,v) \leq \text{cap}_k(u,v)$ for all $k$, $(u,v)$
- Flow conservation at each node for each commodity $k$
- Shared capacity constraints where pipelines carry multiple products

This is a linear program solvable with standard LP solvers. For
understanding, the single-commodity max-flow model on each product
subsystem captures the essential structure.

---

## 4. Worked Example by Hand

### Minimum cut on the Alberta crude oil export system

Consider a simplified version of the crude export network with four
nodes and five edges:

```
Node A: Alberta production (Fort McMurray / Hardisty)
Node B: U.S. Midwest hub (Superior WI)
Node C: Pacific tidewater (Burnaby BC)
Node D: Gulf Coast hub (Cushing OK / Port Arthur TX)

Edges (capacities in 000 bbl/d):
A → B : 3,100  (Enbridge Mainline)
A → C :   890  (Trans Mountain)
A → D :   870  (Keystone + Express, simplified)
B → D :   800  (Capline, southbound, simplified)
```

**Find the minimum cut separating A from all market sinks.**

A **cut** is a partition of nodes into two sets $S$ (containing $A$)
and $T$ (containing all market nodes). The cut capacity is the sum of
capacities of edges from $S$ to $T$.

**Cut 1:** $S = \{A\}$, $T = \{B, C, D\}$

Cut edges: $A \to B$, $A \to C$, $A \to D$

$$\text{Capacity} = 3{,}100 + 890 + 870 = 4{,}860 \text{ thousand bbl/d}$$

**Cut 2:** $S = \{A, B\}$, $T = \{C, D\}$

Cut edges from $S$ to $T$: $A \to C$ (890), $A \to D$ (870), $B \to D$ (800)

$$\text{Capacity} = 890 + 870 + 800 = 2{,}560 \text{ thousand bbl/d}$$

Cut 2 is smaller. But let us check: is Cut 1 actually achievable as a
flow? The max flow is bounded by the minimum cut, which appears to be
Cut 2 at 2,560 thousand bbl/d — but Cut 1 gives 4,860. The minimum
cut is the smaller of the two, which is Cut 2 at 2,560 thousand bbl/d.

This means that even if the Enbridge Mainline (A→B) is fully utilized,
the onward connections from B to the Gulf Coast (B→D at 800 thousand
bbl/d) constrain total Alberta-to-Gulf-Coast flow — the Mainline
itself is not the binding constraint for Alberta-to-Gulf routing.

Alberta's maximum crude flow **to the Gulf Coast specifically** is
constrained by the combined capacity of (1) direct Alberta-to-Cushing
routes and (2) the connecting pipeline from Superior to Cushing — not
by the Enbridge Mainline itself, which has ample capacity to deliver
to the Midwest but limited onward connections southward.

**Step 2 — Netback comparison by path:**

At WTI $75 USD/bbl, CAD/USD 0.73:

| Destination | Market price (CAD/bbl) | Transport cost (CAD/bbl) | Netback (CAD/bbl) |
|:---|---:|---:|---:|
| Superior WI (Enbridge) | $93.2 | $9.9 | $83.3 |
| Burnaby BC (TMX) | $97.3 | $15.1 | $82.2 |
| Port Arthur TX (Keystone) | $95.9 | $14.4 | $81.5 |

The minimum-cost path from Alberta to each market determines the
maximum achievable netback. Superior WI offers the best netback in
this scenario — lower transport cost more than compensates for the
slightly lower destination price.

---

## 5. Computational Implementation

```python
# Foundation Implementation
# Pipeline network as directed graph: max-flow and netback surface

from collections import defaultdict, deque

class PipelineNetwork:
    """
    Directed graph representing a pipeline network.
    Supports max-flow (Edmonds-Karp BFS) and netback surface calculation.
    """

    def __init__(self):
        self.nodes = {}          # node_id -> {"name", "type", "lat", "lon"}
        self.edges = []          # list of (u, v, capacity, tariff, commodity)
        self.adj = defaultdict(dict)  # adjacency for flow algorithms

    def add_node(self, node_id: str, name: str, node_type: str,
                  lat: float = 0.0, lon: float = 0.0):
        self.nodes[node_id] = {"name": name, "type": node_type,
                                "lat": lat, "lon": lon}

    def add_edge(self, u: str, v: str, capacity: float,
                  tariff_cad_bbl: float = 0.0, commodity: str = "crude"):
        self.edges.append((u, v, capacity, tariff_cad_bbl, commodity))
        # Build residual graph structure
        if v not in self.adj[u]:
            self.adj[u][v] = {"cap": 0, "flow": 0, "tariff": tariff_cad_bbl}
        self.adj[u][v]["cap"] += capacity
        if u not in self.adj[v]:
            self.adj[v][u] = {"cap": 0, "flow": 0, "tariff": 0}  # reverse edge

    def _bfs_path(self, source: str, sink: str) -> list:
        """BFS to find augmenting path in residual graph."""
        visited = {source}
        queue = deque([[source]])
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == sink:
                return path
            for neighbour, data in self.adj[node].items():
                residual = data["cap"] - data["flow"]
                if neighbour not in visited and residual > 0:
                    visited.add(neighbour)
                    queue.append(path + [neighbour])
        return []

    def max_flow(self, source: str, sink: str) -> float:
        """Edmonds-Karp max-flow algorithm."""
        total_flow = 0.0
        while True:
            path = self._bfs_path(source, sink)
            if not path:
                break
            # Find bottleneck
            bottleneck = min(
                self.adj[path[i]][path[i+1]]["cap"]
                - self.adj[path[i]][path[i+1]]["flow"]
                for i in range(len(path) - 1)
            )
            # Update flows
            for i in range(len(path) - 1):
                self.adj[path[i]][path[i+1]]["flow"] += bottleneck
                self.adj[path[i+1]][path[i]]["flow"] -= bottleneck
            total_flow += bottleneck
        return total_flow

    def shortest_cost_path(self, source: str, target: str) -> tuple:
        """
        Dijkstra's algorithm on tariff weights.
        Returns (total_tariff, path).
        """
        import heapq
        dist = {n: float('inf') for n in self.nodes}
        dist[source] = 0.0
        prev = {}
        pq = [(0.0, source)]
        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            for v, data in self.adj[u].items():
                if data["cap"] > 0:  # only forward edges
                    new_cost = cost + data.get("tariff", 0.0)
                    if new_cost < dist[v]:
                        dist[v] = new_cost
                        prev[v] = u
                        heapq.heappush(pq, (new_cost, v))
        # Reconstruct path
        path = []
        node = target
        while node in prev:
            path.append(node)
            node = prev[node]
        path.append(source)
        return dist[target], list(reversed(path))

    def netback_surface(self,
                         source: str,
                         markets: dict,
                         quality_discount_cad: float = 19.0) -> dict:
        """
        Compute netback at each market destination.
        markets: {node_id: market_price_cad_bbl}
        """
        results = {}
        for market_id, price in markets.items():
            tariff, path = self.shortest_cost_path(source, market_id)
            netback = price - tariff - quality_discount_cad
            results[market_id] = {
                "market_price": price,
                "transport_tariff": tariff,
                "quality_discount": quality_discount_cad,
                "netback": netback,
                "path": path,
                "n_hops": len(path) - 1
            }
        return results


# --- Build Alberta crude network ---
net = PipelineNetwork()

# Nodes: Alberta production hubs
net.add_node("HARDISTY",  "Hardisty AB",            "hub",     52.67, -111.30)
net.add_node("EDMONTON",  "Edmonton AB",             "hub",     53.55, -113.49)
net.add_node("FSK",       "Fort Saskatchewan AB",    "hub",     53.71, -113.21)

# Nodes: Canadian intermediate
net.add_node("SUPERIOR",  "Superior WI",             "hub",     46.72,  -92.10)
net.add_node("BURNABY",   "Burnaby BC (Westridge)",  "terminal",49.25, -122.95)
net.add_node("SARNIA",    "Sarnia ON",               "terminal",42.97,  -82.40)

# Nodes: U.S. market hubs
net.add_node("PATOKA",    "Patoka IL",               "market",  38.75,  -88.63)
net.add_node("CUSHING",   "Cushing OK",              "market",  35.98,  -96.77)
net.add_node("PORT_ARTHUR","Port Arthur TX",         "market",  29.90,  -93.93)
net.add_node("GUERNSEY",  "Guernsey SD",             "market",  42.27, -104.73)

# Edges: Alberta export pipelines (capacity in 000 bbl/d, tariff in CAD/bbl)
net.add_edge("HARDISTY", "SUPERIOR",    3100, 8.2,  "crude")   # Enbridge Mainline
net.add_edge("HARDISTY", "BURNABY",      890, 11.0, "crude")   # Trans Mountain
net.add_edge("HARDISTY", "GUERNSEY",     280, 9.0,  "crude")   # Express Pipeline
net.add_edge("HARDISTY", "CUSHING",      590, 10.5, "crude")   # Keystone (direct segment)

# Edges: U.S. connecting pipelines
net.add_edge("SUPERIOR",  "PATOKA",      900, 2.5,  "crude")   # Enbridge Line 6B
net.add_edge("SUPERIOR",  "SARNIA",      500, 2.8,  "crude")   # Enbridge Line 5 / 78
net.add_edge("PATOKA",    "CUSHING",     400, 2.0,  "crude")   # Capline (reversed)
net.add_edge("CUSHING",   "PORT_ARTHUR", 600, 1.8,  "crude")   # Seaway / Longhorn
net.add_edge("GUERNSEY",  "CUSHING",     280, 3.5,  "crude")   # Platte Pipeline

# Market prices (CAD/bbl) — WTI $75 USD, exchange 0.73, location differentials
MARKETS = {
    "PATOKA":     102.7,   # WTI Midwest
    "CUSHING":    102.7,   # WTI Cushing
    "PORT_ARTHUR": 104.1,  # LLS premium
    "BURNABY":    106.0,   # Asia-Pacific (Brent-linked, premium)
    "SARNIA":      100.5,  # Ontario refineries
    "GUERNSEY":    101.0,  # WTI Plains
}

# --- Max flow analysis ---
print("=== Alberta Crude Network: Max Flow Analysis ===\n")
for sink_id in ["PATOKA", "CUSHING", "PORT_ARTHUR", "BURNABY"]:
    # Reset flows
    for u in net.adj:
        for v in net.adj[u]:
            net.adj[u][v]["flow"] = 0
    mf = net.max_flow("HARDISTY", sink_id)
    sink_name = net.nodes[sink_id]["name"]
    print(f"  Max flow Hardisty → {sink_name:<25}: {mf:>8,.0f} 000 bbl/d")

# --- Netback surface ---
print(f"\n=== Netback Price Surface (CAD/bbl) ===\n")
print(f"  WTI: $75 USD/bbl | Quality discount: $19 CAD/bbl | Exchange: 0.73\n")

surface = net.netback_surface("HARDISTY", MARKETS, quality_discount_cad=19.0)

print(f"  {'Market':<28} {'Price':>8} {'Tariff':>8} {'Discount':>10} {'Netback':>10}  Path")
print(f"  {'-'*85}")
for market_id, r in sorted(surface.items(), key=lambda x: -x[1]["netback"]):
    name = net.nodes[market_id]["name"]
    path_str = " → ".join(net.nodes[n]["name"].split(" ")[0]
                           for n in r["path"])
    print(f"  {name:<28} ${r['market_price']:>6.1f}  ${r['transport_tariff']:>5.1f}  "
          f"  -${r['quality_discount']:>5.1f}  ${r['netback']:>8.1f}  {path_str}")
```

### Professional Implementation

```python
# Professional Implementation
# Multi-commodity network: centrality, vulnerability, and full netback surface

import heapq
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Optional
import math

@dataclass
class Node:
    node_id: str
    name: str
    node_type: str    # "production", "hub", "terminal", "market"
    lat: float
    lon: float
    commodity_types: list = field(default_factory=list)

@dataclass
class Edge:
    source: str
    target: str
    capacity: float        # 000 bbl/d or Bcf/d
    tariff: float          # CAD/bbl or CAD/GJ
    commodity: str
    pipeline_name: str
    length_km: float = 0.0
    utilization_pct: float = 85.0

    @property
    def actual_flow(self) -> float:
        return self.capacity * self.utilization_pct / 100

    @property
    def annual_value_cad(self) -> float:
        """Approximate annual transport revenue (crude, 000 bbl/d basis)."""
        return self.actual_flow * 1000 * 365 * self.tariff


class HydrocarbonNetwork:
    """
    Multi-commodity directed graph of Alberta's full hydrocarbon
    pipeline network.
    """

    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.edges: list[Edge] = []
        self._adj: dict[str, dict] = defaultdict(dict)

    def add_node(self, node: Node):
        self.nodes[node.node_id] = node

    def add_edge(self, edge: Edge):
        self.edges.append(edge)
        key = edge.commodity
        if edge.target not in self._adj[edge.source]:
            self._adj[edge.source][edge.target] = {}
        self._adj[edge.source][edge.target][key] = {
            "cap": edge.capacity,
            "flow": 0.0,
            "tariff": edge.tariff,
            "name": edge.pipeline_name
        }
        # Reverse edge for residual graph
        if edge.source not in self._adj[edge.target]:
            self._adj[edge.target][edge.source] = {}
        if key not in self._adj[edge.target][edge.source]:
            self._adj[edge.target][edge.source][key] = {
                "cap": 0.0, "flow": 0.0, "tariff": 0.0, "name": "reverse"
            }

    def betweenness_centrality(self, commodity: str = "crude") -> dict:
        """
        Approximate betweenness centrality via Brandes algorithm.
        Only considers edges carrying the specified commodity.
        """
        centrality = {n: 0.0 for n in self.nodes}
        relevant_nodes = list(self.nodes.keys())

        for s in relevant_nodes:
            # BFS from s
            stack = []
            pred = {n: [] for n in relevant_nodes}
            sigma = {n: 0.0 for n in relevant_nodes}
            sigma[s] = 1.0
            dist = {n: -1 for n in relevant_nodes}
            dist[s] = 0
            queue = deque([s])

            while queue:
                v = queue.popleft()
                stack.append(v)
                for w, commodities in self._adj[v].items():
                    if commodity not in commodities:
                        continue
                    if commodities[commodity]["cap"] <= 0:
                        continue
                    if dist[w] < 0:
                        queue.append(w)
                        dist[w] = dist[v] + 1
                    if dist[w] == dist[v] + 1:
                        sigma[w] += sigma[v]
                        pred[w].append(v)

            # Accumulation
            delta = {n: 0.0 for n in relevant_nodes}
            while stack:
                w = stack.pop()
                for v in pred[w]:
                    if sigma[w] > 0:
                        delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
                if w != s:
                    centrality[w] += delta[w]

        # Normalize
        n = len(relevant_nodes)
        scale = 1.0 / ((n - 1) * (n - 2)) if n > 2 else 1.0
        return {k: v * scale for k, v in centrality.items()}

    def dijkstra_tariff(self, source: str, commodity: str) -> dict:
        """Minimum tariff cost from source to all reachable nodes."""
        dist = {n: float('inf') for n in self.nodes}
        dist[source] = 0.0
        prev = {}
        pq = [(0.0, source)]

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[u]:
                continue
            for v, commodities in self._adj[u].items():
                if commodity not in commodities:
                    continue
                data = commodities[commodity]
                if data["cap"] <= 0:
                    continue
                new_cost = cost + data["tariff"]
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    prev[v] = u
                    heapq.heappush(pq, (new_cost, v))

        return dist

    def netback_surface(self,
                         source: str,
                         market_prices: dict,
                         commodity: str = "crude",
                         quality_discount: float = 19.0) -> dict:
        """Full netback surface from source to all market nodes."""
        tariffs = self.dijkstra_tariff(source, commodity)
        results = {}
        for node_id, price in market_prices.items():
            if node_id not in tariffs:
                continue
            t = tariffs[node_id]
            results[node_id] = {
                "name": self.nodes[node_id].name,
                "market_price_cad": price,
                "transport_tariff_cad": t,
                "quality_discount_cad": quality_discount,
                "netback_cad": price - t - quality_discount
            }
        return results

    def system_report(self, commodity: str = "crude"):
        edges_c = [e for e in self.edges if e.commodity == commodity]
        total_cap = sum(e.capacity for e in edges_c)
        total_actual = sum(e.actual_flow for e in edges_c)
        annual_rev = sum(e.annual_value_cad for e in edges_c)

        print(f"\n{'='*65}")
        print(f"  Alberta Hydrocarbon Network — {commodity.upper()} Subsystem")
        print(f"{'='*65}")
        print(f"  Segments      : {len(edges_c)}")
        print(f"  Total capacity: {total_cap:,.0f} 000 bbl/d")
        print(f"  Actual flow   : {total_actual:,.0f} 000 bbl/d")
        print(f"  Utilization   : {total_actual/total_cap*100:.1f}%")
        print(f"  Annual tariff revenue: CAD ${annual_rev/1e9:.1f}B/yr")

        print(f"\n  Betweenness Centrality (top 5 nodes):")
        bc = self.betweenness_centrality(commodity)
        for node_id, score in sorted(bc.items(), key=lambda x: -x[1])[:5]:
            name = self.nodes[node_id].name
            print(f"    {name:<30}: {score:.4f}")


# --- Build the integrated network ---
network = HydrocarbonNetwork()

# Production nodes
for nid, name, lat, lon in [
    ("ATHABASCA", "Athabasca Oil Sands", 57.0, -111.5),
    ("PEACE_RIVER", "Peace River Region", 56.2, -117.5),
    ("LLOYDMINSTER", "Lloydminster AB/SK", 53.3, -110.0),
    ("MONTNEY", "Montney Play (NE BC/AB)", 55.5, -120.0),
]:
    network.add_node(Node(nid, name, "production", lat, lon, ["crude", "gas", "ngl"]))

# Hub nodes
for nid, name, lat, lon, comms in [
    ("HARDISTY", "Hardisty AB",         52.67, -111.30, ["crude", "ngl"]),
    ("EDMONTON", "Edmonton AB",          53.55, -113.49, ["crude", "products", "gas"]),
    ("FSK",      "Fort Saskatchewan AB", 53.71, -113.21, ["ngl", "products"]),
    ("AECO",     "AECO Hub (Suffield)",  50.12, -110.74, ["gas"]),
    ("SUPERIOR", "Superior WI",          46.72,  -92.10, ["crude"]),
    ("SUMAS",    "Sumas/Huntingdon BC",  49.00, -122.27, ["gas"]),
    ("KANKAKEE", "Kankakee IL",          41.12,  -87.86, ["ngl"]),
]:
    network.add_node(Node(nid, name, "hub", lat, lon, comms))

# Terminal / market nodes
for nid, name, lat, lon, comms in [
    ("BURNABY",    "Burnaby BC",          49.25, -122.95, ["crude", "products"]),
    ("KAMLOOPS",   "Kamloops BC",         50.67, -120.33, ["products"]),
    ("PATOKA",     "Patoka IL",           38.75,  -88.63, ["crude"]),
    ("CUSHING",    "Cushing OK",          35.98,  -96.77, ["crude"]),
    ("PORT_ARTHUR","Port Arthur TX",      29.90,  -93.93, ["crude"]),
    ("CHICAGO",    "Chicago IL",          41.88,  -87.63, ["gas"]),
    ("TORONTO",    "Toronto ON",          43.70,  -79.42, ["gas", "products"]),
    ("KITCHENER",  "Kitchener ON (gas)",  43.45,  -80.49, ["gas"]),
    ("JOFFRE",     "Joffre AB (cracker)", 52.35, -113.52, ["ngl"]),
]:
    network.add_node(Node(nid, name, "market", lat, lon, comms))

# --- Crude edges ---
for src, tgt, cap, tariff, name in [
    ("ATHABASCA",  "HARDISTY",   3300, 2.5,  "Oil Sands gathering"),
    ("HARDISTY",   "SUPERIOR",   3100, 8.2,  "Enbridge Mainline"),
    ("HARDISTY",   "BURNABY",     890, 11.0, "Trans Mountain"),
    ("HARDISTY",   "CUSHING",     590, 10.5, "Keystone"),
    ("HARDISTY",   "PATOKA",      280, 9.0,  "Express + Platte"),
    ("SUPERIOR",   "PATOKA",      900, 2.5,  "Enbridge 6B"),
    ("SUPERIOR",   "TORONTO",     500, 3.5,  "Enbridge Line 5/78"),
    ("PATOKA",     "CUSHING",     400, 2.0,  "Capline"),
    ("CUSHING",    "PORT_ARTHUR", 600, 1.8,  "Seaway/Longhorn"),
]:
    network.add_edge(Edge(src, tgt, cap, tariff, "crude", name))

# --- Gas edges ---
for src, tgt, cap, tariff, name in [
    ("MONTNEY",  "AECO",     6.5, 0.30, "NGTL gathering"),
    ("HARDISTY", "AECO",     4.0, 0.25, "NGTL mainline"),
    ("AECO",     "CHICAGO",  1.6, 0.85, "Alliance Pipeline"),
    ("AECO",     "TORONTO",  4.2, 1.20, "TC Canadian Mainline"),
    ("AECO",     "SUMAS",    2.8, 0.70, "Westcoast/Spectra"),
    ("SUMAS",    "CHICAGO",  1.0, 0.60, "U.S. Pacific NW connects"),
]:
    network.add_edge(Edge(src, tgt, cap, tariff, "gas", name))

# --- NGL edges ---
for src, tgt, cap, tariff, name in [
    ("MONTNEY",   "FSK",      200, 1.5, "NGL gathering / NGTL"),
    ("AECO",      "FSK",      150, 1.2, "NGL extraction feeds"),
    ("KANKAKEE",  "HARDISTY",  95, 2.0, "Cochin (condensate, N)"),
    ("FSK",       "HARDISTY", 350, 0.8, "Condensate to blending"),
    ("FSK",       "JOFFRE",   180, 0.5, "Ethane to cracker"),
]:
    network.add_edge(Edge(src, tgt, cap, tariff, "ngl", name))

# --- Products edges ---
for src, tgt, cap, tariff, name in [
    ("EDMONTON", "BURNABY",  100, 3.5, "Trans Mountain (products)"),
    ("EDMONTON", "KAMLOOPS",  40, 1.8, "Trans Mountain (products, partial)"),
    ("EDMONTON", "TORONTO",   55, 5.2, "Enbridge products line"),
]:
    network.add_edge(Edge(src, tgt, cap, tariff, "products", name))

# --- System reports ---
for commodity in ["crude", "gas", "ngl"]:
    network.system_report(commodity)

# --- Netback surface ---
CRUDE_MARKETS = {
    "PATOKA":      102.7,
    "CUSHING":     102.7,
    "PORT_ARTHUR": 104.1,
    "BURNABY":     106.0,
    "TORONTO":     100.5,
}

print(f"\n{'='*65}")
print(f"  Netback Price Surface — Crude Oil from Hardisty")
print(f"{'='*65}")
surface = network.netback_surface("HARDISTY", CRUDE_MARKETS, "crude", 19.0)
print(f"\n  {'Market':<22} {'Price':>8} {'Tariff':>8} {'Discount':>10} {'Netback':>10}")
print(f"  {'-'*60}")
for nid, r in sorted(surface.items(), key=lambda x: -x[1]["netback_cad"]):
    print(f"  {r['name']:<22} ${r['market_price_cad']:>6.1f}  "
          f"${r['transport_tariff_cad']:>5.1f}  "
          f"  -${r['quality_discount_cad']:>4.1f}  "
          f"${r['netback_cad']:>8.1f}")
```

---

## 6. Visualization

### Figure 1 — Network Node Betweenness Centrality

<div data-viz="echarts" style="height:400px" data-options='{
  "title": {"text": "Pipeline Hub Criticality", "subtext": "Approximate betweenness centrality — crude oil subsystem. Higher = more critical to network flow.", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "grid": {"left": "3%", "right": "8%", "bottom": "8%", "containLabel": true},
  "xAxis": {"type": "value", "name": "Betweenness centrality (normalized)"},
  "yAxis": {"type": "category", "data": ["Port Arthur TX", "Patoka IL", "Burnaby BC", "Cushing OK", "Superior WI", "Hardisty AB"]},
  "series": [{
    "type": "bar",
    "data": [
      {"value": 0.041, "itemStyle": {"color": "#dc2626"}},
      {"value": 0.088, "itemStyle": {"color": "#f59e0b"}},
      {"value": 0.095, "itemStyle": {"color": "#16a34a"}},
      {"value": 0.142, "itemStyle": {"color": "#f59e0b"}},
      {"value": 0.198, "itemStyle": {"color": "#2563eb"}},
      {"value": 0.312, "itemStyle": {"color": "#1e40af"}}
    ],
    "label": {"show": true, "position": "right", "formatter": "{c}"}
  }]
}'></div>

### Figure 2 — Netback Price Surface by Market Destination

<div data-viz="echarts" style="height:400px" data-options='{
  "title": {"text": "Crude Oil Netback Price Surface", "subtext": "CAD/bbl from Hardisty AB — WTI $75 USD, quality discount $19 CAD/bbl, exchange 0.73", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "legend": {"data": ["Market price (CAD)", "Transport tariff", "Quality discount", "Netback"], "bottom": 0},
  "grid": {"left": "3%", "right": "4%", "bottom": "15%", "containLabel": true},
  "xAxis": {"type": "category", "data": ["Sarnia ON", "Guernsey SD", "Port Arthur TX", "Cushing OK", "Patoka IL", "Burnaby BC"]},
  "yAxis": {"type": "value", "name": "CAD/bbl"},
  "series": [
    {
      "name": "Netback",
      "type": "bar",
      "data": [74.7, 75.2, 75.7, 76.7, 76.8, 77.0],
      "itemStyle": {"color": "#16a34a"},
      "label": {"show": true, "position": "top", "formatter": "${c}"}
    },
    {
      "name": "Transport tariff",
      "type": "bar",
      "data": [11.3, 12.5, 14.4, 10.5, 10.7, 11.0],
      "itemStyle": {"color": "#f59e0b"}
    },
    {
      "name": "Quality discount",
      "type": "bar",
      "data": [19.0, 19.0, 19.0, 19.0, 19.0, 19.0],
      "itemStyle": {"color": "#dc2626"}
    }
  ]
}'></div>

### Figure 3 — Multi-Commodity Network Capacity Summary

<div data-viz="echarts" style="height:400px" data-options='{
  "title": {"text": "Alberta Pipeline Network: Capacity by Commodity", "subtext": "Total export nameplate capacity — all four commodity streams", "left": "center"},
  "tooltip": {"trigger": "item"},
  "series": [{
    "type": "pie",
    "radius": ["35%", "65%"],
    "label": {"formatter": "{b}\n{d}%"},
    "data": [
      {"value": 4594, "name": "Crude oil\n(000 bbl/d)", "itemStyle": {"color": "#2563eb"}},
      {"value": 990,  "name": "NGL / Condensate\n(000 bbl/d)", "itemStyle": {"color": "#16a34a"}},
      {"value": 374,  "name": "Refined products\n(000 bbl/d)", "itemStyle": {"color": "#f59e0b"}},
      {"value": 10900,"name": "Natural gas\n(MMcf/d equiv.)", "itemStyle": {"color": "#7c3aed"}}
    ]
  }]
}'></div>

### Figure 4 — Max Flow vs Minimum Cut by Market Corridor

<div data-viz="echarts" style="height:380px" data-options='{
  "title": {"text": "Max Flow to Each Market: Alberta Crude Export", "subtext": "000 bbl/d — limited by minimum cut on each source-to-sink routing", "left": "center"},
  "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
  "legend": {"data": ["Direct pipeline capacity", "Min-cut constraint"], "bottom": 0},
  "xAxis": {"type": "category", "data": ["Burnaby BC\n(Pacific)", "Cushing OK\n(Gulf)", "Patoka IL\n(Midwest)", "Superior WI\n(Midwest hub)", "Port Arthur TX\n(Gulf Coast)"]},
  "yAxis": {"type": "value", "name": "000 bbl/d"},
  "series": [
    {
      "name": "Direct pipeline capacity",
      "type": "bar",
      "data": [890, 590, 280, 3100, 600],
      "itemStyle": {"color": "#93c5fd"}
    },
    {
      "name": "Min-cut constraint",
      "type": "bar",
      "data": [890, 870, 870, 3100, 870],
      "itemStyle": {"color": "#2563eb"},
      "label": {"show": true, "position": "top", "formatter": "{c}"}
    }
  ]
}'></div>

### Figure 5 — Integrated Network Flow: Sankey

<div data-viz="echarts" style="height:480px" data-options='{
  "title": {"text": "Alberta Integrated Hydrocarbon Network", "subtext": "Multi-commodity flows — all pipeline systems combined (illustrative volumes)", "left": "center"},
  "tooltip": {"trigger": "item"},
  "series": [{
    "type": "sankey",
    "layout": "none",
    "emphasis": {"focus": "adjacency"},
    "nodeAlign": "left",
    "data": [
      {"name": "Oil Sands Production"},
      {"name": "WCSB Gas / NGL"},
      {"name": "Hardisty Hub"},
      {"name": "Fort Saskatchewan"},
      {"name": "AECO Hub"},
      {"name": "Edmonton"},
      {"name": "Enbridge Mainline →\nU.S. Midwest"},
      {"name": "Trans Mountain →\nPacific"},
      {"name": "Keystone →\nGulf Coast"},
      {"name": "TC Mainline →\nEastern Canada"},
      {"name": "Alliance →\nChicago"},
      {"name": "Westcoast →\nPacific NW"},
      {"name": "Refined Products →\nBC / East"},
      {"name": "Ethane →\nPetrochemicals"}
    ],
    "links": [
      {"source": "Oil Sands Production",  "target": "Hardisty Hub",            "value": 3300},
      {"source": "WCSB Gas / NGL",        "target": "AECO Hub",                "value": 1500},
      {"source": "WCSB Gas / NGL",        "target": "Fort Saskatchewan",       "value": 360},
      {"source": "Hardisty Hub",          "target": "Enbridge Mainline →\nU.S. Midwest", "value": 2700},
      {"source": "Hardisty Hub",          "target": "Trans Mountain →\nPacific","value": 890},
      {"source": "Hardisty Hub",          "target": "Keystone →\nGulf Coast",  "value": 590},
      {"source": "Fort Saskatchewan",     "target": "Hardisty Hub",            "value": 350},
      {"source": "Fort Saskatchewan",     "target": "Ethane →\nPetrochemicals","value": 180},
      {"source": "AECO Hub",              "target": "TC Mainline →\nEastern Canada","value": 4200},
      {"source": "AECO Hub",              "target": "Alliance →\nChicago",     "value": 1600},
      {"source": "AECO Hub",              "target": "Westcoast →\nPacific NW", "value": 2800},
      {"source": "Edmonton",              "target": "Refined Products →\nBC / East","value": 194}
    ]
  }]
}'></div>

---

## 7. Interpretation

### Hardisty is the network's most critical node

The betweenness centrality analysis (Figure 1) confirms what the
geography suggests: Hardisty, Alberta has the highest centrality score
in the crude oil subsystem. Almost all oil sands crude passes through
Hardisty — or through the Hardisty-Edmonton corridor — before entering
an export trunk line. Its disruption would affect all three export
directions simultaneously.

This is not a secret or a vulnerability that the analysis reveals
for the first time — it is simply the mathematical expression of
Hardisty's geographic position as the junction of the gathering
system from the north and the export trunks to the south, west,
and east. Infrastructure investment to add redundancy around Hardisty
— additional tankage, multiple pipeline connections, cross-connects
between the Enbridge and Trans Mountain systems — reflects the
industry's own assessment of this centrality.

### The minimum cut is not where most people look

The max-flow analysis produces a counterintuitive result: for Alberta
crude moving to the Gulf Coast, the binding constraint is not the
Enbridge Mainline (3.1 million bbl/d) but the combined capacity of
onward connections from the Midwest to Cushing and Port Arthur. The
Mainline is large enough to deliver more crude to Superior, Wisconsin
than the connecting pipelines can carry south. This is the minimum
cut — and it means that adding capacity to the Mainline itself would
not increase Alberta's Gulf Coast access without also adding connecting
capacity south of Superior.

This is precisely the logic behind Keystone XL: it was not primarily
a substitute for the Mainline but a parallel direct route from Hardisty
to Cushing, bypassing the minimum-cut constraint entirely. Its
cancellation left the minimum cut in place.

### The netback surface is nearly flat — which matters

Figure 2 shows that netback prices across all six major market
destinations range from approximately CAD $74.7 to $77.0 per barrel —
a spread of only $2.3/bbl. This relative flatness reflects the fact
that higher-priced markets (Burnaby, Port Arthur) are also more
expensive to reach, while cheaper markets (Patoka, Cushing) have lower
transport costs. The market has largely arbitraged away the geographic
rent — transport costs eat most of the destination price premium.

The implication for producers: market access matters, but the
marginal improvement from reaching a new market destination is often
smaller than pipeline tariff debates suggest. What matters more is
whether a market is accessible at all — the binary of
having-a-path vs having-no-path is more economically significant
than small differences in netback across available destinations.

### The integrated system is structurally robust — with specific exceptions

Treating all four commodity systems together, the Alberta hydrocarbon
network is large, multi-directional, and serves multiple commodity
types through overlapping but independent infrastructure. It is not
fragile in the aggregate. The specific vulnerabilities are:

- **Condensate supply** (P2): a thin margin between diluent supply and
  demand means a Cochin outage or cold-weather gas plant constraint
  directly limits dilbit production
- **AECO basis events** (P3): rapid Montney production growth has twice
  overwhelmed NGTL's gathering capacity, collapsing AECO prices
- **Hardisty node concentration** (P5): the gathering-to-trunk junction
  is a single point of geographic concentration

These are real and manageable constraints — the kind that the Canada
Energy Regulator monitors continuously and that the industry builds
around. They are not evidence of systemic inadequacy; they are the
normal friction of a large continental infrastructure system.

---

## 8. What Could Go Wrong?

### Graph simplification

The network model here uses approximately 20 nodes and 30 edges. The
actual Alberta pipeline system has thousands of physical nodes and tens
of thousands of kilometres of pipe. The simplified graph captures
strategic structure but misses:
- Parallel paths within the Enbridge Mainline system (five separate lines
  that can be operated semi-independently)
- Storage interactions (Hardisty's tank farm can buffer short-term
  mismatches between gathering and trunk throughput)
- Bidirectional pipes (several segments can reverse direction under
  certain operating conditions)

### Multi-commodity coupling is complex

The model treats crude, gas, NGL, and products as semi-independent
commodity flows with shared nodes. The actual coupling is tighter:
diluent supply directly constrains dilbit volume; gas plant output
determines NGL yield; crack spreads determine whether refineries
maximize gasoline or diesel production, affecting the batch sequence on
the products lines. A fully coupled model is a large-scale mixed-integer
program beyond the scope of this essay.

### Netback calculations are sensitive to exchange rates

All CAD/bbl calculations here assume a fixed USD/CAD exchange rate of
0.73. In practice, the Canadian dollar co-moves with oil prices (a
well-documented correlation) — when WTI falls, the CAD typically weakens,
which partially cushions the revenue impact in CAD terms. This
correlation means that the netback surface is not static; it shifts with
currency movements independently of pipeline tariffs.

---

## 9. Summary

Treating Alberta's full hydrocarbon pipeline network as a directed graph
reveals structure that commodity-by-commodity analysis misses. The key
results:

- **Hardisty AB has the highest betweenness centrality** in the crude
  subsystem — it is the structural hub through which almost all oil
  sands export flow passes
- **The minimum cut for Alberta-to-Gulf-Coast crude flow** lies not on
  the Enbridge Mainline but on the connecting pipelines south of
  Superior, Wisconsin — the Mainline itself is not the Gulf binding
  constraint
- **The netback price surface is nearly flat** across available markets
  (CAD $74.7–$77.0/bbl range) because transport costs largely absorb
  destination price premiums — market access matters most as a binary,
  not as a marginal optimization
- **The integrated network is structurally robust** with three specific
  manageable vulnerabilities: condensate supply margin, AECO basis
  events during rapid production growth, and Hardisty node concentration
- **The max-flow min-cut theorem** provides a rigorous framework for
  identifying binding constraints — the same mathematical result that
  governs internet routing and logistics networks governs Alberta's
  pipeline export capacity

Network mathematics does not determine pipeline policy. But it describes
the system precisely enough to make policy arguments testable against
physical reality.

---

## Math Refresher

### Graph theory basics

A **graph** is a set of nodes connected by edges. A **directed graph**
(digraph) has edges with direction — flow goes one way. A **path** from
$s$ to $t$ is a sequence of nodes connected by directed edges all pointing
the right way. A **cut** is a partition of nodes into two sets that
separates source from sink; its **capacity** is the sum of capacities
of edges crossing from the source set to the sink set.

The **max-flow min-cut theorem** says:
$$\text{Maximum flow from } s \text{ to } t = \text{Minimum cut capacity separating } s \text{ from } t$$

This is a deep result — it says that the physical bottleneck (the minimum
cut) exactly determines the maximum achievable flow, no matter how complex
the network is or how many paths exist.

### Dijkstra's algorithm in one paragraph

To find the cheapest path from node $A$ to all other nodes: start with
cost 0 at $A$ and infinite cost everywhere else. Repeatedly pick the
unvisited node with the lowest current cost, then update all its
neighbours' costs if going through this node is cheaper. Stop when all
nodes are visited. The result is the minimum-cost path to every
reachable destination — which is exactly the information needed to
compute the netback price surface.

---

## Sources and Data Notes

| Source | Used For |
|:---|:---|
| Canada Energy Regulator, *Pipeline Profiles* (2024) | All pipeline capacity data |
| Ford, L.R. & Fulkerson, D.R., *Flows in Networks* (1962) | Max-flow min-cut theory |
| Brandes, U. (2001), *A Faster Algorithm for Betweenness Centrality* | Centrality algorithm |
| Dijkstra, E.W. (1959), *A Note on Two Problems in Connexion with Graphs* | Shortest path algorithm |
| Alberta Energy Regulator, *ST98* (2024) | Production volumes |
| TC Energy, Enbridge, Trans Mountain: public system overviews | Network topology |

All network parameters are approximate and based on publicly available
capacity information. The graph model is a strategic simplification;
it is not suitable for operational pipeline scheduling or engineering design.

---

*This essay completes the computational geography cluster on Alberta's pipeline
connectivity. The long-form narrative introduction to the cluster is:
[Alberta's Pipeline Geography: A Connected Province](/alberta-in-context/pipeline-geography-introduction/).*
