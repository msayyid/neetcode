# def groupAnagrams(strs):
#         # brute force approach
#         anagram_list = []
#         final_list = []
#         my_map = dict()
#         for i in range(len(strs)):
#             key = "".join(sorted(strs[i]))
#             # my_map[key] = [strs[i]]
#             if key in my_map:
#                 my_map[key].append(strs[i])
#             else:
#                 my_map[key] = [strs[i]]
    
#         # print(my_map)
#         return list(my_map.values())



def groupAnagrams(strs):
    res = {}

    for s in strs:
        count = [0] * 26 
        for c in s:
            count[ord(c) - ord("a")] += 1
        if tuple(count) not in res:
            res[tuple(count)] = [s]
        else: res[tuple(count)].append(s)
    return list(res.values())
        


strs = ["act","pots","tops","cat","stop","hat"]      
print(groupAnagrams(strs))

# print(str(["s", "h"]))



# **Group Anagrams — Session Notes**

# **Problem:** Given a list of strings, group all anagrams together. Anagrams are strings that contain the exact same characters, just in different order (e.g. "act" and "cat").

# ---

# **First Approach — Sorting (O(m · k log k) time / O(m · k) space)**

# **Core idea:** If you sort the characters of any anagram, they all produce the same string. So `"act"`, `"cat"` both become `"act"`
#  when sorted — that sorted string can be used as a dictionary key to group them.

# **Mistakes I made:**
# - Initially tried to count how many times each string appears — but `"act"` and `"cat"` 
# are different strings so they'd never match, counting occurrences is useless here
# - Used `sorted(strs[i]).join("")` — wrong! `join` lives on the string not the list. Correct syntax is `"".join(sorted(strs[i]))`
# - Used `sorted[strs[i]]` with square brackets — `sorted` is a function, always needs `()`
# - Tried storing a count as the map value instead of a list of strings — you lose the original words this way, you need to store the actual strings
# - Wrote `my_map[key] = [strs[i]]` before the `if/else`, which overwrote the existing list every iteration — the `if/else` should do all the work
# - Wrote `[].append(s)` which returns `None` — always write `[s]` directly to create a list with a first element
# - Used `final_list.append(anagram_list.append(...))` — `list.append()` returns `None`, so nesting them fills your list with `None`s

# **What the map looks like:**
# ```
# "act" -> ["act", "cat"]
# "opst" -> ["pots", "tops", "stop"]
# "aht" -> ["hat"]
# ```

# **Final working solution:**
# ```python
# def groupAnagrams(strs):
#     my_map = {}
#     for i in range(len(strs)):
#         key = "".join(sorted(strs[i]))
#         if key in my_map:
#             my_map[key].append(strs[i])
#         else:
#             my_map[key] = [strs[i]]
#     return list(my_map.values())
# ```

# **Complexities:**
# - Time: **O(m · k log k)** — `m` strings, each sorted in `k log k`
# - Space: **O(m · k)** — every character of every string is stored in the map values. It's not just O(m) because each string has length `k`, so total characters = m × k

# ---

# **Optimized Approach — Character Count (O(m · k) time / O(m · k) space)**

# **Core idea:** Instead of sorting, count how many times each letter appears. Represent this as an array of 26 zeros (one slot per letter a-z). Any two anagrams will produce the exact same count array, so use that as the key.

# Example:
# ```
# "act" -> [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
# "cat" -> [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]  # identical!
# ```

# **New things I learned:**
# - `ord(c) - ord('a')` gives you the index of a letter in the alphabet — `ord('a')=97`, `ord('b')=98` etc, so subtracting `ord('a')` gives 0 for 'a', 1 for 'b', and so on
# - Lists cannot be dictionary keys (they are mutable/unhashable) — you must convert to a `tuple` first: `tuple(count)`
# - Tuples CAN be dictionary keys because they are immutable

# **Mistakes I made:**
# - Tried to update `res` inside the inner loop — you must finish building the full count array first, then use it as a key after the inner loop
# - Used `ord[c]` with square brackets instead of `ord(c)` — `ord` is a function
# - Flipped the `if/else` condition and also tried accessing `res[count]` before checking if the key exists, which crashes

# **Final working solution:**
# ```python
# def groupAnagrams(strs):
#     res = {}
#     for s in strs:
#         count = [0] * 26
#         for c in s:
#             count[ord(c) - ord('a')] += 1
#         if tuple(count) not in res:
#             res[tuple(count)] = [s]
#         else:
#             res[tuple(count)].append(s)
#     return list(res.values())
# ```

# **Complexities:**
# - Time: **O(m · k)** — `m` strings, inner loop runs `k` times per string, no sorting so no `log k`
# - Space: **O(m · k)** — keys cost O(26 · m) = O(m) since each key is fixed size 26, but values store all original strings costing O(m · k), which dominates

# **The real optimization:** We removed the `log k` factor from time complexity. Space stayed the same because we still store every string.

# ---

# **Key takeaways:**
# - When grouping things, think about what shared property can be a dictionary key
# - `list.append()` always returns `None` — never nest it
# - Lists can't be dict keys, tuples can
# - `"".join(sorted(s))` not `sorted(s).join("")`
# - Build your data structure completely before using it as a key