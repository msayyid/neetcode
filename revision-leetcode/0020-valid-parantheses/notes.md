# Valid Parentheses - Notes

## Core idea

We need to check if brackets are:

* correctly matched
* in the correct order

Key observation:

> The **last opened bracket must be the first one to close** → this is a **stack (LIFO)** problem.

---

# Approach 1 - Opening → Closing Map (your original)

## Idea

* push opening brackets onto stack
* when we see a closing bracket:

  * check if it matches the **top of the stack**
  * if yes → pop
  * if not → return False

---

## Logic

* if char is opening → push
* if char is closing:

  * if stack empty → ❌ invalid
  * if top does not match → ❌ invalid
  * else → pop

---

## Important part (where confusion happens)

```python
if stack and s[i] == brackets[stack[-1]]:
```

Meaning:

* stack must not be empty
* current closing must match the last opening

---

## Final check

```python
if stack: return False
```

Why:

* leftover openings → invalid

Example:

```
"(("
```

---

## Common mistake (your earlier issue)

❌ comparing with previous element:

```python
s[i - 1]
```

✔ correct:

```python
stack[-1]
```

Because we care about **last unmatched opening**, not previous character.

---

## Complexity

* Time: O(n)
* Space: O(n)

---

# Approach 2 - One Map (Closing → Opening)

## Idea

Flip thinking:

> “When I see a closing bracket, what opening should be on top of the stack?”

---

## Mapping

```python
")" → "("
"]" → "["
"}" → "{"
```

---

## Logic

* if char is closing (in map):

  * if stack empty → ❌
  * if top != expected → ❌
  * else → pop
* else:

  * push (opening)

---

## Key line

```python
if not stack or stack[-1] != mapping[char]:
    return False
```

---

## Why this is cleaner

* only one map
* no separate opening/closing sets
* fewer checks

---

## Mental model

> “Closing bracket tells me what opening I expect.”

---

## Final check

```python
return not stack
```

---

# Key Differences

| Approach | Mapping           | Check direction                       |
| -------- | ----------------- | ------------------------------------- |
| 1        | opening → closing | compare closing with `brackets[top]`  |
| 2        | closing → opening | compare `top` with `mapping[closing]` |

---

# Edge Cases to remember

1. Starts with closing:

```
")("
```

→ invalid

2. Mismatch:

```
"(]"
```

→ invalid

3. Wrong order:

```
"([)]"
```

→ invalid

4. Leftover openings:

```
"(("
```

→ invalid

---

# Final takeaway

* Use stack for order
* Always compare with **top of stack**
* Never compare with previous character
* Stack must be empty at the end
