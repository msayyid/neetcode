# LeetCode 290 - Word Pattern Notes

## 1. Problem Summary

We are given:

```python
pattern = "abba"
s = "dog cat cat dog"
```

We need to check whether the words in `s` follow the same pattern as the characters in `pattern`.

The important rule is that there must be a bijection.

That means:

```text
Each pattern character maps to exactly one word.
Each word maps back to exactly one pattern character.
```

Example:

```text
pattern = "abba"
s = "dog cat cat dog"

a -> dog
b -> cat
```

This is valid, so return `True`.

But:

```text
pattern = "abba"
s = "dog dog dog dog"
```

This is invalid because:

```text
a -> dog
b -> dog
```

Two different pattern letters map to the same word.

## 2. My Initial Understanding

Your first idea was to use one dictionary:

```python
my_map = {}
```

You mapped each pattern character to a word.

Example:

```text
a -> dog
b -> cat
```

This part was correct because you understood that each pattern character should always match the same word.

You also manually parsed the string word by word using a pointer. That showed good understanding of how `split()` works internally.

Where you were confused:

You only checked one direction:

```text
pattern -> word
```

But the problem also needs the reverse direction:

```text
word -> pattern
```

Without the reverse check, your solution allowed invalid cases where different pattern characters mapped to the same word.

## 3. Mistakes I Made

### Mistake 1 - Only using one dictionary

Your first solution only checked:

```text
Does this pattern character always map to the same word?
```

That catches this case:

```text
pattern = "abba"
s = "dog cat cat fish"
```

Because:

```text
a -> dog at first
a -> fish later
```

So it correctly returns `False`.

But it does not catch:

```text
pattern = "abba"
s = "dog dog dog dog"
```

Because:

```text
a -> dog
b -> dog
```

Each letter is consistent by itself, but two letters share the same word.

Why this is wrong:

The problem requires a one-to-one mapping, not just a one-direction mapping.

### Mistake 2 - Not checking word uniqueness

The problem says:

```text
No two letters map to the same word.
```

So we must also check whether a word has already been used by another pattern character.

That is why we need:

```python
word_to_pattern = {}
```

### Mistake 3 - Manual parsing made the problem more complex

Your manual word extraction worked as practice, but for interviews, it is usually better to use:

```python
s.split()
```

Because the problem already gives a clean string:

```text
No leading/trailing spaces
Words separated by one space
```

So using `split()` is normal and expected.

## 4. Things I Learned

### Bijection means two-way mapping

A bijection means both sides must be unique.

For this problem:

```text
pattern character -> word
word -> pattern character
```

Both directions must be valid.

### One dictionary is not always enough

One dictionary only checks one direction.

For example:

```python
pattern_to_word = {
    "a": "dog",
    "b": "dog"
}
```

This dictionary looks valid if you only check each key. But it violates the rule because `"dog"` is reused.

### `split()` complexity

This line:

```python
s = s.split()
```

takes:

```text
Time: O(n)
Space: O(n)
```

where `n` is the length of the string `s`.

Why?

Python scans through the string and creates a list of words.

Example:

```python
"dog cat cat dog".split()
```

becomes:

```python
["dog", "cat", "cat", "dog"]
```

### Updating the dictionary after checking is clean

Your final cleaned version does this:

```python
if pattern[i] in pattern_to_word and pattern_to_word[pattern[i]] != s[i]:
    return False

pattern_to_word[pattern[i]] = s[i]
```

This is cleaner because:

* If the mapping already exists and is wrong, return `False`.
* Otherwise, safely assign/update it.

Same for the reverse map.

## 5. Pattern Recognition

## Main pattern: HashMap / Bijection Pattern

This is a HashMap problem because we need to remember relationships between values.

The trigger word is:

```text
bijection
```

Other clues:

```text
same pattern
one-to-one mapping
each X maps to exactly one Y
each Y maps to exactly one X
no two keys map to the same value
```

When you see these clues, think:

```text
Use two hash maps.
One map for X -> Y.
One map for Y -> X.
```

In this problem:

```python
pattern_to_word = {}
word_to_pattern = {}
```

Why this pattern applies:

We are not just checking if characters and words are equal. We are checking whether their relationship stays consistent across the whole input.

Similar problem types:

```text
Isomorphic Strings
Word Pattern
Matching usernames to IDs
Checking one-to-one encoding/decoding
Pattern matching with symbols
```

## 6. Approaches Tried

# Approach 1 - One HashMap

## Main idea

Use one dictionary to map each pattern character to its word.

Example:

```text
a -> dog
b -> cat
```

## Step-by-step algorithm

1. Create a dictionary.
2. Read each pattern character and corresponding word.
3. If the character is not in the dictionary, add the mapping.
4. If the character is already in the dictionary, check whether it maps to the same word.
5. If not, return `False`.
6. Return `True` at the end.

## Pseudocode

```text
map = {}

for each pattern character and word:
    if character not in map:
        map[character] = word
    else:
        if map[character] != word:
            return False

return True
```

## Time complexity

```text
O(n)
```

## Space complexity

```text
O(n)
```

## Why this approach works partially

It correctly checks whether one pattern character always maps to the same word.

Example it catches:

```text
pattern = "abba"
s = "dog cat cat fish"
```

Because `a` maps to both `"dog"` and `"fish"`.

## Limitation

It does not check whether two different pattern characters map to the same word.

Example it fails:

```text
pattern = "abba"
s = "dog dog dog dog"
```

It allows:

```text
a -> dog
b -> dog
```

But this is invalid.

## Interview expected?

This is a good starting idea, but it is not complete and not interview-expected as the final answer.

# Approach 2 - Manual parsing without `split()`

## Main idea

Instead of using `s.split()`, manually build each word character by character.

## Step-by-step algorithm

1. Use one pointer for the pattern.
2. Use another pointer for the string.
3. Build a word until a space is found.
4. Check the pattern-to-word mapping.
5. Check the word-to-pattern mapping.
6. Continue until the pattern is finished.
7. Make sure there are no extra words left.

## Pseudocode

```text
pattern_to_word = {}
word_to_pattern = {}

i = 0
j = 0

while i < length(pattern):
    if j reached end of s:
        return False

    word = ""

    while j < length(s) and s[j] is not space:
        word += s[j]
        j += 1

    skip the space

    p = pattern[i]

    check p -> word
    check word -> p

    i += 1

if there are still words left:
    return False

return True
```

## Time complexity

```text
O(n)
```

where `n` is the length of `s`.

## Space complexity

```text
O(n)
```

because we still store mappings in dictionaries.

## Why this approach works

It works because it checks both directions:

```text
pattern -> word
word -> pattern
```

## Limitations

It is more code and easier to make mistakes with pointers.

For example, you must be careful with:

```text
moving past spaces
checking extra words
checking pattern ending early
```

## Interview expected?

Usually no, unless the interviewer says:

```text
Do not use split()
```

It is good practice, but not the cleanest interview solution.

# Approach 3 - Two HashMaps with `split()`

## Main idea

Use `split()` to get words, then use two dictionaries:

```python
pattern_to_word = {}
word_to_pattern = {}
```

One checks:

```text
pattern character -> word
```

The other checks:

```text
word -> pattern character
```

## Step-by-step algorithm

1. Convert `s` into a list of words.
2. If the number of words is not equal to the length of `pattern`, return `False`.
3. Create two dictionaries.
4. Loop through every index.
5. Get the current pattern character and current word.
6. Check if the pattern character already maps to a different word.
7. Check if the word already maps to a different pattern character.
8. If either check fails, return `False`.
9. Otherwise, update both dictionaries.
10. Return `True`.

## Pseudocode

```text
words = split s into words

if length(words) != length(pattern):
    return False

pattern_to_word = {}
word_to_pattern = {}

for i from 0 to length(words) - 1:
    p = pattern[i]
    word = words[i]

    if p exists in pattern_to_word and pattern_to_word[p] != word:
        return False

    pattern_to_word[p] = word

    if word exists in word_to_pattern and word_to_pattern[word] != p:
        return False

    word_to_pattern[word] = p

return True
```

## Time complexity

```text
O(n)
```

where `n` is the length of the string `s`.

## Space complexity

```text
O(n)
```

because:

* `split()` stores the words
* dictionaries store mappings

## Why this approach works

It enforces both rules:

```text
Each pattern character has one word.
Each word has one pattern character.
```

So it prevents both kinds of invalid cases.

## Limitations

It uses extra space for `s.split()`, but this is completely fine for the given constraints.

## Interview expected?

Yes. This is the clean interview-expected solution.

## 7. Optimized Approach

Your final optimized approach is:

```text
Two HashMaps + split()
```

The final logic is clean:

```python
if pattern[i] in pattern_to_word and pattern_to_word[pattern[i]] != s[i]:
    return False

pattern_to_word[pattern[i]] = s[i]

if s[i] in word_to_pattern and word_to_pattern[s[i]] != pattern[i]:
    return False

word_to_pattern[s[i]] = pattern[i]
```

Why it is better than your first approach:

Your first approach checked only:

```text
pattern -> word
```

Your final approach checks:

```text
pattern -> word
word -> pattern
```

So it fully satisfies the bijection requirement.

Pattern used:

```text
HashMap / Bijection Pattern
```

Why this pattern applies:

The problem asks us to check a relationship between two sets of values:

```text
pattern letters
words
```

Because the relationship must be one-to-one, we use two dictionaries.

## 8. Final Code

You already wrote the clean final code:

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word = dict()
        word_to_pattern = dict()

        s = s.split()

        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            if pattern[i] in pattern_to_word and pattern_to_word[pattern[i]] != s[i]:
                return False
            pattern_to_word[pattern[i]] = s[i]

            if s[i] in word_to_pattern and word_to_pattern[s[i]] != pattern[i]:
                return False
            word_to_pattern[s[i]] = pattern[i]

        return True
```

This is interview-expected.

A small naming improvement would be to avoid reusing `s` as a list:

```python
words = s.split()
```

That is slightly clearer.

## 9. Interview Script

“I need to check whether the string follows the given pattern. The key point is that the mapping must be one-to-one. So each pattern character must always map to the same word, and each word must always map back to the same pattern character.

First, I split the string into words. If the number of words is different from the length of the pattern, then it cannot be a full match, so I return false.

Then I use two hash maps. One stores pattern character to word, and the other stores word to pattern character.

As I loop through the pattern and words together by index, I check whether the current pattern character was already mapped to a different word. If yes, I return false. Then I check the reverse: if the current word was already mapped to a different pattern character, I also return false.

If both checks pass, I store/update both mappings. If I finish the loop without conflicts, then the string follows the pattern, so I return true.

The brute force or incomplete version would be to only use one dictionary from pattern to word. But that fails when two different pattern characters map to the same word, such as `a -> dog` and `b -> dog`.

The optimized and interview-expected version uses two hash maps to enforce the bijection.

Time complexity is O(n), because we scan the words once and splitting the string is also linear. Space complexity is O(n), because we store the list of words and the hash maps.”

## 10. Edge Cases and Dry Run

### Edge Case 1 - Valid pattern

```python
pattern = "abba"
s = "dog cat cat dog"
```

Mappings:

```text
a -> dog
b -> cat
cat -> b
dog -> a
```

Return:

```text
True
```

### Edge Case 2 - Same pattern letter maps to different words

```python
pattern = "abba"
s = "dog cat cat fish"
```

At the end:

```text
a was dog before
a is now fish
```

Return:

```text
False
```

### Edge Case 3 - Two pattern letters map to same word

```python
pattern = "abba"
s = "dog dog dog dog"
```

Mappings start:

```text
a -> dog
dog -> a
```

Then:

```text
b -> dog
```

But `"dog"` already maps to `a`, not `b`.

Return:

```text
False
```

### Edge Case 4 - Different lengths

```python
pattern = "abba"
s = "dog cat cat"
```

Pattern length:

```text
4
```

Number of words:

```text
3
```

Return:

```text
False
```

## Dry Run

Input:

```python
pattern = "abba"
s = "dog cat cat dog"
```

After split:

```python
s = ["dog", "cat", "cat", "dog"]
```

Start:

```python
pattern_to_word = {}
word_to_pattern = {}
```

### i = 0

```text
pattern[0] = a
s[0] = dog
```

Add:

```text
a -> dog
dog -> a
```

### i = 1

```text
pattern[1] = b
s[1] = cat
```

Add:

```text
b -> cat
cat -> b
```

### i = 2

```text
pattern[2] = b
s[2] = cat
```

Check:

```text
b already maps to cat
cat already maps to b
```

Valid.

### i = 3

```text
pattern[3] = a
s[3] = dog
```

Check:

```text
a already maps to dog
dog already maps to a
```

Valid.

Return:

```text
True
```

## 11. Key Takeaways

```text
When the problem says bijection, think two hash maps.
```

Remember:

```text
pattern -> word is not enough.
word -> pattern is also needed.
```

The common failing case is:

```python
pattern = "abba"
s = "dog dog dog dog"
```

This is why the second dictionary matters.

Best interview version:

```text
Use split()
Check lengths
Use two hash maps
Return false on conflict
Return true if no conflicts
```

Complexities:

```text
Time: O(n)
Space: O(n)
```

Your final solution is clean, correct, and interview-expected.
