class Solution:
    def isPalindrome(self, s: str) -> bool:
        # numbers = "01234567890"
        # alph_nums = "abcdefghijklmnopqrstuvwxyz01234567890"
        alph_nums = {
                'a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z',
                '0','1','2','3','4','5','6','7','8','9','0'}
        s_only = ""
        for i in range(len(s)):
            if s[i].lower() in alph_nums:
                s_only += s[i].lower()
        s_back = ""
        for i in range(len(s_only) - 1, -1, -1):
            s_back += s_only[i]
        
        if s_back == s_only:
            return True
        return False