**Design HashMap**

---

**Solution 1 — Direct Address Table**

*Approach:* Since keys are bounded (`0 <= key <= 1,000,000`), I used the key itself as the index into a pre-allocated array of size `1,000,001`. The value at each index IS the value for that key. No hashing needed.

*Default sentinel:* Initialized every slot to `-1` to mean "no mapping exists". This works safely because `-1` is outside the valid value range (`0 <= value <= 1,000,000`) — so `-1` can never be confused with a real value.

*Operations:*
- `put(key, value)` → `arr[key] = value`
- `get(key)` → `return arr[key]` (returns `-1` if never set)
- `remove(key)` → `arr[key] = -1`

*Time:* O(1) for all operations — direct index access.

*Space:* O(1,000,001) — always, regardless of how many keys are actually inserted. Fixed cost.

*Key insight:* When key ranges are small and bounded, you can skip hashing entirely and use the key as a direct array index. This is called a **direct address table**.

---

**Solution 2 — Chaining HashMap**

*Approach:* Implemented a real HashMap using **chaining** for collision handling. The map has 1000 buckets, keys are mapped to buckets via `key % 1000`. Each bucket holds the head of a linked list of `Node(key, value, next)` objects.

*Why 1000 buckets:* No longer need 1,000,001 slots. Multiple keys can share a bucket via chaining, so a much smaller array works.

*Node class:*
```python
class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
```
Holds `key`, `value`, and `next` (defaulted to `None`). The key lives inside the node — the bucket index is NOT the key.

*put:*
- Hash key to get bucket index
- If bucket is `None` → create new Node directly
- Else walk the list: if key matches → update value and return; if end of list reached → append new Node and return

*get:*
- Hash key to get bucket, walk the list looking for matching key, return its value or `-1` if not found

*remove:*
- Track a `prev` pointer (starts as `None`) alongside `current`
- Walk the list until key is found
- If `prev is None` (removing the head) → `self.my_map[index] = current.next` — make the bucket point to the next node
- If `prev` exists (middle/tail) → `prev.next = current.next` — skip over the current node
- `prev = current` and `current = current.next` happen every iteration when key doesn't match

*Why `prev` starts as `None`:* At the start we're at the head and there's no previous node. `None` signals "we're still at the head" which triggers the special head-removal case.

---

**Mistakes made in Solution 2:**
- Forgot `self.next = next` in Node — without it `current.next` throws an error
- Tried to `for` loop over a Node — linked lists use `while current is not None` with a `current` pointer
- Mixed up `current.value` and `current.next` when attaching new nodes
- Misplaced `return` statements inside wrong blocks
- Set `prev = current` initially instead of `prev = None`

---

**Time & Space — Solution 2:**

*Time:* O(1) average, O(N) worst case for all three operations.
- Average is O(1) because with a good hash function, N keys spread evenly across 1000 buckets, so each bucket has roughly N/1000 nodes — a small constant number regardless of total keys
- Worst case is O(N) when all keys hash to the same bucket, creating one giant linked list

*Space:* O(N) where N is number of inserted keys.
- Each key creates exactly one node, living in exactly one bucket — so total nodes = N
- The 1000 buckets themselves are a fixed constant O(1000) = O(1)
- Total: O(1000 + N) = O(N)
- Note: B * N would only apply if every bucket had N nodes each — impossible since you only have N nodes total to distribute

---

**Solution 2 vs Solution 1:**
- Solution 2 is better in space for sparse insertions — it only uses space proportional to actual inserted keys rather than always allocating 1,000,001 slots
- Solution 2 is a real HashMap — it handles collisions, stores key inside the node, and uses a hash function