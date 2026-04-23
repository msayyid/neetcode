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
                else:
                    answer[i] = 0
        return answer