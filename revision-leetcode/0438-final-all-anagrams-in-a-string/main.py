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

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        result = []
        if k > len(s):
            return result
        count1, count2 = [0] * 26, [0] * 26
        for i in range(k):
            count1[ord(p[i]) - ord("a")] += 1
            count2[ord(s[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1

        l = 0
        for r in range(k, len(s)):
            if matches == 26:
                result.append(l)

            # adding the current element
            index = ord(s[r]) - ord("a")
            count2[index] += 1
            if count2[index] == count1[index]:
                matches += 1
            elif count2[index] - 1 == count1[index]:
                matches -= 1

            # removing/decremting the element at l pointer
            index = ord(s[l]) - ord("a")
            count2[index] -= 1
            if count2[index] == count1[index]:
                matches += 1
            elif count2[index] + 1 == count1[index]:
                matches -= 1

            l += 1

        if matches == 26:
            result.append(l)
        return result