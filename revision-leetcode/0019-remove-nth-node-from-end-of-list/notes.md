# 🧠 Problem: Remove Nth Node From End of List

---

# ✅ Approach 1: Two-Pass (Counting)

## 💡 Idea

* First pass → count total nodes
* Second pass → remove `(count - n)`th node from start

---

## ⚙️ Steps

1. Traverse list → get `count`
2. Compute:

   ```
   target = count - n
   ```
3. Use **dummy node**
4. Move to **node before target**
5. Skip target:

   ```
   curr.next = curr.next.next
   ```

---

## ❗ Key Insight

* You **must stop at previous node**, not target itself
* Because deletion requires:

  ```
  prev.next = prev.next.next
  ```

---

## ⚠️ Edge Case

* Removing head (e.g., `[1], n=1`)
* Solved using:

  ```
  dummy → head
  ```

---

## ⏱ Complexity

* Time: O(n) + O(n) = **O(n)**
* Space: **O(1)**

---

## ❌ Common Mistakes

* Going to target instead of previous node
* Forgetting dummy → breaks when deleting head
* Off-by-one errors in loop

---

## 🧠 When to use

* When you want **simple, safe, readable logic**
* Good for beginners / first implementation

---

# 🚀 Approach 2: One-Pass (Fast & Slow Pointers)

## 💡 Idea

* Keep a **gap of n+1 nodes** between fast and slow
* When fast reaches end → slow is before target

---

## ⚙️ Steps

1. Create dummy:

   ```
   dummy → head
   ```
2. Set:

   ```
   fast = slow = dummy
   ```
3. Move `fast` **n+1 steps ahead**
4. Move both together:

   ```
   while fast:
       fast = fast.next
       slow = slow.next
   ```
5. Delete:

   ```
   slow.next = slow.next.next
   ```

---

## 🔑 Core Insight

```text
Maintain distance between fast and slow
→ when fast hits None
→ slow is right before target
```

---

## ❗ Why n+1 (VERY IMPORTANT)

* Ensures slow lands **before** target
* If you used `n`:

  * slow lands **on target**
  * cannot delete easily

---

## ⚠️ Edge Case

* Removing head handled automatically by dummy

---

## ⏱ Complexity

* Time: **O(n)** (single pass)
* Space: **O(1)**

---

## ❌ Common Mistakes

* Using `n` instead of `n+1`
* Forgetting dummy → head removal breaks
* Not understanding pointer gap
* Off-by-one errors

---

## 🧠 When to use

* Preferred in interviews
* Shows deeper understanding of pointers
* More elegant solution

---

# ⚖️ Comparison

| Feature        | Two-Pass   | One-Pass        |
| -------------- | ---------- | --------------- |
| Passes         | 2          | 1               |
| Time           | O(n)       | O(n)            |
| Difficulty     | Easier     | Harder          |
| Interview pref | Acceptable | Preferred       |
| Key skill      | Counting   | Pointer control |

---

# 🧠 What You Learned (Important)

* Linked list deletion = **skip node**
* Dummy node = avoids edge cases
* Difference between:

  * **target node**
  * **node before target**
* Pointer gap technique (fast/slow)

---

# 🔥 Your Personal Weak Points (from this problem)

* Confusion between **target vs previous node**
* Understanding why `n+1` instead of `n`
* Visualizing pointer positions

👉 Now fixed.