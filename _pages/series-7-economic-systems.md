---
layout: page
permalink: /series/7/
title: "Series 7: Economic Systems"
subtitle: "Reading industries as spatial systems — infrastructure, flows, markets, and the mathematics that connects them"
series_number: 7
series_key: "Economic Systems"
total_essays: 10
difficulty_range: 2-4
estimated_hours: 40
tags: [economic-geography, modelling, networks, infrastructure, energy, trade]
---

## Series Overview

Where Series 1–6 build mathematical tools and apply them to physical geography — terrain, hydrology, climate, ice — this series works the other way around. We begin with a real industry system, ask geographic questions about it, and then develop the mathematics needed to answer them rigorously.

The subject matter is economic geography in the fullest sense: the spatial organisation of production, infrastructure, and exchange. The industries covered are not case studies chosen for illustration. They are the systems that structure where people live, how goods move, and what places can and cannot become. Understanding them as a systems-thinking geographer — quantitatively, spatially, critically — is a distinct and transferable skill.

Each cluster is an industry vertical. The mathematical tools introduced in one cluster recur and extend in later ones. By the end of the series, readers will have a working toolkit for reading any capital-intensive industry as a spatial system.

## Pedagogical Philosophy

**Domain first, mathematics second.** We do not introduce a theorem and then look for applications. We encounter a real system — a pipeline network, a commodity market, a trade corridor — ask what is actually happening and why it matters geographically, and then develop the mathematics that lets us answer precisely.

**Industries as geographic systems.** Every industry has spatial structure: nodes where things are produced or transformed, edges along which they move, constraints that determine what is possible, and price signals that reveal where the constraints bind. Geographic analysis identifies these structures; mathematical modelling quantifies their consequences.

**Transferable thinking across verticals.** The graph-theoretic tools used to analyse pipeline capacity in Cluster P reappear when analysing port networks in Cluster T. The price surface concepts from crude oil netbacks recur in spatial arbitrage and trade margin analysis. The series is structured so that each cluster reinforces and extends the last.

## Learning Objectives

By completing this series, readers will be able to:

1. **Decompose an industry into its spatial components** — identify nodes, flows, constraints, and price-forming mechanisms
2. **Apply graph theory to infrastructure networks** — directed graphs, capacity, max-flow min-cut, betweenness centrality
3. **Model price formation across space** — netback calculations, basis differentials, spatial arbitrage conditions
4. **Quantify infrastructure constraints and their economic consequences** — capacity utilisation, throughput economics, bottleneck identification
5. **Read commodity market data geographically** — connect price signals to physical infrastructure constraints
6. **Construct and interpret network flow models** — from pipeline systems to trade corridors and supply chains
7. **Apply systems thinking across industry contexts** — transfer tools and concepts from one vertical to another

## Mathematical Threads

The series introduces and develops five interlocking mathematical concepts:

**Graph theory and network flow** — directed graphs, adjacency, max-flow min-cut, betweenness centrality. Introduced in Cluster P (pipeline networks); extended in later clusters.

**Price surface analysis** — netback pricing, basis differentials, spatial arbitrage. The geographic insight that prices differ across space because of transport costs and constraints.

**Throughput and capacity economics** — utilisation rates, batch scheduling, inventory dynamics. The mathematics of moving things through constrained physical systems.

**Transport hydraulics** — pipe flow (Weymouth equation for gas, Darcy-Weisbach for liquids). The physics that sets the engineering constraints economic models must respect.

**Mass balance and commodity transformation** — fractionation yields, refinery product splits, input-output relationships. How physical transformation shapes what can be moved where.

## Prerequisites

**Assumed:** Algebra, unit conversion, proportional reasoning. Comfort reading quantitative analysis.

**Helpful but not required:** Series 1 (particularly Model 9: Graph Theory and Flow Routing; Model 10: Gravity Models). Series 1 develops the mathematical foundations; this series applies them to economic systems.

**Not assumed:** Economics training. Domain knowledge of any specific industry. We build what we need from first principles.

## Entry Points by Background

**Geography students:** Start at Model 1. The domain-first approach is designed for readers who understand place and space but may not have formal economics or mathematics training.

**Economics students:** The geographic framing — spatial constraints, infrastructure networks, regional price differentials — adds dimensions that standard economics training rarely covers. Models 4–5 (refined products logistics, integrated network) may be the most novel.

**Industry professionals (energy, transport, logistics):** The mathematical framing of systems you know operationally provides analytical tools for the kind of quantitative spatial reasoning that geographers bring to industry problems.

**Readers of the Alberta in Context essay series:** The models here are the quantitative underpinning of the arguments made in those essays. Reading both threads together — domain narrative alongside mathematical model — is the intended experience.

## Model Sequence

### Cluster P — Energy Infrastructure

Alberta's hydrocarbon pipeline system as a case study in network geography. Five models build from individual commodity streams to a unified network analysis.

**Model 1: Alberta's Crude Oil Pipeline Network**
The continental crude oil system — Enbridge, Trans Mountain, Keystone, Express. Volumetric flow rate, pipe hydraulics, capacity utilisation. Netback pricing: how transport tariffs and quality discounts shape the price received at the wellhead. Market direction and the geography of price discrimination.

**Model 2: NGL and Condensate Pipeline Systems**
The fractionation cascade — separating ethane, propane, butane, and condensate from raw NGL mix. Mass balance and yield ratios. The diluent supply chain: condensate flows north to dilute bitumen; dilbit flows south to refineries. A closed loop of commodity dependency.

**Model 3: Natural Gas Transmission from Alberta**
The NOVA intra-Alberta gathering network and its export corridors. The Weymouth equation: how pipe diameter, pressure differential, and gas properties determine throughput capacity. AECO vs Henry Hub: the basis differential as a measure of infrastructure constraint. Annual revenue foregone from the Canada-US price gap.

**Model 4: Refined Products Distribution**
Gasoline, diesel, and jet fuel from Alberta's refineries to western Canadian consumers. Batch scheduling and product sequencing in multi-product pipelines. Throughput rates, transit times, terminal inventory, and days of supply. The supply security arithmetic for an isolated market like British Columbia.

**Model 5: The Integrated Network**
Alberta's full hydrocarbon system as a directed network graph. Max-flow min-cut applied to each commodity stream. Betweenness centrality: which hubs are most critical to network function? The netback price surface across all market destinations. Sankey diagram of integrated commodity flows.

### Cluster T — Trade and Transport

Canada's goods trade as a spatial system: the gravity model as a geographic instrument, corridor analysis, port hierarchy, modal choice, and integrated network flow. Five models build from bilateral trade prediction to a full multi-modal network under a Windsor Corridor disruption scenario.

**Model 6: Canada's Trade Gravity Model**
The gravity equation — GDP, distance, and the border effect. Why Canadian provinces trade less with each other than distance predicts, and why Alberta's geography compounds the penalty. Calibration from bilateral trade data; the Anderson-van Wincoop structural form.

**Model 7: Canada's Trade Corridor Systems**
Three continental corridor systems — Windsor-Detroit (auto/manufacturing), Vancouver-Prince Rupert (Pacific gateway), Halifax-Montréal (Atlantic). Link capacity, chokepoint identification, Wardner equilibrium under demand variation. Leaflet map of the full corridor network.

**Model 8: Canada's Port Economics**
Port hierarchy from Vancouver to Thunder Bay. Throughput functions, economies of scale, queuing theory at constrained facilities. Hinterland catchment areas and the spatial economics of mode competition. TEU-equivalent cost structure by cargo type.

**Model 9: Freight Modal Split**
Cost functions for rail, truck, and marine by commodity class. Break-even distance thresholds. CN/CP duopoly and its geographic consequences. Discrete choice (logit) model: how shipper decisions aggregate to system-level modal share.

**Model 10: The Integrated Trade Network**
Canada's goods trade as a 12-node directed network: seven regional nodes, three gateway ports, two cross-border exchange points. Max-flow min-cut for each commodity class. Betweenness centrality reveals which nodes bind the system. The Windsor problem: corridor disruption propagation and redundancy arithmetic. Sankey diagram of integrated commodity flows.

### Cluster U — Urban Economic Systems *(planned)*

Land rent gradients, agglomeration economies, Zipf's law and the rank-size distribution of cities. The mathematics of where economic activity concentrates.

### Cluster R — Resource Economics *(planned)*

Extraction curves, royalty regimes, the Hotelling rule for optimal depletion. How geography shapes resource rents and the geographic distribution of resource wealth.

### Cluster M — Markets and Price Formation *(planned)*

Commodity pricing, spatial arbitrage, futures markets as geographic instruments. Price as a signal of spatial constraint.

## Estimated Time Investment

**Per model:** 2–4 hours (reading, working through examples, exploring visualisations)

**Cluster P (5 models):** 10–20 hours for thorough engagement

**Cluster T (5 models):** 10–20 hours for thorough engagement

**Accelerated path per cluster:** 6–10 hours (focus on visualisations and worked examples, skim derivations)

---

**Start with Cluster P:** [Alberta's Crude Oil Pipeline Network](/2026/03/08/alberta-pipeline-crude-oil/) — energy infrastructure, pipeline hydraulics, netback pricing.

**Start with Cluster T:** [Canada's Trade Gravity Model](/2026/03/09/canada-trade-gravity-model/) — bilateral trade, border effects, gravity equation.

**Companion reading:** [Alberta in Context](/series/alberta-in-context/) — the narrative essay series that applies these models to the political economy of a landlocked province.
