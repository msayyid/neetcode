# 804. Unique Morse Code Words - Revision Notes

## 1. Problem Summary

We are given a list of lowercase English words.

Each letter has a Morse code representation.

For each word, we transform it into one Morse code string by joining the Morse codes of its letters.

Example:

```text
"cab"

c -> "-.-."
a -> ".-"
b -> "-..."

Transformation = "-.-..--..."
```

We need to return how many unique Morse transformations exist among all words.

Key idea:

```text
Convert every word into Morse code and store the result in a set.
The set automatically keeps only unique transformations.
```

Important constraints:

```text
1 <= words.length <= 100
1 <= words[i].length <= 12
words[i] contains only lowercase English letters
```

The constraints are very small, but we still describe the general complexity as `O(n * m)`.

---

# 2. My Initial Understanding

Your understanding was correct.

You said:

* Loop through each word.
* Inside that, loop through each character.
* Convert each character to its Morse code.
* Use:

```python
alphabet[ord(w) - ord("a")]
```

to find the correct Morse code.

* Build the transformed Morse string.
* Add it to a set if it is not already there.
* Return the length of the set.

That is the correct idea.

The only small unnecessary part was checking:

```python
if new_conc not in my_set:
```

Because sets already ignore duplicates automatically.

So this is enough:

```python
my_set.add(new_conc)
```

---

# 3. Mistakes I Made

## Mistake 1: Created an unused dictionary

You had:

```python
my_map = {}
```

But it was never used.

Why it is unnecessary:

You already had the Morse alphabet stored in a list, and you used indexing with `ord()`. So no dictionary was needed.

A dictionary version would also be fine, but in your solution, `my_map` can be removed.

---

## Mistake 2: Checked before adding to a set

You wrote:

```python
if new_conc not in my_set:
    my_set.add(new_conc)
```

This works, but it is not needed.

Sets automatically avoid duplicates.

Cleaner version:

```python
my_set.add(new_conc)
```

Why this is better:

* Shorter
* Cleaner
* Same result
* More standard

---

## Mistake 3: Slight confusion about space complexity

You correctly noticed that:

* `alphabet` has 26 values
* `new_conc` stores one transformed word
* `my_set` stores unique transformations

The important idea is:

```text
Fixed-size things are O(1).
Input-dependent things are not O(1).
```

So:

```text
alphabet = O(1)
new_conc = O(m)
set = O(n * m)
```

---

# 4. Things I Learned

## 1. `ord()` can map letters to indexes

This expression:

```python
ord(w) - ord("a")
```

turns a lowercase letter into its alphabet index.

Examples:

```text
'a' -> 0
'b' -> 1
'c' -> 2
...
'z' -> 25
```

So this works:

```python
alphabet[ord(w) - ord("a")]
```

Because the Morse list is ordered from `a` to `z`.

---

## 2. A set is useful for counting unique values

A set only stores unique items.

Example:

```python
s = set()

s.add("abc")
s.add("abc")
s.add("xyz")

len(s)  # 2
```

So when a problem asks:

```text
How many different / unique / distinct values?
```

a set is often a strong clue.

---

## 3. Fixed constraints can be treated as constant in practice

Here:

```text
words.length <= 100
word length <= 12
```

So the maximum number of characters checked is:

```text
100 * 12 = 1200
```

That is tiny.

But in Big-O, we usually describe the general relationship:

```text
n = number of words
m = max/average length of each word

Time = O(n * m)
```

---

## 4. Morse string length is still proportional to word length

Each letter maps to a Morse string of length at most 4.

So a word of length `m` creates a Morse transformation of length at most about `4m`.

In Big-O:

```text
4m -> O(m)
```

We ignore the constant 4.

---

# 5. Pattern Recognition

## Main pattern: Hash Set / Unique Transformation

This problem uses the:

```text
Hash Set pattern
```

The trigger is the wording:

```text
Return the number of different transformations
```

Words like these often suggest a set:

```text
unique
different
distinct
no duplicates
count how many types
```

Why this pattern applies here:

We do not need to store how many times each Morse transformation appears.

We only care whether we have seen a transformation before.

So a set is perfect.

---

## How to recognize this in future problems

Think of a set when the problem asks:

```text
How many unique results are there?
Have we seen this before?
Remove duplicates.
Count distinct values.
```

Similar problem types:

```text
Count unique emails
Count unique normalized strings
Count distinct island shapes
Check if duplicates exist
Find unique transformations
```

---

# 6. Approaches Tried

## Approach 1: Convert each word and store in a set

### Main idea

For every word:

1. Convert each character into Morse code.
2. Join all Morse codes into one string.
3. Add the transformed string to a set.
4. Return the size of the set.

---

### Step-by-step algorithm

```text
1. Store the Morse codes in a list from a to z.
2. Create an empty set.
3. For each word in words:
   1. Create an empty string.
   2. For each character in the word:
      1. Convert the character to an index using ord(char) - ord("a").
      2. Use that index to get the Morse code.
      3. Add that Morse code to the transformed string.
   3. Add the transformed string to the set.
4. Return len(set).
```

---

### Pseudocode

```text
morse = [codes from a to z]
seen = empty set

for word in words:
    transformed = ""

    for char in word:
        index = ord(char) - ord("a")
        transformed += morse[index]

    add transformed to seen

return size of seen
```

---

### Time complexity

```text
O(n * m)
```

Where:

```text
n = number of words
m = max/average length of each word
```

We visit every character once.

Even though the LeetCode constraints are small, this is still the proper Big-O answer.

---

### Space complexity

```text
O(n * m)
```

Why:

* The Morse alphabet list is fixed size, so `O(1)`.
* Each transformed word can be length proportional to `m`.
* In the worst case, all `n` words have unique transformations.
* So the set can store up to `n` transformed strings.

Therefore:

```text
Set space = O(n * m)
```

---

### Why this approach works

Each word has exactly one Morse transformation.

If two words transform to the same Morse string, they should count as one unique transformation.

A set naturally handles this because it keeps only one copy of each transformation.

---

### Limitations of this approach

There are no serious limitations for this problem.

The only small improvement is code cleanliness:

Instead of:

```python
if new_conc not in my_set:
    my_set.add(new_conc)
```

use:

```python
my_set.add(new_conc)
```

---

### Is it interview-expected?

Yes.

This is the expected solution for this problem.

---

# 7. Optimized Approach

Your approach is already optimized.

The optimized pattern is:

```text
Hash Set + character transformation
```

Why it is better than a brute force comparison:

A worse approach would be:

```text
Store all transformations in a list.
For every new transformation, scan the list to check if it already exists.
```

That could add unnecessary repeated checking.

Using a set makes checking uniqueness simple and efficient.

Final optimized idea:

```text
Build each Morse transformation once.
Put it into a set.
Return the number of unique transformations.
```

---

# 8. Final Code

You did not ask for full final code, so no full code here.

Cleaner version of your logic would just remove:

```python
my_map = {}
```

and replace:

```python
if new_conc not in my_set:
    my_set.add(new_conc)
```

with:

```python
my_set.add(new_conc)
```

Your solution is already correct.

---

# 9. Interview Script

You can say:

```text
First, I store the Morse code values for the 26 lowercase English letters in a list.

Then I loop through every word. For each word, I build its Morse transformation by looping through its characters.

To find the Morse code of a character, I use ord(char) - ord("a") to convert the character into an index from 0 to 25. Then I use that index to access the Morse list.

After building the full Morse transformation for the word, I add it to a set.

I use a set because the problem asks for the number of different transformations, and a set automatically removes duplicates.

At the end, I return the length of the set.

The time complexity is O(n * m), where n is the number of words and m is the average or maximum length of a word, because I process every character once.

The space complexity is O(n * m) in the worst case, because all transformations could be unique and stored in the set.
```

---

# 10. Edge Cases and Dry Run

## Edge cases

### 1. Only one word

```text
words = ["a"]
```

Transformation:

```text
"a" -> ".-"
```

Unique transformations:

```text
1
```

Answer:

```text
1
```

---

### 2. Different words, same transformation

```text
words = ["gin", "zen"]
```

Both transform to:

```text
"--...-."
```

Set:

```text
{"--...-."}
```

Answer:

```text
1
```

---

### 3. Different words, different transformations

```text
words = ["gin", "gig"]
```

Transformations:

```text
"gin" -> "--...-."
"gig" -> "--...--."
```

Set:

```text
{"--...-.", "--...--."}
```

Answer:

```text
2
```

---

## Dry run

Input:

```text
words = ["gin", "zen", "gig", "msg"]
```

Morse transformations:

```text
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
```

Set updates:

```text
After "gin":
{"--...-."}

After "zen":
{"--...-."}
Same transformation, so set does not change.

After "gig":
{"--...-.", "--...--."}

After "msg":
{"--...-.", "--...--."}
Same transformation as "gig", so set does not change.
```

Final answer:

```text
2
```

---

# 11. Key Takeaways

```text
1. When the problem asks for unique / different / distinct values, think about using a set.

2. ord(char) - ord("a") is a useful trick for converting lowercase letters into indexes from 0 to 25.

3. Fixed-size lookup tables, like the 26-letter Morse alphabet, are O(1) space.

4. The real input-dependent space comes from the set of transformed words.

5. Time complexity is O(n * m), because we process every character of every word.

6. Your solution is correct, optimized, and interview-expected.
```
