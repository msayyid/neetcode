class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # print("this is l:", l)
                # print("this is r:", r)
                result = (is_palindrome(s, l + 1, r) or is_palindrome(s, l, r-1))
                return result
            l += 1
            r -= 1
        return True
        

sol = Solution()

print(sol.validPalindrome("abbda"))      # True
print(sol.validPalindrome("aba"))      # True
print(sol.validPalindrome("abca"))     # True
print(sol.validPalindrome("abc"))      # False
print(sol.validPalindrome("deeee"))    # True
print(sol.validPalindrome("racecar"))  # True
print(sol.validPalindrome("raceacar")) # True
print(sol.validPalindrome("abcdef"))   # False
print(sol.validPalindrome("a"))        # True
print(sol.validPalindrome(""))         # True
print(sol.validPalindrome("ab"))       # True