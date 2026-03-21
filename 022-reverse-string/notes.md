**Reverse String — Notes**

---

**Solution 1: Two Pointers (Optimal)**

**Approach:** Place `left` at start, `right` at end. While `left < right`, swap and move both pointers inward.

**Why this works:** We stop when the pointers meet in the middle — at that point everything has been swapped. Handles both even and odd lengths cleanly.

**Time:** O(n) — roughly n/2 swaps.
**Space:** O(1) — only two pointers. ✅ Satisfies the in-place constraint.

**Interview verdict:** ✅ Correct and optimal.

---

**Solution 2: Stack**

**Approach:** Push all characters onto a stack, then pop them back into `s`. Since a stack is LIFO, popping gives reverse order.

**Time:** O(n)
**Space:** O(n) — the stack holds all characters. ❌ Fails the O(1) constraint.

**Interview verdict:** ❌ Clever logic, wrong for this problem due to space constraint. But useful to know — shows understanding of LIFO behaviour.

---

**Solution 3: Recursion**

**Approach:** Same logic as two pointers but expressed recursively. Base case `if l < r` stops when pointers meet in the middle.

**Time:** O(n)
**Space:** O(n) — recursion call stack grows with input size. ❌ Fails the O(1) constraint.

**Interview verdict:** ❌ Elegant, but recursion always carries hidden O(n) space cost. Don't be fooled by the lack of explicit data structures.

---

**Key lesson:** Recursion and stacks both cost O(n) space even when it's not obvious. When a problem demands O(1) space, default to an iterative approach.