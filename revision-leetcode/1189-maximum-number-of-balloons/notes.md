# LeetCode 1189 - Maximum Number of Balloons Notes

## 1. Problem Summary

You are given a string `text`.

You need to find how many times you can form the word:

```text
balloon
```

Each character in `text` can be used only once.

The word `"balloon"` needs:

```text
b -> 1
a -> 1
l -> 2
o -> 2
n -> 1
```

So the main idea is:

```text
Count the characters, then find which required character limits the number of full "balloon" words.
```

Important constraint:

```text
1 <= text.length <= 10^4
```

So an `O(n)` solution is expected.

---

# 2. My Initial Understanding

You correctly understood that you needed to count characters first.

You started with:

```python
count = {}
for c in text:
    count[c] = count.get(c, 0) + 1
```

This part was correct.

You also created a dictionary for the word `"balloon"`:

```python
balloon["b"] = 1
balloon["a"] = 1
balloon["l"] = 2
balloon["o"] = 2
balloon["n"] = 1
```

That also showed the right direction.

Where you got stuck was deciding what to do after counting. You were thinking about manually subtracting letters and building another dictionary, but the simpler idea is to calculate how many balloons each letter can support.

---

# 3. Mistakes I Made

## Mistake 1: Trying to build the word manually

You started going toward something like:

```python
if key == "b":
    if val - balloon[key] >= 0:
```

This is not wrong thinking, but it makes the problem harder than needed.

Why?

Because you do not need to actually construct each `"balloon"` one by one. You only need to know the maximum possible number.

Better way:

```text
Count each needed character.
Divide l and o by 2.
Take the minimum.
```

---

## Mistake 2: Confusion around `// 2`

You were unsure why we use:

```python
count.get("l", 0) // 2
count.get("o", 0) // 2
```

The reason is that `"balloon"` needs 2 `l`s and 2 `o`s.

Example:

```text
l count = 5
```

You can make only 2 full pairs of `l`.

```text
5 // 2 = 2
```

The extra 1 `l` is useless because another balloon needs 2 `l`s.

---

## Mistake 3: Thinking `5n` might not be `O(n)`

You noticed that this code scans the string 5 times:

```python
text.count("b")
text.count("a")
text.count("l")
text.count("o")
text.count("n")
```

You were right that this is `5n`.

But in Big O:

```text
5n = O(n)
```

So both versions are technically `O(n)`, but the dictionary version is better in practice because it scans once.

---

# 4. Things I Learned

## 1. Frequency counting

When a problem asks how many times characters/items appear, think of a hashmap/dictionary.

Pattern trigger:

```text
Problem asks about counts/frequencies of characters or numbers.
```

Here, we count how many times each character appears in `text`.

---

## 2. Limiting resource idea

The answer is controlled by the character that runs out first.

Example:

```text
b = 10
a = 10
l = 10
o = 1
n = 10
```

Even though most letters are available, you cannot make even 1 `"balloon"` because you need 2 `o`s.

So:

```text
o // 2 = 0
answer = 0
```

---

## 3. Why use `min()`

Each required letter tells us how many balloons it can support:

```text
b count       -> balloons supported by b
a count       -> balloons supported by a
l count // 2  -> balloons supported by l
o count // 2  -> balloons supported by o
n count       -> balloons supported by n
```

The final answer is the smallest of these.

```text
The weakest/lowest available character decides the answer.
```

---

## 4. Why `get(char, 0)` is useful

If a character does not exist in the dictionary, `get` returns `0`.

Example:

```python
count.get("b", 0)
```

Means:

```text
Give me the count of "b".
If "b" does not exist, give me 0.
```

This prevents errors and makes the code clean.

---

# 5. Pattern Recognition

## Main Pattern

```text
Hashmap / Frequency Counting
```

## Trigger

Think of this pattern when the problem says:

```text
How many times can we form something?
How many characters/items do we have?
Each item can be used once.
Need to compare available counts with required counts.
```

## Why this pattern applies here

We need to know how many of each letter we have in `text`.

The word `"balloon"` has required frequencies:

```text
b: 1
a: 1
l: 2
o: 2
n: 1
```

So the problem becomes a frequency comparison problem.

## Similar problem types

This pattern appears in problems like:

```text
Can we construct ransom note from magazine?
Can we form words from characters?
Find common characters.
Check if two strings are anagrams.
Count occurrences of numbers or letters.
```

---

# 6. Approaches Tried

## Approach 1: Manual construction idea

### Main Idea

Count characters, then try to subtract the required letters for `"balloon"`.

### Step-by-step algorithm

```text
1. Count all characters in text.
2. Store required characters for "balloon".
3. Try to check if enough characters exist.
4. Repeat or build another structure.
```

### Pseudocode

```text
count characters in text

while enough b, a, l, o, n exist:
    subtract 1 b
    subtract 1 a
    subtract 2 l
    subtract 2 o
    subtract 1 n
    answer += 1
```

### Time Complexity

Could still be okay, but it is less clean.

### Space Complexity

```text
O(1)
```

Because there are only lowercase English letters.

### Why it works

It simulates making balloons one by one.

### Limitation

It is more complicated than necessary.

### Interview Expected?

Not the cleanest interview answer. It is more like a starting idea.

---

## Approach 2: Frequency count + minimum

### Main Idea

Count all characters once. Then calculate how many balloons each required character can support.

### Step-by-step algorithm

```text
1. Create a dictionary count.
2. Count every character in text.
3. Get count of b.
4. Get count of a.
5. Get count of l and divide by 2.
6. Get count of o and divide by 2.
7. Get count of n.
8. Return the minimum of these values.
```

### Pseudocode

```text
count = empty dictionary

for char in text:
    count[char] += 1

b = count of "b"
a = count of "a"
l = count of "l" // 2
o = count of "o" // 2
n = count of "n"

return min(b, a, l, o, n)
```

### Time Complexity

```text
O(n)
```

We scan the string once.

### Space Complexity

```text
O(1)
```

Even though we use a dictionary, the string only contains lowercase English letters, so at most 26 keys.

### Why it works

Each balloon needs fixed numbers of each character.

The letter with the smallest available amount decides how many full balloons can be made.

### Limitation

No real limitation for this problem. This is clean and efficient.

### Interview Expected?

Yes. This is interview-expected.

---

## Approach 3: Using `text.count()`

### Main Idea

Use Python’s built-in `.count()` method to count each needed letter.

### Step-by-step algorithm

```text
1. Count "b" in text.
2. Count "a" in text.
3. Count "l" in text and divide by 2.
4. Count "o" in text and divide by 2.
5. Count "n" in text.
6. Return the minimum.
```

### Pseudocode

```text
b = text.count("b")
a = text.count("a")
l = text.count("l") // 2
o = text.count("o") // 2
n = text.count("n")

return min(b, a, l, o, n)
```

### Time Complexity

```text
O(n)
```

But practically it scans the string 5 times:

```text
5n = O(n)
```

### Space Complexity

```text
O(1)
```

### Why it works

It directly counts only the letters needed for `"balloon"`.

### Limitation

It is slightly less efficient in practice than the dictionary version because it scans the string multiple times.

### Interview Expected?

It is acceptable for an easy problem, but the dictionary version is more standard because it shows frequency counting clearly.

---

# 7. Optimized Approach

The optimized approach is:

```text
Frequency count + minimum limiting character
```

Why it is better:

```text
It scans the string once.
It avoids manually building balloons.
It directly calculates the answer.
```

The pattern is hashmap/frequency counting.

Why that pattern applies:

```text
We need to know how many times each required character appears.
```

The important observation is:

```text
"l" and "o" appear twice in "balloon", so their counts must be divided by 2.
```

Then:

```text
answer = min(b, a, l // 2, o // 2, n)
```

---

# 8. Final Code

You already wrote the correct final code.

Your dictionary version is clean, correct, and interview-expected.

Cleaner note:

```text
Your version is already standard.
No need to overcomplicate it.
```

---

# 9. Interview Script

You can explain it like this:

```text
First, I count the frequency of every character in the input string.

The word "balloon" requires one b, one a, two l's, two o's, and one n.

After counting, I check how many balloons each required character can support.

For b, a, and n, the number of balloons supported is just their count.

For l and o, since each balloon needs two of them, I divide their counts by 2 using integer division.

The final answer is the minimum of these values, because the character that runs out first limits how many full balloons I can form.

This runs in O(n) time because I scan the string once, and O(1) space because there are only 26 lowercase letters.
```

For the `text.count()` version:

```text
Another simple approach is to directly count b, a, l, o, and n using text.count().

This still gives O(n) time in Big O, but it scans the string five times, so the dictionary version is slightly better in practice.
```

---

# 10. Edge Cases and Dry Run

## Edge Case 1: Missing required letter

```text
text = "leetcode"
```

Counts:

```text
b = 0
a = 0
l = 1
o = 1 // 2 = 0
n = 0
```

Answer:

```text
0
```

Because we cannot form `"balloon"`.

---

## Edge Case 2: Enough letters for exactly one balloon

```text
text = "nlaebolko"
```

Relevant counts:

```text
b = 1
a = 1
l = 2 // 2 = 1
o = 2 // 2 = 1
n = 1
```

Answer:

```text
min(1, 1, 1, 1, 1) = 1
```

---

## Edge Case 3: More of some letters but not enough of others

```text
b = 10
a = 10
l = 10
o = 1
n = 10
```

For `o`:

```text
1 // 2 = 0
```

Answer:

```text
0
```

Because each balloon needs 2 `o`s.

---

## Dry Run

Input:

```text
text = "loonbalxballpoon"
```

Counts needed:

```text
b = 2
a = 2
l = 4
o = 4
n = 2
```

Convert to balloon support:

```text
b = 2
a = 2
l = 4 // 2 = 2
o = 4 // 2 = 2
n = 2
```

Answer:

```text
min(2, 2, 2, 2, 2) = 2
```

---

# 11. Key Takeaways

```text
1. This is a frequency counting problem.
2. Count the letters first.
3. "balloon" needs 2 l's and 2 o's.
4. Use // 2 to count full pairs.
5. The answer is the minimum supported balloons among b, a, l, o, and n.
6. The dictionary version is cleaner and more interview-expected.
7. text.count() version is also O(n), but scans the string 5 times.
```

Main thing to remember:

```text
When forming a word from letters, the rarest required character limits the answer.
```
