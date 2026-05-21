## Practice Problem: Minimum Warehouse Dispatch Operations

You are given an array `warehouses`, where `warehouses[i]` represents the warehouse ID of the `i-th` item.

A logistics coordinator needs to dispatch all items from the inventory.

In one operation, the coordinator can do **one** of the following:

1. If there are at least two items left, choose two items from **different warehouses** and dispatch both of them.

   * This means if the chosen items are `x` and `y`, then:

   ```text
   warehouses[x] != warehouses[y]
   ```

2. If there is at least one item left, choose one item and dispatch it alone.

After dispatching an item, it is removed from the inventory. The remaining items keep their relative order.

Your task is to return the **minimum number of operations** needed to dispatch all items.

---

## Function Signature

```python
def calculateMinShipments(warehouses: List[int]) -> int:
```

---

## Input

```text
warehouses: List[int]
```

An array of integers where each value represents the warehouse ID of an item.

---

## Output

Return an integer: the minimum number of operations required to dispatch all items.

---

## Constraints

```text
1 <= len(warehouses) <= 10^5
1 <= warehouses[i] <= 10^9
```

---

## Example 1

```text
Input:
warehouses = [1, 3, 1, 2]

Output:
2
```

### Explanation

One optimal way:

```text
Operation 1: dispatch items from warehouses 1 and 2
Remaining: [3, 1]

Operation 2: dispatch items from warehouses 3 and 1
Remaining: []
```

So the answer is `2`.

---

## Example 2

```text
Input:
warehouses = [2, 9, 7, 8, 8]

Output:
3
```

### Explanation

One optimal way:

```text
Operation 1: dispatch 2 and 8
Remaining: [9, 7, 8]

Operation 2: dispatch 9 and 8
Remaining: [7]

Operation 3: dispatch 7 alone
Remaining: []
```

Minimum operations = `3`.

---

## Example 3

```text
Input:
warehouses = [5, 5, 5, 5]

Output:
4
```

### Explanation

All items are from the same warehouse, so no two items can be paired together.

Each item must be dispatched alone.

---

## Example 4

```text
Input:
warehouses = [1, 2, 3, 4]

Output:
2
```

### Explanation

All items can be paired:

```text
Operation 1: dispatch 1 and 2
Operation 2: dispatch 3 and 4
```

Minimum operations = `2`.

---

## Example 5

```text
Input:
warehouses = [1, 1, 1, 2, 3]

Output:
3
```

### Explanation

One possible optimal way:

```text
Operation 1: dispatch 1 and 2
Operation 2: dispatch 1 and 3
Operation 3: dispatch 1 alone
```

Minimum operations = `3`.

---

## Your Goal

Try to solve it without directly using the formula first.

Think about:

```text
What stops us from pairing every item?
What happens if one warehouse appears too many times?
When can the answer simply be ceil(n / 2)?
```

Expected complexity:

```text
Time: O(n)
Space: O(k)
```

where `k` is the number of unique warehouses.
