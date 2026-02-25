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

# Group Anagrams — Quick Reference
# Two approaches, same idea: use a hashmap to group strings by a shared key.
# Approach 1 — Sort as key: "".join(sorted(s)) → O(m · k log k) time
# Approach 2 — Count as key: tuple([0] * 26) incremented with ord(c) - ord('a') → O(m · k) time — removes the log k by avoiding sort
# Both: O(m · k) space — you store every character of every string
# Traps to remember:

# "".join(sorted(s)) not sorted(s).join("")
# [].append(s) returns None — use [s]
# Lists can't be dict keys — convert to tuple
# Build the full key before using it in the map

# Optimized solution:
# pythondef groupAnagrams(strs):
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