# Online Stock Span - Revision Notes

## 1. Problem Summary

We need to design a class called `StockSpanner`.

Each time `next(price)` is called, we are given today's stock price.

We must return the **span** of today's price.

The span means:

> Starting from today and going backward, count how many consecutive days had price less than or equal to today's price.

We stop counting when we find a previous price that is **greater** than today's price.

Example:

```text
prices = [100, 80, 60, 70, 60, 75]

For price = 75:
75 >= 60, count
75 >= 70, count
75 >= 60, count
75 < 80, stop

span = 4
```

Important constraints:

```text
1 <= price <= 100000
At most 10000 calls to next()
```

Because `next()` can be called many times, we should avoid scanning all previous prices every time.

---

# 2. My Initial Understanding

Your first understanding was correct:

You thought:

> Store all prices in a list, and for every new price, go backward and count prices that are less than or equal to the current price.

Your brute force code:

```python
class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        count = 0
        self.prices.append(price)

        for i in range(len(self.prices) - 1, -1, -1):
            if self.prices[i] <= price:
                count += 1
            else:
                break

        return count
```

This shows that you understood the problem correctly.

You also correctly noticed:

> This can become square time because every call may scan many previous prices.

That was the main performance issue.

---

# 3. Mistakes I Made

## Mistake 1: Thinking only in terms of storing all prices

The brute force solution stores every price and checks backward every time.

This is correct, but inefficient.

Why?

Because if prices are increasing:

```text
[10, 20, 30, 40, 50]
```

Each new price scans almost all previous prices.

Total work becomes:

```text
1 + 2 + 3 + ... + n = O(n^2)
```

So it works, but it is not the optimized interview solution.

---

## Mistake 2: Saying the popped span represents bigger elements

You said something like:

> The popped element's whole span represents how many elements before it were bigger.

The better wording is:

> The popped element's span represents how many consecutive previous elements were less than or equal to that popped price.

Example:

```text
60, 70
```

For `70`, span is `2` because:

```text
60 <= 70
70 <= 70
```

So `(70, 2)` means:

> 70 already covers itself and the previous smaller/equal price.

Then if `75` comes, since:

```text
75 >= 70
```

`75` also covers everything `70` covered.

That is why we can add the whole span.

---

## Mistake 3: The idea felt vague even though the code made sense

This is normal for monotonic stack problems.

The important mental model is:

> The stack stores useful blockers, not all prices.

A blocker is a previous price that is greater than the current price.

Smaller or equal prices cannot block the current price, so we absorb them.

---

# 4. Things I Learned

## Key idea 1: Span means consecutive backward count

For each price:

```text
count today
go backward
keep counting while previous price <= current price
stop at first previous price > current price
```

---

## Key idea 2: Brute force scans backward every time

Brute force is simple:

```text
Store all prices
For every new price, scan backward
Count until a bigger price appears
```

But this can be slow.

---

## Key idea 3: Monotonic stack stores compressed groups

Instead of storing every price separately, we store:

```text
(price, span)
```

Each pair means:

> This price represents a group of consecutive days behind it that it already covers.

Example:

```text
60, 70
```

Instead of keeping both separately after processing `70`, we can store:

```text
(70, 2)
```

Because `70` covers both `60` and `70`.

---

## Key idea 4: Why we add the popped span

Suppose stack top is:

```text
(70, 2)
```

And current price is:

```text
75
```

Since:

```text
70 <= 75
```

Current price `75` covers the whole group represented by `70`.

So instead of adding `1`, we add `2`.

```text
span += popped_span
```

This avoids recounting old days.

---

## Key idea 5: The stack is decreasing

The optimized stack keeps prices in decreasing order.

Example:

```text
[(100, 1), (80, 1), (75, 4)]
```

Prices go down from left to right:

```text
100 > 80 > 75
```

Why?

Because whenever a new price is greater than or equal to the top, we pop the top.

So smaller/equal prices are removed.

---

# 5. Pattern Recognition

## Main pattern

This is a **monotonic decreasing stack** problem.

## What clue tells me to use this pattern?

The problem says:

> Look backward from today until you find a previous price greater than today.

This is a strong clue for monotonic stack.

You are looking for the nearest previous greater element.

The span is basically:

> How far can I go backward before a greater price blocks me?

## Why monotonic stack applies here

We only care about previous prices that can block future spans.

A smaller/equal previous price cannot block the current price, so we can remove it and merge its span into the current price.

That is exactly what a monotonic stack helps with:

```text
Remove useless smaller/equal elements
Keep useful greater blockers
```

## Common signs for this pattern

Think of monotonic stack when the problem says:

```text
next greater
previous greater
next smaller
previous smaller
span
days until
look backward/forward until bigger/smaller
```

## Similar problem types

Same idea appears in:

```text
Daily Temperatures
Next Greater Element
Previous Greater Element
Largest Rectangle in Histogram
Asteroid Collision
Stock Span
```

---

# 6. Approaches Tried

## Approach 1: Brute Force List Scan

### Main idea

Store all prices in a list.

For every new price, scan backward and count consecutive prices less than or equal to today's price.

### Step-by-step algorithm

```text
1. Initialize an empty list prices.
2. When next(price) is called:
   a. Append price to prices.
   b. Set count = 0.
   c. Start from the last index and move backward.
   d. If prices[i] <= price, increase count.
   e. If prices[i] > price, stop.
   f. Return count.
```

### Pseudocode

```text
prices = []

next(price):
    append price to prices
    count = 0

    for i from end of prices to start:
        if prices[i] <= price:
            count += 1
        else:
            break

    return count
```

### Time complexity

Per call:

```text
O(n)
```

Worst-case total for `n` calls:

```text
O(n^2)
```

### Space complexity

```text
O(n)
```

Because we store all prices.

### Why this works

It directly follows the definition of span.

We start from today and move backward until we find a greater price.

### Limitation

It can be too slow because it may scan many previous prices on every call.

### Interview expected?

This is a good starting/brute force approach.

But the expected optimized interview solution is the monotonic stack approach.

---

## Approach 2: Monotonic Stack With `(price, span)`

### Main idea

Store pairs:

```text
(price, span)
```

Each pair represents a compressed group.

When a new price comes, pop all previous prices that are less than or equal to it.

For every popped price, add its stored span to the current span.

### Step-by-step algorithm

```text
1. Initialize an empty stack.
2. When next(price) is called:
   a. Set span = 1 because today always counts.
   b. While stack is not empty and stack top price <= current price:
      - Add stack top span to span.
      - Pop stack top.
   c. Push (price, span) into the stack.
   d. Return span.
```

### Pseudocode

```text
stack = []

next(price):
    span = 1

    while stack is not empty and stack.top.price <= price:
        span += stack.top.span
        pop stack

    push (price, span)
    return span
```

### Time complexity

Amortized per call:

```text
O(1)
```

Total for `n` calls:

```text
O(n)
```

Why?

Each price is pushed once and popped at most once.

### Space complexity

```text
O(n)
```

In the worst case, prices are strictly decreasing, so nothing gets popped.

Example:

```text
100, 90, 80, 70
```

Stack keeps all of them.

### Why this works

If the current price is greater than or equal to the stack top price, then the current price also covers everything that stack top price covered.

So we can add the whole stored span instead of recounting day by day.

### Limitation

The idea is harder to understand at first because the stack stores compressed groups, not just raw prices.

### Interview expected?

Yes.

This is the standard and interview-expected solution.

---

# 7. Optimized Approach

The optimized approach uses a monotonic decreasing stack.

The stack stores:

```text
(price, span)
```

The stack keeps only useful blockers.

A previous price is useful if it is greater than future prices, because it can stop the span.

If a previous price is smaller or equal to the current price, it cannot block the current price.

So we pop it and absorb its span.

Example:

```text
prices = [100, 80, 60, 70, 60, 75]
```

Before `75`, stack is:

```text
[(100,1), (80,1), (70,2), (60,1)]
```

Current price:

```text
75
```

Start:

```text
span = 1
```

Top is `(60,1)`:

```text
60 <= 75
```

Pop and add span:

```text
span = 2
```

Top is `(70,2)`:

```text
70 <= 75
```

Pop and add span:

```text
span = 4
```

Top is `(80,1)`:

```text
80 > 75
```

Stop.

Answer:

```text
4
```

Push:

```text
(75,4)
```

New stack:

```text
[(100,1), (80,1), (75,4)]
```

The stack remains decreasing.

---

# 8. Final Code

You already wrote the clean interview-expected version:

```python
class StockSpanner:

    def __init__(self):
        self.stack = []  # stores pairs: (price, span)

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price, span))
        return span
```

This is the cleaner version compared to keeping two separate stacks.

Your second version with separate `stack` and `spans` also works, but the pair version is cleaner because the price and its span stay together.

---

# 9. Interview Script

Here is how you can explain it in an interview:

First, I would explain the brute force approach.

For every new stock price, I can store it in a list and scan backward from today. I count every consecutive previous price that is less than or equal to today's price. As soon as I find a price greater than today's price, I stop. This works because it directly follows the definition of span.

However, this is inefficient. In the worst case, if prices are increasing, every new call scans all previous prices. So for `n` calls, the total time can become `O(n^2)`.

To optimize this, I use a monotonic decreasing stack. Each stack element stores a pair: `(price, span)`. The idea is that each price can represent a group of previous prices that were already less than or equal to it.

When a new price comes in, I start its span as `1` because today's price always counts. Then, while the stack is not empty and the top price is less than or equal to the current price, I pop that top element and add its span to the current span. I can add the whole span because if the current price is greater than or equal to that top price, then it also covers everything that top price already covered.

After popping all smaller or equal prices, the top of the stack, if it exists, is greater than the current price, so it blocks the span. Then I push `(current price, current span)` onto the stack and return the span.

The time complexity is amortized `O(1)` per call because each price is pushed once and popped at most once. The total time for `n` calls is `O(n)`, and the space complexity is `O(n)`.

The pattern here is monotonic stack because the problem asks us to look backward until we find a greater element.

---

# 10. Edge Cases and Dry Run

## Edge case 1: Only one price

```text
next(100) -> 1
```

Today always counts, so span is always at least `1`.

---

## Edge case 2: Strictly decreasing prices

```text
100, 90, 80, 70
```

Each price is smaller than the previous one.

Output:

```text
1, 1, 1, 1
```

Nothing gets popped because every previous price is greater.

Stack becomes:

```text
[(100,1), (90,1), (80,1), (70,1)]
```

---

## Edge case 3: Strictly increasing prices

```text
10, 20, 30, 40
```

Output:

```text
1, 2, 3, 4
```

Each new price absorbs all previous prices.

---

## Edge case 4: Equal prices

```text
50, 50, 50
```

Output:

```text
1, 2, 3
```

Because the condition is:

```text
previous price <= current price
```

Equal prices are included in the span.

That is why the while condition uses:

```python
<=
```

not just:

```python
<
```

---

## Dry Run

Input:

```text
[100, 80, 60, 70, 60, 75, 85]
```

### next(100)

```text
span = 1
stack empty
push (100,1)
return 1
```

Stack:

```text
[(100,1)]
```

---

### next(80)

```text
span = 1
100 > 80, stop
push (80,1)
return 1
```

Stack:

```text
[(100,1), (80,1)]
```

---

### next(60)

```text
span = 1
80 > 60, stop
push (60,1)
return 1
```

Stack:

```text
[(100,1), (80,1), (60,1)]
```

---

### next(70)

```text
span = 1
60 <= 70, pop (60,1), span = 2
80 > 70, stop
push (70,2)
return 2
```

Stack:

```text
[(100,1), (80,1), (70,2)]
```

---

### next(60)

```text
span = 1
70 > 60, stop
push (60,1)
return 1
```

Stack:

```text
[(100,1), (80,1), (70,2), (60,1)]
```

---

### next(75)

```text
span = 1
60 <= 75, pop, span = 2
70 <= 75, pop, span = 4
80 > 75, stop
push (75,4)
return 4
```

Stack:

```text
[(100,1), (80,1), (75,4)]
```

---

### next(85)

```text
span = 1
75 <= 85, pop, span = 5
80 <= 85, pop, span = 6
100 > 85, stop
push (85,6)
return 6
```

Stack:

```text
[(100,1), (85,6)]
```

Output:

```text
[1, 1, 1, 2, 1, 4, 6]
```

---

# 11. Key Takeaways

The most important things to remember:

```text
Span = count consecutive previous days including today where price <= current price.
```

Brute force:

```text
Scan backward every time.
Correct but can be O(n^2) total.
```

Optimized:

```text
Use monotonic decreasing stack.
Store (price, span).
Pop smaller/equal prices.
Add their spans to current span.
Push current price with its calculated span.
```

The key reasoning:

```text
If current price >= popped price,
then current price also covers everything the popped price covered.
```

Pattern trigger:

```text
"Look backward until a greater price appears"
```

That is a clue for:

```text
Monotonic stack / previous greater element
```

Your final solution is interview-expected.
