# Car Fleet - Revision Notes

## 1. Problem Summary

We are given cars on a one-lane road going to the same target.

Each car has:

```text
position[i] = where the car starts
speed[i] = how fast the car moves
```

Cars cannot pass each other.

If a faster car behind catches a slower car in front, it must slow down and become part of that car’s fleet.

We need to return how many fleets reach the target.

Key idea:

```text
Instead of simulating movement, calculate each car's time to reach the target.
```

Formula:

```text
time = (target - position) / speed
```

Important constraint:

```text
All positions are unique.
```

So no two cars start at the same place.

---

# 2. My Initial Understanding

You understood that we need to sort the cars because the order on the road matters.

You correctly realized:

```text
Cars in front affect cars behind.
Cars behind cannot pass cars in front.
```

You also understood that we calculate the time each car needs to reach the target:

```text
time = distance / speed
```

The confusing part was understanding why we compare the current car’s time with the fleet time in front.

---

# 3. Mistakes I Made

## Mistake 1: Thinking speed directly decides the fleet

At first, it felt like we should compare speeds.

But the better comparison is not speed. It is:

```text
arrival time to target
```

A faster car behind may still join a slower car ahead if it catches it.

## Mistake 2: Confusion around `current_fleet_time`

`current_fleet_time` does not mean the current car’s time.

It means:

```text
the arrival time of the fleet in front
```

So when we compare:

```text
time > current_fleet_time
```

we are asking:

```text
Is this car too slow to catch the fleet ahead?
```

## Mistake 3: In the stack version, popping the fleet ahead

You tried:

```python
if stack and time <= stack[-1]:
    stack.pop()
stack.append(time)
```

This is wrong because if the current car catches the fleet ahead, the fleet ahead should stay.

Example:

```text
fleet ahead time = 3
current car time = 2
```

The current car catches the fleet, but the fleet still reaches in `3` hours, not `2`.

So we should not pop. We should simply not append.

---

# 4. Things I Learned

## 1. Sort cars from front to back

We sort by position descending:

```text
closest to target -> furthest from target
```

Because cars behind can be affected by cars in front.

## 2. Arrival time matters more than speed

For each car:

```text
time = (target - position) / speed
```

This tells us how long the car would take to reach the target alone.

## 3. Bigger time means slower arrival

If a car has a bigger time than the fleet ahead:

```text
current time > fleet time ahead
```

Then it is too slow to catch the fleet.

So it creates a new fleet.

## 4. Smaller or equal time means it joins

If:

```text
current time <= fleet time ahead
```

Then the car is fast enough to catch the fleet ahead before or at the target.

So it joins that fleet.

## 5. The problem can be solved without real simulation

We do not need to move cars step by step.

We only need:

```text
position order + arrival time
```

---

# 5. Pattern Recognition

## Main pattern

```text
Sorting + Greedy
```

It can also be viewed as a simplified monotonic stack problem.

## Trigger: what tells me to think of this pattern?

The clue is:

```text
Cars cannot pass each other.
```

Whenever a problem says objects cannot cross/pass each other, their order matters.

That usually means:

```text
sort by position
process in order
track some condition from previous/front item
```

## Why greedy works here

When processing from front to back, the fleet in front is already decided.

A car behind has only two possibilities:

```text
1. It catches the fleet ahead
2. It cannot catch it and becomes a new fleet
```

There is no need to go back and change earlier fleets.

## Similar problem types

This pattern appears in problems where:

```text
objects move in one direction
objects cannot pass each other
groups merge together
we compare arrival times or boundaries
```

Examples of similar ideas:

```text
collision problems
interval merging
monotonic stack problems
cars/people moving in one direction
```

---

# 6. Approaches Tried

## Approach 1: Greedy with `current_fleet_time`

### Main idea

Sort cars from closest to target to furthest. Then calculate each car’s arrival time.

Track the arrival time of the fleet in front.

### Step-by-step algorithm

1. Pair each car’s position and speed.
2. Sort cars by position descending.
3. Set `fleets = 0`.
4. Set `current_fleet_time = 0`.
5. For each car:

   * Calculate its time to reach the target.
   * If its time is greater than `current_fleet_time`, it cannot catch the fleet ahead.
   * Count it as a new fleet.
   * Update `current_fleet_time`.
   * Otherwise, it joins the fleet ahead.

### Pseudocode

```text
cars = pair(position, speed)
sort cars by position descending

fleets = 0
current_fleet_time = 0

for each car in cars:
    time = (target - position) / speed

    if time > current_fleet_time:
        fleets += 1
        current_fleet_time = time

return fleets
```

### Time complexity

```text
O(n log n)
```

Because sorting takes `O(n log n)`.

The pairing, reversing, and loop are all `O(n)`.

So total:

```text
O(n log n + n) = O(n log n)
```

### Space complexity

```text
O(n)
```

Because we store the cars in a list.

### Why this approach works

When processing from front to back, each car only needs to compare itself with the fleet in front.

If it reaches later than the fleet ahead, it cannot catch it.

If it reaches earlier or at the same time, it catches and joins.

### Limitations

It requires sorting, so we cannot do better than `O(n log n)` with this direct approach.

### Is it interview-expected?

Yes. This is clean, simple, and interview-expected.

---

## Approach 2: Stack Version

### Main idea

The stack stores arrival times of fleets.

Each value in the stack represents one fleet.

At the end:

```text
number of fleets = len(stack)
```

### Step-by-step algorithm

1. Pair each car’s position and speed.
2. Sort cars by position descending.
3. Create an empty stack.
4. For each car:

   * Calculate its arrival time.
   * If the stack is empty, append the time.
   * Else, compare with the fleet time at the top of the stack.
   * If current time is greater, it is too slow to catch the fleet ahead, so append it.
   * Otherwise, it joins the fleet ahead, so do nothing.

### Pseudocode

```text
cars = pair(position, speed)
sort cars by position descending

stack = []

for each car in cars:
    time = (target - position) / speed

    if stack is empty OR time > stack.top():
        stack.push(time)
    else:
        do nothing

return length of stack
```

### Time complexity

```text
O(n log n)
```

Sorting dominates.

### Space complexity

```text
O(n)
```

The stack can store up to `n` fleet times.

### Why this approach works

The top of the stack represents the fleet directly in front.

If the current car’s time is smaller or equal, it catches that fleet, so we do not add a new fleet.

If the current car’s time is bigger, it cannot catch the fleet ahead, so it becomes a new fleet.

### Limitation

The stack is slightly unnecessary because we only need the top value.

### Is it interview-expected?

Yes, but the `current_fleet_time` version is a bit cleaner.

The stack version is also common because this problem is often categorized under stack.

---

# 7. Optimized Approach

The optimized approach is the greedy approach using `current_fleet_time`.

It is better than the stack version because we do not actually need to store all fleet times.

We only need the latest fleet time in front.

So instead of:

```text
stack[-1]
```

we can just use:

```text
current_fleet_time
```

The pattern is:

```text
Sorting + Greedy
```

Why it applies:

```text
Cars cannot pass, so order matters.
Cars merge into fleets, so we only care whether the current car catches the fleet ahead.
```

---

# 8. Final Code

You did not ask for final code, so no full code here.

But your current solution is correct and interview-expected.

Cleaner standard version:

```text
Use current_fleet_time instead of stack unless the interviewer specifically wants stack.
```

---

# 9. Interview Script

I would explain it like this:

> First, I pair each car’s position with its speed. Then I sort the cars by position in descending order, so I process cars from closest to the target to furthest. This is important because cars are on a one-lane road, so a car behind cannot pass a car in front.
>
> For each car, I calculate how long it would take to reach the target alone using distance divided by speed.
>
> I keep a variable called `current_fleet_time`, which represents the arrival time of the fleet in front. If the current car’s time is less than or equal to this fleet time, then it is fast enough to catch that fleet before or at the target, so it joins the fleet and I do not increase the count.
>
> But if the current car’s time is greater, then it is too slow to catch the fleet ahead, so it becomes a new fleet. I increase the fleet count and update `current_fleet_time`.
>
> Sorting takes `O(n log n)`, and the loop takes `O(n)`, so the total time complexity is `O(n log n)`. The space complexity is `O(n)` because I store the cars.

Stack version interview explanation:

> The stack version uses the same idea, but instead of storing one `current_fleet_time`, I store fleet arrival times in a stack. The top of the stack represents the fleet in front. If the current car’s time is greater than the top, it cannot catch the fleet ahead, so I push it as a new fleet. Otherwise, it joins the fleet ahead, so I do nothing. The answer is the length of the stack.

---

# 10. Edge Cases and Dry Run

## Edge cases

### 1. Only one car

```text
position = [5]
speed = [2]
```

Answer is always:

```text
1
```

One car is one fleet.

### 2. Cars meet exactly at the target

If:

```text
current time == fleet time ahead
```

They are one fleet.

So equal time means join.

### 3. Every car is slower than the fleet ahead

Each car becomes a new fleet.

### 4. Every car catches the fleet ahead

All cars become one fleet.

---

## Small dry run

```text
target = 10
position = [4, 1, 0, 7]
speed    = [2, 2, 1, 1]
```

Pair and sort descending:

```text
(7, 1), (4, 2), (1, 2), (0, 1)
```

Calculate times:

```text
position 7 -> (10 - 7) / 1 = 3
position 4 -> (10 - 4) / 2 = 3
position 1 -> (10 - 1) / 2 = 4.5
position 0 -> (10 - 0) / 1 = 10
```

Process:

```text
3   -> new fleet
3   -> joins fleet ahead
4.5 -> new fleet
10  -> new fleet
```

Answer:

```text
3
```

---

# 11. Key Takeaways

Remember this rule:

```text
bigger time = new fleet
smaller/equal time = joins fleet ahead
```

Sort cars:

```text
closest to target -> furthest from target
```

Because:

```text
cars behind cannot pass cars in front
```

Main pattern:

```text
Sorting + Greedy
```

Stack version and `current_fleet_time` version are basically the same idea.

The cleaner interview version is usually:

```text
sort cars, calculate time, track current_fleet_time
```
