# 1. Brute force with list checks

```python
if nums1[i] not in intersections and nums1[i] in nums2
```

### Idea

* Loop `nums1`
* Check:

  * not already added (avoid duplicates)
  * exists in `nums2`

### Time

* `in intersections` → O(k)
* `in nums2` → O(m)

```text
O(n * (k + m)) → O(n² + n*m)
```

### Space

```text
O(k) → O(n)
```

### Verdict

* ❌ Too slow
* ❌ Not interview-ready

---

# 2. Double loop brute force

```python
for i in nums1:
    for j in nums2:
```

### Idea

* Compare every pair

### Time

```text
O(n * m)
```

### Space

```text
O(min(n, m))  (set for result)
```

### Verdict

* ❌ Still brute force
* ❌ Not ideal for interviews

---

# 3. One-liner set intersection

```python
list(set(nums1) & set(nums2))
```

### Idea

* Convert both → sets
* Use built-in intersection

### Time

```text
O(n + m)
```

### Space

```text
O(n + m)
```

### Verdict

* ✅ Optimal
* ⚠️ Too concise alone (no explanation)
* ✅ Good if you explain it

---

# 4. Two sets + loop

```python
set1 = set(nums1)
set2 = set(nums2)
for num in set1:
    if num in set2:
```

### Idea

* Build both sets
* Manually compute intersection

### Time

```text
O(n + m)
```

### Space

```text
O(n + m)
```

### Verdict

* ✅ Interview-friendly
* ✅ Shows understanding

---

# 5. One set + result set

```python
set2 = set(nums2)
for num in nums1:
    if num in set2:
        result.add(num)
```

### Idea

* Only one set
* Use result set to handle duplicates

### Time

```text
O(n + m)
```

### Space

```text
O(m + k) → O(m)
```

### Verdict

* ✅ Very good
* ✅ Slightly better space than #4
* ✅ Clean logic

---

# 6. One set + remove (your best one)

```python
if num in set1:
    ans.append(num)
    set1.remove(num)
```

### Idea

* Use set for lookup
* **Remove to prevent duplicates**

### Time

```text
O(n + m)
```

### Space

```text
O(n)
```

### Key insight

* No need for result set
* Duplicate prevention via removal

### Verdict

* ✅✅ Best balance
* ✅ Interview-ready
* ✅ Clean and efficient

---

# Final Comparison Table

| Approach                | Time        | Space    | Interview |
| ----------------------- | ----------- | -------- | --------- |
| 1. List brute           | O(n² + n*m) | O(n)     | ❌         |
| 2. Double loop          | O(n*m)      | O(n)     | ❌         |
| 3. One-liner            | O(n + m)    | O(n + m) | ⚠️        |
| 4. Two sets             | O(n + m)    | O(n + m) | ✅         |
| 5. One set + result set | O(n + m)    | O(m)     | ✅✅        |
| 6. One set + remove     | O(n + m)    | O(n)     | ✅✅✅       |

---

# Final Answer (what to use in interviews)

### Best choices:

* ✅ **Approach 6 (remove)** → strongest
* ✅ **Approach 5 (result set)** → also very solid
* ✅ **Approach 4 (two sets)** → safe and clear

### Avoid:

* ❌ brute force
* ⚠️ one-liner without explanation

---

# Key takeaway

All optimal solutions rely on:

```text
Set → O(1) lookup → avoid nested loops
```

---
---

---
### Idea

* Put `nums1` into a set → fast lookup
* Loop through `nums2`
* If number is in set → add to result **and remove it**

---

### Why remove?

* So we **don’t add duplicates**
* Once used → it’s “consumed”

---

### One-line memory trick

> “Check in set, add to answer, remove to avoid duplicates.”

---

### Complexity

* Time: O(n + m)
* Space: O(n)
