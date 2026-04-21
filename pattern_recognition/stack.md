# 🔥 How to Recognize This Pattern Instantly (Stack Cancellation Pattern)

## 🔑 The Trigger Words

When you see problems with phrases like:

* “remove adjacent”
* “cancel out”
* “pair up and remove”
* “undo previous”
* “valid sequence”
* “simplify string/expression”

👉 **Your brain should immediately think: STACK**

---

## 🧠 The Mental Model

Ask yourself:

> “Do elements get removed based on the most recent previous element?”

If YES → **stack**

Because:

* Stack = LIFO (Last In, First Out)
* Exactly matches “check last thing added”

---

## ⚡ Core Template (VERY IMPORTANT)

Memorize this:

```python
stack = []

for x in input:
    if stack and stack[-1] matches x:
        stack.pop()
    else:
        stack.append(x)

return result_from_stack
```

---

## 🧩 Apply to This Problem

Condition:

```python
stack[-1] == current_char
```

Action:

* Equal → remove (pop)
* Not equal → keep (push)

---

## 🔄 Other Problems With SAME Pattern

### 1. Valid Parentheses

Condition:

```python
stack[-1] == matching_open_bracket
```

---

### 2. Backspace String Compare

Condition:

```python
char == '#'
```

Action:

* Pop instead of append

---

### 3. Remove K Adjacent Duplicates

Condition:

* Count reaches k → remove group

---

### 4. Simplify Path (Unix)

Condition:

* `".."` → pop previous directory

---

## 🚨 Recognition Shortcut (Interview Trick)

Ask:

> “Does the current element interact with the previous one only?”

If YES → **stack**

---

## ❌ When NOT to use stack

If:

* You need global comparison (not just last element)
* You care about frequencies overall
* Order doesn’t matter

→ then NOT stack

---

## 🧠 Your Exact Thought Process (what interviewer wants)

Say this out loud:

> “Since removals only depend on the most recent character, I can simulate the process using a stack where I compare the current character with the top.”

That’s a **10/10 explanation line**.

---

## 🎯 Final Cheat Rule

> “If elements cancel each other based on adjacency or recent history → use stack”