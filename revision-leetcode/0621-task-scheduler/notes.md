# LeetCode 621: Task Scheduler - Revision Notes

## 1. Problem Summary

You are given a list of CPU tasks, like:

```python
tasks = ["A","A","A","B","B","B"]
n = 2
```

Each task takes exactly `1` CPU interval.

The rule is:

> The same task must have at least `n` intervals between two executions.

So if we run `A` at time `1` and `n = 2`, we cannot run `A` again at time `2` or `3`. We can run it again at time `4`.

We need to return the minimum number of intervals needed to finish all tasks, including possible idle intervals.

Example:

```text
A -> B -> idle -> A -> B -> idle -> A -> B
```

Answer:

```text
8
```

## 2. Key Idea

The most frequent tasks are the hardest to schedule because they cause the most cooldown problems.

So the greedy idea is:

> At each interval, run the available task with the highest remaining frequency.

To do that, we use:

```text
max heap -> choose the most frequent available task
queue -> store tasks that are cooling down
time -> simulate CPU intervals
```

Python only has a min heap, so we use negative counts to simulate a max heap.

---

# 3. My Initial Understanding

You understood the problem correctly:

* Each task takes `1` unit of time.
* Same tasks need a cooldown gap of `n`.
* The goal is to minimize idle time.
* The most frequent tasks should be handled early because they create the most scheduling pressure.

You were confused about:

* How to use a heap here.
* Why we need a queue as well.
* Whether multiple tasks can have the same availability time.
* How to reason about time complexity.

That confusion is normal for this problem because it combines two ideas:

```text
heap + cooldown simulation
```

---

# 4. Mistakes I Made

## Mistake 1: Returning inside the loop

You had:

```python
while max_heap or q:
    ...
    return time
```

This returns after the first interval.

Why it is wrong:

The CPU simulation must continue until both:

```text
heap is empty
queue is empty
```

So `return time` must be after the loop finishes.

---

## Mistake 2: Checking cooldown queue only inside `if max_heap`

You had the queue check inside:

```python
if max_heap:
    ...
    if q and q[0][1] == time:
        ...
```

Why it is wrong:

Sometimes the heap is empty because all tasks are cooling down. In that case, we still need to check whether a task from the queue becomes available.

So this check should be outside:

```python
if q and q[0][1] == time:
    heapq.heappush(max_heap, q.popleft()[0])
```

---

## Mistake 3: Importing `Counter` from the wrong place

You wrote:

```python
from typing import Counter
```

Correct:

```python
from collections import Counter
```

`Counter` is a frequency counter from `collections`.

---

## Mistake 4: Complexity wording

You said something like:

```text
heappush/heappop log n over n times, n + log n
```

The better reasoning is:

```text
Loop count * work per loop
```

So if we do heap operations each interval:

```text
O(total_intervals * log heap_size)
```

But in this problem, heap size is at most `26` because tasks are only `A-Z`.

So:

```text
O(total_intervals * log 26) = O(total_intervals)
```

And under the constraints, this is usually simplified to:

```text
O(N)
```

---

# 5. Things I Learned

## 1. Max heap is useful when we need the largest/frequent item first

Python `heapq` is a min heap.

So to simulate a max heap:

```python
max_heap = [-count for count in count.values()]
```

Example:

```text
A: 3 -> -3
B: 3 -> -3
```

The smallest negative number represents the biggest positive count.

---

## 2. Cooldown queue stores tasks that cannot be used yet

After running a task, if it still has remaining count, we put it in the queue:

```python
q.append([cnt, time + n])
```

This means:

```text
This task can come back after its cooldown time is reached.
```

The queue stores:

```text
[remaining_count, available_time]
```

---

## 3. Why queue order works

You asked whether multiple tasks can have the same availability time.

In this simulation, we process only one task per time interval.

So only one task is added to the queue per time unit.

Because `time` increases by `1`, `time + n` also increases naturally.

So the queue remains ordered by availability time.

---

## 4. Heap and queue have different jobs

Heap answers:

```text
Which available task should I run now?
```

Queue answers:

```text
Which tasks are cooling down, and when can they come back?
```

This is the main mental model.

---

# 6. Pattern Recognition

## Main Pattern

```text
Greedy + Max Heap + Cooldown Queue + Time Simulation
```

## Trigger: When should I think of this pattern?

Think of this pattern when the problem says:

```text
Choose the best/highest priority item repeatedly
```

and also:

```text
After using an item, it cannot be used again immediately
```

Common clues:

* “Most frequent”
* “Cooldown”
* “Wait n intervals”
* “Minimum time”
* “Schedule tasks”
* “Repeatedly choose next best option”
* “Item becomes available later”

This problem has both:

```text
Need to choose the most frequent available task
Need to delay repeated tasks because of cooldown
```

That is why heap + queue fits.

## Similar problem types

This pattern appears in:

* Task scheduling with cooldown
* Reorganize string problems
* CPU/process scheduling
* Choosing most frequent item but delaying reuse
* Problems where used items become available again later

---

# 7. Approaches Tried

## Approach 1: Heap + Cooldown Queue Simulation

### Main idea

Use a max heap to always select the task with the highest remaining frequency.

After processing a task, put it into a cooldown queue until it is allowed to be used again.

### Step-by-step algorithm

1. Count task frequencies using `Counter`.
2. Push negative frequencies into a heap.
3. Create a queue for cooling tasks.
4. Start `time = 0`.
5. While heap or queue is not empty:

   * Increase time by `1`.
   * If heap is not empty:

     * Pop the most frequent available task.
     * Process it once.
     * If it still has remaining count, add it to cooldown queue.
   * Check whether the first task in the queue is available again.
   * If yes, push it back into heap.
6. Return `time`.

### Pseudocode

```text
count frequencies

max_heap = negative frequencies
heapify(max_heap)

q = empty queue
time = 0

while max_heap is not empty OR q is not empty:
    time += 1

    if max_heap is not empty:
        cnt = pop from max_heap
        cnt += 1   # because cnt is negative

        if cnt != 0:
            add [cnt, time + n] to q

    if q is not empty and q[0].available_time == time:
        move q[0] back to max_heap

return time
```

### Why this works

The greedy choice is to always do the task with the highest remaining count.

Why?

Because frequent tasks are the ones most likely to cause idle time later. If we delay them too much, we may be forced to idle more.

The queue ensures we respect the cooldown rule.

So together:

```text
heap gives best available task
queue prevents illegal repeated tasks
```

### Time complexity

Let:

```text
N = number of tasks
```

The heap contains at most 26 task types.

So each heap operation is:

```text
O(log 26) = O(1)
```

The simulation runs across CPU intervals.

So:

```text
Time: O(total_intervals)
```

For LeetCode constraints, this is usually simplified to:

```text
O(N)
```

### Space complexity

The frequency map, heap, and queue store at most 26 task types.

```text
Space: O(26) = O(1)
```

### Limitations

This approach is slightly more code than the math solution.

It is very understandable, but you must be careful with:

* cooldown timing
* queue check placement
* returning after the loop
* negative counts

### Interview expectation

This is interview-acceptable.

It is especially good if you explain it clearly as a scheduling simulation.

---

## Approach 2: Math / Greedy Formula

We discussed that another expected solution exists, but we did not fully implement it.

### Main idea

The most frequent task determines the minimum skeleton of the schedule.

Example:

```text
A A A
```

If `n = 2`, then we need gaps:

```text
A _ _ A _ _ A
```

Other tasks can fill the gaps.

### Formula idea

Let:

```text
max_freq = highest task frequency
max_count = number of tasks with that max frequency
```

Then one possible formula is based on:

```text
(max_freq - 1) groups
```

Each group has size:

```text
n + 1
```

Final answer is the max of:

```text
len(tasks)
formula_result
```

### Why max with len(tasks)?

Because if there are enough other tasks to fill all idle spaces, then answer is just:

```text
len(tasks)
```

No idle time needed.

### Interview expectation

This is also interview-expected and often considered the cleaner/optimized solution.

But for learning heaps, the heap + queue solution is better for understanding the process.

---

# 8. Optimized Approach

For your current learning stage, the optimized heap-based approach is:

```text
max heap + cooldown queue
```

It is better than trying to manually build a schedule because:

* It always picks the most urgent available task.
* It automatically handles cooldown.
* It naturally counts idle intervals when heap is empty but queue is not.
* It avoids complex manual ordering.

The pattern applies because the problem has two requirements:

```text
1. Choose the highest frequency available task.
2. Temporarily block recently used tasks.
```

That exactly maps to:

```text
max heap + queue
```

---

# 9. Interview Script

Here is how you can explain it in an interview:

> First, I count the frequency of each task because the tasks with higher frequency are the hardest to schedule. My greedy idea is to always process the task with the highest remaining count among the tasks that are currently available.

> To support that, I use a max heap. Since Python has a min heap, I store negative counts. Each time unit, I pop the most frequent task, process it once, and reduce its count.

> However, after using a task, I cannot immediately put it back into the heap because of the cooldown rule. So I use a queue to store tasks that are cooling down. Each item in the queue stores the remaining count and the time when that task becomes available again.

> During each time interval, I first try to process a task from the heap. If no task is available but the queue still has cooling tasks, that interval becomes idle. After each interval, I check whether the front of the queue is ready to return to the heap.

> The loop continues until both the heap and queue are empty. The total time counted is the minimum number of intervals.

> The reason this works is that we always prioritize the most frequent available task, which reduces the chance of being forced into idle time later, while the queue guarantees that cooldown rules are respected.

> Since there are only 26 uppercase task types, heap operations are constant time. The overall time is O(N), and the space is O(1).

---

# 10. Edge Cases and Dry Run

## Edge cases

### Case 1: No cooldown

```python
tasks = ["A", "A", "B"]
n = 0
```

No idle needed.

Answer:

```text
3
```

### Case 2: All tasks are different

```python
tasks = ["A", "B", "C"]
n = 2
```

No repeated task, so no cooldown problem.

Answer:

```text
3
```

### Case 3: Only one task type

```python
tasks = ["A", "A", "A"]
n = 2
```

Schedule:

```text
A idle idle A idle idle A
```

Answer:

```text
7
```

### Case 4: Enough other tasks to fill idle gaps

```python
tasks = ["A","C","A","B","D","B"]
n = 1
```

Can schedule without idle:

```text
A B C D A B
```

Answer:

```text
6
```

---

## Dry run

Input:

```python
tasks = ["A","A","A","B","B","B"]
n = 2
```

Frequency:

```text
A: 3
B: 3
```

Heap:

```text
[-3, -3]
```

Queue:

```text
[]
```

### Time 1

Pop `A`.

```text
A count: 3 -> 2 remaining
```

Put into cooldown:

```text
q = [A remaining 2, available at time 3]
```

Schedule:

```text
A
```

### Time 2

Pop `B`.

```text
B count: 3 -> 2 remaining
```

Put into cooldown:

```text
q = [A available 3, B available 4]
```

Schedule:

```text
A B
```

### Time 3

Heap is empty.

So CPU idles.

Now `A` becomes available and moves back to heap.

Schedule:

```text
A B idle
```

### Time 4

Pop `A`.

```text
A count: 2 -> 1 remaining
```

Put it into cooldown.

At the same time, `B` becomes available and returns to heap.

Schedule:

```text
A B idle A
```

### Time 5

Pop `B`.

```text
B count: 2 -> 1 remaining
```

Put it into cooldown.

Schedule:

```text
A B idle A B
```

### Time 6

Heap is empty.

CPU idles.

`A` becomes available again.

Schedule:

```text
A B idle A B idle
```

### Time 7

Pop `A`.

```text
A count: 1 -> 0
```

A is finished.

`B` becomes available again.

Schedule:

```text
A B idle A B idle A
```

### Time 8

Pop `B`.

```text
B count: 1 -> 0
```

B is finished.

Schedule:

```text
A B idle A B idle A B
```

Both heap and queue are empty.

Answer:

```text
8
```

---

# 11. Key Takeaways

* This is a scheduling problem with cooldown.
* The main trigger is: repeated tasks cannot be used immediately again.
* Use a max heap when you need to repeatedly choose the most frequent/highest priority item.
* Use a queue when used items need to wait before becoming available again.
* The heap stores available tasks.
* The queue stores cooling tasks.
* Python `heapq` is a min heap, so use negative counts for max heap behavior.
* The heap solution is interview-acceptable.
* Complexity is effectively:

```text
Time: O(N)
Space: O(1)
```

because there are only 26 possible task types.
