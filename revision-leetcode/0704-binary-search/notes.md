## 📝 Code Analysis & Lessons Learned

### 1. Mistakes to Remember (The "Don't Do This" List)
When you first started, you had two main bugs that are classic "binary search traps":

* **The Infinite Loop Trap:** In your first version, you used `while left < right` and didn't have a specific `if nums[mid] == target: return mid`. If the target was found at `mid`, the pointers wouldn't move, and the loop would run forever.
* **The Index Error:** Using `while left < right` forces you to check `nums[left]` *after* the loop. If the input list is empty (`[]`), `left` is 0 but there is no index 0, causing a crash.
* **Asymmetric Boundaries:** Using `right = mid` instead of `right = mid - 1`. If you’ve already checked `mid` and it isn't the target, **get rid of it.** Keeping it in the search range makes your logic more complex.

### 2. Why This New Version is Better
* **The `left <= right` Condition:** This ensures that even if the search range narrows down to a single element, the loop runs one last time to check that specific element.
* **Early Exit:** `if nums[mid] == target: return mid` is the fastest way to solve the problem.
* **Automatic Safety:** If `nums` is empty, `left` (0) is not `<= right` (-1), so the loop never starts, and the code safely returns `-1`.

---

## 💡 Interview Patterns: Binary Search

Binary search isn't just for sorted arrays; it’s a **pattern** for any problem where you can discard half of the possibilities in each step.



### Pattern A: "Find the Exact Value" (What you just did)
* **Use when:** You need to find one specific number.
* **Template:** `while left <= right` with `mid - 1` and `mid + 1`.

### Pattern B: "Find the Boundary" (The Left-most or Right-most)
* **Use when:** The array has duplicates (e.g., `[1, 2, 2, 2, 3]`) and you need the *first* occurrence of `2`.
* **Logic:** Even if you find `target`, you don't return. You keep moving `right = mid - 1` to see if there's an even earlier one.

### Pattern C: "Search on Answer"
* **Use when:** You aren't searching an array, but a **range of numbers**.
* **Example:** "Find the smallest integer $x$ such that $x^2 > 500$."
* **Logic:** Your `left` is 1, your `right` is 500. You binary search the *numbers themselves* until you find the boundary.

---

## 🚀 Pro-Tips for Interviews

1.  **State the Complexity:** Always mention that Binary Search is $O(\log n)$ time and $O(1)$ space. Interviewers love hearing this before you even start typing.
2.  **The "Mid" Overflow:** Even though Python handles large numbers, mention the overflow issue:
    * *Standard:* `mid = (left + right) // 2`
    * *Pro:* `mid = left + (right - left) // 2` (This shows you understand how memory works in lower-level languages like C++).
3.  **Clarify Duplicates:** If the interviewer gives you a binary search problem, ask: *"Are there duplicate numbers, and if so, which index should I return?"* This shows you are thinking about edge cases.
