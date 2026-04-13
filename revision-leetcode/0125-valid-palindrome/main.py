class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            elif s[l].isalnum() and not s[r].isalnum():
                r -= 1
            
            elif not s[l].isalnum() and s[r].isalnum():
                l += 1
            else:
                l += 1
                r -= 1
        return True
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            