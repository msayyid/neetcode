# LeetCode 202 - Happy Number Notes

## 1. Problem Summary

We are given a positive integer `n`.

We repeatedly replace `n` with:

```text
sum of the squares of its digits
```

If the process eventually reaches `1`, the number is happy.

If the process enters a loop and never reaches `1`, the number is not happy.

Example:

```text
19
1² + 9² = 82

82
8² + 2² = 68

68
6² + 8² = 100

100
1² + 0² + 0² = 1
```

So `19` is happy.

Key idea:

```text
If we see the same number again before reaching 1, we are stuck in a cycle.
```

Important constraint:

```text
1 <= n <= 2^31 - 1
```

So `n` can be large, but it has only up to around 10 digits.

---

# 2. My Initial Understanding

At first, you understood that we need to repeatedly calculate the sum of squared digits.

You tried a recursive approach:

```python
new_sum = [int(x) * int(x) for x in str(num)]
num = sum(new_sum)
```

This part was correct.

You also correctly realized that for `19`:

```text
19 -> 82 -> 68 -> 100 -> 1
```

But you were confused about:

```text
How do we know when to stop if the number is not happy?
```

You first tried using an `attempt` counter, like stopping after 10 attempts.

That was a natural starting idea, but not fully correct.

---

# 3. Mistakes I Made

## Mistake 1 - Using the original `n` instead of the changing `num`

In your first recursive code, you had:

```python
new_sum = [int(x)*int(x) for x in str(n)]
```

But `n` was always the original number.

So for `n = 19`, every recursive call kept doing:

```text
1² + 9² = 82
```

That is why it felt stuck at `82`.

Correct idea:

```python
new_sum = [int(x) * int(x) for x in str(num)]
```

Because `num` changes every recursive call.

---

## Mistake 2 - Using a fixed attempt limit

You used:

```python
if attempt == 10:
    return
```

The problem is that `10` is just a guess.

Some numbers may need more steps.

Some may repeat earlier.

Instead of guessing, we should detect the real reason to stop:

```text
If a number repeats, we are in a cycle.
```

---

## Mistake 3 - Not returning the recursive result

You wrote:

```python
recur(new_sum)
```

But if using recursion, you would need:

```python
return recur(new_sum)
```

Otherwise, the `True` or `False` result from deeper recursive calls does not come back to the original function.

However, for this problem, the iterative `while` loop version is cleaner.

---

# 4. Things I Learned

## 1. Same input gives same next output

This problem is deterministic.

That means:

```text
same number -> same next number
```

Example:

```text
4 -> 16
```

Every time we see `4`, it will always go to `16`.

So if we ever see `4` again, the same path will repeat forever.

---

## 2. Repeated number means cycle

Example for `n = 2`:

```text
2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4
```

Now `4` appeared again.

So from there:

```text
4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4
```

will repeat forever.

Therefore:

```python
if n in seen:
    return False
```

means:

```text
We have already been here, so this is a loop.
```

---

## 3. Why time complexity uses `log n`

When we loop through digits:

```python
for i in str(n)
```

we are not looping `n` times.

We are looping through the number of digits.

Example:

```text
n = 9        -> 1 digit
n = 99       -> 2 digits
n = 999      -> 3 digits
n = 9999     -> 4 digits
```

Every time the number becomes about 10 times bigger, the digit count increases by only 1.

So:

```text
number of digits = O(log n)
```

More specifically:

```text
digits ≈ log10(n)
```

---

## 4. Logarithm is similar to tree levels

In a binary tree, `log n` often means:

```text
how many times we divide by 2
```

For digits, it means:

```text
how many times we divide by 10
```

Example:

```text
1000 -> 100 -> 10 -> 1
```

That is why the number of digits is logarithmic.

---

# 5. Pattern Recognition

## Main Pattern

```text
Cycle Detection
```

More specifically:

```text
Repeated state detection using a set
```

## Trigger: How do I know this pattern applies?

Look for clues like:

```text
Repeat a process
Keep transforming a value
It may loop forever
Need to know whether it reaches a target
```

This problem says:

```text
Repeat the process until the number equals 1, or it loops endlessly.
```

The phrase:

```text
loops endlessly
```

is the big clue.

That should make you think:

```text
I need cycle detection.
```

## Why this pattern applies here

Each number leads to exactly one next number.

So the process forms a chain:

```text
n -> next -> next -> next ...
```

If the chain reaches `1`, return `True`.

If the chain repeats a number, it has entered a cycle, return `False`.

## Similar problem types

This pattern appears when:

```text
A value changes repeatedly
A linked list may have a cycle
A state machine may repeat states
A sequence either reaches a target or loops forever
```

Similar DSA ideas:

```text
Linked List Cycle
Detecting repeated states in simulations
Floyd's cycle detection
Hash set cycle detection
```

---

# 6. Approaches Tried

## Approach 1 - Recursive attempt counter

### Main idea

Keep recursively calculating the sum of squared digits and stop after some number of attempts.

### Step-by-step algorithm

```text
1. Start with n.
2. If n is 1, return True.
3. Calculate the sum of squared digits.
4. Increase attempt count.
5. If attempts reach some fixed limit, stop.
6. Otherwise recurse on the new number.
```

### Pseudocode

```text
function recur(num):
    if num == 1:
        return True

    new_num = sum of squared digits of num
    attempts += 1

    if attempts == 10:
        stop

    recur(new_num)
```

### Time Complexity

Hard to properly define because the stopping point is artificial.

### Space Complexity

```text
O(k)
```

because recursive calls use stack space, where `k` is the number of calls.

### Why this approach is incomplete

The attempt limit is a guess.

It does not correctly prove whether the number is happy or not.

A number is not unhappy because it took 10 attempts.

It is unhappy because it entered a cycle.

### Interview expected?

No.

This is a useful starting approach, but not interview-expected.

---

## Approach 2 - Hash Set Cycle Detection

### Main idea

Store every number we have seen.

If we see the same number again, we are in a loop.

### Step-by-step algorithm

```text
1. Create an empty set called seen.
2. While n is not 1:
   - If n is already in seen, return False.
   - Add n to seen.
   - Replace n with the sum of the squares of its digits.
3. If the loop ends, n is 1, so return True.
```

### Pseudocode

```text
seen = empty set

while n != 1:
    if n in seen:
        return False

    add n to seen

    n = sum of squared digits of n

return True
```

### Time Complexity

One transformation scans the digits of `n`.

```text
O(log n)
```

because the number of digits is `log n`.

There are multiple transformations, but for this problem the values quickly become small.

Interview-friendly answer:

```text
Time: O(log n)
```

More precise general form:

```text
O(k * log n)
```

where `k` is the number of transformations before reaching `1` or detecting a cycle.

Because of the constraints and shrinking behavior, `k` is treated as small/bounded.

### Space Complexity

The set stores seen numbers.

General answer:

```text
O(k)
```

Interview-friendly answer for this problem:

```text
O(log n) or O(1), depending on explanation
```

Since numbers quickly shrink into a small bounded range, many people treat it as:

```text
O(1)
```

### Why this approach works

If a number repeats, the future path will also repeat.

Because:

```text
same number -> same next number
```

So a repeated number means we are stuck in a cycle and will never reach `1`.

### Limitations

Uses extra space for the `seen` set.

### Interview expected?

Yes.

This is a clean and expected solution.

---

# 7. Optimized Approach

The optimized approach is the hash set cycle detection approach.

Final idea:

```python
seen = set()

while n != 1:
    if n in seen:
        return False

    seen.add(n)

    n = sum(int(i) * int(i) for i in str(n))

return True
```

Why it is better than the attempt counter:

```text
It does not guess.
It detects the actual reason the process fails: a cycle.
```

Pattern used:

```text
Cycle detection with a set
```

Why this pattern applies:

```text
The problem says the process may loop endlessly.
If a state repeats, the same path repeats forever.
```

---

# 8. Final Code

You asked for notes, so no full final code is needed here.

But your working code is correct and interview-expected.

One small cleaner version is:

```python
n = sum(int(i) ** 2 for i in str(n))
```

Instead of:

```python
n = sum([int(i) * int(i) for i in str(n)])
```

Both are fine.

The generator version avoids creating an extra list.

---

# 9. Interview Script

Here is how you can explain it in an interview:

```text
First, I need to repeatedly replace the number with the sum of the squares of its digits.

If the number eventually becomes 1, then it is happy.

The main issue is knowing when to stop if it never reaches 1. Since the transformation is deterministic, the same number will always produce the same next number. So if I ever see the same number again, that means I am in a cycle and I will never reach 1.

To detect this, I use a set called seen. While n is not 1, I check if n is already in seen. If it is, I return false because we found a loop. Otherwise, I add n to seen and update n to the sum of the squares of its digits.

If the loop ends, that means n became 1, so I return true.

The pattern here is cycle detection using a hash set.

For time complexity, each transformation scans the digits of n, which is O(log n). The numbers quickly shrink into a small range, so this is usually treated as O(log n) overall for this problem. The space complexity is O(k) for the seen set, or practically O(1) because the cycle range is bounded.
```

---

# 10. Edge Cases and Dry Run

## Edge Case 1 - `n = 1`

```text
n is already 1
return True
```

Your loop handles this because:

```python
while n != 1:
```

will not run.

---

## Edge Case 2 - Number enters a cycle

Example:

```text
n = 2
```

Dry run:

```text
seen = {}

n = 2
2 not in seen
seen = {2}
next = 4

n = 4
4 not in seen
seen = {2, 4}
next = 16

n = 16
16 not in seen
seen = {2, 4, 16}
next = 37

...

eventually:

n = 4
4 is already in seen
return False
```

---

## Edge Case 3 - Number becomes 1

Example:

```text
n = 19
```

Dry run:

```text
seen = {}

n = 19
seen = {19}
next = 82

n = 82
seen = {19, 82}
next = 68

n = 68
seen = {19, 82, 68}
next = 100

n = 100
seen = {19, 82, 68, 100}
next = 1

n = 1
stop loop
return True
```

---

# 11. Key Takeaways

Remember these:

```text
1. Do not use a random attempt limit.
2. If a number repeats, we are in a cycle.
3. Same number always gives the same next number.
4. Use a set to remember numbers already seen.
5. The pattern is cycle detection.
6. Looping through digits costs O(log n), not O(n).
7. Your final solution is interview-expected.
```

Most important sentence:

```text
If I see the same number again before reaching 1, the process will repeat forever, so the number is not happy.
```
