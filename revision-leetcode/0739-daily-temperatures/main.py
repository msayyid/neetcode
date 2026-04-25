from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:#
        count = 0
        n = len(temperatures)
        answer = [0] * n
        for i in range(n):
            count = 1
            for j in range(i + 1, n):
                if temperatures[i] < temperatures[j]:
                    answer[i] = count
                    break
                elif temperatures[i] >= temperatures[j]:
                    count += 1
        return answer
    

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            # while there's something in stack and
            # today's [i] temperatures is warmer than top of the stack's
            # we update the answer and stack
            while stack and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return answer


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            stack.append(i)
        return answer
