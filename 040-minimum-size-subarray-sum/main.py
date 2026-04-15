from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= target:
                    min_length = min(min_length, j - i + 1)
                    break
        return 0 if min_length == float("inf") else min_length


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        min_length = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_length = min(min_length, r - l + 1)
                total -= nums[l]
                l += 1
        
        return 0 if min_length == float("inf") else min_length
    

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        min_length = float("inf")

        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l + r) // 2
                cur_sum = prefix[mid + 1] - prefix[i]
                if cur_sum >= target:
                    r = mid
                else:
                    l = mid + 1
            if l != n:
                min_length = min(min_length, l - i + 1)
        
        if min_length == float("inf"):
            return 0
        return min_length