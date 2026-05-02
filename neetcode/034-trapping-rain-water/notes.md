# Trapping Rain Water - Notes

## Core idea

For every index `i`, the trapped water depends on:

```python
water[i] = min(leftMax, rightMax) - height[i]
```

Where:

* `leftMax` = tallest bar on the left side
* `rightMax` = tallest bar on the right side
* `height[i]` = current bar height

The reason we use `min(leftMax, rightMax)` is:

* water needs a wall on both sides
* the shorter side limits how high water can rise
* small bars in between do not matter, because they get submerged

So we are really calculating:

> how much empty vertical space exists above each bar

---

## Important intuition

Do **not** think about the nearest wall.

Think about the **best possible boundary** on each side.

At index `i`:

* tallest left wall tells us the strongest left boundary
* tallest right wall tells us the strongest right boundary
* the smaller of those two becomes the water level

Then we subtract the current bar height because the bar itself takes up space.

---

# 1. Brute Force

## Idea

For each index:

1. find the tallest bar on the left
2. find the tallest bar on the right
3. compute trapped water at that index

This is the most direct version and the easiest to understand conceptually.

---

## Code

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # Total trapped water
        res = 0
        
        # Number of bars
        n = len(height)

        # Check every index one by one
        for i in range(n):
            # Start both max values at the current bar height
            # This guarantees the result never goes negative here
            leftMax = rightMax = height[i]

            # Find the tallest wall from index 0 to i
            for j in range(i):
                leftMax = max(leftMax, height[j])

            # Find the tallest wall from index i+1 to the end
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])

            # Water above index i is limited by the shorter boundary
            # Then subtract the current bar height
            res += min(leftMax, rightMax) - height[i]

        return res
```

---

## How to think about it

At each index `i`, this code asks:

* what is the highest wall to my left?
* what is the highest wall to my right?
* if water fills this area, how high can it rise above me?

Then:

```python
min(leftMax, rightMax) - height[i]
```

gives the amount of water trapped above that bar.

---

## Why it is slow

For every index, we scan:

* left side again
* right side again

So we keep recomputing the same max values many times.

That gives:

* Time: `O(n^2)`
* Space: `O(1)`

---

## Main weakness

The logic is correct, but it repeats too much work.

---

# 2. Prefix / Precomputed Max Arrays

## Idea

This approach keeps the **same formula**:

```python
water[i] = min(leftMax[i], rightMax[i]) - height[i]
```

But instead of recomputing left and right max values for every index, we precompute them once.

We build:

* `leftMax[i]` = tallest bar from index `0` to `i`
* `rightMax[i]` = tallest bar from index `i` to `n - 1`

Then we use those arrays to compute the answer in one final loop.

---

## Code

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # Handle empty input
        if not height:
            return 0

        n = len(height)

        # leftMax[i] will store the tallest bar from 0 to i
        leftMax = [0] * n

        # rightMax[i] will store the tallest bar from i to n-1
        rightMax = [0] * n

        # Build leftMax array
        # First position only sees itself
        leftMax[0] = height[0]
        for i in range(1, n):
            # Max up to index i is either:
            # - previous max up to i-1
            # - current height
            leftMax[i] = max(leftMax[i - 1], height[i])

        # Build rightMax array
        # Last position only sees itself
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            # Max from i to end is either:
            # - next max from i+1 to end
            # - current height
            rightMax[i] = max(rightMax[i + 1], height[i])

        # Now compute total trapped water
        res = 0
        for i in range(n):
            # Water above index i is still:
            # shorter boundary minus current height
            res += min(leftMax[i], rightMax[i]) - height[i]

        return res
```

---

## How to think about it

This does not change the logic at all.

It only changes **how we obtain** the left and right max values.

Instead of saying:

> for each i, go search left and right

we say:

> let me store the answer for every position once, then reuse it

---

## Meaning of these arrays

### `leftMax[i]`

This stores the tallest bar seen so far from the left up to index `i`.

Example:

```python
height = [0,2,0,3,1]
leftMax = [0,2,2,3,3]
```

### `rightMax[i]`

This stores the tallest bar seen so far from the right starting at index `i`.

Example:

```python
height = [0,2,0,3,1]
rightMax = [3,3,3,3,1]
```

---

## Why this line works

```python
leftMax[i] = max(leftMax[i - 1], height[i])
```

Because:

* `leftMax[i - 1]` already means "tallest bar from 0 to i-1"
* now we just compare that with the current bar
* so we get the tallest bar from 0 to i

Same idea for:

```python
rightMax[i] = max(rightMax[i + 1], height[i])
```

---

## Complexity

* Time: `O(n)`
* Space: `O(n)`

---

## Main strength

Same easy formula as brute force, but much faster.

---

## Main weakness

Uses extra arrays.

---

# 3. Two Pointers - Optimal

## Idea

This approach still uses the same core principle:

```python
water = min(leftMax, rightMax) - current_height
```

But it avoids:

* nested scans
* extra arrays

Instead, it uses:

* one pointer from the left
* one pointer from the right
* one running `leftMax`
* one running `rightMax`

The key idea is:

> always process the side with the smaller boundary

Because the smaller boundary is the one that limits the water.

---

## Code

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        # If array is empty, no water can be trapped
        if not height:
            return 0

        # Two pointers at both ends
        l, r = 0, len(height) - 1

        # Best boundary seen so far from left and right
        leftMax, rightMax = height[l], height[r]

        # Total trapped water
        res = 0

        # Continue until pointers meet
        while l < r:
            # If left boundary is smaller, left side limits the water
            if leftMax < rightMax:
                # Move left pointer inward
                l += 1

                # Update the best left boundary seen so far
                leftMax = max(leftMax, height[l])

                # Water trapped at this position depends on leftMax
                res += leftMax - height[l]

            else:
                # Otherwise right side is the smaller or equal boundary
                # So process the right side
                r -= 1

                # Update the best right boundary seen so far
                rightMax = max(rightMax, height[r])

                # Water trapped at this position depends on rightMax
                res += rightMax - height[r]

        return res
```

---

## Why it works

This is the hardest part conceptually.

The full formula is:

```python
water[i] = min(leftMax, rightMax) - height[i]
```

In the two pointer method, we do **not** know both sides fully at every step.

So why can we still compute correctly?

Because if:

```python
leftMax < rightMax
```

then the water level is definitely limited by `leftMax`.

Why?

Because even if the right side changes later, it is already at least bigger than `leftMax` right now, so the smaller side is known.

That means:

* the left side is the bottleneck
* the water for that side is already determined
* it is safe to process that index and move on

Same logic when the right side is smaller.

---

## Dumbed-down intuition

Imagine water between two sides.

If left wall is `3` and right wall is `10`, water level is `3`.

You do not care that the right side is `10`.
The left side already limits everything.

So:

* smaller side decides the water level
* process the smaller side
* move inward

That is the entire trick.

---

## Why this line is safe

```python
res += leftMax - height[l]
```

This is safe only when `leftMax < rightMax`, because then the left side is confirmed to be the limiting boundary.

Similarly:

```python
res += rightMax - height[r]
```

is safe when the right side is the smaller boundary.

---

## Mental model

At every step ask:

> which side is weaker right now?

That side:

* determines the water level
* can be solved immediately
* then we move that pointer inward

---

## Complexity

* Time: `O(n)`
* Space: `O(1)`

---

## Main strength

Fastest and most memory efficient approach.

---

## Main difficulty

The logic is less obvious than brute force or prefix arrays.

---

# Comparison Summary

## Brute Force

* easiest to understand
* directly follows the definition
* recomputes everything
* `O(n^2)` time, `O(1)` space

## Prefix Arrays

* same logic as brute force
* stores left/right max for each index
* avoids recomputation
* `O(n)` time, `O(n)` space

## Two Pointers

* same underlying formula
* no extra arrays
* uses smaller boundary rule
* `O(n)` time, `O(1)` space

---

# Final key notes to remember

## 1. Main formula

```python
water[i] = min(leftMax, rightMax) - height[i]
```

---

## 2. Why `min(...)`?

Because water can only rise up to the shorter boundary.

---

## 3. Why subtract `height[i]`?

Because the current bar already occupies space.
We only want the empty space above it.

---

## 4. Nearest wall vs tallest wall

Do **not** use nearest wall thinking.

We care about the **tallest possible boundary** on each side.

---

## 5. Small bars in between

Small bars do not stop water.
They get submerged.

---

## 6. Two pointer rule

If `leftMax < rightMax`:

* process left

Else:

* process right

Because the smaller boundary determines the water.

---

## Final one-line intuition

**Water trapped at an index equals the empty space between the current bar and the shorter of the tallest walls on both sides.**
