**My confusion**

**so i in partition is needed to confirm and say this is the last lower than pivot element
and j is for swapping**



**Problem: Sort an Array — Quicksort**

**Why Quicksort?**
Needed O(n log n) time with smallest space complexity. Chose quicksort over merge sort because quicksort sorts **in-place** using only O(log n) space (recursion stack), while merge sort needs O(n) extra space for temporary arrays.

**How it works:**
Pick a pivot, move all smaller elements to its left and larger to its right, then recursively do the same on the left and right sub-arrays. Stop when sub-array has 1 or 0 elements (already sorted). No "collecting back" needed — array is sorted in place.

**Key mistake made:**
At the end of partition, wrote `nums[i], nums[i] = nums[high], nums[i]` — swapping element with itself instead of `nums[i], nums[high] = nums[high], nums[i]`.

**What `i` means in partition:**
`i` tracks the **last confirmed position of an element smaller than pivot**. Starts at `low - 1` because at the beginning no elements have been confirmed smaller yet — boundary is before the array starts.

**What partition returns:**
The **final position of the pivot** after all smaller elements are on its left and larger on its right. Quicksort uses this to define the **boundaries of the next recursive calls** — left sub-array is `[low, pivot-1]`, right is `[pivot+1, high]`.

**Random pivot:**
Used `random.randint(low, high)` to pick pivot randomly, then swapped it to `high` before partitioning. Avoids worst case O(n²) on already-sorted arrays.

**Time:** O(n log n) average | **Space:** O(log n)

---