# First Unique Character in a String - Notes

## Problem Summary

Given a string, return the index of the first character that appears only once.
If no such character exists, return -1.

Key requirement:

* Must return the **index in the original string**
* Order matters

---

## Core Insight

The problem has two separate concerns:

* **Frequency** - how many times each character appears
* **Order** - which character appears first in the string

Important realization:

> You cannot solve this using frequency alone
> You must preserve the original order of the string

---

## Approach 1 - Brute Force (Initial Thinking)

### Idea

For each character:

* Check if it appears anywhere else in the string
* If not, return its index

### Your Evolution

* Initially, you tried checking only the **right side**
* Realized this fails because duplicates can appear **before**
* Final fix: compare with all indices except itself

### Key Learning

> Always check the full string, not just one direction

### Complexity

* Time: O(n²)
* Space: O(1)

### Drawback

* Repeats the same work many times
* Inefficient for large inputs

---

## Approach 2 - Hashmap (Optimal Thinking)

### Idea

Split the problem into two passes:

1. Count frequency of each character
2. Scan string again to find first character with frequency 1

---

### Important Realization (Very Important)

You initially thought:

> "Hashmap doesn’t maintain order, so it won’t work"

Correction:

> We do NOT use hashmap for order
> We use it only for frequency

Order is preserved by scanning the **string again**

---

### Mental Model

* Hashmap = knowledge (frequency)
* String = timeline (order)

We:

1. Build knowledge
2. Walk timeline

---

### Mistake You Avoided

You considered:

* Iterating over hashmap keys to find value = 1

Why this is wrong:

* Hashmap does not guarantee correct order of first appearance
* Problem requires **first occurrence in string**

---

### Complexity

* Time: O(n)
* Space: O(1) (since only 26 lowercase letters)

---

## Approach 3 - Array (Optimized Hashmap)

### Idea

Replace hashmap with a fixed-size array of 26 elements.

Each index represents a character:

* index 0 → 'a'
* index 1 → 'b'
* ...
* index 25 → 'z'

---

### Key Mechanism

Convert character to index using:

> character_index = ord(c) - ord('a')

---

### Your Mistake (Important)

You tried:

* Looping over the count array
* Returning index where frequency == 1

Problem:

> That index represents a letter, NOT its position in the string

---

### Key Realization

> The array tells you "which letters are unique"
> The string tells you "where they appear first"

---

### Correct Thinking

* First pass: count frequencies using array
* Second pass: scan string and check frequency

---

### Mental Model Reinforced

> Array → how many times
> String → where first

You always need both.

---

### Complexity

* Time: O(n)
* Space: O(1)

---

## enumerate - Key Understanding

You learned:

* `enumerate(s)` gives both index and value
* Equivalent to:

  * index via range
  * value via indexing

---

### Why it's useful

* Cleaner code
* Avoids repeated indexing like `s[i]`
* Reduces mistakes

---

## Final Pattern (Very Important)

This problem teaches a reusable pattern:

### Two-pass pattern

1. Count / preprocess information
2. Scan original data to preserve order

---

## Problems Where This Appears

* First unique element
* Ransom note
* Anagram checks
* Frequency-based problems
* Majority element

---

## Final Takeaways

* Frequency alone is not enough - order matters
* Never rely on hashmap order for problems requiring sequence
* Always separate:

  * "what is true" (frequency)
  * "where it happens" (index/order)
* Prefer O(n) solutions over brute force when possible

---

## Your Progression Summary

* Started with partial brute force (right-side check)
* Fixed logic to full comparison
* Identified inefficiency (repeated work)
* Moved to hashmap (frequency caching)
* Resolved confusion about order
* Implemented optimal array solution
* Understood enumerate and cleaner iteration
