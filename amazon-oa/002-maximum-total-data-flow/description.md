# Maximum Total Data Flow

You are given an integer array `bandwidth`, where `bandwidth[i]` represents the bandwidth capacity of the `i-th` processing node.

There are also `streamCount` data channels that need to be connected. Each data channel must choose exactly two nodes:

```text
(main node, secondary node)
```

The data flow of one channel is defined as:

```text
bandwidth[main] + bandwidth[secondary]
```

Each channel must use a unique ordered pair of nodes.

A pair `(x, y)` is considered different from `(y, x)`.
It is also allowed to use the same node as both the main and secondary node, so `(x, x)` is valid.

Return the maximum possible total data flow by choosing exactly `streamCount` unique ordered pairs.

---

## Example 1

```text
Input: bandwidth = [6, 4, 7], streamCount = 4
Output: 52
```

Explanation:

The possible ordered pairs and their data flows include:

```text
(7, 7) = 14
(7, 6) = 13
(6, 7) = 13
(6, 6) = 12
(7, 4) = 11
(4, 7) = 11
...
```

The best 4 pairs are:

```text
(7, 7), (7, 6), (6, 7), (6, 6)
```

So the maximum total data flow is:

```text
14 + 13 + 13 + 12 = 52
```

---

## Example 2

```text
Input: bandwidth = [5, 4, 8, 4, 7], streamCount = 6
Output: 86
```

Explanation:

The largest ordered pair sums are:

```text
(8, 8) = 16
(8, 7) = 15
(7, 8) = 15
(8, 5) = 13
(5, 8) = 13
(7, 7) = 14
```

Choosing the top 6 pair sums gives:

```text
16 + 15 + 15 + 14 + 13 + 13 = 86
```

---

## Constraints

```text
1 <= bandwidth.length <= 2 * 10^5
1 <= bandwidth[i] <= 2 * 10^5
1 <= streamCount <= min(10^9, bandwidth.length^2)
```

---

## Function Signature

```python
def determineMaxDataFlow(bandwidth: List[int], streamCount: int) -> int:
```

---

## Notes

* Ordered pairs are counted separately.

  * `(i, j)` and `(j, i)` are different if `i != j`.
* Self-pairs are allowed.

  * `(i, i)` is valid.
* You need the maximum sum of the top `streamCount` pair sums.
* A brute force solution that generates all `n^2` pairs will not pass large test cases.
