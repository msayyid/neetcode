# 📌 643. Maximum Average Subarray I - Notes

## 🔹 Problem Summary

* Given array `nums` and integer `k`
* Find a **contiguous subarray of size k**
* Return the **maximum average**

---

## 🔑 Key Insight

> Since `k` is fixed → maximizing **average** = maximizing **sum**

So we focus on:

```
max_sum / k
```

---

## 🧠 Core Idea - Fixed Sliding Window

* Window size is **always k**
* Don’t store elements → just track **sum**

---

## ⚙️ Algorithm Steps

### 1. Initialize first window

```python
window_sum = sum(nums[:k])
max_sum = window_sum
```

---

### 2. Slide the window

For each new element:

* Add new element
* Remove old element

```python
window_sum += nums[r]
window_sum -= nums[r - k]
```

---

### 3. Track maximum

```python
max_sum = max(max_sum, window_sum)
```

---

### 4. Return result

```python
return max_sum / k
```

---

## 🔍 Example Walkthrough

```
nums = [1,12,-5,-6,50,3], k = 4
```

Initial window:

```
[1,12,-5,-6] → sum = 2
```

Slide:

```
+50, -1 → sum = 51  ← max
+3, -12 → sum = 42
```

Final:

```
max_sum = 51 → average = 12.75
```

---

## ⏱️ Complexity

* Time: **O(n)**
* Space: **O(1)**

---

## ❌ Common Mistakes

### 1. Using a list as window

* ❌ unnecessary
* ❌ slower operations

---

### 2. Recomputing sum every time

```python
sum(nums[i:i+k])  # O(k) each time → O(nk)
```

---

### 3. Wrong removal index

```python
nums[r - k]  # must remove the leftmost element
```

---

## 🧠 Pattern Recognition

### Use this approach when:

* Subarray size is **fixed**
* Asked for:

  * max sum
  * min sum
  * average

---

## 🆚 Fixed vs Variable Window

| Type            | When to use                                    |
| --------------- | ---------------------------------------------- |
| Fixed window    | size = k                                       |
| Variable window | conditions (no duplicates, sum ≥ target, etc.) |

---

## 🗣️ Interview Explanation (simple)

> “Since the window size is fixed, I use a sliding window.
> I maintain the sum of k elements and update it by adding the next element and removing the previous one.
> I track the maximum sum and return max_sum divided by k.”

---

## 🧠 One-line Memory Trick

> Fixed window → **add right, remove left**
