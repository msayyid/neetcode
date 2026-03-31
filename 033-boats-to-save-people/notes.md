**Boats to Save People — Two Pointers + Sorting**

**The Idea**

Sort the array, then use two pointers (lightest and heaviest). The heaviest person is "picky" — only a few people are light enough to share their boat. The lightest person is "easy" — almost anyone can share their boat. So always try to help the picky person first by pairing them with the lightest available. If even the lightest can't join them, nobody can, and the heaviest goes alone.

**Pseudocode — Approach 1 (Two Pointer + Sort)**
```
sort people
l = 0, r = len - 1, count = 0

while l <= r:
    if people[l] + people[r] > limit:
        # heaviest goes alone
        r -= 1
        count += 1
    else:
        # pair them together
        l += 1
        r -= 1
        count += 1

return count
```

**Pseudocode — Approach 2 (Two Pointer + Counting Sort)**
```
# Step 1: counting sort
m = max(people)
count = [0] * (m + 1)        # index represents weight, value represents frequency
for p in people:
    count[p] += 1             # e.g. count[3] = 2 means 2 people weigh 3

# Step 2: reconstruct sorted people array in place
idx = 0, i = 1
while idx < len(people):
    while count[i] == 0:      # skip weights that don't appear
        i += 1
    people[idx] = i           # place weight i into people
    count[i] -= 1             # one less person of weight i
    idx += 1
# people is now sorted in O(n + m) instead of O(n log n)

# Step 3: same two pointer logic as approach 1
res, l, r = 0, 0, len(people) - 1
while l <= r:
    remain = limit - people[r]   # same as checking people[l] + people[r] <= limit
    r -= 1
    res += 1
    if l <= r and remain >= people[l]:  # lightest can join heaviest
        l += 1

return res
```

**Mistakes I made**
- Had too many conditions (`== limit`, `people[l] == limit`, `people[r] == limit`) — all unnecessary, only two cases matter: `> limit` or `<= limit`
- When `people[l] + people[r] > limit`, I forgot to count that boat — the heavy person still needs one even going alone
- Used `while l < r` which missed the last person when `l == r`. Fixed by changing to `while l <= r` which handles it inside the loop cleanly

**New things I learned**
- Two pointer on a sorted array can greedily guarantee all combinations are checked — you don't need to check every pair explicitly
- Counting sort works by using the **weight as the index** of a count array, counting frequencies, then reconstructing the sorted array by walking through the count array. This avoids comparison-based sorting entirely
- `remain = limit - people[r]` and `people[l] + people[r] <= limit` are mathematically identical — just rearranged
- In approach 2, `r` is always decremented and `res` always incremented first (heaviest always gets a boat), then we check if the lightest can join — slightly different structure but same logic as approach 1

**Why greedy works here**
- If the heaviest can't pair with the lightest, they can't pair with anyone — so they must go alone
- If the lightest CAN pair with the heaviest, there's no reason to save them for later — the lightest can always find another partner, but the heaviest might not

**Complexities**

| Solution | Time | Space | When better |
|---|---|---|---|
| Two pointer + sort | O(n log n) | O(1) | when m (max weight) is very large |
| Two pointer + counting sort | O(n + m) | O(m) | when n is large but m is small/bounded |

where m = max weight in people. In this problem m <= 30,000 so counting sort is a valid and faster alternative, but trades O(1) space for O(m) space.
