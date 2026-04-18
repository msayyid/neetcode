## Approach 1: The "Kick-Out" Method (Two Pointers)
**Concept:** Start with the largest possible window (the whole array) and shrink it from the outside in until only $k$ elements remain.

### The Logic
* **Setup:** Place `l` at index `0` and `r` at index `n - 1`.
* **Shrink:** Compare the distance of `arr[l]` and `arr[r]` from $x$.
* **Decision:** The element that is **further away** gets kicked out.
    * If `left_dist > right_dist`: Move `l` forward (`l += 1`).
    * If `right_dist >= left_dist`: Move `r` backward (`r -= 1`).
    * *Note: In a tie, we keep the left one because the problem prefers smaller values.*
* **Stop:** When exactly $k$ elements are left (`r - l + 1 == k`).

### Complexity
* **Time:** $O(N - k)$. We perform one comparison for every element we remove.
* **Space:** $O(1)$.

---

## Approach 2: The "Ideal Start" Method (Binary Search)
**Concept:** Instead of walking one-by-one, we use Binary Search to find the **starting index** ($l$) of our $k$-length window.

### The Logic
* **The Range:** We are searching for a **starting index**. The window *could* start anywhere from index `0` to index `n - k`.
* **The Middle Point:** We pick a potential start-line, `mid`.
* **The "Trade-Off" Check:** We compare the element we currently have at the start (`arr[mid]`) with the element we *could* have if we moved the window right (`arr[mid + k]`).
* **The Decision:**
    * **Is `arr[mid]` closer?** (or tied). Moving the window right would mean swapping a closer number for a further one. That's a bad deal.
        * **Action:** The best start must be at `mid` or to the left. (`r = mid`).
    * **Is `arr[mid + k]` closer?** Moving the window right is a good deal! We gain a closer number and lose a further one.
        * **Action:** The current `mid` is a bad start; the real one is to the right. (`l = mid + 1`).



### Complexity
* **Time:** $O(\log(N - k) + k)$. We find the start in log time, then slice $k$ elements.
* **Space:** $O(1)$.

---

## Mistakes I Made & Things I Learned

### Mistakes to Watch For
1.  **Thinking "mid" is the target:** In this problem, we aren't looking for $x$. We are looking for a **starting index**. Binary search is just the tool to find that index.
2.  **Pointer confusion:** In the Two-Pointer method, the pointers represent the **actual boundaries** of the result. In Binary Search, the pointers represent the **range of possible start-lines**.
3.  **Tie-breaker rules:** It's easy to forget that if distances are equal, we **must** keep the smaller number. In both approaches, this means favoring the left side.

### Key Learnings
1.  **Sorted Array = Jumping:** Because the array is sorted, we can "jump" over elements in Binary Search. If one trade-off is bad, every trade-off further in that direction is also bad.
2.  **The +k Logic:** In the Binary Search version, `arr[mid + k]` is the "scout." It tells us if there is something better just outside our current window view.
3.  **Efficiency vs. Intuition:** The Two-Pointer method is easier to visualize, but the Binary Search method is much more powerful for massive datasets because it doesn't need to visit every element.

---

### Final Comparison Table
| Feature | Two Pointers | Binary Search |
| :--- | :--- | :--- |
| **Mental Model** | Squeezing from the ends | Testing the "Start Line" |
| **Complexity** | $O(N)$ | $O(\log N)$ |
| **Use Case** | $k$ is close to $N$ | $N$ is very large |
| **Ease of Coding** | High | Medium (The `mid + k` is tricky) |
