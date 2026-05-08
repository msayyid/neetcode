# Asteroid Collision - Revision Notes

## 1. Problem Summary

We are given a list of asteroids.

Each asteroid has:

```text
absolute value = size
sign = direction
```

```text
positive = moving right
negative = moving left
```

When two asteroids collide:

```text
smaller one explodes
same size = both explode
same direction = never collide
```

The goal is to return the final state after all collisions.

Key idea:

> A collision only happens when a previous asteroid is moving right and the current asteroid is moving left.

That means only this situation can collide:

```text
-->   <--
```

In code:

```python
stack[-1] > 0 and a < 0
```

## 2. My Initial Understanding

At first, you tried to solve it by comparing asteroids in pairs.

You thought about popping two asteroids and deciding which one survives.

You also considered pushing differences or keeping only one direction.

What you understood correctly:

* Bigger asteroid survives.
* Same size means both disappear.
* Direction matters.
* Some asteroids should not collide.

Where you were confused:

* You were comparing asteroids too much like fixed pairs.
* You were not fully considering that one asteroid can collide with multiple previous asteroids.
* You were unsure why only `positive then negative` causes collision.

Example that exposed the issue:

```python
[10, 2, -5]
```

`-5` first collides with `2`, destroys it, then may collide with `10`.

So collision is not always just between one pair.

## 3. Mistakes I Made

### Mistake 1: Trying to pop asteroids in pairs

You tried something like:

```python
a1 = asteroids.pop()
a2 = asteroids.pop()
```

Why this is a problem:

* The list may have one asteroid left, causing an error.
* Collisions are not always clean pairs.
* One asteroid may need to collide with several previous asteroids.

Example:

```python
[10, 2, -5]
```

`-5` needs to check against `2`, then maybe against `10`.

### Mistake 2: Thinking negative then positive might collide

Example:

```python
[-5, 10]
```

This does not collide because:

```text
-5 moves left
10 moves right
```

They move away from each other:

```text
<--   -->
```

Only this collides:

```text
-->   <--
```

### Mistake 3: Not seeing the need for repeated checking

When the current asteroid destroys the stack top, the current asteroid is still alive.

So it may need to continue checking.

Example:

```python
[10, 2, -5]
```

`-5` destroys `2`, but then must compare with `10`.

That is why we need a `while` loop, not just one `if`.

## 4. Things I Learned

### Key observation

A collision only happens when:

```python
stack[-1] > 0 and a < 0
```

Meaning:

```text
previous asteroid moves right
current asteroid moves left
```

### Why stack works

The stack stores asteroids that have survived so far.

When a new asteroid comes in, it only needs to check the most recent surviving asteroid.

That most recent asteroid is at the top of the stack.

### Why `while` is needed

A current asteroid can destroy multiple previous asteroids.

So we keep checking while collision is possible.

### Why `a = 0` is used

You used:

```python
a = 0
```

to mark that the current asteroid was destroyed.

Since constraints say:

```text
asteroids[i] != 0
```

using `0` as a destroyed marker is safe.

Then this check works:

```python
if a:
    stack.append(a)
```

Meaning:

```text
if current asteroid is still alive, add it to stack
```

## 5. Pattern Recognition

### Main pattern

Stack simulation.

### Trigger

Think of stack when:

* You process items from left to right.
* The current item may cancel/remove previous items.
* You need to repeatedly compare with the most recent valid previous item.
* The problem has a “collision”, “matching”, or “removing previous elements” behavior.

### Why stack applies here

Asteroids move in a row.

When processing from left to right, the only asteroid the current one can collide with first is the most recent surviving asteroid before it.

That is exactly what stack top represents.

### Common signs for this pattern

Look for phrases like:

```text
collide
remove
destroy
previous element
nearest previous
valid state after operations
```

Similar problem types:

* Valid Parentheses
* Remove Adjacent Duplicates
* Daily Temperatures
* Next Greater Element
* Baseball Game
* Backspace String Compare

## 6. Approaches Tried

## Approach 1: Pair-popping approach

### Main idea

Pop two asteroids at a time and compare them.

### Step-by-step idea

1. Pop one asteroid.
2. Pop another asteroid.
3. Compare their directions and sizes.
4. Push the survivor back.

### Pseudocode

```python
while asteroids:
    a1 = asteroids.pop()
    a2 = asteroids.pop()

    compare a1 and a2
    push survivor back
```

### Time complexity

Could be unclear and error-prone.

In theory it may seem close to `O(n)`, but the logic is broken.

### Space complexity

`O(1)` extra, if modifying input.

### Why this approach does not work well

It assumes collisions happen in fixed pairs.

But one asteroid can collide with multiple previous asteroids.

Example:

```python
[10, 2, -5]
```

`-5` collides with `2`, then possibly with `10`.

### Interview expected?

No. This is not the expected approach.

It is a useful starting idea, but not reliable.

---

## Approach 2: Stack approach

### Main idea

Use a stack to keep asteroids that survived so far.

For each asteroid, check whether it collides with the stack top.

Collision only happens when:

```python
stack[-1] > 0 and a < 0
```

### Step-by-step algorithm

1. Create an empty stack.

2. Loop through each asteroid `a`.

3. While:

   * stack is not empty
   * current asteroid is moving left
   * stack top is moving right

   compare their sizes.

4. If current asteroid is bigger:

   * pop the stack top
   * current asteroid may continue colliding

5. If stack top is bigger:

   * current asteroid is destroyed

6. If both are same size:

   * pop stack top
   * current asteroid is destroyed

7. If current asteroid survives, append it to stack.

8. Return stack.

### Pseudocode

```python
stack = []

for a in asteroids:
    while stack and a < 0 and stack[-1] > 0:
        diff = a + stack[-1]

        if diff < 0:
            stack.pop()

        elif diff > 0:
            a = 0
            break

        else:
            stack.pop()
            a = 0
            break

    if a:
        stack.append(a)

return stack
```

### Time complexity

```text
O(n)
```

Each asteroid is pushed at most once and popped at most once.

### Space complexity

```text
O(n)
```

In the worst case, all asteroids survive and stay in the stack.

### Why this approach works

The stack keeps only surviving asteroids.

The current asteroid only needs to check the most recent surviving asteroid before it.

If that asteroid is destroyed, the current asteroid checks the next one.

This correctly handles chain collisions.

### Limitations

Uses extra space.

But this is expected and accepted.

### Interview expected?

Yes. This is the standard interview-expected solution.

## 7. Optimized Approach

The optimized approach is the stack simulation.

It is better than pair-popping because it handles chain collisions correctly.

The key condition is:

```python
while stack and a < 0 and stack[-1] > 0:
```

This means:

```text
only keep resolving while the current asteroid can collide with the previous surviving asteroid
```

The pattern is stack because the current asteroid interacts with the most recent unresolved previous asteroid.

## 8. Final Code

You asked for notes, so no full code needed.

Your code is correct and interview-expected.

Cleaner wording for your important comments:

```python
# A collision is only possible when the previous asteroid moves right
# and the current asteroid moves left.
```

```python
# If current asteroid survived all possible collisions, keep it.
```

## 9. Interview Script

You can explain it like this:

> I process the asteroids from left to right and use a stack to store the asteroids that have survived so far.
>
> The important observation is that not every opposite sign causes a collision. A collision only happens when the previous asteroid is positive and the current asteroid is negative, because that means they are moving toward each other.
>
> So for each asteroid, I compare it with the top of the stack while the stack top is positive and the current asteroid is negative.
>
> If the current asteroid is larger, I pop the stack top and keep checking because the current asteroid may collide with more previous asteroids.
>
> If the stack top is larger, the current asteroid is destroyed.
>
> If both sizes are equal, both are destroyed.
>
> If the current asteroid survives all possible collisions, I push it onto the stack.
>
> This works because the stack top always represents the nearest surviving asteroid to the left, which is the only one the current asteroid can collide with first.
>
> The time complexity is O(n), because each asteroid is pushed and popped at most once. The space complexity is O(n) for the stack.

## 10. Edge Cases and Dry Run

### Edge cases

```python
[5, 5]
```

Same direction, no collision.

Result:

```python
[5, 5]
```

---

```python
[-5, 10]
```

Moving away from each other, no collision.

Result:

```python
[-5, 10]
```

---

```python
[5, -5]
```

Same size, both destroyed.

Result:

```python
[]
```

---

```python
[10, 2, -5]
```

Chain collision.

Result:

```python
[10]
```

---

```python
[2, 4, -4, -1]
```

`4` and `-4` destroy each other.

Then `2` and `-1` collide, `2` survives.

Result:

```python
[2]
```

### Dry run: `[10, 2, -5]`

```text
stack = []

a = 10
no collision
stack = [10]

a = 2
no collision
stack = [10, 2]

a = -5
stack top = 2
2 moves right, -5 moves left, so collision happens

2 is smaller, so pop 2
stack = [10]

now compare -5 with 10
10 is bigger, so -5 is destroyed

final stack = [10]
```

## 11. Key Takeaways

* Only `positive then negative` can collide.
* Use a stack when the current item may remove previous items.
* The stack stores asteroids that survived so far.
* Use a `while` loop because one asteroid may collide multiple times.
* `a = 0` is a clean way to mark the current asteroid as destroyed.
* Your final solution is correct and interview-expected.
* The main pattern is stack simulation.
