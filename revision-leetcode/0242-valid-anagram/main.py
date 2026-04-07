class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        my_map = dict()
        for i in range(len(s)):
            my_map[s[i]] = my_map.get(s[i], 0) + 1
        
        for i in range(len(t)):
            if t[i] in my_map:
                my_map[t[i]] -= 1
            else: return False
        
        for k, v in my_map.items():
            if v != 0:
                return False
        return True
        

        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        my_map = dict()
        for i in range(len(s)):
            my_map[s[i]] = my_map.get(s[i], 0) + 1
            my_map[t[i]] = my_map.get(t[i], 0) - 1
        
        for val in my_map.values():
            if val != 0:
                return False
        return True
        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            # index = 26 - (ord("z") - ord(s[i])) - 1
            index = ord(s[i]) - ord("a")
            count[index] += 1
        
        for i in range(len(t)):
            # index = 26 - (ord("z") - ord(t[i])) - 1
            index = ord(s[i]) - ord("a") # better, cleaner
            count[index] -= 1
        
        for num in count:
            if num != 0:
                return False

        return True
        

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            index_s = ord(s[i]) - ord("a")
            index_t = ord(t[i]) - ord("a")
            count[index_s] += 1
            count[index_t] -= 1
    
        
        for num in count:
            if num != 0:
                return False

        return True
        