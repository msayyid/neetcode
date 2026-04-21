# Minimum Window Substring - Notes

---

## Problem Summary

Given two strings `s` and `t`, find the **smallest substring of `s`** that contains:

* all characters of `t`
* including duplicates

If no such substring exists → return `""`

---

## Core Idea

This is a **sliding window problem** with:

* **expansion** (right pointer `r`)
* **contraction** (left pointer `l`)

Goal:

* Expand until the window is **valid**
* Then shrink to make it **as small as possible**

---

## Key Data Structures

### 1. `count_t`

Stores required frequencies of characters in `t`

Example:

```python
t = "AAB"
count_t = {A:2, B:1}
```

---

### 2. `window`

Stores frequencies of characters in the current window

---

### 3. `have` and `need`

```python
need = len(count_t)
have = number of characters that meet required frequency
```

Important:

* `need` = number of **unique characters**
* NOT total characters

---

## When is a window VALID?

A window is valid when:

```python
have == need
```

Meaning:

> Every required character has reached its required frequency

---

## Sliding Window Algorithm

### Step 1 - Build frequency map

```python
count_t
```

---

### Step 2 - Expand window

For each `r`:

* add `s[r]` to `window`
* if:

```python
window[c] == count_t[c]
```

→ increment `have`

---

### Step 3 - Shrink window

While:

```python
have == need
```

* update result (shortest window)
* remove `s[l]` from window
* if:

```python
window[s[l]] < count_t[s[l]]
```

→ decrement `have`

* move `l`

---

### Step 4 - Continue

Repeat expand + shrink until end of string

---

## Key Observations

### 1. We do NOT compare full dictionaries

Wrong:

```python
count_t == window
```

Because:

* window may contain extra characters
* window may have higher frequencies

---

### 2. We only care about minimum requirement

Correct idea:

> Each character must appear **at least** required number of times

---

### 3. `have` tracks satisfied characters

* increase only when:

```python
window[c] == count_t[c]
```

* decrease only when:

```python
window[c] < count_t[c]
```

---

## Why `have` works

Instead of checking all characters every time (slow),

we track how many are satisfied incrementally.

This makes the solution **O(n)**.

---

## Time Complexity

```text
O(n)
```

* `r` moves forward once
* `l` moves forward once

---

## Space Complexity

```text
O(k)
```

* where `k` = number of unique characters

---

# Mistakes I Made

---

### 1. Comparing dictionaries directly

I tried:

```python
count1 == count2
```

Problem:

* fails when frequencies exceed required
* ignores valid windows with extra characters

---

### 2. Overcomplicating with `get_real_count`

I created a function to filter relevant characters.

Problem:

* unnecessary work
* increases complexity
* wrong abstraction

---

### 3. Not understanding duplicates

I thought:

> need should include duplicate counts

But actually:

```python
need = number of unique characters
```

Duplicates are handled via frequency comparison.

---

### 4. Not tracking correct window boundaries

I used:

```python
s[:i+1]
```

Problem:

* ignores left pointer
* always starts from index 0

Correct:

```python
s[l:r+1]
```

---

### 5. Confusion when shrinking window

I didn’t understand:

```python
if window[s[l]] < count_t[s[l]]:
    have -= 1
```

Now I understand:

* removing a character can break validity
* when frequency drops below required → window becomes invalid

---

# Things I Learned

---

### 1. Sliding window pattern

This problem follows:

```text
expand → validate → shrink → repeat
```

---

### 2. “At least” vs “exact match”

This problem is about:

```text
meeting minimum requirements
```

NOT:

```text
exact frequency match
```

---

### 3. Tracking validity efficiently

Instead of rechecking the whole window:

* use `have` and `need`

---

### 4. When to increase/decrease `have`

* increase → when requirement is first met
* decrease → when requirement is broken

---

### 5. Window shrinking is greedy

Once valid:

* shrink as much as possible
* stop exactly when it becomes invalid

---

# Things I Didn’t Know Before

---

### 1. Why `need = len(count_t)`

I thought it should include duplicates.

Now I know:

* we track unique characters
* duplicates are handled via frequency

---

### 2. Why equality check fails

I assumed:

```python
window == count_t
```

But:

* window can have extra values
* still valid

---

### 3. Importance of exact moment of satisfaction

Key idea:

```python
window[c] == count_t[c]
```

This is the moment a character becomes satisfied.

---

### 4. Importance of dropping below requirement

Key idea:

```python
window[c] < count_t[c]
```

This is when validity is lost.

---

# Final Mental Model

Think of it like:

* `count_t` = requirements
* `window` = current resources
* `have` = how many requirements satisfied
* `need` = total requirements

---

Algorithm:

```text
1. Expand window until all requirements met
2. Shrink window to minimum size
3. Save best result
4. Repeat
```

---

# One-line summary

> Expand until valid, shrink while valid, track the smallest window.
