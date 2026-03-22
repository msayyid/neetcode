class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        # def is_palindrome(s, l, r): # this is a On On with extra space solution
        #     return s[l:r+1] == s[l:r+1][::-1]
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                result = is_palindrome(s, l + 1, r) or is_palindrome(s, l, r - 1)
                return result
            l, r = l + 1, r - 1
        return True