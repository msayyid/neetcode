from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0  # pointer for children (greed)
        j = 0  # pointer for cookies (size)
        count = 0

        # iterate while both pointers are within bounds
        while i < len(g) and j < len(s):
            # if current cookie can satisfy current child
            if s[j] >= g[i]:
                count += 1      # child is satisfied
                i += 1          # move to next child
                j += 1          # move to next cookie
            else:
                j += 1          # cookie too small, try next larger cookie

        return count
    

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0

        for child in g:
            for i in range(len(s)):
                if s[i] >= child:
                    count += 1
                    s.pop(i)  # remove used cookie
                    break

        return count