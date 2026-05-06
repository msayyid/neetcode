# LeetCode 225 - Implement Stack using Queues

## 1. Problem Summary

We need to implement a **stack** using **queue operations**.

A stack follows:

```text
Last In, First Out
```

Example:

```text
push(1)
push(2)
push(3)

pop() should return 3
```

But a queue follows:

```text
First In, First Out
```

Example:

```text
queue = [1, 2, 3]

popleft() returns 1
```

So the main challenge is:

> How can we make a queue behave like a stack?

---

# 2. My Initial Understanding

You already understood the difference between a stack and a queue:

```text
Stack:
last pushed element comes out first

Queue:
first pushed element comes out first
```

At first, the confusing part was not the idea of stack/queue itself.

The confusing part was:

```text
How does moving elements between queues make the newest element come first?
```

Then you understood the key idea:

> Put the newest element first, then move the old elements behind it.

That is the whole trick.

---

# 3. Mistakes / Confusions I Had

## Mistake 1: Using stack operations directly

Your first version used:

```python
self.stack.append(x)
self.stack.pop()
self.stack[-1]
```

This works as a stack, but it does not solve the actual problem because the problem says we should implement stack using **queue behavior**.

Why it is not accepted conceptually:

```text
pop() from the back is a stack operation, not a queue operation.
```

So this is not the interview-expected solution for this problem.

---

## Mistake 2: Confusion about swapping queues

You were confused by this line:

```python
self.main, self.temp = self.temp, self.main
```

The important idea is:

```text
temp has the correct stack order after push.
main is empty.
```

So we swap them.

Before swap:

```text
main = []
temp = [2, 1]
```

After swap:

```text
main = [2, 1]
temp = []
```

Now `main` is again the queue we use for `pop()` and `top()`.

---

## Mistake 3: Not seeing why rotating works in one queue

At first, the one-queue version looked strange.

But then you dry-ran it correctly:

```text
push(1)
q = [1]

push(2)
q = [1, 2]
rotate once
q = [2, 1]

push(3)
q = [2, 1, 3]
rotate twice
q = [3, 2, 1]
```

The key lesson:

```text
After pushing a new element, rotate all old elements behind it.
```

---

# 4. Things I Learned

## Key idea

To simulate a stack using queues:

```text
front of queue = top of stack
```

If the newest element is always at the front, then:

```python
pop()
```

can simply remove from the front.

---

## Important observation

For both the two-queue and one-queue approaches:

```text
push is expensive
pop is easy
top is easy
```

Because we rearrange the queue during `push`.

---

## Queue operations allowed

For this problem, allowed queue-style operations are usually:

```python
append(x)      # add to back
popleft()      # remove from front
queue[0]       # look at front
len(queue)
```

But this is not queue-style:

```python
pop()          # removes from back
queue[-1]      # looks at back
```

Those behave like stack operations.

---

# 5. Pattern Recognition

## Main pattern

```text
Queue simulation / data structure design
```

This is a design problem where we are asked to build one data structure using another.

## Trigger: How do I know this pattern applies?

The problem says:

```text
Implement Stack using Queues
```

That is the direct clue.

Whenever a problem asks:

```text
Implement X using Y
```

you should think:

```text
How can I rearrange Y so it behaves like X?
```

For this problem:

```text
Stack needs newest first.
Queue naturally gives oldest first.
```

So we need to rearrange the queue so the newest item becomes the front.

---

# 6. Approaches Tried

---

# Approach 1: Using deque like a stack

## Main idea

Use Python `deque` directly as a stack.

Push to the back.

Pop from the back.

Top is the last element.

## Pseudocode

```text
push(x):
    stack.append(x)

pop():
    return stack.pop()

top():
    return stack[-1]

empty():
    return len(stack) == 0
```

## Time complexity

```text
push: O(1)
pop: O(1)
top: O(1)
empty: O(1)
```

## Space complexity

```text
O(n)
```

## Why it works

It works because `deque` supports adding and removing from the back.

So it naturally behaves like a stack.

## Limitation

This does not follow the problem requirement.

The problem wants us to use queues, but this version uses stack behavior:

```python
pop()
stack[-1]
```

## Interview expected?

```text
No.
```

This is a good starting point to understand stack behavior, but not the real solution for this problem.

---

# Approach 2: Two Queues

## Main idea

Use:

```text
main = stores elements in stack order
temp = temporary queue used during push
```

The newest element should always become the front.

So when we push a new element:

1. Put the new element into `temp`.
2. Move all old elements from `main` into `temp`.
3. Now `temp` has correct stack order.
4. Swap `main` and `temp`.

## Example

Before pushing `2`:

```text
main = [1]
temp = []
```

Push `2` into temp:

```text
main = [1]
temp = [2]
```

Move old elements behind it:

```text
main = []
temp = [2, 1]
```

Swap:

```text
main = [2, 1]
temp = []
```

Now the front of `main` is the stack top.

## Pseudocode

```text
push(x):
    temp.append(x)

    while main is not empty:
        temp.append(main.popleft())

    swap main and temp

pop():
    return main.popleft()

top():
    return main[0]

empty():
    return len(main) == 0
```

## Time complexity

```text
push: O(n)
pop: O(1)
top: O(1)
empty: O(1)
```

## Space complexity

```text
O(n)
```

We store all elements across the two queues.

## Why this works

After every push, `main` is rearranged like this:

```text
newest, older, older, oldest
```

Example:

```text
main = [3, 2, 1]
```

So:

```text
front of main = top of stack
```

That makes `pop()` easy.

## Limitation

Push takes `O(n)` because we move all existing elements every time.

## Interview expected?

```text
Yes.
```

This is a valid and common solution.

---

# Approach 3: One Queue

## Main idea

Use only one queue.

When we push a new element, it goes to the back first.

Then we rotate all the old elements behind it.

## Example

Push `1`:

```text
q = [1]
```

Push `2`:

```text
q = [1, 2]
```

Rotate old elements once:

```text
q = [2, 1]
```

Push `3`:

```text
q = [2, 1, 3]
```

Rotate old elements twice:

```text
q = [1, 3, 2]
q = [3, 2, 1]
```

Now the newest element is at the front.

## Pseudocode

```text
push(x):
    q.append(x)

    repeat len(q) - 1 times:
        q.append(q.popleft())

pop():
    return q.popleft()

top():
    return q[0]

empty():
    return len(q) == 0
```

## Time complexity

```text
push: O(n)
pop: O(1)
top: O(1)
empty: O(1)
```

## Space complexity

```text
O(n)
```

## Why this works

When we push a new value, it first goes to the back.

Then we move all old elements from the front to the back.

This makes the new value move to the front.

So the queue becomes:

```text
newest, older, older, oldest
```

Example:

```text
q = [3, 2, 1]
```

Now:

```text
front of queue = stack top
```

## Limitation

Push is still `O(n)` because we rotate old elements.

## Interview expected?

```text
Yes.
```

This is usually the cleaner and more standard solution than the two-queue version.

---

# 7. Optimized / Cleanest Approach

The cleanest approach is the **one-queue approach**.

Why?

Because it uses fewer data structures:

```text
Two-queue version: main + temp
One-queue version: only queue
```

Both have the same time complexity:

```text
push: O(n)
pop: O(1)
top: O(1)
empty: O(1)
```

But one queue is simpler once you understand rotation.

## Core idea

```text
After every push, rotate the queue so the newest element comes to the front.
```

That gives us stack behavior.

---

# 8. Edge Cases

## Empty stack

```text
empty() should return True
```

## One element

```text
push(1)
top() -> 1
pop() -> 1
empty() -> True
```

## Multiple elements

```text
push(1)
push(2)
push(3)

top() -> 3
pop() -> 3
pop() -> 2
pop() -> 1
```

## Important LeetCode detail

LeetCode usually guarantees:

```text
pop() and top() are only called when the stack is not empty.
```

So returning `-1` is not necessary for LeetCode, but it is okay for your own safe version.

---

# 9. Dry Run for One-Queue Approach

Operations:

```text
push(1)
push(2)
push(3)
pop()
top()
```

Start:

```text
q = []
```

Push `1`:

```text
q = [1]
```

Push `2`:

```text
q = [1, 2]
rotate once
q = [2, 1]
```

Push `3`:

```text
q = [2, 1, 3]
rotate twice

move 2 to back:
q = [1, 3, 2]

move 1 to back:
q = [3, 2, 1]
```

Now:

```text
pop() returns 3
q = [2, 1]
```

Then:

```text
top() returns 2
```

Correct stack behavior.

---

# 10. Interview Script

## Brute force / not allowed version

"My first thought is that a stack can be implemented directly using a deque by appending to the back and popping from the back. That gives O(1) push, pop, and top. However, that does not satisfy the problem requirement because it uses stack-like operations such as popping from the back. Since the problem specifically asks to implement a stack using queues, I need to use queue-style operations instead."

---

## Two-queue explanation

"To simulate a stack with queues, I need the newest element to be removed first. Since a queue removes from the front, I will make sure the newest element is always at the front of my main queue.

For push, I put the new element into a temporary queue first. Then I move all existing elements from the main queue into the temporary queue. This puts the new element before all older elements. After that, I swap the two queues, so the main queue again contains the stack in correct order.

Then pop is easy because the top of the stack is at the front of the main queue. So pop is just popleft, and top is just looking at the front.

The time complexity is O(n) for push because I may move all existing elements. Pop, top, and empty are O(1). Space complexity is O(n)."

---

## One-queue explanation

"A cleaner solution is to use only one queue. When I push a new element, it first goes to the back of the queue. But I need it at the front because it is the top of the stack.

So after adding it, I rotate all the old elements. That means I remove each old element from the front and add it to the back. If there were n old elements, I rotate n times. After this rotation, the newest element becomes the front of the queue.

Now the front of the queue always represents the top of the stack. So pop is popleft, top is queue[0], and empty checks whether the queue is empty.

The time complexity is O(n) for push, and O(1) for pop, top, and empty. Space complexity is O(n). This is the cleaner interview solution."

---

# 11. Key Takeaways

Remember this:

```text
To make a queue behave like a stack, keep the newest element at the front.
```

Two ways to do that:

```text
Two queues:
put new element in temp, move old elements behind it, then swap.

One queue:
put new element at back, then rotate old elements behind it.
```

Most important idea:

```text
front of queue = top of stack
```

Once that is true:

```text
pop = popleft()
top = queue[0]
```

The best version to remember for interviews:

```text
One queue with rotation
```

Complexities:

```text
push: O(n)
pop: O(1)
top: O(1)
empty: O(1)
space: O(n)
```
