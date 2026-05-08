# 409. Longest Palindrome - Revision Notes

## 1. Problem Summary

We are given a string `s` containing lowercase and uppercase English letters.

We need to return the length of the longest palindrome that can be built using those letters.

Important detail:

```text
We can rearrange the letters.
```

So this is not about finding a palindrome already inside the string.

Example:

```text
s = "abccccdd"
```

We can rearrange some letters to build:

```text
"dccaccd"
```

Length is:

```text
7
```

Key idea:

```text
A palindrome needs pairs of characters on both sides.
Only one character with an odd count can be placed in the middle.
```

Constraints:

```text
1 <= s.length <= 2000
s contains lowercase and uppercase English letters only
```

Also:

```text
"A" and "a" are different characters.
```

---

# 2. My Initial Understanding

At first, you started by checking whether the whole string was already a palindrome:

```python
if s == s[::-1]:
    return len(s)
```

This part is logically fine, but it is not enough for this problem.

Then you tried to build new strings using loops and check:

```python
if new_string == new_string[::-1]:
```

That means your first approach was more like:

```text
Try different combinations/orders and check if they form a palindrome.
```

What you understood correctly:

```text
A palindrome reads the same forward and backward.
```

Where the confusion happened:

```text
The problem does not ask for a palindrome that already exists in the original order.
It asks for the longest palindrome we can build by rearranging the letters.
```

So the main shift was:

```text
Do not think about order.
Think about character counts.
```

---

# 3. Mistakes I Made

## Mistake 1: Treating it like a substring/subsequence problem

You were trying to build strings and check whether each one was a palindrome.

Why this is not ideal:

```text
The order of characters does not matter here.
We only care how many times each character appears.
```

For example:

```text
s = "abccccdd"
```

The answer is not found by looking at the original order. We can rearrange letters however we want.

---

## Mistake 2: Adding every character with count 1

You had this logic:

```python
elif val == 1:
    length += val
```

The issue:

```text
If many characters appear once, we cannot use all of them in the palindrome.
```

Example:

```text
s = "abc"
```

Counts:

```text
a: 1
b: 1
c: 1
```

Your earlier logic would add all 3 and return:

```text
3
```

But `"abc"` cannot be rearranged into a palindrome of length 3.

The best possible palindrome is:

```text
"a"
```

or

```text
"b"
```

or

```text
"c"
```

So the answer is:

```text
1
```

Why?

```text
Only one odd-count character can go in the middle.
```

---

## Mistake 3: Thinking odd count means unusable

Odd counts are still useful.

Example:

```text
count = 5
```

We cannot use all 5 as pairs, but we can use:

```text
4
```

Because:

```text
2 go on the left
2 go on the right
1 may go in the middle
```

So for odd counts:

```text
use count - 1
```

Then at the end, if there was at least one odd count, add:

```text
+1
```

for the middle character.

---

# 4. Things I Learned

## Key palindrome rule

A palindrome can have:

```text
Many even-count characters
At most one odd-count character
```

Examples:

```text
"ccddcc" -> valid
"ccdaddc" -> valid, "a" is in the middle
"abc" -> cannot use all 3
```

---

## Even counts can be fully used

Example:

```text
c: 4
d: 2
```

We can use all of them:

```text
ccddcc
```

Because they can be split evenly between the left and right sides.

---

## Odd counts can mostly be used

Example:

```text
a: 5
```

We can use:

```text
4
```

as pairs.

The remaining `1` can possibly be used as the middle character.

---

## Only one odd character can be in the middle

Example:

```text
a: 1
b: 1
c: 1
```

We cannot use all 3.

Best length:

```text
1
```

Because only one character can sit in the center.

---

## The `has_odd` flag

This flag remembers:

```text
Did I see at least one odd frequency?
```

If yes, we can add one middle character at the end.

```python
has_odd = True
```

Then after the loop:

```python
if has_odd:
    length += 1
```

---

# 5. Pattern Recognition

## Main Pattern

```text
Hashmap / Frequency Counting
```

## Trigger: What clue tells me to use this pattern?

The problem says:

```text
"can be built with those letters"
```

This is the big clue.

Whenever the problem asks:

```text
Can we build something from given characters?
How many letters can we use?
Can we rearrange the letters?
Are character counts enough?
```

You should think:

```text
Frequency counting
```

Because the original order does not matter.

---

## Why this pattern applies here

To build a palindrome, we only need to know:

```text
How many times each character appears.
```

We do not need to know:

```text
Where each character appears.
```

So a hashmap is perfect:

```python
count[c] = count.get(c, 0) + 1
```

---

## Common signs for this pattern

Use frequency counting when you see phrases like:

```text
"using these letters"
"can be rearranged"
"build from characters"
"number of occurrences"
"anagram"
"same characters"
```

---

## Similar problem types

This same pattern appears in problems like:

```text
Valid Anagram
Ransom Note
Group Anagrams
First Unique Character
Find All Anagrams in a String
Word Pattern
Isomorphic Strings
```

---

# 6. Approaches Tried

## Approach 1: Brute Force String Building

### Main idea

Try to build different strings and check if each one is a palindrome.

### Step-by-step algorithm

```text
1. Start from each character.
2. Add other characters.
3. Check whether the new string is a palindrome.
4. Keep track of the maximum length.
```

### Pseudocode

```text
max_length = 0

for each starting index:
    new_string = current character

    for each other index:
        add character to new_string

        if new_string is palindrome:
            update max_length

return max_length
```

### Time complexity

This approach can become very inefficient because you are building many strings and checking reverses.

Approximate:

```text
O(n^3) or worse depending on implementation
```

### Space complexity

```text
O(n)
```

because of the temporary string.

### Why this approach is not good

The problem allows rearranging characters, so checking built strings in the original order is not the right direction.

### Interview expectation

```text
Not interview-expected.
```

It is a starting idea, but not the correct pattern for this problem.

---

## Approach 2: Frequency Counting

### Main idea

Count how many times each character appears.

Then:

```text
Use all even counts.
Use count - 1 from odd counts.
If there was at least one odd count, add 1 for the middle.
```

### Step-by-step algorithm

```text
1. Create a hashmap to count characters.
2. Loop through the string and fill the hashmap.
3. Create length = 0.
4. Create has_odd = False.
5. For each character frequency:
   - If frequency is even, add all of it.
   - If frequency is odd, add frequency - 1 and set has_odd = True.
6. After the loop, if has_odd is True, add 1.
7. Return length.
```

### Pseudocode

```text
count = hashmap

for char in s:
    count[char] += 1

length = 0
has_odd = false

for frequency in count values:
    if frequency is even:
        length += frequency
    else:
        length += frequency - 1
        has_odd = true

if has_odd:
    length += 1

return length
```

### Time complexity

```text
O(n)
```

We scan the string once.

### Space complexity

```text
O(1)
```

Because the string only contains uppercase and lowercase English letters, there are at most:

```text
52
```

possible unique characters.

If the character set was unlimited, we would say:

```text
O(k)
```

where `k` is the number of unique characters.

### Why this approach works

A palindrome needs matching pairs on both sides.

Even counts can be fully used as pairs.

Odd counts can contribute their even part:

```text
val - 1
```

And one odd character can be used as the center.

### Limitations

This gives the length only, not the actual palindrome string.

But the problem only asks for the length, so this is perfect.

### Interview expectation

```text
Yes, this is interview-expected.
```

---

# 7. Optimized Approach

Your final optimized approach is:

```text
Hashmap frequency counting + odd flag
```

It is better than the brute force idea because:

```text
It does not try to generate palindromes.
It only counts characters.
It uses the mathematical property of palindromes.
```

The key rule:

```text
Pairs go on the sides.
One odd character can go in the middle.
```

So the optimized logic is:

```text
For each frequency:
    if even -> use all
    if odd -> use frequency - 1

If any odd existed:
    add 1
```

This is clean, efficient, and easy to explain.

---

# 8. Final Code

You already wrote a correct version.

A slightly cleaner standard version is:

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        length = 0
        has_odd = False

        for val in count.values():
            if val % 2 == 0:
                length += val
            else:
                length += val - 1
                has_odd = True

        if has_odd:
            length += 1

        return length
```

The only cleanup was changing:

```python
for key, val in count.items():
```

to:

```python
for val in count.values():
```

because you do not use the key.

---

# 9. Interview Script

Here is how you can explain it in an interview:

```text
First, I thought about checking whether the string itself is a palindrome, but the problem allows us to rearrange the letters, so the order does not matter.

Because of that, I only need to count how many times each character appears.

For a palindrome, characters usually need to come in pairs, because one copy goes on the left side and one copy goes on the right side.

So if a character has an even frequency, I can use all of it.

If a character has an odd frequency, I can use frequency - 1 of it, because that gives me the largest even number of that character. The leftover one could be used as the middle character.

But a palindrome can only have one middle character, so I keep a boolean flag called has_odd. If I see any odd frequency, I add one extra character at the end.

This gives the longest possible palindrome length.

The time complexity is O(n), because I scan the string once. The space complexity is O(1), because there are only uppercase and lowercase English letters.
```

---

# 10. Edge Cases and Dry Run

## Edge Case 1: Single character

```text
s = "a"
```

Counts:

```text
a: 1
```

Use:

```text
0 pairs + 1 middle = 1
```

Answer:

```text
1
```

---

## Edge Case 2: All characters unique

```text
s = "abc"
```

Counts:

```text
a: 1
b: 1
c: 1
```

Use:

```text
0 pairs
+ 1 middle
```

Answer:

```text
1
```

---

## Edge Case 3: All even counts

```text
s = "aabbcc"
```

Counts:

```text
a: 2
b: 2
c: 2
```

Use all:

```text
2 + 2 + 2 = 6
```

Answer:

```text
6
```

---

## Edge Case 4: Multiple odd counts

```text
s = "aaabb"
```

Counts:

```text
a: 3
b: 2
```

Use:

```text
a: 3 -> use 2
b: 2 -> use 2
```

Since there is an odd count, add 1 middle:

```text
2 + 2 + 1 = 5
```

Answer:

```text
5
```

Possible palindrome:

```text
"ababa"
```

---

## Dry Run

Input:

```text
s = "abccccdd"
```

Counts:

```text
a: 1
b: 1
c: 4
d: 2
```

Start:

```text
length = 0
has_odd = False
```

Process `a: 1`

```text
odd
length += 1 - 1 = 0
has_odd = True
```

Process `b: 1`

```text
odd
length += 1 - 1 = 0
has_odd = True
```

Process `c: 4`

```text
even
length += 4
length = 4
```

Process `d: 2`

```text
even
length += 2
length = 6
```

After loop:

```text
has_odd = True
```

So:

```text
length += 1
length = 7
```

Answer:

```text
7
```

---

# 11. Key Takeaways

```text
This is not a substring problem.
This is a frequency counting problem.
```

Remember the palindrome rule:

```text
Even counts can be fully used.
Odd counts can use count - 1.
Only one odd character can be used in the middle.
```

Pattern trigger:

```text
"can be built with these letters" means order does not matter.
Think hashmap / frequency counting.
```

Final complexity:

```text
Time: O(n)
Space: O(1)
```

Your final solution is correct, clean, and interview-expected.
