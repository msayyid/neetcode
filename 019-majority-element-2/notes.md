**Majority Element II — Notes**

*Key insight:* At most **2 elements** can appear more than n/3 times. If three elements each appeared more than n/3 times, their total would exceed n — impossible.

---

*Solution 1 — Hashmap (O(n) time, O(1) space):*

**Phase 1 — Build and trim the map:**

For each element, increment its count in the map. After each increment, check if the map has grown beyond 2 keys. If it has, trim it — decrement every value by 1 and remove any key whose value hits 0. Use a `new_count` dict during trimming instead of modifying the original map — modifying a dict while iterating over it breaks the loop.

After trimming, the map always has at most 2 keys. These are the 2 surviving candidates — the ones that weren't voted out.

**Why we can't trust the map values for verification:**

The values in the map got decremented during trimming, so they reflect net votes not true frequencies. Same problem as Boyer-Moore phase 1 counts.

**Phase 2 — Verify candidates:**

For each key remaining in the map, use `nums.count(key)` to get its actual frequency in the original array. If it's `> n//3`, add it to the result.

---

*Solution 2 — Boyer-Moore Voting (O(n) time, O(1) space):*

**Phase 1 — Find candidates (voting):**

Battle royale analogy. Two standing zones, each holding a candidate with a strength count. For each new element:
- Matches cand1 → cand1 gains +1 strength
- Matches cand2 → cand2 gains +1 strength
- Matches neither → both lose -1 strength
- If either strength hits 0 → replaced by new element with strength 1

Use `None` initialisation so first two distinct elements get naturally assigned — avoids index crashes on single element arrays.

**Why we can't trust phase 1 counts for verification:**

During voting, counts get decremented every time two different elements cancel each other out. So by the end, they reflect net votes not true frequencies. For example, if `5` appears 4 times but got cancelled twice along the way, count1 might be 2 — which could fail the `> n//3` check even though 5 is a valid winner. So we reset counts to 0 and do a clean second pass.

**Phase 2 — Verify candidates:**

Reset both counts to 0. Loop through nums counting actual occurrences of each candidate. Only then check `> n//3`.

---

*Mistakes made:*
- Tracked candidates as indices instead of values — caused clashing bugs when both candidates got replaced simultaneously at the same index
- Trusted phase 1 counts for verification — they're net votes not true frequencies
- Initialised with `nums[0]`, `nums[1]` — crashes on single element arrays
- Used `=` instead of `==` in a condition

*New things learned:*
- `defaultdict(int)` removes need for `.get()` checks
- `count1 = count2 = 0` — clean way to reset multiple variables at once
- Never modify a dict while iterating over it — use a new dict instead
- Boyer-Moore extended to 2 candidates for n/3 majority (classic Boyer-Moore does 1 candidate for n/2 majority)

*Complexities:* Both solutions O(n) time, O(1) space.

---

**Pseudocode — Solution 1 (Hashmap with trimming):**

```
# at most 2 winners possible due to n/3 constraint

# PHASE 1 - build and trim the map
count = defaultdict(int)

for each num:
    count[num] += 1            # increment frequency

    if len(count) <= 2:        # at most 2 candidates, nothing to trim
        continue

    # map grew to 3 keys, trim it
    new_count = defaultdict(int)
    for each (key, val) in count:
        if val > 1:            # after decrement, still alive
            new_count[key] = val - 1
    count = new_count          # replace original with trimmed version
                               # (never modify dict while iterating it)

# PHASE 2 - verify (map values are net votes, not true frequencies)
result = []
for each candidate in count:
    if nums.count(candidate) > n//3:
        result.append(candidate)
return result
```

---

**Pseudocode — Solution 2 (Boyer-Moore Voting):**

```
# at most 2 winners possible due to n/3 constraint

# PHASE 1 - find candidates via battle royale
cand1, cand2 = None, None      # None avoids crashes on short arrays
count1, count2 = 0, 0

for each num:
    if num == cand1         → count1 += 1        # ally found
    elif num == cand2       → count2 += 1        # ally found
    elif count1 == 0        → cand1 = num, count1 = 1   # empty slot
    elif count2 == 0        → cand2 = num, count2 = 1   # empty slot
    else                    → count1 -= 1, count2 -= 1  # mutual cancel

# PHASE 2 - get real counts (phase 1 counts are net votes, not true frequencies)
count1 = count2 = 0
for each num:
    if num == cand1 → count1 += 1
    elif num == cand2 → count2 += 1

# PHASE 3 - verify
if count1 > n//3 → add cand1 to result
if count2 > n//3 → add cand2 to result
return result
```