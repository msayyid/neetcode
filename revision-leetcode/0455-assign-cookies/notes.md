### 455. Assign Cookies - Notes

---

# 1. Brute Force Approach

### Idea

For each child:

* try all cookies
* assign the first cookie that satisfies them
* make sure that cookie is not reused

---

### Logic

* loop through children
* for each child:

  * loop through cookies
  * if cookie ≥ greed:

    * assign it
    * mark/remove cookie
    * break

---

### Key problem

We must **avoid reusing cookies**

Ways:

* `used[]` array
* or remove cookie (`pop()`)

---

### Complexity

* Time: **O(n * m)**
* Space:

  * `used[]` → **O(m)**
  * `pop()` → **O(1)** extra (but slow operations)

---

### Weakness

* many unnecessary comparisons
* very slow for large inputs

---

### When to think brute force

* no sorting
* no greedy insight yet
* trying all possibilities

---

# 2. Greedy Approach (Optimal)

### Core Idea

> Always satisfy the **least greedy child first** using the **smallest possible cookie**

---

### Why this works

* if smallest cookie can't satisfy smallest child → it can't satisfy anyone
* so we discard it
* ensures optimal usage of resources

---

### Steps

1. Sort both arrays:

   * `g` (greed)
   * `s` (cookies)

2. Use two pointers:

   * `i` → children
   * `j` → cookies

3. While both pointers valid:

   * if `s[j] >= g[i]`:

     * assign cookie
     * move both pointers
   * else:

     * cookie too small → move `j`

---

### Complexity

* Time:

  * Sorting → **O(n log n + m log m)**
  * Traversal → **O(n + m)**
  * Total → **O(n log n + m log m)**

* Space:

  * Python sort → **O(n + m)**

---

### Key Insight

> If a cookie cannot satisfy the least greedy child, it is useless for all remaining children.

---

### Common Mistakes

❌ Matching `g[i]` with `s[i]` directly
→ loses flexibility

❌ Moving child pointer when cookie too small
→ wrong (child still unsatisfied)

❌ Thinking sorting is O(1) space
→ not true in Python

---

### Why Greedy > Brute Force

| Aspect     | Brute Force | Greedy       |
| ---------- | ----------- | ------------ |
| Time       | O(n * m)    | O(n log n)   |
| Efficiency | Poor        | Optimal      |
| Idea       | Try all     | Smart choice |

---

# Final Takeaway

* Brute force = try everything
* Greedy = **sort + assign optimally**

---

Remember one line:

> "Give the smallest sufficient cookie to the least greedy child"
