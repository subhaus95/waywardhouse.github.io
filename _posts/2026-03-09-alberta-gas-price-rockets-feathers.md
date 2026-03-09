---
layout: essay
title: "Rockets and Feathers"
subtitle: "Why Alberta pump prices spike overnight but fall for weeks — and whether this week's crude crash will actually reach the forecourt"
date: 2026-03-09
categories: [Economic Geography]
tags: [alberta, energy, oil-prices, inflation, market-structure, tag-hash-viz, tag-hash-story]
difficulty: 2
viz: true
image: /assets/images/pipeline-geography.png
excerpt: "WTI crude touched $119 a barrel on Sunday before the G7 coordinated a strategic reserve release and knocked it back to $104. By Monday morning, Calgary pumps had already repriced for the spike. Whether they'll reprice for the drop is a different question — one with a name in the economics literature: the rockets and feathers hypothesis."
description: >
  Gasoline pump prices in Alberta respond within hours to crude price increases and over weeks
  to decreases. This essay examines why, using this week's Iran-driven crude spike as a
  live case study, and what it means for Alberta consumers who are already paying some of
  the highest fuel prices in recent memory.
---

On Sunday afternoon, a Calgary resident checked the GassBuddy app and saw the station on their block sitting at 148.9 cents per litre. By Monday morning it had changed to 158.9. By Monday evening, after news broke that French President Macron and the G7 had agreed to coordinate a release of up to 400 million barrels from strategic petroleum reserves, WTI crude had dropped from its intraday high of approximately $119 a barrel to around $104 — a 13% retreat in hours. The station was still at 158.9.

This is the pattern that drives Alberta drivers to Reddit. Prices go up like a rocket. They come down like a feather. The lived experience is of a market that moves asymmetrically — fast when it hurts consumers, slow when it would help them. And the frustration is not misplaced: there is a substantial body of economic research confirming that the asymmetry is real, is structural, and is most pronounced in exactly the kind of market Alberta has.

---

## What Happened This Week

The crude oil market had been tracking Iran-related geopolitical risk since February. When U.S. and Israeli air strikes on Iranian nuclear and naval infrastructure were confirmed on Saturday, the Strait of Hormuz — through which approximately 20 million barrels of oil pass every day, roughly 20% of global seaborne supply — was effectively closed to commercial traffic by Iranian naval action. The market's reaction was immediate and extreme.

<div data-viz="echarts" style="height:360px" data-options='{"backgroundColor":"#0f172a","title":{"text":"WTI Crude: The Spike and the G7 Response, March 6–9, 2026","subtext":"Intraday prices — the entire move from $87 to $119 and back to $104 happened in under 72 hours","textStyle":{"color":"#f8fafc","fontSize":15},"subtextStyle":{"color":"#94a3b8","fontSize":11},"left":"center"},"tooltip":{"trigger":"axis","backgroundColor":"#1e293b","borderColor":"#334155","textStyle":{"color":"#f8fafc"}},"grid":{"left":"8%","right":"5%","bottom":"12%","containLabel":true},"xAxis":{"type":"category","data":["Fri Mar 6\nclose","Sat Mar 7\nmorning","Sat Mar 7\nevening","Sun Mar 8\nopen","Sun Mar 8\npeak","Mon Mar 9\nmorning","Mon Mar 9\npost-G7"],"axisLabel":{"color":"#94a3b8","fontSize":10},"axisLine":{"lineStyle":{"color":"#334155"}}},"yAxis":{"type":"value","name":"WTI USD/bbl","nameTextStyle":{"color":"#94a3b8"},"min":80,"max":130,"axisLabel":{"color":"#94a3b8"},"splitLine":{"lineStyle":{"color":"#1e293b"}},"axisLine":{"lineStyle":{"color":"#334155"}}},"series":[{"name":"WTI spot","type":"line","data":[87,94,103,110,119,115,104],"lineStyle":{"color":"#f59e0b","width":3},"itemStyle":{"color":"#f59e0b"},"symbol":"circle","symbolSize":7,"areaStyle":{"color":{"type":"linear","x":0,"y":0,"x2":0,"y2":1,"colorStops":[{"offset":0,"color":"rgba(245,158,11,0.2)"},{"offset":1,"color":"rgba(245,158,11,0)"}]}}},{"type":"line","markLine":{"silent":true,"lineStyle":{"color":"#ef4444","type":"dashed"},"label":{"color":"#ef4444","formatter":"Strait of Hormuz closed"},"data":[{"xAxis":"Sat Mar 7\nevening"}],"symbol":["none","none"]},"data":[]},{"type":"line","markLine":{"silent":true,"lineStyle":{"color":"#16a34a","type":"dashed"},"label":{"color":"#16a34a","formatter":"G7 SPR announcement"},"data":[{"xAxis":"Mon Mar 9\npost-G7"}],"symbol":["none","none"]},"data":[]}]}'></div>

<p class="viz-caption">Source: OilPrice.com (<https://oilprice.com>), CNBC, Reuters. WTI intraday prices are approximate; the exact peak touched $119–120/bbl in Sunday evening electronic trading before retreating. Brent crude followed a near-identical pattern, peaking near $119.50.</p>

The G7 response — confirmed Monday morning by Macron as rotating G7 president, following an emergency call with IEA Director Fatih Birol — proposed releasing up to 400 million barrels from strategic petroleum reserves across the G7 nations. This would be the largest coordinated SPR release in history, roughly twice the size of the 180–240 million barrel IEA release following Russia's invasion of Ukraine in 2022. Markets responded: Brent dropped from $119.50 to around $106, WTI fell to approximately $104.

Whether the G7 release will hold prices down is a different question. The strategic reserves exist to buffer short-term supply shocks. They do not produce new oil. If the Strait of Hormuz remains effectively closed, the 400 million barrel release buys roughly 20 days of the disrupted supply — time for diplomatic resolution or military de-escalation, not a permanent fix. Analysts at Goldman Sachs and JP Morgan were already noting Monday afternoon that the market would quickly price in the sustainability question.

Calgary pump prices as of Monday evening, March 9: **154.9 cents per litre** at the most competitive stations, up from 148.9 at the same stations on Friday. The crude market had already moved up and partially back. The pump had moved up and not moved back.

---

## Two Years of Prices — and What They Actually Reflect

<section class="story-section">
  <div class="story-sticky">
    <div class="story-graphic">
      <div id="pump-chart" data-viz="echarts" data-options='{"backgroundColor":"#0f172a","title":{"text":"Alberta Pump Price vs WTI Crude, 2024–2026","subtext":"Scroll through the story to see what drove each movement","textStyle":{"color":"#f8fafc","fontSize":14},"subtextStyle":{"color":"#94a3b8","fontSize":11},"left":"center"},"tooltip":{"trigger":"axis","backgroundColor":"#1e293b","borderColor":"#334155","textStyle":{"color":"#f8fafc"}},"legend":{"data":["Calgary pump price (c/L)","WTI crude (USD/bbl, right)"],"bottom":10,"textStyle":{"color":"#cbd5e1"}},"grid":{"left":"8%","right":"10%","bottom":"15%","containLabel":true},"xAxis":{"type":"category","data":["Jan 24","Mar 24","May 24","Jul 24","Sep 24","Nov 24","Jan 25","Mar 25","May 25","Jul 25","Sep 25","Nov 25","Jan 26","Mar 9/26"],"axisLabel":{"color":"#94a3b8","rotate":30,"fontSize":10},"axisLine":{"lineStyle":{"color":"#334155"}}},"yAxis":[{"type":"value","name":"Pump price (c/L)","nameTextStyle":{"color":"#94a3b8"},"min":100,"max":175,"axisLabel":{"color":"#94a3b8"},"splitLine":{"lineStyle":{"color":"#1e293b"}},"axisLine":{"lineStyle":{"color":"#334155"}}},{"type":"value","name":"WTI (USD/bbl)","nameTextStyle":{"color":"#94a3b8"},"min":50,"max":130,"axisLabel":{"color":"#94a3b8"},"splitLine":{"show":false},"axisLine":{"lineStyle":{"color":"#334155"}}}],"series":[{"name":"Calgary pump price (c/L)","type":"line","yAxisIndex":0,"data":[122,131,143,148,124,130,145,140,150,155,135,138,148,155],"lineStyle":{"color":"#f59e0b","width":3},"itemStyle":{"color":"#f59e0b"},"symbol":"circle","symbolSize":5},{"name":"WTI crude (USD/bbl, right)","type":"line","yAxisIndex":1,"data":[73,80,79,81,68,70,75,68,65,68,66,70,75,104],"lineStyle":{"color":"#64748b","width":2,"type":"dashed"},"itemStyle":{"color":"#64748b"},"symbol":"circle","symbolSize":5}]}'></div>
    </div>
  </div>
  <div class="story-steps">
    <div class="story-step" data-step="0"
         data-update='{"pump-chart": {"title": {"subtext": "Two years of Calgary pump prices vs WTI crude — spot the disconnects"}}}'>
      <h3>The two-year picture</h3>
      <p>The amber line is what Calgarians paid at the pump. The grey dashed line is what a barrel of WTI crude cost in US dollars on the same day. They should track each other — and they do, roughly. But the relationship has been distorted by tax policy, refinery margins, and market structure.</p>
      <p>The most obvious disconnect is January 2024 versus January 2025: prices are higher in January 2025 despite crude being barely different. Tax policy explains part of that gap.</p>
    </div>
    <div class="story-step" data-step="1"
         data-update='{"pump-chart": {"title": {"subtext": "2024: The provincial fuel tax holiday held prices down — artificially"},"series": [{"markArea": {"silent": true, "itemStyle": {"color": "rgba(22,163,74,0.12)", "borderColor": "#16a34a", "borderWidth": 1}, "label": {"color": "#16a34a", "position": "insideTop", "formatter": "AB tax waived"}, "data": [[{"xAxis": "Jan 24"}, {"xAxis": "Nov 24"}]]}},{}]}}'>
      <h3>2024: The tax holiday</h3>
      <p>Through most of 2024, the Alberta government waived its 13 cents/litre provincial fuel tax as part of the Affordability Action Plan. This held pump prices approximately 13 c/L below where they would otherwise have been.</p>
      <p>The result: Alberta had the cheapest gasoline in Canada through 2024, and WTI prices declining through the second half of the year pushed pump prices down further. Consumers felt relief. But the tax waiver was masking the underlying cost structure — a fact that became apparent the moment it ended.</p>
    </div>
    <div class="story-step" data-step="2"
         data-update='{"pump-chart": {"title": {"subtext": "January 2025: The tax comes back — prices jump 12.5 c/L overnight"},"series": [{"markArea": {"silent": true, "itemStyle": {"color": "rgba(239,68,68,0.12)", "borderColor": "#ef4444", "borderWidth": 1}, "label": {"color": "#ef4444", "position": "insideTop", "formatter": "Tax reinstated"}, "data": [[{"xAxis": "Jan 25"}, {"xAxis": "Mar 25"}]]}},{}]}}'>
      <h3>January 2025: The overnight jump</h3>
      <p>On January 1, 2025, the provincial fuel tax was reinstated at 12.5 cents per litre. Pump prices jumped almost exactly that amount the same day — before crude prices had moved at all.</p>
      <p>This illustrates the first asymmetry: cost increases pass through immediately. The tax reinstatement is not the same as a crude price move, but the mechanism is identical — any upward cost pressure at the wholesale level appears at the pump within hours.</p>
    </div>
    <div class="story-step" data-step="3"
         data-update='{"pump-chart": {"title": {"subtext": "March 2026: WTI spikes 45% in 72 hours — pump responds in 24"},"series": [{"markArea": {"silent": true, "itemStyle": {"color": "rgba(245,158,11,0.15)", "borderColor": "#f59e0b", "borderWidth": 1.5}, "label": {"color": "#f59e0b", "position": "insideTop", "formatter": "Mar 2026"}, "data": [[{"xAxis": "Jan 26"}, {"xAxis": "Mar 9/26"}]]}},{}]}}'>
      <h3>This week: the Hormuz spike</h3>
      <p>WTI went from roughly $87/bbl on Friday to $119 intraday Sunday — a 37% move in 48 hours. Calgary pump prices responded within 24 hours, adding 7 cents per litre by Monday morning.</p>
      <p>Note that the G7 SPR announcement has already knocked WTI back to approximately $104 — still elevated, but 13% below the peak. The pump price has not yet moved back. This is not unusual. This is the pattern.</p>
    </div>
    <div class="story-step" data-step="4"
         data-update='{"pump-chart": {"title": {"subtext": "The pattern: quick up, slow down — visible across the full two-year window"},"series": [{"markArea": {"silent": true, "itemStyle": {"color": "rgba(239,68,68,0.08)"}, "label": {"color": "#f87171", "position": "insideTop", "fontSize": 10}, "data": [[{"xAxis": "Jan 24", "name": "Spike 1"}, {"xAxis": "Mar 24"}],[{"xAxis": "May 25", "name": "Spike 2"}, {"xAxis": "Jul 25"}],[{"xAxis": "Jan 26", "name": "Hormuz spike"}, {"xAxis": "Mar 9/26"}]]}},{}]}}'>
      <h3>The rockets and feathers pattern</h3>
      <p>Look at the three periods where pump prices climbed quickly: early 2024, mid-2025, and right now. In each case, crude moved up and prices followed within days.</p>
      <p>Now look at September 2024 and September 2025 — the months after summer peaks. In both cases, crude had already fallen, but pump prices took four to six weeks to reflect the full decline. The upward movements are fast. The downward movements are gradual. That asymmetry has a name.</p>
    </div>
  </div>
</section>

---

## What Actually Determines the Pump Price

Before explaining why the asymmetry exists, it helps to understand what the pump price is made of. At 154.9 cents per litre in Calgary today:

<div data-viz="echarts" style="height:300px" data-options='{"backgroundColor":"#0f172a","title":{"text":"What Is in the Calgary Pump Price: March 9, 2026","subtext":"154.9 c/L — crude and refining account for more than half; taxes add roughly 30 c/L","textStyle":{"color":"#f8fafc","fontSize":15},"subtextStyle":{"color":"#94a3b8","fontSize":11},"left":"center"},"tooltip":{"trigger":"item","formatter":"{b}: {c} c/L ({d}%)","backgroundColor":"#1e293b","borderColor":"#334155","textStyle":{"color":"#f8fafc"}},"legend":{"orient":"vertical","left":"left","top":"middle","textStyle":{"color":"#cbd5e1"},"itemGap":8},"series":[{"type":"pie","radius":["35%","65%"],"center":["62%","52%"],"data":[{"value":65,"name":"Crude oil cost (at WTI $104, CAD converted)","itemStyle":{"color":"#78350f"}},{"value":32,"name":"Refining margin","itemStyle":{"color":"#f97316"}},{"value":10,"name":"Federal excise tax","itemStyle":{"color":"#1e40af"}},{"value":13,"name":"Alberta provincial fuel tax (reinstated Jan 2025)","itemStyle":{"color":"#2563eb"}},{"value":7,"name":"GST (5% on total)","itemStyle":{"color":"#3b82f6"}},{"value":6,"name":"Transport and retail margin","itemStyle":{"color":"#64748b"}},{"value":22,"name":"Wholesale/rack margin and blending costs","itemStyle":{"color":"#dc2626"}}],"label":{"color":"#f8fafc","fontSize":10,"formatter":"{d}%"},"emphasis":{"itemStyle":{"shadowBlur":10,"shadowColor":"rgba(0,0,0,0.5)"}}}]}'></div>

<p class="viz-caption">Source: Natural Resources Canada, "Transportation Fuel Prices" (<https://natural-resources.canada.ca/domestic-international-markets/transportation-fuel-prices>); author calculation at current WTI ~$104 CAD-adjusted. Crude cost converted at CAD/USD ~1.44. Note: no federal consumer carbon levy (removed April 2025). Components are approximate and vary by station and supply chain.</p>

The crude oil component at current prices is roughly 65 cents of a 154.9 c/L price — about 42%. The refining margin (converting crude to gasoline) adds another 32 cents. Then come the taxes: federal excise (10 c/L, fixed), provincial fuel tax (12.5 c/L, reinstated in 2025), and GST (5% on the combined total, which compounds with price — higher crude means higher GST revenue). The wholesale/rack margin and blending costs cover the distribution from refinery to terminal to station.

The critical insight is that the crude oil component is the most volatile. When WTI moves 37% in 48 hours, the crude component of the pump price moves by a similar proportion — which is why prices that started at 148.9 c/L moved to approximately 154–158 c/L almost immediately. The taxes are fixed. The refining margin moves slowly. The rack margin moves quickly because refiners and wholesale distributors price on replacement cost, not historical cost.

---

## The Rockets and Feathers Hypothesis

The asymmetric price adjustment has a name in the economics literature: the **rockets and feathers hypothesis**. Prices rocket up and float down like feathers. The phenomenon was first formally documented by Robert Bacon in 1991 studying UK petrol markets, and was confirmed empirically for U.S. gasoline by Borenstein, Cameron and Gilbert in 1997 — now one of the most-cited papers in energy economics.

<div data-viz="echarts" style="height:340px" data-options='{"backgroundColor":"#0f172a","title":{"text":"The Rockets and Feathers Pattern: Crude vs Pump (Stylised)","subtext":"Days relative to a crude price shock — prices rise in ~4 days, fall over ~28-40 days","textStyle":{"color":"#f8fafc","fontSize":15},"subtextStyle":{"color":"#94a3b8","fontSize":11},"left":"center"},"tooltip":{"trigger":"axis","backgroundColor":"#1e293b","borderColor":"#334155","textStyle":{"color":"#f8fafc"}},"legend":{"data":["Crude price shock (normalised)","Pump price — upward shock","Pump price — downward shock"],"bottom":10,"textStyle":{"color":"#cbd5e1"},"type":"scroll"},"grid":{"left":"8%","right":"5%","bottom":"18%","containLabel":true},"xAxis":{"type":"category","data":["Day 0","Day 2","Day 4","Day 6","Day 8","Day 10","Day 14","Day 21","Day 28","Day 35","Day 42"],"axisLabel":{"color":"#94a3b8"},"axisLine":{"lineStyle":{"color":"#334155"}}},"yAxis":{"type":"value","name":"% of shock transmitted","nameTextStyle":{"color":"#94a3b8"},"min":0,"max":105,"axisLabel":{"color":"#94a3b8","formatter":"{value}%"},"splitLine":{"lineStyle":{"color":"#1e293b"}},"axisLine":{"lineStyle":{"color":"#334155"}}},"series":[{"name":"Crude price shock (normalised)","type":"line","data":[0,100,100,100,100,100,100,100,100,100,100],"lineStyle":{"color":"#64748b","width":1,"type":"dashed"},"symbol":"none","itemStyle":{"color":"#64748b"}},{"name":"Pump price — upward shock","type":"line","data":[0,45,78,90,95,98,100,100,100,100,100],"lineStyle":{"color":"#ef4444","width":3},"itemStyle":{"color":"#ef4444"},"symbol":"none"},{"name":"Pump price — downward shock","type":"line","data":[0,10,18,25,35,42,52,68,78,88,96],"lineStyle":{"color":"#16a34a","width":3},"itemStyle":{"color":"#16a34a"},"symbol":"none"}]}'></div>

<p class="viz-caption">Source: Stylised representation based on Borenstein, Cameron, and Gilbert (1997) (<https://doi.org/10.1162/003355397555118>); Antweiler (2015) Canadian analysis (<https://wernerantweiler.ca/blog.php?item=2015-04-22>); author. Upward pass-through: approximately 50% within 2 days, 90%+ within 8 days. Downward pass-through: 50% takes approximately 21 days in Canadian markets (Antweiler 2015 estimate for Vancouver; Alberta likely similar).</p>

Werner Antweiler at UBC analysed 779 weekly observations of Vancouver pump prices from 2000 to 2014. He found the asymmetry is statistically significant but estimated it as "economically modest" in the Vancouver context — upward price movements are approximately 4% ahead of downward movements per period, with roughly six weeks required for half of a price shock to fully transmit downward.

The Canadian result is smaller than the U.S. equivalent, likely because Canadian retail margins are thinner (typically 5–8 c/L versus 10–15 c/L in the U.S.), leaving retailers less room to absorb cost changes in either direction. They must pass through immediately on the way up; but they also have less incentive to hold margins artificially high on the way down, since they're not particularly profitable to start with. The asymmetry exists, but it is not primarily a profit-padding phenomenon — it has structural explanations.

### Why the Asymmetry Exists: The Three Mechanisms

**Inventory accounting.** Retail stations buy fuel from terminals at rack prices. When a station loads 30,000 litres at a rack price set before the crude price jump, it has purchased that fuel at the old price. The next day, the rack price is higher — the station prices its *existing* inventory at the *new* replacement cost, not the historical cost. This maximises margin on the inventory it already paid for at lower prices. When crude falls, the reverse happens: the station has inventory purchased at the higher price, and prices it at replacement cost — but replacement cost is now lower. The station holds the higher price until inventory turns over, which takes days to a week depending on throughput.

**Rack price signalling.** Wholesale terminal operators (Suncor, Shell, Imperial/Esso dominate the Alberta market) set rack prices daily and sometimes multiple times per day. These rack prices signal to retailers what their next load will cost. Retailers with thin margins use the rack price almost mechanically to set retail price, adding their fixed margin. When the rack jumps, retail jumps. When the rack falls, the signal reaches retail — but retailers check that competitors haven't already adjusted before they move, producing coordination-via-observation that slows downward price moves.

**Consumer search behaviour.** Consumers search harder for cheaper prices when prices are high — they drive past stations, check GassBuddy, fill up across town. They search less actively when prices are low. This means that the competitive pressure that forces prices down is weaker precisely when prices are high and retailers have the most to gain from holding. When prices fall back, consumer urgency drops — and so does the competitive pressure that would accelerate the descent.

---

## The Market Structure Problem

Alberta's retail gasoline market is not oligopolistic in the classic sense — there are hundreds of retail stations. But the wholesale tier is concentrated. Suncor Energy, through its Petro-Canada brand, Shell Canada, and Imperial Oil (under the Esso brand) collectively supply the majority of Alberta's retail gasoline volume from their refineries and terminals. These three are competitors at retail but near-monopolists at the refining and terminal level in specific regions of the province.

<div data-viz="echarts" style="height:280px" data-options='{"backgroundColor":"#0f172a","title":{"text":"Alberta Retail Gasoline: Brand Share by Volume","subtext":"Approximate station count and volume — wholesale tier is more concentrated than retail brand share suggests","textStyle":{"color":"#f8fafc","fontSize":15},"subtextStyle":{"color":"#94a3b8","fontSize":11},"left":"center"},"tooltip":{"trigger":"item","formatter":"{b}: {c}%","backgroundColor":"#1e293b","borderColor":"#334155","textStyle":{"color":"#f8fafc"}},"legend":{"orient":"vertical","left":"left","top":"middle","textStyle":{"color":"#cbd5e1"}},"series":[{"type":"pie","radius":["35%","65%"],"center":["62%","52%"],"data":[{"value":28,"name":"Petro-Canada (Suncor)","itemStyle":{"color":"#dc2626"}},{"value":22,"name":"Esso (Imperial/ExxonMobil)","itemStyle":{"color":"#f97316"}},{"value":18,"name":"Shell","itemStyle":{"color":"#f59e0b"}},{"value":12,"name":"Co-op / Fas Gas","itemStyle":{"color":"#16a34a"}},{"value":9,"name":"Costco","itemStyle":{"color":"#2563eb"}},{"value":11,"name":"Independents and other brands","itemStyle":{"color":"#64748b"}}],"label":{"color":"#f8fafc","fontSize":11,"formatter":"{d}%"},"emphasis":{"itemStyle":{"shadowBlur":10,"shadowColor":"rgba(0,0,0,0.5)"}}}]}'></div>

<p class="viz-caption">Source: Canadian Fuels Association (<https://www.canadianfuels.ca/our-industry/fuel-retailing/>); Kalibrate (formerly Kent Group) Canadian petroleum price snapshot, 2024 (<https://kalibrate.com/canada/>). Volume share differs from station count share — Costco's high-throughput stations punch above their count share in volume.</p>

The two structural brakes on downward price movement in Alberta are worth naming clearly.

**Focal pricing.** In concentrated retail markets, prices tend to cluster at focal points — typically ending in 9. Stations watch each other and move together rather than competing aggressively on margin. There is no explicit coordination (that would be illegal price-fixing), but the economic incentive to observe competitors before cutting price is rational. No station wants to be the first to cut and lose margin; each waits for evidence that the market has shifted. On the way up, this wait-and-see dynamic disappears — every station raises immediately because nobody loses customers by matching a market-wide increase.

**Costco as price leader.** Costco's model is genuinely different: low fuel margins are a membership incentive. Costco typically prices 3–6 c/L below the branded market in Alberta. Its pricing influence is real but geographically limited — only locations within driving distance of a Costco benefit from the price discipline it provides. In rural Alberta and smaller cities, the Costco effect is absent.

The Competition Bureau of Canada has examined retail gasoline pricing multiple times. It has not found evidence of illegal coordination. What it has found — and what the economic evidence confirms — is that the market structure creates conditions where upward price transmission is fast and complete, while downward transmission is slow and incomplete, through entirely legal mechanisms.

---

## Will Prices Actually Fall?

The question Alberta drivers are asking right now: WTI dropped from $119 to $104 on Monday. Will the pump follow?

The answer is: eventually, partially, and more slowly than it rose.

The complicating factor this week is that the G7 SPR release addresses only the supply shock, not the underlying geopolitical risk. If the Strait of Hormuz remains disrupted, each barrel from the strategic reserves is a one-time draw on a finite stockpile. The market is already pricing in the sustainability question — Goldman Sachs analysts noted Monday that with the Strait still closed, WTI is unlikely to return to its pre-Hormuz level of $87 until commercial shipping resumes. A $100–$110 range is the market's current expectation for the resolution scenario; higher if the closure extends.

<div data-viz="echarts" style="height:300px" data-options='{"backgroundColor":"#0f172a","title":{"text":"Market Scenarios: Where Could WTI Go from Here?","subtext":"Current: ~$104/bbl — range of outcomes depending on Strait of Hormuz resolution timeline","textStyle":{"color":"#f8fafc","fontSize":15},"subtextStyle":{"color":"#94a3b8","fontSize":11},"left":"center"},"tooltip":{"trigger":"axis","backgroundColor":"#1e293b","borderColor":"#334155","textStyle":{"color":"#f8fafc"}},"legend":{"data":["Rapid resolution (1–2 wks)","Moderate disruption (1–2 mo)","Extended closure (3–6 mo)"],"bottom":10,"textStyle":{"color":"#cbd5e1"}},"grid":{"left":"8%","right":"5%","bottom":"18%","containLabel":true},"xAxis":{"type":"category","data":["Today\nMar 9","Week 1","Week 2","Week 4","Week 6","Week 8","Week 12"],"axisLabel":{"color":"#94a3b8","fontSize":10},"axisLine":{"lineStyle":{"color":"#334155"}}},"yAxis":{"type":"value","name":"WTI USD/bbl","nameTextStyle":{"color":"#94a3b8"},"min":70,"max":140,"axisLabel":{"color":"#94a3b8"},"splitLine":{"lineStyle":{"color":"#1e293b"}},"axisLine":{"lineStyle":{"color":"#334155"}}},"series":[{"name":"Rapid resolution (1–2 wks)","type":"line","data":[104,98,92,88,87,87,87],"lineStyle":{"color":"#16a34a","width":2},"itemStyle":{"color":"#16a34a"},"symbol":"circle","symbolSize":5},{"name":"Moderate disruption (1–2 mo)","type":"line","data":[104,106,103,100,96,90,88],"lineStyle":{"color":"#f59e0b","width":2},"itemStyle":{"color":"#f59e0b"},"symbol":"circle","symbolSize":5},{"name":"Extended closure (3–6 mo)","type":"line","data":[104,110,115,118,122,125,130],"lineStyle":{"color":"#ef4444","width":2},"itemStyle":{"color":"#ef4444"},"symbol":"circle","symbolSize":5}]}'></div>

<p class="viz-caption">Source: Author scenarios based on Goldman Sachs energy research note, March 9, 2026 (no public URL available); JPMorgan Commodities research (no public URL available); IEA energy security analysis (<https://www.iea.org/articles/frequently-asked-questions-on-energy-security>). The rapid resolution scenario implies a return to pre-crisis $87/bbl levels over 4–6 weeks. Extended closure would push prices well above the Sunday peak.</p>

In the rapid resolution scenario — the Strait reopens within two weeks, G7 reserves buffer the short-term gap — Alberta pump prices could be back below 145 c/L by late March. In the moderate disruption scenario, expect 150–155 c/L through April. In the extended closure scenario, the Sunday high of 158–160 c/L becomes the floor, not the peak.

The rockets-and-feathers research gives us a reasonable calibration for the downward path. Even in the rapid resolution scenario, history suggests prices will decline roughly as follows: 3–4 c/L in the first week after crude falls, another 3–4 c/L in the second week, and the remainder over weeks three through six. The full decline from 158 c/L to a hypothetical 140 c/L — a drop of 18 c/L — would likely take four to six weeks to fully appear at the pump, even if crude prices move there in a matter of days.

---

## What This Means for Alberta Drivers

Consumers paying 154.9 c/L in Calgary today are paying the equivalent of approximately &#36;1.40–&#36;1.50 per litre in real terms relative to the 2019 baseline, after adjusting for general inflation. Fuel is consuming a meaningfully larger share of household budgets than it did five years ago, particularly for lower-income households and for those in regions of the province without transit alternatives to car ownership.

The GassBuddy app and similar price-comparison tools have reduced the asymmetry somewhat at the retail level by making consumer search dramatically cheaper. When prices spike, the proportion of consumers actively comparison-shopping increases — and that consumer behaviour creates competitive pressure on individual stations to price competitively even in a rising market. But the app cannot fix the wholesale structure: if every terminal in a region is charging a higher rack price, every retailer will charge more regardless of how aggressively consumers shop.

The Competition Bureau's most practical recommendation for this market has been transparency: requiring refiners to publish rack prices publicly, making the wholesale price signal visible to regulators and media. This is not price control. It is the informational precondition for effective competition.

The longer-run policy question — whether Alberta should revisit its fuel tax volatility management, whether the federal government should implement a price-smoothing mechanism analogous to what some European countries use during supply shocks — is outside the scope of a Monday morning analysis. But the consumer frustration driving those Reddit threads is pointing at a structural reality, not a misunderstanding of how markets work.

The market works exactly as it was designed to. That is precisely the problem.

---

*Crude oil price data: OilPrice.com, Reuters, CNBC (March 6–9, 2026). Alberta pump price data: Gas Wizard (gaswizard.ca), GassBuddy. Historical prices: Statistics Canada Table 18-10-0001-01; Kalibrate Canadian Petroleum Price Snapshot series; GlobalPetrolPrices.com. Pump price component estimates: Natural Resources Canada fuel price components methodology. Rockets and feathers research: Borenstein, Cameron and Gilbert (1997); Antweiler (2015); St. Louis Fed (2014). Market structure data: Canadian Fuels Association; Kent Group fuel retail estimates.*

## References

Antweiler, Werner. 2015. "Do Gasoline Prices Rise Like Rockets and Fall Like Feathers?" *Werner Antweiler's Blog*, University of British Columbia Sauder School of Business, April 22. <https://wernerantweiler.ca/blog.php?item=2015-04-22>

Bacon, Robert W. 1991. "Rockets and Feathers: The Asymmetric Speed of Adjustment of UK Retail Gasoline Prices to Cost Changes." *Energy Economics* 13 (3): 211–218. <https://doi.org/10.1016/0140-9883(91)90022-R>

Borenstein, Severin, A. Colin Cameron, and Richard Gilbert. 1997. "Do Gasoline Prices Respond Asymmetrically to Crude Oil Price Changes?" *Quarterly Journal of Economics* 112 (1): 305–339. <https://doi.org/10.1162/003355397555118>

Canadian Fuels Association. 2024. "Fuel Retailing." <https://www.canadianfuels.ca/our-industry/fuel-retailing/>

Competition Bureau Canada. 2023. *Canada Needs More Grocery Competition: Retail Grocery Market Study Report*. June 27. <https://competition-bureau.canada.ca/en/retail-grocery-market-study>

International Energy Agency. 2022. "IEA Member Countries to Make 60 Million Barrels of Oil Available Following Russia's Invasion of Ukraine." March 1. <https://www.iea.org/news/iea-member-countries-to-make-60-million-barrels-of-oil-available-following-russias-invasion-of-ukraine>

Natural Resources Canada. 2024. "Transportation Fuel Prices." <https://natural-resources.canada.ca/domestic-international-markets/transportation-fuel-prices>

Natural Resources Canada. 2024. "Diesel Prices." <https://natural-resources.canada.ca/domestic-international-markets/diesel-prices>

Owyang, Michael T., and E. Katarina Vermann. 2014. "Rockets and Feathers: Why Don't Gasoline Prices Always Move in Sync with Oil Prices?" *The Regional Economist*, Federal Reserve Bank of St. Louis, October. <https://www.stlouisfed.org/publications/regional-economist/october-2014/rockets-and-feathers-why-dont-gasoline-prices-always-move-in-sync-with-oil-prices>

Peltzman, Sam. 2000. "Prices Rise Faster than They Fall." *Journal of Political Economy* 108 (3): 466–502. <https://doi.org/10.1086/262126>

Statistics Canada. 2024. "Monthly Average Retail Prices for Gasoline and Fuel Oil, by Geography." Table 18-10-0001-01. <https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000101>

Statistics Canada. 2024. "Consumer Price Index, Monthly, Not Seasonally Adjusted." Table 18-10-0004-01. <https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401>
