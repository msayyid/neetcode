## Valid Anagram - Notes

### Problem

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, otherwise `False`.

---

## Key Idea

Two strings are anagrams if:

* They have the **same length**
* They contain the **same characters with the same frequencies**

---

## Approach 1: Sorting (Brute Force)

### Idea

Sort both strings and compare them.

### Complexity

* Time: O(n log n)
* Space: O(n) (Python `sorted()` creates a new array)

### Notes

* Not optimal due to sorting
* Simple and acceptable for small inputs

---

## Approach 2: Hashmap (Optimal - General Case)

### Idea

Count characters in `s`, subtract using `t`, and check if all counts return to zero.

---

### Initial Version (Your Implementation)

Steps:

1. Count characters from `s`
2. Decrease counts using `t`
3. Check if all values are zero

### Complexity

* Time: O(n)
* Space: O(k), where k = unique characters (worst case O(n))

---

### Mistake You Made

```python
if t[i] in my_map:
    my_map[t[i]] -= 1
```

Problem:

* If `t[i]` is NOT in the map, you ignore it
* This can lead to incorrect results

---

### Fix

```python
if t[i] not in my_map:
    return False
my_map[t[i]] -= 1
```

---

### Improved Version (One Loop)

Better approach:

* Process `s` and `t` simultaneously

Concept:

* Increment for `s[i]`
* Decrement for `t[i]`

Benefits:

* Fewer loops
* Cleaner logic
* No need for "missing key" check

---

### Final Hashmap Insight

* Time: O(n)
* Space: O(n)
* Works for **Unicode / large character sets**
* This is the **best general solution**

---

## Approach 3: Count Array (Best for This Problem)

### Idea

Use a fixed array of size 26 (for lowercase English letters)

---

### Your Initial Version

```python
index = 26 - (ord("z") - ord(s[i])) - 1
```

Issue:

* Overcomplicated
* Hard to read
* Not expected in interviews

---

### Improvement

```python
index = ord(s[i]) - ord('a')
```

Reason:

* 'a' → 0
* 'b' → 1
* ...
* 'z' → 25

Cleaner and standard

---

### Final Optimized Version (Your Best Version)

* One loop
* Increment for `s`
* Decrement for `t`

---

### Complexity

* Time: O(n)
* Space: O(26) → O(1)

---

## Important Insight: When to Use What

### Use Count Array when:

* Characters are limited (e.g., lowercase English letters)
* You want O(1) space

### Use Hashmap when:

* Characters are large or unknown (Unicode)
* Flexibility is needed

---

## Follow-up: Unicode Characters

If inputs contain Unicode:

* Count array **does NOT work**
* Must use hashmap

Your hashmap solution already supports this.

---

## Key Optimization Pattern Learned

> When comparing two arrays/strings, try to process both in the same loop

Example:

* +1 for one input
* -1 for the other

This reduces passes and simplifies logic

---

## Final Comparison

| Approach    | Time       | Space | Notes                    |
| ----------- | ---------- | ----- | ------------------------ |
| Sorting     | O(n log n) | O(n)  | Simple but not optimal   |
| Hashmap     | O(n)       | O(n)  | Best general solution    |
| Count array | O(n)       | O(1)  | Best for limited charset |

---

## Interview Takeaway

* Start with hashmap (safe, general)
* Then optimize to count array if constraints allow
* Mention Unicode limitation clearly

---

## Your Progress

* Correctly identified optimal solution
* Improved from 3-pass → 1-pass
* Fixed correctness bug (missing key case)
* Simplified index logic
* Understood tradeoffs between approaches

This is exactly how strong candidates evolve solutions during interviews.
