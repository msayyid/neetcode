from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        res = []
        count1 = [0] * 26
        count2 = [0] * 26
        for c in p:
            count1[ord(c) - ord("a")] += 1

        for c in s[:k]:
            count2[ord(c) - ord("a")] += 1
        
        if count1 == count2:
            res.append(0)
        
        for r in range(k, len(s)):
            count2[ord(s[r]) - ord('a')] += 1
            count2[ord(s[r - k]) - ord("a")] -= 1
            if count1 == count2:
                res.append(r - k + 1)
        return res

