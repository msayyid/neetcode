from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            print(stack)
            if self.is_numeric(o):
                stack.append(int(o))
            elif o == "C":
                stack.pop()
            elif o == "D":
                stack.append(stack[-1] * 2)
            # elif o == "+":
            else:
                stack.append(stack[-1] + stack[-2])

        return sum(stack)

    def is_numeric(self, o):
        try:
            float(o)
            return True
        except ValueError:
            return False
            
        
        
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == "+":
                stack.append(stack[-1] + stack[-2])
            elif o == "D":
                stack.append(stack[-1] * 2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
        return sum(stack)