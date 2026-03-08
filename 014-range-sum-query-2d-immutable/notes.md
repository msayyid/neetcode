**Range Sum Query 2D — Notes**

**Problem:** Given a 2D matrix, answer multiple rectangle sum queries in O(1). The class is initialized once with the matrix, then `sumRegion(row1, col1, row2, col2)` can be called up to 10,000 times.

---

**Approaches considered:**

**1. Brute force (rejected):** For each `sumRegion` call, loop through every cell inside the rectangle. This would be O(m×n) per query — with 10,000 queries that becomes extremely costly.

**2. Row-only prefix sums (rejected):** Pre-compute running sums for each row so that any single-row range sum is O(1). However, a rectangle spans multiple rows, so you'd still need to loop through each row and add up their range sums. That's O(m) per query — better than brute force but still not O(1).

**3. 2D prefix sum matrix (chosen):** Pre-process once in O(m×n), then answer every query in O(1).

---

**The bigger matrix — why and how:**

Created a `(rows+1) x (cols+1)` matrix filled with 0s called `sumMat`, where `sumMat[i][j]` stores the sum of all elements in the rectangle from `(0,0)` to `(i-1, j-1)` in the original matrix.

The extra row and column of zeros at the top and left prevent out of bounds errors — the formula needs to look at `row1-1` or `col1-1`, which without padding would crash when querying the edges of the original matrix.

---

**Building sumMat — the key insight:**

```python
for r in range(rows):
    prefix = 0
    for c in range(cols):
        prefix += matrix[r][c]
        above = self.sumMat[r][c+1]
        self.sumMat[r+1][c+1] = prefix + above
```

- `prefix` = running sum of the **current row only** up to column `c`. Resets to 0 for each new row because each row starts fresh.
- `above = sumMat[r][c+1]` = the cell directly above in sumMat. This is the critical insight — **that cell already stores the sum of the entire rectangle above it**, because it was computed in the previous iteration of `r`. We don't need to recompute anything, we just trust what's already stored.
- `prefix + above` = current row's sum up to `c` + everything above = the full rectangle from `(0,0)` to current cell.

This is a dynamic programming pattern — solving a bigger problem by reusing already computed smaller results rather than recomputing from scratch.

---

**sumRegion formula (inclusion-exclusion):**

```python
bottomRight - above - left + topLeft
```

- `bottomRight` = sum of entire rectangle from (0,0) to (row2, col2)
- Subtract `above` = the rectangle above our region that we don't want
- Subtract `left` = the rectangle to the left of our region that we don't want
- Add back `topLeft` = the top-left corner rectangle that got subtracted **twice** (once in `above`, once in `left`)

The `+1` offsets in `sumRegion` map original matrix coordinates to the bigger `sumMat` coordinates.

---

**Mistakes/things that took time:**
- Initially didn't understand why `+1` dimensions were needed
- Confused `sumMat` for a function — it's just a 2D list
- The biggest confusion: didn't immediately see that `above` is not just one cell's value but the **sum of an entire rectangle** already pre-computed. Once that clicked, the whole building logic made sense.

---

**Complexities:**
- Time: O(m×n) to build — acceptable because you must read every cell at least once, cost is paid once upfront regardless of query count
- Time: O(1) per query — just arithmetic on 4 precomputed values
- Space: O(m×n) for `sumMat`