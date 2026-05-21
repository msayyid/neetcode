from math import ceil
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = dict()
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        for val in freq.values():
            if val < 2:
                return -1 
        count = 0
        for key, val in freq.items():
            while val > 2 and val != 4:
                val -= 3
                # freq[key] -= 3
                count += 1
            while val > 0 and val % 2 == 0:
                # freq[key] -= 2
                val -= 2
                count += 1
            # else val == 1:
            #     return -1
        return count
        


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = dict()
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1

        count = 0
        for val in freq.values():
            if val == 1:
                return -1
            # print(f"val - {val}, ceil value - {ceil(val/3)}")
            count += ceil(val / 3)
        return count