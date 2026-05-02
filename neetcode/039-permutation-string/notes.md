# Permutation in String - Notes

## Problem

We are given two strings:

* `s1` -> the pattern
* `s2` -> the bigger string

We must return `True` if **any permutation of `s1`** appears as a **substring** inside `s2`.

---

## What is a permutation?

A permutation means:

* same characters
* same frequencies
* order can be different

Example:

```text
s1 = "abc"

permutations:
abc
acb
bac
bca
cab
cba
```

So if `s2` contains `"cab"` or `"bca"` or any other arrangement, the answer is `True`.

---

## Key observation

We do **not** actually need to generate all permutations.

We only need to check whether some substring in `s2`:

* has length `len(s1)`
* has the same character counts as `s1`

That means this is really an **anagram checking** problem.

---

# Approach 1 - Brute Force

## Idea

Check every substring of `s2` with length `k = len(s1)`.

For each substring:

* count its characters
* compare its count with the count of `s1`

If they match, return `True`.

Otherwise, after checking all substrings, return `False`.

---

## Why this works

If two strings have:

* the same length
* the same frequency of every character

then one is a permutation of the other.

So if a window in `s2` has the same count as `s1`, that window is a valid permutation.

---

## Code

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False

        def get_count(s):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            return count

        count1 = get_count(s1)

        for i in range(len(s2) - k + 1):
            substring = s2[i:i+k]
            count2 = get_count(substring)

            if count1 == count2:
                return True
        
        return False
```

---

## How the loop works

### Step 1

Set:

```python
k = len(s1)
```

If `s1 = "abc"`, then `k = 3`.

So we only care about substrings of length 3 in `s2`.

---

### Step 2

Loop through all possible starting positions:

```python
for i in range(len(s2) - k + 1):
```

Why this range?

Because each substring is `s2[i:i+k]`.

We need `i + k` to stay inside the string.

---

### Step 3

Extract current substring:

```python
substring = s2[i:i+k]
```

Example:

```text
s2 = "lecabee"
k = 3
```

Substrings checked:

* `"lec"`
* `"eca"`
* `"cab"`
* `"abe"`
* `"bee"`

---

### Step 4

Build frequency count for this substring:

```python
count2 = get_count(substring)
```

---

### Step 5

Compare with `s1` count:

```python
if count1 == count2:
    return True
```

If counts match, substring is a permutation of `s1`.

---

## Complexity

### Time complexity

Let:

* `n = len(s2)`
* `k = len(s1)`

#### `count1 = get_count(s1)`

This takes `O(k)`.

#### Main loop

There are about `n - k + 1` windows, which is `O(n)`.

Inside each iteration:

* `substring = s2[i:i+k]` -> `O(k)`
* `get_count(substring)` -> `O(k)`
* `count1 == count2` -> compares 26 elements -> `O(1)`

So each iteration is `O(k)`.

Total:

```text
O(n * k)
```

### Space complexity

We use arrays of size 26.

That is constant extra memory:

```text
O(1)
```

---

## Weakness of this approach

We rebuild the frequency count from scratch for every window.

That repeated work is what makes it slower.

---

# Approach 2 - Optimal Sliding Window

## Main idea

Instead of rebuilding the count for every substring, we:

* build the first window once
* then slide the window one step at a time
* when window moves:

  * one character leaves
  * one character enters

So instead of recounting the whole window, we only update 2 values.

This is the key optimization.

---

## Code

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False

        count1 = [0] * 26
        for c in s1:
            count1[ord(c) - ord("a")] += 1

        count2 = [0] * 26
        for c in s2[:k]:
            count2[ord(c) - ord("a")] += 1

        if count1 == count2:
            return True

        for r in range(k, len(s2)):
            count2[ord(s2[r]) - ord("a")] += 1
            count2[ord(s2[r - k]) - ord("a")] -= 1

            if count1 == count2:
                return True

        return False
```

---

# Detailed explanation of the second approach

This is the most important part.

---

## Step 1 - Handle impossible case

```python
if k > len(s2):
    return False
```

If `s1` is longer than `s2`, no substring of `s2` can match it.

---

## Step 2 - Build count for `s1`

```python
count1 = [0] * 26
for c in s1:
    count1[ord(c) - ord("a")] += 1
```

This stores the target frequency.

Example:

```text
s1 = "abc"
```

Then `count1` will represent:

* a: 1
* b: 1
* c: 1

---

## Step 3 - Build count for first window in `s2`

```python
count2 = [0] * 26
for c in s2[:k]:
    count2[ord(c) - ord("a")] += 1
```

If `k = 3`, then this builds the count for the first 3 characters.

Example:

```text
s2 = "lecabee"
k = 3
first window = "lec"
```

So `count2` initially represents `"lec"`.

---

## Step 4 - Check the first window

```python
if count1 == count2:
    return True
```

We must do this because the answer might already be in the first window.

---

# Step 5 - Main loop in the sliding window

```python
for r in range(k, len(s2)):
```

This is the part that confuses many people, so let’s go slowly.

---

## What does `r` mean?

`r` is the index of the **new character entering the window**.

We already used the first window `s2[0:k]`.

So now we start from index `k`, because that is the first new character after the initial window.

---

## Example

Let:

```text
s1 = "abc"
s2 = "lecabee"
k = 3
```

Initial window:

```text
"lec"
```

Its indices are:

```text
0, 1, 2
```

The next character after that is at index `3`, which is `'a'`.

That is why the loop starts with:

```python
r = 3
```

---

## What happens when the window moves?

Window size must always stay `k`.

So when the window shifts right by 1:

* one old character leaves from the left
* one new character enters from the right

---

## First movement example

### Old window:

```text
"lec"
```

### New window:

```text
"eca"
```

What changed?

* `'l'` left
* `'a'` entered

So instead of recounting `"eca"` from scratch, we do:

* subtract 1 for `'l'`
* add 1 for `'a'`

---

## How code does that

### Add the new character

```python
count2[ord(s2[r]) - ord("a")] += 1
```

If `r = 3`, then `s2[r] = 'a'`.

So we increase count of `'a'`.

---

### Remove the old character

```python
count2[ord(s2[r - k]) - ord("a")] -= 1
```

Why `r - k`?

Because that is the index of the character leaving the window.

If:

```text
r = 3
k = 3
```

then:

```text
r - k = 0
```

and `s2[0] = 'l'`.

So we decrease count of `'l'`.

---

## Why `r - k` works

Suppose current new character is at index `r`.

The previous window had size `k`.

So the character leaving is exactly `k` positions behind `r`.

That is why:

```text
remove index = r - k
```

---

## Same example again, slowly

### Initial window

```text
"lec"
```

### `r = 3`

* add `s2[3] = 'a'`
* remove `s2[0] = 'l'`

Now window becomes:

```text
"eca"
```

---

### `r = 4`

* add `s2[4] = 'b'`
* remove `s2[1] = 'e'`

Window becomes:

```text
"cab"
```

---

### `r = 5`

* add `s2[5] = 'e'`
* remove `s2[2] = 'c'`

Window becomes:

```text
"abe"
```

---

## Then compare after each update

```python
if count1 == count2:
    return True
```

If updated window matches `s1` frequency, we found a permutation.

---

# Very important mental model for the main loop

At every step:

```text
Add -> s2[r]
Remove -> s2[r - k]
```

That is the whole loop idea.

If you remember just this, the sliding window becomes much easier.

---

# Why this is better than brute force

## Brute force

For every new window:

* build count from scratch

That costs `O(k)` per window.

---

## Sliding window

For every new window:

* update only 2 characters

That costs `O(1)` per window.

So we avoid repeated work.

---

# Complexity of optimal solution

## Time complexity

### Build `count1`

`O(k)`

### Build first `count2`

`O(k)`

### Main loop

Runs about `n - k` times, which is `O(n)`.

Inside each iteration:

* add one char -> `O(1)`
* remove one char -> `O(1)`
* compare two arrays of size 26 -> `O(1)`

So each iteration is constant time.

Total:

```text
O(n)
```

More precisely you could say `O(n + k)`, but in interviews this is usually simplified to:

```text
O(n)
```

---

## Space complexity

Two arrays of size 26:

```text
O(1)
```

---

# Comparison of both approaches

## Brute force

### Idea

Check every substring and rebuild its count.

### Time

```text
O(n * k)
```

### Space

```text
O(1)
```

### Pros

* easier to understand
* good first solution in interview

### Cons

* repeated counting
* slower

---

## Optimal sliding window

### Idea

Build first window once, then update counts while sliding.

### Time

```text
O(n)
```

### Space

```text
O(1)
```

### Pros

* efficient
* interview expected solution

### Cons

* loop indexing can be confusing at first

---

# What to say in an interview

A good explanation would be:

> First, I can solve it by checking every substring of length `len(s1)` and comparing character frequencies. That works in `O(n*k)`.
>
> To optimize it, I use a sliding window. I keep a frequency array for the current window in `s2`. When the window moves, I add the new character entering the window and remove the old character leaving it. This avoids rebuilding the count each time and reduces the complexity to `O(n)`.

---

# Final takeaway

## Brute force mindset

“Check every window and count from scratch.”

## Optimal mindset

“Reuse previous window count. Only 2 characters change when the window moves.”

## Main loop rule

Always remember:

```text
Add -> s2[r]
Remove -> s2[r - k]
```

That is the most important part of this problem.



---
---
---

# 🧠 Problem Idea (Permutation in String)

We need to check:

> Does any substring of `s2` (length = len(s1)) have the **same character frequency** as `s1`?

---

# 🔑 Core Idea (Matches Approach)

Instead of comparing full arrays every time:

👉 Track how many characters currently match

```text
matches = number of indices where count1[i] == count2[i]
```

* If `matches == 26` → permutation found

---

# ⚙️ Setup

### 1. Frequency arrays

```text
count1 → frequency of s1
count2 → frequency of current window in s2
```

---

### 2. Build first window

```text
Window size = len(s1)
Fill count2 using first window of s2
```

---

### 3. Initialize matches

```text
matches = number of indices where count1[i] == count2[i]
```

---

# 🔁 Sliding Window

Loop through `s2`:

```text
r → new character entering
l → old character leaving
```

At each step:

---

## ➕ Step 1: Add new character

```text
count2[new_char] += 1
```

### Cases:

* ✅ became equal → `matches += 1`
* ❌ was equal, now too big → `matches -= 1`

---

## ➖ Step 2: Remove old character

```text
count2[old_char] -= 1
```

### Cases:

* ✅ became equal → `matches += 1`
* ❌ was equal, now too small → `matches -= 1`

---

# 🎯 When to return

```text
if matches == 26 → return True
```

At the end:

```text
return matches == 26
```

---

# 🧠 Key Insight

Only **2 characters change per step**:

* one enters
* one leaves

👉 So only those indices can affect `matches`

---

# ⚠️ Important Conditions (Memorize)

### ADD

```python
if count1[i] == count2[i]:
    matches += 1
elif count1[i] + 1 == count2[i]:
    matches -= 1
```

👉 `+1` means:

> we made it too big → broke equality

---

### REMOVE

```python
if count1[i] == count2[i]:
    matches += 1
elif count1[i] - 1 == count2[i]:
    matches -= 1
```

👉 `-1` means:

> we made it too small → broke equality

---

# 🧩 Mental Model (Very Important)

For each update, only ask:

```text
Did this letter:
- become equal? → +1
- stop being equal? → -1
```

---

# ⏱️ Complexity

* Time: O(n)
* Space: O(1) (26 letters)

---

# 🚫 Common Mistakes

* ❌ Updating `count1` instead of `count2`
* ❌ Forgetting first window initialization
* ❌ Using `!=` instead of detecting transitions
* ❌ Forgetting final `return matches == 26`

---

# 🎯 Interview Tip

Say:

> “Instead of comparing frequency arrays every time, I track how many characters match and update that count as the window slides.”

---

# 🧠 One-Line Summary

> Maintain a sliding window and track how many of the 26 character counts match. If all match, we found a permutation.

----
----
----


# ⚡ Permutation in String - Matches Cheat Sheet

* Build `count1` (s1) and `count2` (first window in s2)
* `matches = number of indices where count1[i] == count2[i]`
* Slide window:

  * add right char → update count → adjust `matches`
  * remove left char → update count → adjust `matches`
* If `matches == 26` → return `True`
* End → `return matches == 26`

---

# 🧠 Update Rules

**ADD:**

* equal now → `+1`
* was equal, now too big → `-1`

**REMOVE:**

* equal now → `+1`
* was equal, now too small → `-1`

---

# 🔑 Memory Trick

> Only 2 letters change → only update `matches` for those

---

# 🎯 One-liner

> Track how many characters match instead of comparing arrays
