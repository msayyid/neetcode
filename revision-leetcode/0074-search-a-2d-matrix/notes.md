**LeetCode 74 — Search a 2D Matrix — Medium**

---

**Pattern**
Binary search on a virtually flattened sorted 2D matrix.

---

**Key Insight**
Because each row is sorted and the first element of each row is greater than the last element of the previous row, the entire matrix is globally sorted. You can binary search it as if it were a flat array — without actually flattening it — by converting a flat index `mid` into row and column using `mid // n` and `mid % n` where `n` = number of columns.

---

**The // and % trick — cinema analogy**
Think of a cinema with 4 seats per row. Ticket #9:
- `9 // 4 = 2` → row 2 (how many complete rows you passed)
- `9 % 4 = 1` → seat 1 (how far into the current row)

`//` gives the row, `%` gives the column. Zero-indexed.

---

**Approach 1 — Brute force linear scan**
Loop through every element. Simple but doesn't meet the O(log m×n) requirement.
```
for each row i:
    for each col j:
        if matrix[i][j] == target → return True
return False
```
time: O(m×n) | space: O(1)

---

**Approach 2 — Flatten then binary search (my first attempt)**
Flatten the matrix into a 1D array, then run standard binary search. The binary search part is O(log m×n) but the flattening step is O(m×n) — killing the overall complexity.
```
flatten matrix into array  ← O(m×n) bottleneck
binary search the array
```
time: O(m×n) | space: O(m×n)

---

**Approach 3 — Virtual flat binary search (optimal ✓)**
Binary search treating the matrix as a virtual flat array. No flattening needed. Convert flat index to row/col on the fly.
```
m = rows, n = cols
left = 0, right = m*n - 1

while left <= right:
    mid = (left + right) // 2
    row = mid // n
    col = mid % n
    if matrix[row][col] == target → return True
    elif matrix[row][col] > target → right = mid - 1
    else → left = mid + 1

return False
```
```python
def searchMatrix(self, matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    while left <= right:
        mid = (left + right) // 2
        row, col = mid // n, mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False
```
time: O(log(m×n)) | space: O(1)

---

**Approach 4 — Two binary searches**
First binary search to find the correct row by checking if target falls between first and last element of each row. Then a second binary search within that row.
```
binary search rows:
    if matrix[mid][0] <= target <= matrix[mid][-1]:
        break  ← found the row
    elif matrix[mid][0] < target → left = mid + 1
    else → right = mid - 1

binary search within found row for target
```
Same complexity as approach 3 because: `log(m×n) = log(m) + log(n)`

time: O(log m + log n) = O(log(m×n)) | space: O(1)

---

**Mistakes & things I learned**
- confused m and n — m is rows, n is columns
- tried to average values instead of indices in binary search
- didn't realise I already had m and n via `len(matrix)` and `len(matrix[0])`
- the flattening step O(m×n) is what broke approach 2, not the binary search itself
- `mid // n` and `mid % n` converts a flat index to (row, col) with no extra space
- `log(m×n) = log(m) + log(n)` — approaches 3 and 4 are mathematically identical

---

**When to spot this pattern**
- 2D matrix that is globally sorted → treat as flat 1D array
- need O(log n) on a 2D structure → binary search with index conversion
- any time you want to binary search a matrix without the cost of flattening