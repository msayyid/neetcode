class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for c in s:
            valid = False
            if '0' <= c and c <='9':
                valid = True

            elif 'a' <= c and c <= 'z':
                valid = True

            elif 'A' <= c and c <= 'Z':
                valid = True
                c = chr(ord(c) + 32)
            
            if valid:
                s2 += c

        l = 0
        r = len(s2) - 1
        while l < r:
            if s2[l] != s2[r]:
                return False

            l += 1
            r -= 1

        return True
    

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.isValid(s[l]):
                l += 1
            
            while l < r and not self.isValid(s[r]):
                r -= 1

            if l < r:
                c1 = self.toLower(s[l])
                c2 = self.toLower(s[r])

                if c1 != c2: 
                    return False

                l += 1
                r -= 1
        return True



    def isValid(self, c):
        return ('0' <= c and c <= '9') or ('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z')

    def toLower(self, c):
        if "A" <= c <= "Z":
            return chr(ord(c) + 32)
        return c