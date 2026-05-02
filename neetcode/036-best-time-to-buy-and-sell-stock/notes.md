**Best Time to Buy and Sell Stock**

**Problem:** Given an array of prices, find the maximum profit from a single buy and sell. You must buy before you sell. Return 0 if no profit is possible.

---

**My initial approach (Brute Force):**
I started with a nested loop. For each day `i` (buy), I checked every future day `j` (sell) and tracked the maximum `sell - buy`. This works correctly but is slow.

- `j` starts at `i + 1` because you cannot sell before buying.
- Time: O(n²) — because for each `i`, the inner loop runs `n-i` times, totalling `n(n-1)/2` which simplifies to O(n²). In Big O we drop constants (`/2`) and lower order terms (`-n`).
- Space: O(1)

---

**Optimised approach (Two Pointers):**
The key insight is: as we scan through prices, we always want to buy at the cheapest price seen so far. If we find a day cheaper than our current buy day, we switch to it — because subtracting a smaller buy from any future sell will always give more profit.

- `buy` starts at index 0, `sell` starts at index 1
- If `prices[sell] > prices[buy]` → calculate profit and update `max_profit`
- If `prices[sell] < prices[buy]` → set `buy = sell` (found a cheaper day)
- `sell` increments every iteration, `buy` only moves when a cheaper price is found
- We loop on `sell` not `buy`, because buy can stay fixed at the cheapest day

- Time: O(n) — single pass through the array
- Space: O(1)

---

**Pseudocode:**
```
set max_profit = 0
set buy = 0, sell = 1

while sell < len(prices):
    if prices[sell] > prices[buy]:
        update max_profit with (prices[sell] - prices[buy])
    else:
        buy = sell
    sell += 1

return max_profit
```

---

**Mistakes & things to remember:**
- My first code attempt was buggy — it tried to track buy/sell with conditions on adjacent elements, which didn't correctly find the global minimum buy
- Don't forget: Big O drops constants and lower order terms — `n(n-1)/2` is still O(n²)
- The reason `buy = sell` works: any future sell minus a cheaper buy will **always** be better, so there's no reason to keep the old buy day

---

**Cleanup reminder for interviews:**
These two lines:
```python
profit = prices[sell] - prices[buy]
max_profit = max(max_profit, profit)
```
can be written as one:
```python
max_profit = max(max_profit, prices[sell] - prices[buy])
```
Small thing, but shows Python fluency in interviews!