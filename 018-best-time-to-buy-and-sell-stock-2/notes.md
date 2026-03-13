**Best Time to Buy and Sell Stock II**

**The idea:**
Buy and sell every consecutive day where tomorrow's price is higher than today's. Collecting all small daily profits always adds up to the same maximum profit as finding the perfect buy/sell window — because `(2-1) + (3-2) = (3-1)`. No need to track buy/sell state at all.

**The mistake I almost made:**
Overcomplicating it — thinking I needed to track when to buy, when to sell, and all possible windows. The insight is simpler: just collect every upward difference.

**Why `range(len(prices)-1)`:**
Because we check `prices[i+1]` inside the loop, so we must stop one step before the end, otherwise we get an index out of bounds error.

**What I learned:**
- Medium doesn't always mean complex algorithms — sometimes the hard part is just the insight
- This is part of a family of Buy and Sell Stock problems (I, II, III, IV) — the later ones are genuinely harder with DP
- Greedy works here: taking every small profit is always optimal

**Time:** O(n) — one pass through the array
**Space:** O(1) — only one variable `total`

