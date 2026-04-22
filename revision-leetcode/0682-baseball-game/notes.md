# Baseball Game - Notes

## Core Idea

We simulate the game using a **stack**.

Why stack?

* We always care about the **most recent scores**
* Operations depend on **last one or last two values**
* Stack naturally supports:

  * add (append)
  * remove last (pop)
  * access last elements

---

## Operations Breakdown

We process each operation one by one:

### 1. Number (e.g. `"5"`, `"-2"`)

* Convert to int
* Push to stack

```
stack.append(int(o))
```

---

### 2. `"+"` → sum of last two scores

* Take last two elements
* Add them
* Push result

```
stack.append(stack[-1] + stack[-2])
```

---

### 3. `"D"` → double last score

* Take last element
* Multiply by 2
* Push result

```
stack.append(stack[-1] * 2)
```

---

### 4. `"C"` → remove last score

* Pop last element

```
stack.pop()
```

---

## Final Step

After processing all operations:

```
return sum(stack)
```

---

## Example Walkthrough

Input:

```
["5","2","C","D","+"]
```

Step-by-step:

* "5" → [5]
* "2" → [5, 2]
* "C" → [5]
* "D" → [5, 10]
* "+" → [5, 10, 15]

Final sum:

```
5 + 10 + 15 = 30
```

---

## Time Complexity

* Loop through operations → O(n)
* Each operation → O(1)
* Final sum → O(n)

**Total: O(n)**

---

## Space Complexity

* Stack can grow up to size n

**Space: O(n)**

---

## Why Stack Works Perfectly

Because:

* `"C"` removes the most recent → stack pop
* `"D"` uses last → stack[-1]
* `"+"` uses last two → stack[-1], stack[-2]

This is exactly **LIFO behavior**

---

## Mistakes to Avoid

### 1. Overchecking numeric values

❌ Using `try/except` or `float()`

* Not needed
* Slower
* Overcomplicates code

---

### 2. Forgetting order in `"+"`

Make sure:

```
last + second_last
```

Not reversed (though same result, concept matters)

---

### 3. Not handling negative numbers

* `" -2 "` is valid
* `int(o)` handles it correctly

---

### 4. Accessing empty stack

* In this problem, constraints guarantee safety
* But in real-world → check length

---

## Key Insight (Important)

This is a **simulation problem**, not math.

You are NOT calculating directly.
You are **building the history step-by-step**.

---

## Pattern Recognition

This problem teaches:

* Stack simulation
* Handling sequential operations
* Using previous state efficiently

Similar problems:

* Valid Parentheses
* Remove Adjacent Duplicates
* Stack-based evaluations

---

## Interview Takeaway

If you see:

* “last element”
* “previous two values”
* “undo last action”

→ Think **STACK immediately**
