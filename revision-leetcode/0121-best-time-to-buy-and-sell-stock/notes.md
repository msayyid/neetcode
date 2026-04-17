# 🧠 Problem: Best Time to Buy and Sell Stock I

### Goal

* Buy once, sell once
* Maximize profit
* Must **buy before you sell**

---

# 🔴 Approach 1: Brute Force

## Idea

* Try **every possible pair** of days
* For each day `i` (buy), try all future days `j` (sell)

---

## Logic

* Loop through all `i`
* For each `i`, loop through `j > i`
* Compute:

  ```
  profit = prices[j] - prices[i]
  ```
* Track maximum profit

---

## Complexity

* Time: O(n²)
* Space: O(1)

---

## Why it works

* Checks **all valid buy-sell combinations**
* Guaranteed correct but slow

---

## Mistakes to avoid

* ❌ Using `min(prices)` and `max(prices)` directly
  → ignores order (buy must come first)

---

## When to mention in interview

* Always start with brute force
* Then optimize

---

# 🟢 Approach 2: Optimal (Greedy / One Pass)

## Core Idea

* Track **minimum price so far**
* At each step:

  * pretend you sell today
  * compute profit from best buy so far

---

## Logic

* Keep:

  * `l` → index of minimum price (buy day)
  * `profit` → max profit so far

* For each day `i`:

  * If current price is smaller → update `l`
  * Else → calculate profit and update max

---

## Key Insight

> The best sell today depends on the **lowest price before today**

---

## Complexity

* Time: O(n)
* Space: O(1)

---

## Why it works

* Instead of checking all pairs:

  * we **carry the best buy forward**
* Eliminates inner loop → faster

---

## Mistakes you made (important)

* ❌ Not updating `l` → always using first price
* ❌ Thinking total profit matters (that’s a different problem - Stock II)

---

## Pattern recognition

Use this when:

* Only **one transaction allowed**
* Need **max difference with order**

---

## One-line memory

> “Track min so far, maximize profit”

---

# ⚖️ Comparison Summary

| Approach    | Idea            | Time  | Use                |
| ----------- | --------------- | ----- | ------------------ |
| Brute Force | try all pairs   | O(n²) | baseline           |
| Optimal     | track min price | O(n)  | interview solution |

---

# 🔁 Final intuition

* Brute force = “check everything”
* Optimal = “carry best buy forward”