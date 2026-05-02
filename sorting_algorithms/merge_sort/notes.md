# Merge Sort

## 🎯 Pattern
**Divide and Conquer** — break the problem into smaller subproblems of the same type, solve them recursively, then combine the results.

Other algorithms with this pattern: Quick Sort, Binary Search, Closest Pair of Points.

## 💡 The Core Idea
"If I can sort two halves of an array, I can merge them into one sorted array."

The whole algorithm is built on this single promise. The recursion just keeps splitting the array until each piece is size 1 (already sorted by definition), then merges everything back up.

## 🧠 The Two Functions

1. **merge(A, B)** — Takes TWO ALREADY SORTED arrays and returns one sorted array. This is the function that actually does the sorting work using two pointers.

2. **merge_sort(arr)** — Takes ONE UNSORTED array and returns it sorted. This is the recursive function. It splits, recurses, and calls merge.

## 🔑 Recursion Insight
- Don't trace every recursive call in your head — TRUST that merge_sort does its job correctly on smaller inputs.
- Every recursion needs:
  - Base case: when to stop (here: array of size <= 1 is already sorted)
  - Recursive case: break problem into smaller versions of itself

## 📜 Pseudocode
```
function merge_sort(arr):
    if length(arr) <= 1:
        return arr                          # base case
    
    mid = length(arr) // 2
    left  = merge_sort(arr[0:mid])          # sort left half
    right = merge_sort(arr[mid:end])        # sort right half
    return merge(left, right)               # combine


function merge(A, B):
    result = []
    i = 0, j = 0
    
    while i < length(A) and j < length(B):  # main loop
        if A[i] <= B[j]:
            append A[i] to result
            i += 1
        else:
            append B[j] to result
            j += 1
    
    while i < length(A):                     # leftovers from A
        append A[i] to result
        i += 1
    
    while j < length(B):                     # leftovers from B
        append B[j] to result
        j += 1
    
    return result
```
## ⏱️ Complexity
- **Time: O(n log n)** — log n levels of splitting × n work per level for merging. Same in best, average, AND worst case (unlike Quick Sort).
- **Space: O(n)** — the result array in merge can hold up to n elements; slicing also creates new sub-arrays. NOT in-place.

## ❌ Mistakes I Made
1. Empty `return` in base case — wrote `return` instead of `return arr`. `return` alone gives back `None`, which broke `merge` because `len(None)` throws an error. ALWAYS return the value, not nothing.
2. Confused `merge` and `merge_sort` — tried to call `merge(left)` thinking one function could do both jobs. They are SEPARATE: merge combines, merge_sort recurses.

## ✨ New Things I Learnt
1. Stable sort — using `<=` (not `<`) when comparing keeps equal elements in their original relative order. Important for interviews.
2. Trust the recursion — don't trace every call mentally. Just handle ONE level: split, recurse, merge.
3. Base case includes empty array too — `<= 1` is more robust than `== 1`.
4. Splitting doesn't sort anything — the merge function is where ALL the actual sorting happens. Recursion just sets up the structure.
5. For an array of size n, recursion goes log₂(n) levels deep.

## 🧹 Code Cleanup Lessons
- Don't store a value in a variable just to return it on the next line — return the expression directly: `return merge(left, right)`.
- Use `<= 1` over `== 1` for base cases to handle empty arrays robustly.