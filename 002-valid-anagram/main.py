# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         # for i in range(len(s)):
#         return True if sorted(s) == sorted(t) else False

# this would be a brute force (cheating approach), and it costs us a lot
# because time here is 2nlogn because of the sorted() function, 
# and space is O1 as we're not creating anymore arrays not expanding

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # my_map1 = {0} * len(s)
        if len(s) != len(t):
            return False
        # # for i in range(len(s)):
        # return True if sorted(s) == sorted(t) else False

        my_map1 = dict()
        for i in range(len(s)):
            # check if the key exists, if not assign new one, if does increment the value/decrement the value
            if s[i] not in my_map1:
                my_map1[s[i]] = 1
            # my_map2[t[i]] += 1
            else: my_map1[s[i]] += 1
        for i in range(len(t)):
            if t[i] in my_map1:
                my_map1[t[i]] -= 1
            else: return False
        
        print(my_map1)
        # print(all(my_map1.values()))
        return all(v == 0 for v in my_map1.values())

sol = Solution()
s = "racecar"
t = "racecar"
print(sol.isAnagram(s, t))

s = "jar"
t = "jam"
print(sol.isAnagram(s, t))


# Problem: given two strings s and t, return true if t is an anagram of s.

# Approach 1 (brute force): just sort both strings and compare. 
# Simple but costs O(n log n) time because of sorting. Space is O(1).

# Approach 2 (hashmap — optimal): first check if lengths are the same, 
# if not return false immediately. Then create an empty map. 
# Loop through s — if the character isn't in the map, create it and assign 1, 
# if it is, increment its value. Then loop through t — if the character isn't in the map 
# at all, return false (different letter), if it is, decrement its value. 
# At the end, if all values in the map are 0 it's an anagram, otherwise it's not.

# A mistake I made: I tried to initialize the map as {0} * len(s) 
# which is actually creating a set, not a dict. The fix was to just 
# create an empty dict with dict() and then before incrementing, 
# check if the key exists first — if not, assign it 1, if yes, increment it.

# The final check — all(): all(v == 0 for v in my_map1.values()) is just a short clean 
# version of looping through all values and returning false the moment any value isn't 0, 
# and true if they all are. It also short-circuits, meaning it stops as soon as 
# it finds a non-zero value, just like a manual loop would.

# The key insight is: we're not storing duplicate keys, 
# just incrementing their count, so the map can never 
# grow beyond 26 keys (alphabet letters). That's why space is O(1). 
# Time is O(n) because we loop through the strings once each, 
# and we can't do better than that since we must look at every character.
# This is optimal — you can't beat O(n) time and O(1) space for this problem.