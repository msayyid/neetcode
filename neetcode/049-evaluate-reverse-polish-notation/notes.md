# Evaluate Reverse Polish Notation - Revision Notes

## 1. Problem Summary

You are given a list of strings called `tokens`.

The list represents a valid arithmetic expression in Reverse Polish Notation.

Example:

```text
["1", "2", "+", "3", "*", "4", "-"]
```

This means:

```text
((1 + 2) * 3) - 4
```

Return the final integer result.

The operators are:

```text
+, -, *, /
```

Important rule:

```text
Division must truncate toward zero.
```

So in Python, for this problem:

```python
int(a / b)
```

is useful because it truncates toward zero.

## 2. My Initial Understanding

You understood the main idea correctly:

```text
Numbers should be saved somewhere.
When an operator appears, we use the previous two numbers.
```

You also correctly recognized that a stack is useful here.

Your first solution already had the correct structure:

```text
number -> push into stack
operator -> pop two values
calculate
push result back
```

The main confusion was about the order of operands for `-` and `/`.

## 3. Mistakes I Made

### Mistake 1: Doing `num1 - num2`

You first tried:

```python
num1 = stack.pop()
num2 = stack.pop()
stack.append(num1 - num2)
```

The issue is that `stack.pop()` removes the last value first.

Example:

```text
["5", "2", "-"]
```

Before `-`, stack is:

```text
[5, 2]
```

Then:

```python
num1 = stack.pop()  # 2
num2 = stack.pop()  # 5
```

So:

```python
num1 - num2
```

means:

```text
2 - 5
```

But the correct expression is:

```text
5 - 2
```

So the correct operation is:

```python
num2 - num1
```

or more clearly:

```python
right = stack.pop()
left = stack.pop()
left - right
```

### Mistake 2: Doing `num1 / num2`

Same issue with division.

Example:

```text
["10", "2", "/"]
```

This means:

```text
10 / 2
```

Stack before `/`:

```text
[10, 2]
```

Pop order:

```python
num1 = 2
num2 = 10
```

So this is wrong:

```python
num1 / num2
```

because it means:

```text
2 / 10
```

Correct:

```python
num2 / num1
```

or:

```python
right = stack.pop()
left = stack.pop()
left / right
```

### Mistake 3: Having an unused variable

In your first version, you had:

```python
total = 0
```

But you never used it.

This does not break the code, but it is unnecessary. In interviews, cleaner code is better.

## 4. Things I Learned

### Key idea 1: RPN naturally uses a stack

Reverse Polish Notation works from left to right.

When you see a number, store it.

When you see an operator, apply it to the last two stored numbers.

That is exactly how a stack works.

### Key idea 2: First popped value is the right operand

This is the most important lesson.

```python
right = stack.pop()
left = stack.pop()
```

Then calculate:

```python
left operator right
```

For example:

```text
["8", "3", "-"]
```

Means:

```text
8 - 3
```

Stack:

```text
[8, 3]
```

Pop:

```python
right = 3
left = 8
```

Then:

```python
left - right
```

Result:

```text
5
```

### Key idea 3: Addition and multiplication do not expose the order issue

For `+`:

```text
2 + 5 = 5 + 2
```

For `*`:

```text
2 * 5 = 5 * 2
```

So even if you accidentally reverse operands, it still works.

But for `-` and `/`, order matters.

```text
5 - 2 != 2 - 5
10 / 2 != 2 / 10
```

### Key idea 4: Division truncates toward zero

In this problem, integer division should truncate toward zero.

So use:

```python
int(left / right)
```

Not:

```python
left // right
```

Because `//` floors downward, which behaves differently for negative numbers.

Example:

```python
int(-3 / 2)  # -1
-3 // 2      # -2
```

For LeetCode RPN, `int(-3 / 2)` matches the required behavior.

## 5. Pattern Recognition

### Main pattern

```text
Stack
```

### Trigger: how to recognize this pattern

Think of a stack when the problem says or implies:

```text
Use the most recent previous values
```

In this problem, every operator works on the two most recent numbers before it.

That is the big clue.

Example:

```text
["2", "1", "+", "3", "*"]
```

The `+` uses the latest two numbers:

```text
2 and 1
```

Then the `*` uses the latest result and the next number:

```text
3 and 3
```

So because the newest values are used first, stack is the natural pattern.

### Common signs that suggest stack

Use stack when you see:

```text
- nested expressions
- undo/reverse behavior
- most recent item is used first
- matching brackets
- previous values need to be remembered
- operators applying to recently seen operands
```

### Similar problem types

This same pattern appears in:

```text
- Valid Parentheses
- Min Stack
- Evaluate Reverse Polish Notation
- Daily Temperatures
- Removing adjacent duplicates
- Basic Calculator style problems
```

## 6. Approaches Tried

## Approach 1: Stack Simulation

### Main idea

Use a stack to store numbers.

When we see an operator, pop two numbers, calculate the result, and push it back.

### Step-by-step algorithm

1. Create an empty stack.
2. Loop through every token.
3. If the token is a number:

   * convert it to integer
   * push it into the stack
4. If the token is an operator:

   * pop the right operand
   * pop the left operand
   * calculate `left operator right`
   * push the result back into the stack
5. At the end, the stack has one value.
6. Return that value.

### Pseudocode

```text
stack = []

for token in tokens:
    if token is a number:
        push token into stack as integer

    else:
        right = pop from stack
        left = pop from stack

        if token is "+":
            push left + right

        if token is "-":
            push left - right

        if token is "*":
            push left * right

        if token is "/":
            push int(left / right)

return stack top
```

### Time complexity

```text
O(n)
```

You visit every token once.

### Space complexity

```text
O(n)
```

In the worst case, the stack may store many numbers.

Example:

```text
["1", "2", "3", "4", "+" ...]
```

### Why this approach works

RPN operators always apply to the two most recent available operands.

A stack gives direct access to the most recent values using `pop()`.

So each operator can be evaluated immediately.

### Limitations

There is no major limitation because this is already the expected optimized solution.

The only thing to be careful about is operand order for subtraction and division.

### Is this interview-expected?

Yes.

This is the standard interview-expected solution.

## 7. Optimized Approach

The optimized approach is the stack approach.

There is no better meaningful approach for this problem because every token must be read at least once.

So the best possible time complexity is:

```text
O(n)
```

Your solution reaches that.

The reason it is optimal:

```text
We process each token once.
Each stack operation is O(1).
So total time is O(n).
```

The pattern used is:

```text
Stack
```

Why stack applies:

```text
The operator always needs the latest two numbers.
A stack is designed for last-in, first-out access.
```

## 8. Final Code

You did not ask for final code, so no full code here.

Cleaner standard version would use names like:

```python
right = stack.pop()
left = stack.pop()
```

instead of:

```python
num1 = stack.pop()
num2 = stack.pop()
```

Your code is correct, but `left` and `right` make it easier to explain.

## 9. Interview Script

Here is how you can explain it in an interview:

```text
The expression is in Reverse Polish Notation, so every operator comes after its operands.

I can evaluate it using a stack. I scan the tokens from left to right. Whenever I see a number, I push it onto the stack. Whenever I see an operator, I pop the last two numbers from the stack, apply the operator, and push the result back.

The important detail is operand order. The first popped value is the right operand, and the second popped value is the left operand. This matters for subtraction and division.

For example, if the stack has [5, 2] and the operator is "-", I pop 2 first and 5 second, then calculate 5 - 2.

At the end, the stack contains one value, which is the final answer.

The time complexity is O(n) because I process each token once. The space complexity is O(n) because the stack can hold up to n values in the worst case.
```

## 10. Edge Cases and Dry Run

### Edge cases

```text
Single number only:
["5"] -> 5
```

```text
Negative numbers:
["-4", "2", "/"] -> -2
```

```text
Subtraction order:
["5", "2", "-"] -> 3
```

```text
Division order:
["10", "2", "/"] -> 5
```

```text
Multiple operations:
["1", "2", "+", "3", "*", "4", "-"] -> 5
```

### Dry run

Input:

```text
["1", "2", "+", "3", "*", "4", "-"]
```

Start:

```text
stack = []
```

Token `"1"`:

```text
push 1
stack = [1]
```

Token `"2"`:

```text
push 2
stack = [1, 2]
```

Token `"+"`:

```text
right = 2
left = 1
1 + 2 = 3
stack = [3]
```

Token `"3"`:

```text
push 3
stack = [3, 3]
```

Token `"*"`:

```text
right = 3
left = 3
3 * 3 = 9
stack = [9]
```

Token `"4"`:

```text
push 4
stack = [9, 4]
```

Token `"-"`:

```text
right = 4
left = 9
9 - 4 = 5
stack = [5]
```

Return:

```text
5
```

## 11. Key Takeaways

```text
RPN = stack problem.
```

Remember this rule:

```python
right = stack.pop()
left = stack.pop()
```

Then:

```python
left operator right
```

Especially for:

```text
- and /
```

Use:

```python
int(left / right)
```

for division because the problem wants truncation toward zero.

Your solution is correct, optimized, and interview-expected. The cleaner version is mainly about better variable names, not a different algorithm.
