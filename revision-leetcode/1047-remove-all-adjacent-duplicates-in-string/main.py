class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()

            else:
                stack.append(c)
        return "".join(stack)
    

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        for i in  range(1, len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
            
        return "".join(stack)