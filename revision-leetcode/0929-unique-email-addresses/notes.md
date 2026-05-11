# 929. Unique Email Addresses - Revision Notes

## 1. Problem Summary

We are given a list of email addresses.

Each email has two parts:

```text
local@domain
```

Example:

```text
test.email+alex@leetcode.com
```

Here:

```text
local = test.email+alex
domain = leetcode.com
```

The rules only apply to the local part:

1. Dots `.` are ignored in the local name.

   ```text
   test.email -> testemail
   ```

2. If there is a `+`, everything after the first `+` is ignored.

   ```text
   test.email+alex -> test.email
   ```

3. The domain part stays exactly the same.

   ```text
   leet.code.com does not become leetcodecom
   ```

The goal is to count how many unique real receiving addresses exist after applying these rules.

## 2. My Initial Understanding

You understood the main idea correctly:

* Loop through every email.
* Build a cleaned version of the email.
* Ignore dots in the local part.
* Stop reading the local part when `+` appears.
* Keep the domain unchanged.
* Store cleaned emails in a set.
* Return the length of the set.

Your first solution manually scanned each character using an index `i`.

That worked because you simulated the rules exactly.

## 3. Mistakes I Made

### Mistake 1: Thinking the first solution was just “brute force”

Your first solution was not a bad brute force. It was a direct simulation.

It was just more manual and verbose.

Better wording:

> I normalized each email according to the rules and stored the result in a set.

### Mistake 2: Space complexity as only `O(n)`

You first thought the set space might be `O(n)`.

But each item in the set is a string, and each string can be length `m`.

So the total set space is:

```text
O(n * m)
```

Where:

* `n` = number of emails
* `m` = average email length

### Mistake 3: Being unsure about `split("+")[0]`

You were unsure what happens if `+` does not exist.

Example:

```python
"testemail".split("+")
```

returns:

```python
["testemail"]
```

So `[0]` safely returns the full string.

### Mistake 4: Being unsure about `replace(".", "")`

You were unsure what happens if there are no dots.

Example:

```python
"testemail".replace(".", "")
```

returns:

```python
"testemail"
```

So nothing breaks.

## 4. Things I Learned

### `split("@")`

Since the problem guarantees exactly one `@`, we can safely do:

```python
local, domain = email.split("@")
```

Example:

```python
"test.email+alex@leetcode.com".split("@")
```

Result:

```python
["test.email+alex", "leetcode.com"]
```

### `split("+")[0]`

This keeps only the part before the first `+`.

Example:

```python
"test.email+alex".split("+")[0]
```

Result:

```python
"test.email"
```

If there is no `+`, it returns the whole local name.

### `replace(".", "")`

This removes all dots from the local name.

Example:

```python
"test.email".replace(".", "")
```

Result:

```python
"testemail"
```

### Sets remove duplicates

After normalizing the emails, we store them in a set.

Example:

```python
{"testemail@leetcode.com", "testemail@leetcode.com"}
```

Only one copy is kept.

So the answer is:

```python
len(my_set)
```

## 5. Pattern Recognition

### Main Pattern: String Normalization + Hash Set

This problem is not really a complex algorithm problem.

The key pattern is:

```text
Normalize input -> store normalized form in a set -> count unique values
```

### Trigger: How to recognize this pattern

Think of this pattern when the problem says:

* Different inputs may represent the same thing.
* Apply rules to transform values into a standard form.
* Count unique results.
* Return how many distinct items remain after processing.

Here, different emails can point to the same real address.

Example:

```text
test.email+alex@leetcode.com
test.e.mail+bob@leetcode.com
```

Both normalize to:

```text
testemail@leetcode.com
```

So we use a set to avoid duplicates.

### Similar problem types

This pattern appears in problems like:

* Unique Morse Code Words
* Group Anagrams
* Normalize file paths
* Compare transformed strings
* Count unique usernames after cleaning rules
* Deduplicate data after formatting

## 6. Approaches Tried

## Approach 1: Manual Character Scanning

### Main idea

Manually loop through each character of the email and build the normalized address.

### Step-by-step algorithm

1. Create an empty set.
2. For each email:

   * Create an empty string `e_address`.
   * Scan the local part until `@`.
   * Ignore dots.
   * Stop local processing if `+` is found.
   * Skip the rest of the local part until `@`.
   * Append the domain exactly as it is.
   * Add the normalized email to the set.
3. Return the size of the set.

### Pseudocode

```text
create empty set

for each email:
    create empty normalized string
    i = 0

    while email[i] is not "@":
        if email[i] is "+":
            break
        if email[i] is ".":
            move i forward
            continue
        add email[i] to normalized
        move i forward

    move i forward until "@"

    while i is inside email:
        add email[i] to normalized
        move i forward

    add normalized to set

return size of set
```

### Time Complexity

```text
O(n * m)
```

Each email is scanned character by character.

### Space Complexity

```text
O(n * m)
```

The set can store up to `n` unique emails, each of length up to `m`.

Temporary string:

```text
O(m)
```

### Why this approach works

It follows the email rules exactly:

* Ignore dots before `@`.
* Ignore everything after `+` before `@`.
* Keep the domain unchanged.
* Use a set to remove duplicates.

### Limitations

The logic is correct, but the code is longer and easier to mess up because it uses manual indexes.

Possible mistakes:

* Forgetting to move `i`
* Accidentally skipping `@`
* Applying dot rule to the domain
* Infinite loop if index update is missed

### Interview verdict

Correct, but not the cleanest.

It shows understanding, but the `split + replace` version is more standard.

## Approach 2: `split` + `replace`

### Main idea

Use Python string methods to directly apply the rules.

### Step-by-step algorithm

1. Create an empty set.
2. For each email:

   * Split it into `local` and `domain` using `@`.
   * Split `local` by `+` and keep the first part.
   * Remove all dots from `local`.
   * Rebuild the normalized email.
   * Add it to the set.
3. Return the size of the set.

### Pseudocode

```text
create empty set

for each email:
    local, domain = split email by "@"
    local = part before "+"
    local = local with all dots removed
    normalized = local + "@" + domain
    add normalized to set

return size of set
```

### Time Complexity

```text
O(n * m)
```

For each email:

* `split("@")` scans the email.
* `split("+")` scans the local part.
* `replace(".", "")` scans the local part.
* Building the final string also takes time.

Each operation is linear, so overall per email is still:

```text
O(m)
```

For all emails:

```text
O(n * m)
```

### Space Complexity

```text
O(n * m)
```

The set stores normalized emails.

Temporary strings/lists for one email take:

```text
O(m)
```

But the dominant space is the set:

```text
O(n * m)
```

### Why this approach works

It maps directly to the problem rules:

```python
local, domain = email.split("@")
```

Separates the email into local and domain.

```python
local = local.split("+")[0]
```

Keeps only the part before `+`.

```python
local = local.replace(".", "")
```

Removes dots from the local part.

```python
normalized = local + "@" + domain
```

Rebuilds the real receiving address.

### Limitations

It creates some temporary strings and lists, but this does not change Big-O complexity.

### Interview verdict

This is the expected and cleaner solution.

Use this version in interviews.

## 7. Optimized Approach

The optimized approach is the `split + replace + set` solution.

It is better than the manual pointer solution because:

* It is shorter.
* It is easier to read.
* It directly matches the problem statement.
* It avoids index bugs.
* It has the same time and space complexity.

Final idea:

```text
Normalize every email, store it in a set, return set size.
```

The important pattern is:

```text
String normalization + hash set
```

## 8. Final Code

You already wrote the clean final version:

```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        my_set = set()

        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            normalized = local + "@" + domain
            my_set.add(normalized)

        return len(my_set)
```

This is interview-expected.

## 9. Interview Script

You can explain it like this:

> First, I need to normalize every email address because different written emails can point to the same real receiving address.
>
> Each email has a local part and a domain part separated by `@`. The special rules only apply to the local part, not the domain.
>
> For each email, I split it into `local` and `domain`. Then, in the local part, I ignore everything after the first `+`, because that part does not affect the receiving address. After that, I remove all dots from the local part. Then I combine the cleaned local part with the original domain.
>
> I store each normalized email in a set because a set automatically removes duplicates.
>
> Finally, I return the size of the set, which gives the number of unique addresses that actually receive emails.
>
> The time complexity is `O(n * m)`, where `n` is the number of emails and `m` is the average email length. The space complexity is `O(n * m)` because in the worst case, all normalized emails are unique and stored in the set.

## 10. Edge Cases and Dry Run

### Edge Case 1: No `+`

```text
a.b@leetcode.com
```

Local:

```text
a.b
```

After removing dots:

```text
ab
```

Normalized:

```text
ab@leetcode.com
```

### Edge Case 2: No dots

```text
abc+test@leetcode.com
```

Before `+`:

```text
abc
```

Normalized:

```text
abc@leetcode.com
```

### Edge Case 3: Same local, different domain

```text
test.email+alex@leetcode.com
test.email+alex@lee.tcode.com
```

Normalize to:

```text
testemail@leetcode.com
testemail@lee.tcode.com
```

These are different because the domains are different.

### Edge Case 4: Dot in domain

```text
test.email@lee.tcode.com
```

The domain stays unchanged:

```text
testemail@lee.tcode.com
```

We do not remove dots from the domain.

## Dry Run

Input:

```python
emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com"
]
```

### Email 1

```text
test.email+alex@leetcode.com
```

Split:

```text
local = test.email+alex
domain = leetcode.com
```

Before `+`:

```text
test.email
```

Remove dots:

```text
testemail
```

Normalized:

```text
testemail@leetcode.com
```

Set:

```text
{"testemail@leetcode.com"}
```

### Email 2

```text
test.e.mail+bob.cathy@leetcode.com
```

Split:

```text
local = test.e.mail+bob.cathy
domain = leetcode.com
```

Before `+`:

```text
test.e.mail
```

Remove dots:

```text
testemail
```

Normalized:

```text
testemail@leetcode.com
```

Set stays:

```text
{"testemail@leetcode.com"}
```

Because it is a duplicate.

### Email 3

```text
testemail+david@lee.tcode.com
```

Split:

```text
local = testemail+david
domain = lee.tcode.com
```

Before `+`:

```text
testemail
```

Remove dots:

```text
testemail
```

Normalized:

```text
testemail@lee.tcode.com
```

Set:

```text
{
  "testemail@leetcode.com",
  "testemail@lee.tcode.com"
}
```

Answer:

```text
2
```

## 11. Key Takeaways

* This problem is about normalization.
* Normalize each email into its real receiving form.
* Rules only apply to the local part.
* Dots are ignored only before `@`.
* Everything after `+` is ignored only before `@`.
* The domain stays unchanged.
* Use a set to count unique normalized emails.
* Expected interview solution: `split + replace + set`.
* Time complexity: `O(n * m)`.
* Space complexity: `O(n * m)`.
