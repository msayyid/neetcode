Your space answer was **O(m + k)** — that's correct! 
- O(m) for the map where m is distinct elements
- O(k) for the heap and result list

Since m ≤ n, you could also write it as **O(n)** in worst case.

---

**Top K Frequent Elements**

**What I did:** 
Built a frequency map using `.get(key, 0) + 1` to count occurrences of each element.

*Solution 1 (min-heap):* Used `heapq` (Python's min-heap) pushing `(frequency, element)` tuples so heap sorts by frequency, smallest on top. After each push, if heap size exceeds k, pop the smallest — this keeps only the top k frequent elements. Finally extracted index `[1]` from each tuple to get actual elements.

*Solution 2 (bucket sort):* Created list `freq` of size n+1 where index = frequency, value = list of elements with that frequency. Iterated from the back (highest frequency first), collecting elements until result has k elements.

**Mistakes made:** Mixed up `.get()` syntax. Had unnecessary if/else branches doing the same thing in heap version. Returned heap tuples directly instead of extracting keys. Tried extracting from `my_map` instead of `heap`. Didn't immediately understand why `freq` must be pre-initialized as lists — you can't `.append()` to something that doesn't exist yet.

**New things learned:** `heapq` is a min-heap — smallest on top. Push tuples to sort by first element. Push first then pop if size exceeds k, not the other way around. Min-heap capped at k is better than max-heap of all elements in both time and space. Bucket sort trick — frequency as index, iterate from back for top k.

**Time:** Solution 1: O(n + m log k) | Solution 2: O(n)

**Space:** Solution 1: O(m + k) | Solution 2: O(n)