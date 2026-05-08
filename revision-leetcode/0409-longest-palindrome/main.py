class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        length = 0
        has_odd = False
        
        for val in count.values():
            if val % 2 == 0:
                length += val
            else:
                length += val - 1
                has_odd = True

        if has_odd:
            length += 1
        
        return length