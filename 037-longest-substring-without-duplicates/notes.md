**Longest Substring Without Repeating Characters**

**Idea:** Use a sliding window `[l, r]` with a set to track unique characters. Expand `r` each iteration; when a duplicate is found, shrink from the left until the window is valid again.

**Brute Force (O(n²)):**
- For each `i`, create a fresh set and expand `j` from `i` until a duplicate is found, then update `res`
- Throws away all progress on each duplicate — inefficient

```python
res = 0
for i in range(len(s)):
    charSet = set()
    for j in range(i, len(s)):
        if s[j] in charSet:
            break
        charSet.add(s[j])
    res = max(res, len(charSet))
return res
```

**Optimised — Sliding Window (O(n)):**
- Instead of resetting, just shrink the window from the left until the duplicate is gone

```python
chars = set()
l = 0, res = 0
for r in range(len(s)):
    while s[r] in chars:
        chars.remove(s[l])
        l += 1
    chars.add(s[r])
    res = max(res, r - l + 1)
return res
```

**Key points:**
- `r - l + 1` gives window length (+1 because 0-indexed)
- The while loop looks expensive but `l` only ever moves forward → O(n) total
- Update `res` **after** the while loop, so the window is always valid at that point

**Complexity:**
- Brute force — Time: O(n²), Space: O(n)
- Sliding window — Time: O(n), Space: O(n)

**Mistakes/things to watch:**
- Brute force instinct was to restart from scratch on each duplicate — the insight is to just *shrink from the left* instead


---

# Note from ChatGPT

Two valid approaches:

* Set (sliding window remove) → easier, safe for interviews
* HashMap (index jump) → more optimal thinking, stronger signal

Both are O(n).
Main difference is **how we handle duplicates**.

---

# Problem: Longest Substring Without Repeating Characters

---

# Approach 1: Sliding Window + Set

## Idea

* Maintain a window with unique characters using a set
* Expand `right`
* If duplicate → shrink from `left` until valid

## Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
```

## Key intuition

* “Remove until valid”
* Window always contains **unique characters**

## Complexity

* Time: O(n)
* Space: O(n)

## Pros

* Simple
* Hard to mess up

## Cons

* Slightly more operations (removals)

---

# Approach 2: Sliding Window + HashMap (Optimal Thinking)

## Idea

* Store last seen index of each character
* When duplicate appears → **jump left pointer directly**

## Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_index:
                left = max(left, char_index[s[right]] + 1)

            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length
```

## Key intuition

* “Jump instead of removing”
* Skip unnecessary steps

## Critical formula

```python
left = max(left, char_index[s[right]] + 1)
```

---

# Mistakes I made (IMPORTANT)

### 1. Wrong pointer movement

* ❌ I moved `left = right + 1`
* ✔ Correct: `left = last_index + 1`

---

### 2. Misunderstanding window reset

* ❌ Thought we “start a new substring”
* ✔ Actually:

  * We **only shrink window enough to remove duplicate**

---

### 3. Forgetting `max(left, …)`

* ❌ Might move `left` backwards
* ✔ Always:

```python
left = max(left, char_index[s[right]] + 1)
```

---

### 4. Confusion about hashmap overwrite

* ❌ Thought overwriting is wrong
* ✔ Correct:

  * Always keep **latest index**
  * Old index is irrelevant

---

### 5. Wrong length calculation due to wrong left

* ❌ Got negative / wrong window size
* ✔ Always:

```python
length = right - left + 1
```

---

# Mental Models

### Set version

> “Remove until no duplicates”

### HashMap version

> “Jump left to just after last occurrence”

---

# When to use which

### In interviews:

* If unsure → use **Set version**
* If confident → use **HashMap version**

---

# Final takeaway

> Never restart the window.
> Always adjust it just enough to stay valid.