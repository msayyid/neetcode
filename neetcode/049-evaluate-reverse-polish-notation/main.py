from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stack = []
        for i in range(len(tokens)):
            
            if tokens[i] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num1) + int(num2))
            elif tokens[i] == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif tokens[i] == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif tokens[i] == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
    

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            
            if token == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif token == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif token == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(token))
        return stack[-1]