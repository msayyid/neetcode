class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        opening = {"(", "[", "{"}
        closing = {")", "]", "}"}
        stack = []
        for i in range(len(s)):
            if s[i] in opening: # if we are in a opening paranthesis we can append
                stack.append(s[i])
            elif s[i] in closing: # if we are in a closing paranthesis 
                # we check if our stack is not empty to pop from it
                # and whether the current closing paranthesis is equal to the top of the stack
                # because top of the stack is the last opening paranthesis we have had
                # which is a previous element if it exists in the input
                if len(stack) > 0 and s[i] == brackets[stack[-1]]:
                    # if all the above is true we pop
                    stack.pop()
                else:
                    # else meaning opening and closing brackets do not match
                    # or stack is empty (does this not breakt eh logic in here?)
                    # i am confused in here 
                    # i want to tackle this part before moving on to the next one 
                    return False
        if stack: return False
        return True
    

class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        opening = {"(", "[", "{"}
        closing = {")", "]", "}"}

        stack = []
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if stack and s[i] == parantheses[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return False if stack else True
    

class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        for c in s:
            if c in parantheses:
                if stack and stack[-1] == parantheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack: return False
        return True
