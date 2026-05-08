# 205. Isomorphic Strings - Revision Notes

## 1. Problem Summary

We are given two strings `s` and `t`.

We need to check if every character in `s` can be replaced with a character in `t` while keeping the same order.

Important rules:

* One character in `s` must always map to the same character in `t`.
* Two different characters in `s` cannot map to the same character in `t`.
* A character can map to itself.
* `s` and `t` have the same length.
* Strings contain valid ASCII characters.

Example:

```text
s = "egg"
t = "add"
```

Mapping:

```text
e -> a
g -> d
```

This is valid, so return `True`.

---

## 2. My Initial Understanding

You first thought:

* `s` and `t` should have a similar number of unique characters.
* You tried counting the characters in both strings.
* You checked whether the number of unique characters was the same.

That idea was partly correct because isomorphic strings usually need the same number of unique mapped characters.

But the missing part was:

```text
The order and consistency of the mappings matter.
```

For example, just comparing unique character counts does not fully prove the strings are isomorphic.

---

## 3. Mistakes I Made

### Mistake 1: Counting frequencies instead of checking mappings

You wrote dictionaries like:

```text
s character -> frequency
t character -> frequency
```

But this problem is not mainly about how many times each character appears.

It is about whether each character has a consistent mapping.

For example:

```text
s = "foo"
t = "bar"
```

`o` appears twice in `s`, but it would need to map to both `a` and `r`, which is invalid.

---

### Mistake 2: Thinking unique count is enough

You checked:

```text
if len(map1) != len(map2):
    return False
```

This can catch some invalid cases, but not all.

The real check is:

```text
Does every character always map to the same corresponding character?
```

---

### Mistake 3: Not knowing how to check order

You were stuck on checking the actual order of characters.

The key realization was:

```text
Compare characters at the same index.
```

So for each index `i`:

```text
s[i] should map to t[i]
```

Example:

```text
s = "egg"
t = "add"
```

At each index:

```text
e -> a
g -> d
g -> d
```

This is valid.

---

## 4. Things I Learned

### Main idea

Use two dictionaries:

```text
s_to_t
t_to_s
```

Why two?

* `s_to_t` checks that one character in `s` always maps to the same character in `t`.
* `t_to_s` checks that two different characters in `s` do not map to the same character in `t`.

---

### Important example

```text
s = "ab"
t = "aa"
```

Forward mapping only:

```text
a -> a
b -> a
```

This looks okay if we only check `s_to_t`, but it is not allowed.

Why?

```text
Two different characters from s cannot map to the same character in t.
```

Reverse mapping catches this:

```text
a -> a
a -> b
```

Conflict, so return `False`.

---

### Key phrase to remember

```text
Each character must have a one-to-one mapping.
```

Meaning:

```text
One s character maps to one t character,
and one t character maps back to one s character.
```

---

## 5. Pattern Recognition

### Main Pattern

```text
Two-way Hash Map / Bijective Mapping
```

This is the same pattern as the Word Pattern problem.

---

### Trigger: When should I think of this pattern?

Think of two hash maps when the problem says something like:

```text
One thing must consistently correspond to another thing.
```

Common clues:

* "map"
* "pattern"
* "replace"
* "same structure"
* "no two items may map to the same item"
* "one-to-one relationship"

---

### Why this pattern applies here

The problem says:

```text
All occurrences of a character must be replaced with another character.
No two characters may map to the same character.
```

That directly means:

```text
s char -> t char
t char -> s char
```

So we need two-way mapping.

---

### Similar problems

This pattern appears in:

```text
Word Pattern
Isomorphic Strings
Pattern matching problems
Encoding/decoding consistency problems
One-to-one relationship problems
```

---

## 6. Approaches Tried

## Approach 1: Frequency Counting

### Main idea

Count how many times each character appears in `s` and `t`, then compare the number of unique characters.

---

### Algorithm

1. Create a dictionary for characters in `s`.
2. Count frequencies of characters in `s`.
3. Create a dictionary for characters in `t`.
4. Count frequencies of characters in `t`.
5. If the number of unique characters is different, return `False`.
6. Otherwise, return `True`.

---

### Pseudocode

```text
create map1
create map2

for each char in s:
    count char in map1

for each char in t:
    count char in map2

if number of keys in map1 != number of keys in map2:
    return False

return True
```

---

### Time Complexity

```text
O(n)
```

You loop through both strings.

---

### Space Complexity

```text
O(k)
```

Where `k` is the number of unique characters.

Since the problem uses ASCII characters, this can also be seen as:

```text
O(1)
```

because the number of possible characters is limited.

---

### Why this approach is incomplete

It does not check whether characters map consistently by position.

Example:

```text
s = "foo"
t = "bar"
```

The character `o` would need to map to both `a` and `r`.

That is invalid, but frequency/unique count alone is not the correct way to check this.

---

### Interview expectation

This is not interview-expected as the final solution.

It is a good starting idea, but incomplete.

---

## Approach 2: Two Hash Maps

### Main idea

Loop through both strings by index.

For every position `i`:

```text
s[i] must always map to t[i]
t[i] must always map back to s[i]
```

---

### Algorithm

1. Create `s_to_t` dictionary.
2. Create `t_to_s` dictionary.
3. Loop from `0` to `len(s) - 1`.
4. Let `c1 = s[i]` and `c2 = t[i]`.
5. Check if `c1` already exists in `s_to_t`.

   * If yes, its value must be `c2`.
   * If not, store `c1 -> c2`.
6. Check if `c2` already exists in `t_to_s`.

   * If yes, its value must be `c1`.
   * If not, store `c2 -> c1`.
7. If no conflicts happen, return `True`.

---

### Pseudocode

```text
s_to_t = empty map
t_to_s = empty map

for i from 0 to length of s - 1:
    c1 = s[i]
    c2 = t[i]

    if c1 exists in s_to_t:
        if s_to_t[c1] != c2:
            return False
    else:
        s_to_t[c1] = c2

    if c2 exists in t_to_s:
        if t_to_s[c2] != c1:
            return False
    else:
        t_to_s[c2] = c1

return True
```

---

### Time Complexity

```text
O(n)
```

We scan the strings once.

---

### Space Complexity

```text
O(k)
```

Where `k` is the number of unique characters.

Since the input is ASCII, we can also say:

```text
O(1)
```

because ASCII character count is limited.

---

### Why this approach works

The first map makes sure:

```text
One character from s always maps to the same character in t.
```

The second map makes sure:

```text
Two different characters from s do not map to the same character in t.
```

Together, they guarantee a valid one-to-one mapping.

---

### Limitations

No major limitation for this problem.

This is the standard and expected solution.

---

### Interview expectation

Yes, this is interview-expected.

It is clean, efficient, and easy to explain.

---

## 7. Optimized Approach

The optimized approach is the two-hash-map solution.

It is better than counting because it checks the actual structure of the strings.

For example:

```text
s = "egg"
t = "add"
```

Mappings:

```text
e -> a
g -> d
```

When we see `g` again, we check:

```text
Previously g mapped to d.
Current character in t is d.
So it is valid.
```

But for:

```text
s = "egg"
t = "adt"
```

Mappings start as:

```text
e -> a
g -> d
```

Then later:

```text
g -> t
```

Conflict, because `g` was already mapped to `d`.

So return `False`.

---

## 8. Final Code

You asked not to dump full solutions unless needed, so no full code here.

Your code is already correct and interview-expected.

Cleaner wording for what your code does:

```text
For each index, check whether the current character pair breaks any previous mapping.
If it does, return False.
Otherwise, store/update the mapping.
```

---

## 9. Interview Script

You can say:

```text
I need to check whether the two strings have the same character pattern.

I use two hash maps. The first map stores the mapping from characters in s to characters in t. This makes sure that if a character in s appears again, it must map to the same character in t as before.

But that alone is not enough, because two different characters in s could map to the same character in t. So I also use a reverse map from t to s.

Then I loop through both strings by index. For each pair s[i] and t[i], I check whether there is already a mapping. If there is and it conflicts with the current character, I return false. Otherwise, I store the mapping.

If I finish the loop without conflicts, the strings are isomorphic.

The time complexity is O(n), because I scan the strings once. The space complexity is O(1) for ASCII characters, or O(k) if we describe it based on unique characters.
```

---

## 10. Edge Cases and Dry Run

### Edge Case 1: Same character maps to itself

```text
s = "abc"
t = "abc"
```

Valid:

```text
a -> a
b -> b
c -> c
```

Return `True`.

---

### Edge Case 2: One character maps to two different characters

```text
s = "egg"
t = "adt"
```

Dry run:

```text
e -> a
g -> d
g -> t
```

`g` cannot map to both `d` and `t`.

Return `False`.

---

### Edge Case 3: Two characters map to the same character

```text
s = "ab"
t = "aa"
```

Forward mapping:

```text
a -> a
b -> a
```

Invalid because two different characters map to the same character.

Reverse map catches this.

Return `False`.

---

### Edge Case 4: Repeated pattern

```text
s = "paper"
t = "title"
```

Mapping:

```text
p -> t
a -> i
p -> t
e -> l
r -> e
```

Everything is consistent.

Return `True`.

---

## 11. Key Takeaways

Remember:

```text
This is not a counting problem.
It is a mapping consistency problem.
```

The main pattern is:

```text
Two-way hash map / one-to-one mapping
```

The trigger is:

```text
If one thing must consistently match another thing,
and duplicates cannot share the same mapping,
use two dictionaries.
```

For this problem:

```text
s_to_t checks consistency.
t_to_s prevents duplicate target mappings.
```