from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(numbers)):
            if target - numbers[i] in my_map:
                return [my_map[target - numbers[i]] + 1, i + 1]
            else:
                my_map[numbers[i]] = i