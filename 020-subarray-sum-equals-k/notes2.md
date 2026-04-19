# 🔵 Problem

Count number of subarrays with sum = `k`

---

# 🟡 Approach 1 - Prefix Array + HashMap

## Idea

* Build prefix array:

  ```
  prefix[i] = sum(nums[0..i])
  ```

* For each `i`, we want:

  ```
  prefix[i] - prefix[j] = k
  ```

Rearrange:

```
prefix[j] = prefix[i] - k
```

---

## Algorithm

1. Build prefix array
2. Use hashmap:

   ```
   {prefix_value : frequency}
   ```
3. For each prefix:

   * compute `complement = prefix[i] - k`
   * if in map → add frequency to count
   * then store current prefix in map

---

## Time & Space

* Time: O(n)
* Space: O(n) (prefix + map)

---

# 🟢 Approach 2 - Optimized (Running Prefix)

## Idea

Same logic, but no prefix array.

Instead:

```
prefix += nums[i]
```

Everything else stays the same.

---

## Time & Space

* Time: O(n)
* Space: O(n) (map only)

---

# 🔴 WHERE YOU WERE STUCK (IMPORTANT)

## 1. “Why are we adding full frequency?”

You were thinking:

> “Are we overcounting if we add `map[complement]`?”

### ✅ Clarification

Each prefix occurrence = **different index**

So:

```
map[complement] = 3
```

Means:

* there are **3 different starting points**
* each forms a **different subarray**

So:

```
count += 3   ✅ correct
```

---

## 🔑 Key insight

> We are counting **subarrays**, not unique sums.

Different start index → different subarray → must count all

---

## 2. Complement confusion

You were unsure:

> “Why prefix - k?”

### ✅ Explanation

We want:

```
subarray_sum = k
```

Which is:

```
prefix[i] - prefix[j] = k
```

Rearrange:

```
prefix[j] = prefix[i] - k
```

So:

> At index `i`, we search for a **previous prefix** equal to `prefix - k`

---

## 🔑 Memory shortcut

> “Current prefix - old prefix = k
> → find old prefix = prefix - k”

---

## 3. Why map stores frequency

You asked:

> “Why not just store existence?”

Because:

Same prefix can appear multiple times:

Example:

```
prefix = 0 appears 3 times
```

Each occurrence = different start → multiple valid subarrays

So we must store:

```
frequency, not just presence
```

---

## 4. Order inside loop (critical)

Correct order:

```
1. update prefix
2. check complement → update count
3. insert prefix into map
```

Why?

> Map must only contain **previous prefixes**, not current one

---

## 5. Why `{0:1}` is needed

Handles subarrays starting at index 0

Example:

```
prefix[i] == k
```

Then:

```
complement = 0
```

So we need:

```
map[0] = 1
```

---

# 🧠 Final Mental Model

At each index:

> “How many previous prefixes can I pair with this one to make sum k?”

Answer:

```
map[prefix - k]
```

---

# ⚡ One-line summary

> Prefix sum + hashmap = count how many valid starting points exist for each ending index

---

# 🔥 Common mistakes (your exact ones)

* ❌ Thinking `+1` instead of `+frequency`
* ❌ Not understanding why complement works
* ❌ Thinking duplicates cause overcounting
  → they don’t, they represent valid multiple subarrays
* ❌ Forgetting `{0:1}`
* ❌ Wrong order (inserting before checking)
