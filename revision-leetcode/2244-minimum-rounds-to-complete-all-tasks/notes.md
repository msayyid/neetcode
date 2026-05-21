## 1. Problem Summary

LeetCode 2244 - Minimum Rounds to Complete All Tasks.

You are given a list of task difficulties. In one round, you can complete either:

```text
2 tasks of the same difficulty
or
3 tasks of the same difficulty
```

Return the minimum number of rounds needed to complete all tasks.

If any difficulty appears only once, return `-1`, because you cannot make a group of 2 or 3 from one task.

Key idea:

```text
For each difficulty, count how many times it appears.
Then split that frequency into groups of 2 and 3 using the minimum number of groups.
```

---

## 2. My Initial Understanding

You correctly understood that:

* Tasks must be grouped by difficulty.
* Frequencies matter, not the original order of `tasks`.
* Any frequency `1` makes the answer impossible.
* You should try to use groups of `3` because they cover more tasks per round.

Your first solution manually reduced each frequency by `3` and then by `2`.

That was a good starting approach because it showed the real logic behind the problem.

---

## 3. Mistakes I Made

### Mistake 1: Overcomplicating the grouping logic

Your first solution:

```python
while val > 2 and val != 4:
    val -= 3
    count += 1

while val > 0 and val % 2 == 0:
    val -= 2
    count += 1
```

This works for many cases, but it is more complicated than needed.

The special case `val != 4` exists because:

```text
4 should be split as 2 + 2
not 3 + 1
```

So you were correctly avoiding leaving `1`, but the logic becomes harder to trust and explain in an interview.

---

### Mistake 2: Not immediately seeing why `ceil(val / 3)` works

You had trouble understanding this part:

```python
count += ceil(val / 3)
```

That is completely normal. The formula feels a bit magical at first.

The reason it works is:

```text
We want the fewest rounds.
A round can take at most 3 tasks.
So the minimum possible number of rounds is roughly val / 3, rounded up.
```

For example:

```text
val = 6 -> 3 + 3 -> 2 rounds -> ceil(6 / 3) = 2
val = 7 -> 3 + 2 + 2 -> 3 rounds -> ceil(7 / 3) = 3
val = 8 -> 3 + 3 + 2 -> 3 rounds -> ceil(8 / 3) = 3
```

The only impossible case is:

```text
val = 1
```

For every `val >= 2`, we can always make valid groups of `2` and `3`.

---

## 4. Things I Learned

### Important observation

For every frequency:

```text
1 -> impossible
2 -> 1 round: 2
3 -> 1 round: 3
4 -> 2 rounds: 2 + 2
5 -> 2 rounds: 3 + 2
6 -> 2 rounds: 3 + 3
7 -> 3 rounds: 3 + 2 + 2
8 -> 3 rounds: 3 + 3 + 2
9 -> 3 rounds: 3 + 3 + 3
```

So from `2` onward, the answer is always:

```python
ceil(freq / 3)
```

Why?

Because using as many `3`s as possible gives the fewest rounds, but if using a `3` leaves a remainder of `1`, we adjust by replacing one `3 + 1` with `2 + 2`.

Example:

```text
10
Naive: 3 + 3 + 3 + 1  invalid
Better: 3 + 3 + 2 + 2  valid

Rounds = 4
ceil(10 / 3) = 4
```

---

## 5. Pattern Recognition

### Main pattern

```text
Hash Map + Greedy Counting
```

### Trigger: how to recognize this pattern

The problem says:

```text
tasks with the same difficulty
```

That is the clue that order does not matter. You only care about how many times each difficulty appears.

So the first thought should be:

```python
count frequencies
```

Then the problem becomes:

```text
For each frequency, what is the minimum number of groups of size 2 or 3?
```

That second part is greedy because:

```text
To minimize rounds, use groups of 3 as much as possible.
```

Common signs for this pattern:

* The array order does not matter.
* You need to group equal values.
* You need minimum operations/rounds.
* Each operation handles a fixed number of items.

Similar problem types:

* Count frequencies and decide operations per value.
* Minimum deletions based on character frequency.
* Grouping cards or tasks by equal values.
* Greedy batching problems.

---

## 6. Approaches Tried

## Approach 1: Manual simulation with groups of 3 and 2

### Main idea

For each frequency:

1. If it is less than `2`, return `-1`.
2. Use groups of `3` while it is safe.
3. Use groups of `2` for the remaining value.
4. Count total rounds.

### Pseudocode

```text
build frequency map

for each frequency:
    if frequency < 2:
        return -1

rounds = 0

for each frequency:
    while frequency > 2 and frequency != 4:
        frequency -= 3
        rounds += 1

    while frequency > 0 and frequency is even:
        frequency -= 2
        rounds += 1

return rounds
```

### Why it works

It tries to use `3`s first because they reduce the number of rounds. But it avoids reducing `4` into `1`, because `4` should be handled as:

```text
2 + 2
```

### Time complexity

```text
O(n + k * m)
```

Where:

* `n` = number of tasks
* `k` = number of unique difficulties
* `m` = number of loop reductions for each frequency

But practically, since each loop reduces by `2` or `3`, it is still proportional to total task count.

So we can say:

```text
O(n)
```

### Space complexity

```text
O(k)
```

Where `k` is the number of unique task difficulties.

### Interview expectation

This is acceptable as a starting solution, but not the cleanest interview answer.

The issue is that the logic is more complicated and needs special handling like:

```python
val != 4
```

That makes it easier to make mistakes.

---

## Approach 2: Greedy formula using `ceil(val / 3)`

### Main idea

For each frequency:

* If frequency is `1`, impossible.
* Otherwise, minimum rounds is `ceil(freq / 3)`.

### Pseudocode

```text
build frequency map

rounds = 0

for each frequency:
    if frequency == 1:
        return -1

    rounds += ceil(frequency / 3)

return rounds
```

### Why it works

Each round can complete at most `3` tasks.

So the absolute minimum number of rounds for `val` tasks is:

```text
ceil(val / 3)
```

For every `val >= 2`, that number of rounds is achievable using groups of `2` and `3`.

Examples:

```text
2 -> ceil(2/3) = 1 -> 2
3 -> ceil(3/3) = 1 -> 3
4 -> ceil(4/3) = 2 -> 2 + 2
5 -> ceil(5/3) = 2 -> 3 + 2
6 -> ceil(6/3) = 2 -> 3 + 3
7 -> ceil(7/3) = 3 -> 3 + 2 + 2
```

### Time complexity

```text
O(n)
```

You count all tasks once, then loop over the frequency map.

### Space complexity

```text
O(k)
```

Where `k` is the number of unique difficulties.

### Interview expectation

This is the cleaner and more interview-expected solution.

---

## 7. Optimized Approach

The optimized approach is your second solution:

```python
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = dict()

        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        count = 0

        for val in freq.values():
            if val == 1:
                return -1

            count += ceil(val / 3)

        return count
```

Why it is better:

* Simpler logic.
* No manual while loops.
* No special `val != 4` condition.
* Easier to explain.
* Less chance of bugs.

Pattern used:

```text
Hash Map + Greedy Math
```

Why the pattern applies:

* Hash map counts how many tasks exist for each difficulty.
* Greedy math chooses the minimum number of rounds for each frequency.

---

## 8. The `ceil(val / 3)` Explanation

Think of it like this:

```text
Each round can do at most 3 tasks.
So to minimize rounds, we want to pack tasks into groups of 3 as much as possible.
```

But sometimes the remainder matters.

### Case 1: divisible by 3

```text
val = 9
3 + 3 + 3
rounds = 3
ceil(9 / 3) = 3
```

### Case 2: remainder is 2

```text
val = 8
3 + 3 + 2
rounds = 3
ceil(8 / 3) = 3
```

### Case 3: remainder is 1

This is the tricky one.

```text
val = 7
3 + 3 + 1  invalid
```

But we can adjust:

```text
3 + 2 + 2  valid
rounds = 3
ceil(7 / 3) = 3
```

Another example:

```text
val = 10
3 + 3 + 3 + 1  invalid
```

Adjust it:

```text
3 + 3 + 2 + 2  valid
rounds = 4
ceil(10 / 3) = 4
```

So even when a remainder of `1` appears, the number of rounds still stays equal to `ceil(val / 3)`.

---

## 9. Edge Cases and Dry Run

### Edge cases

```text
tasks = [1]
freq = 1
return -1
```

```text
tasks = [1, 1]
freq = 2
answer = 1
```

```text
tasks = [1, 1, 1, 1]
freq = 4
answer = 2 because 2 + 2
```

```text
tasks = [1, 1, 1, 1, 1, 1, 1]
freq = 7
answer = 3 because 3 + 2 + 2
```

---

### Dry run

```python
tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4]
```

Frequency map:

```text
2 -> 3
3 -> 2
4 -> 4
```

Now calculate:

```text
difficulty 2: freq = 3 -> ceil(3/3) = 1 round
difficulty 3: freq = 2 -> ceil(2/3) = 1 round
difficulty 4: freq = 4 -> ceil(4/3) = 2 rounds
```

Total:

```text
1 + 1 + 2 = 4
```

Answer:

```text
4
```

---

## 10. Interview Script

I would explain it like this:

```text
First, I notice that tasks can only be completed together if they have the same difficulty, so the original order of the array does not matter. I need to count the frequency of each difficulty.

After that, for each frequency, I need to split it into groups of size 2 or 3. If any frequency is 1, it is impossible, because we cannot make a round with just one task.

To minimize the number of rounds, I should use groups of 3 as much as possible, since they complete more tasks per round. For any frequency greater than or equal to 2, the minimum number of rounds is ceil(freq / 3).

This also works for cases like 4, 7, or 10 where using only 3s would leave a remainder of 1, because we can replace one 3 + 1 with 2 + 2.

So I count frequencies, check for frequency 1, and otherwise add ceil(freq / 3) to the answer.

The time complexity is O(n), because I scan the tasks once and then scan the frequency map. The space complexity is O(k), where k is the number of unique difficulties.
```

---

## 11. Key Takeaways

* When the problem says “same difficulty,” think frequency map.
* A frequency of `1` is impossible.
* To minimize rounds, prefer groups of `3`.
* For every `freq >= 2`, the answer is:

```python
ceil(freq / 3)
```

* The tricky cases are when `freq % 3 == 1`, like `4`, `7`, `10`.
* Those still work because:

```text
3 + 1 becomes 2 + 2
```

* Your first solution showed good reasoning, but the second solution is cleaner and interview-expected.
