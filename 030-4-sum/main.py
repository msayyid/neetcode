from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        temp = []
        res = []
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    for d in range(n):
                        if a != b and b != c and a != c and c != d  and b != d and a != d:
                            temp = []
                            if nums[a] + nums[b] + nums[c] + nums[d] == target:
                                temp.append(nums[a])
                                temp.append(nums[b])
                                temp.append(nums[c])
                                temp.append(nums[d])
                                temp.sort()
                                if temp not in res:
                                    res.append(temp)
        return res
    
# very naive O(n^4) approach is the one above


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                l, r = b + 1, n - 1
                while l < r:
                    cur_sum = nums[a] + nums[b] + nums[l] + nums[r]
                    if cur_sum == target:
                        res.append([nums[a], nums[b], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        r -= 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                    elif cur_sum < target:
                        l += 1
                    else:
                        r -= 1
        return res
 # two pointer approach O(n^3) time 

 