# Min Stack - Revision Notes

## 1. Problem Summary

We need to design a stack that supports:

```text
push(val)
pop()
top()
getMin()
```

The important requirement is:

```text
Every operation must be O(1)
```

A normal stack can do `push`, `pop`, and `top` in `O(1)`, but finding the minimum usually takes `O(n)` because we may need to scan the whole stack.

The key idea is:

> Keep the normal stack order unchanged, and use extra storage to remember the minimum at each point.

---

# 2. My Initial Understanding

Your first idea was to keep the minimum value always on top of the stack.

You were thinking:

```text
If the minimum is always on top, getMin() can be O(1)
```

That part was correct in terms of making `getMin()` fast.

But then you noticed the issue yourself:

```text
If we move the minimum to the top, the normal stack order breaks.
```

For example:

```text
push(5)
push(2)
push(7)
```

The real stack top should be:

```text
7
```

But if we force the minimum to stay on top, then the top becomes:

```text
2
```

That makes `top()` wrong.

So your realization was correct: we cannot reorder the main stack.

---

# 3. Mistakes I Made

## Mistake 1: Thinking `getMin()` removes the minimum

You first thought `getMin()` should remove the minimum value from the stack.

But actually:

```text
getMin() only returns/views the minimum.
```

It does not remove anything.

Similar idea:

```text
top()    -> returns the top, does not remove it
getMin() -> returns the minimum, does not remove it
pop()    -> removes the top
```

---

## Mistake 2: Trying to keep the minimum on top

This breaks normal stack behaviour.

A stack must always follow:

```text
Last In, First Out
```

So the last pushed item must be the item returned by `top()` and removed by `pop()`.

If we move the minimum to the top, we lose that order.

---

## Mistake 3: Small bug in first optimized code

You wrote a good two-stack version, but in `push()`, the first value was added twice to `min_stack`.

The issue was:

```python
if not self.main_stack:
    self.main_stack.append(val)
    self.min_stack.append(val)
else:
    self.main_stack.append(val)

if val < self.min_stack[-1]:
    self.min_stack.append(val)
else:
    self.min_stack.append(self.min_stack[-1])
```

For the first value, `min_stack` gets two values.

Example:

```text
push(5)

main_stack = [5]
min_stack  = [5, 5]
```

The fix is to always push once to the main stack, and always push once to the min stack.

---

# 4. Things I Learned

## `getMin()` means “return”, not “remove”

The word “retrieve” in the problem means:

```text
look at the minimum and return it
```

It does not mean delete it.

---

## We should not disturb the main stack

The main stack must keep the real order of values.

So this should always be true:

```text
top() returns the last pushed value that has not been popped
```

---

## Use extra memory to make operations faster

Since `getMin()` must be `O(1)`, we cannot scan the stack every time.

So we store the minimum history while pushing values.

This is the main trick.

---

## Min stack stores the current minimum at every point

Example:

```text
main_stack = [5, 2, 7, 1, 3]
min_stack  = [5, 2, 2, 1, 1]
```

Each position in `min_stack` tells us:

```text
What was the minimum when this value was pushed?
```

So the current minimum is always:

```text
min_stack[-1]
```

---

# 5. Pattern Recognition

## Main pattern

```text
Stack + auxiliary stack
```

## Trigger

The big clue is:

```text
getMin() must be O(1)
```

Normally, finding the minimum in a stack requires scanning all elements, which is `O(n)`.

So when the problem asks for instant access to something like:

```text
minimum
maximum
previous state
history
```

while still supporting stack operations, think:

```text
Can I store extra information in another stack?
```

## Why this pattern applies here

A stack only gives easy access to the top element.

But we also need easy access to the minimum.

So we keep:

```text
main_stack -> stores actual values
min_stack  -> stores minimum so far
```

This lets both `top()` and `getMin()` be `O(1)`.

## Similar problem types

This pattern appears in problems where you need:

```text
Stack with minimum
Stack with maximum
Undo history
Browser history
Valid parentheses with extra state
Monotonic stack problems
```

---

# 6. Approaches Tried

## Approach 1: Brute Force Normal Stack

### Main idea

Use one normal stack.

For `getMin()`, scan the whole stack and return the smallest value.

---

### Step-by-step algorithm

For `push(val)`:

```text
append val to stack
```

For `pop()`:

```text
remove the top value
```

For `top()`:

```text
return the last value in stack
```

For `getMin()`:

```text
start min_val as infinity
loop through every value in stack
update min_val
return min_val
```

---

### Pseudocode

```text
initialize:
    stack = []

push(val):
    stack.append(val)

pop():
    stack.pop()

top():
    return stack[-1]

getMin():
    min_val = infinity

    for value in stack:
        min_val = min(min_val, value)

    return min_val
```

---

### Time complexity

```text
push    -> O(1)
pop     -> O(1)
top     -> O(1)
getMin  -> O(n)
```

---

### Space complexity

```text
O(n)
```

Only the main stack is stored.

---

### Why this approach works

It works because it keeps all values in the stack and correctly scans them to find the smallest one.

---

### Limitation

It does not satisfy the problem requirement because `getMin()` is `O(n)`, not `O(1)`.

---

### Interview expectation

This is a good starting/brute force approach.

But it is not accepted as the final interview solution because the problem specifically asks for all operations to be `O(1)`.

---

## Approach 2: Keep Minimum Always on Top

### Main idea

Try to keep the smallest value at the top of the stack so `getMin()` can return it quickly.

---

### Why it seems tempting

If the minimum is always on top:

```text
getMin() = stack[-1]
```

So `getMin()` becomes `O(1)`.

---

### Why it does not work

It breaks the normal stack order.

Example:

```text
push(5)
push(2)
push(7)
```

The top should be:

```text
7
```

But if the minimum is forced to the top, the top becomes:

```text
2
```

So `top()` becomes wrong.

---

### Time complexity

It is not worth analyzing fully because the logic itself breaks stack behaviour.

---

### Space complexity

Could be `O(n)`, but the approach is incorrect.

---

### Interview expectation

Not interview-expected.

But it was useful because it helped reveal the real issue:

```text
We need fast access to min without changing stack order.
```

---

## Approach 3: Optimized Two-Stack Approach

### Main idea

Use two stacks:

```text
main_stack -> stores actual values
min_stack  -> stores the minimum so far at each position
```

Every time we push a value into `main_stack`, we also push the current minimum into `min_stack`.

---

### Step-by-step algorithm

For `push(val)`:

```text
append val to main_stack

if min_stack is empty:
    append val to min_stack
else:
    current_min = min(val, min_stack[-1])
    append current_min to min_stack
```

For `pop()`:

```text
pop from main_stack
pop from min_stack
```

For `top()`:

```text
return main_stack[-1]
```

For `getMin()`:

```text
return min_stack[-1]
```

---

### Pseudocode

```text
initialize:
    main_stack = []
    min_stack = []

push(val):
    main_stack.append(val)

    if min_stack is empty:
        min_stack.append(val)
    else:
        min_stack.append(min(val, min_stack[-1]))

pop():
    main_stack.pop()
    min_stack.pop()

top():
    return main_stack[-1]

getMin():
    return min_stack[-1]
```

---

### Time complexity

```text
push    -> O(1)
pop     -> O(1)
top     -> O(1)
getMin  -> O(1)
```

---

### Space complexity

```text
O(n)
```

Technically, we store two stacks:

```text
main_stack = n values
min_stack  = n values
```

So it is:

```text
O(2n)
```

But in Big-O:

```text
O(2n) = O(n)
```

---

### Why this approach works

The main stack keeps the real stack order.

The min stack keeps the minimum value at each stage.

So when we remove an element from the main stack, we also remove the matching minimum state from the min stack.

That means `min_stack[-1]` is always the correct current minimum.

---

### Limitation

It uses extra space.

But that is acceptable because the problem asks for `O(1)` time, and the common tradeoff is extra memory.

---

### Interview expectation

This is the standard interview-expected solution.

---

# 7. Optimized Approach

The final optimized solution is the two-stack approach.

The important idea is:

```text
Do not search for the minimum when getMin() is called.
Instead, remember the minimum while values are being pushed.
```

This is better than brute force because:

```text
Brute force getMin() -> O(n)
Two-stack getMin()   -> O(1)
```

The pattern used is:

```text
Auxiliary stack
```

It applies because we need to remember extra information about the stack state without changing the stack order.

---

# 8. Final Code

You already wrote the correct idea. A cleaner standard version would be:

```python
def push(self, val):
    self.main_stack.append(val)

    if not self.min_stack:
        self.min_stack.append(val)
    else:
        self.min_stack.append(min(val, self.min_stack[-1]))
```

The rest stays simple:

```text
pop()    -> pop from both stacks
top()    -> return main_stack[-1]
getMin() -> return min_stack[-1]
```

---

# 9. Interview Script

## Brute force explanation

“I would first use a normal stack. Push, pop, and top are naturally constant time. For getMin, I can scan through all values in the stack and return the smallest one. This is correct, but getMin takes O(n), so it does not satisfy the requirement that every operation should be O(1).”

---

## Why brute force is inefficient

“The inefficient part is getMin. If the stack has many elements and getMin is called many times, scanning the whole stack repeatedly becomes expensive.”

---

## Optimized explanation

“To make getMin O(1), I use an extra stack called min_stack. The main stack stores the actual values in normal stack order. The min_stack stores the minimum value so far at each point.”

“When I push a new value, I push it into the main stack. Then I compare it with the previous minimum, which is at the top of min_stack. I push the smaller of those two values into min_stack.”

“When I pop, I pop from both stacks. This keeps both stacks aligned.”

“So the current minimum is always at the top of min_stack, and getMin can return it in O(1).”

---

## Pattern explanation for interview

“This is a stack with auxiliary stack pattern. The trigger is that we need constant-time access to extra information, in this case the minimum, while still preserving normal stack behaviour.”

---

## Complexity explanation

“All operations are O(1), because push, pop, top, and getMin only access or modify the end of a list. The space complexity is O(n), because we store the main stack and another stack of minimum values.”

---

# 10. Edge Cases and Dry Run

## Important edge cases

### One element

```text
push(5)
getMin() -> 5
top()    -> 5
```

Both stacks:

```text
main_stack = [5]
min_stack  = [5]
```

---

### Duplicate minimums

```text
push(2)
push(2)
pop()
getMin()
```

This should still return `2`.

That is why storing the minimum at every position is useful.

---

### Negative numbers

The constraints allow negative values:

```text
-2^31 <= val <= 2^31 - 1
```

The two-stack approach works fine with negative numbers.

Example:

```text
push(-3)
push(0)
push(-5)
getMin() -> -5
```

---

## Dry run

Operations:

```text
push(1)
push(2)
push(0)
getMin()
pop()
top()
getMin()
```

Start:

```text
main_stack = []
min_stack  = []
```

After `push(1)`:

```text
main_stack = [1]
min_stack  = [1]
```

After `push(2)`:

```text
main_stack = [1, 2]
min_stack  = [1, 1]
```

Minimum is still `1`.

After `push(0)`:

```text
main_stack = [1, 2, 0]
min_stack  = [1, 1, 0]
```

Now:

```text
getMin() -> 0
```

After `pop()`:

```text
main_stack = [1, 2]
min_stack  = [1, 1]
```

Now:

```text
top()    -> 2
getMin() -> 1
```

---

# 11. Key Takeaways

```text
getMin() does not remove the minimum.
```

```text
Do not reorder the main stack.
```

```text
If a stack problem asks for O(1) access to extra information, think about an auxiliary stack.
```

```text
main_stack stores actual values.
min_stack stores minimum history.
```

```text
Two stacks still give O(n) space, because O(2n) simplifies to O(n).
```

The final two-stack solution is interview-expected.
