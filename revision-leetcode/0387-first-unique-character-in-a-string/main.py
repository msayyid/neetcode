class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            is_unique = True
            for j in range(len(s)):
                if i != j and s[j] == s[i]:
                    is_unique = False
                    break
            if is_unique:
                return i
        return -1
    

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1



class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
    
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1

        for i, c in enumerate(s):
            if count[ord(c) - ord("a")] == 1:
                return i
        return -1