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

 # recursive version kSum
 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res, quad = [], []

        def k_sum(k, start, target):
            # if k is not 2 yet, we still need to choose more numbers
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    # skip duplicates at the current recursion level
                    if i > start and nums[i] == nums[i - 1]:
                        continue

                    # choose nums[i] as one part of the current answer
                    quad.append(nums[i])

                    # we already picked nums[i], so now we need:
                    # (k - 1) more numbers
                    # starting only from i + 1
                    # whose sum must be (target - nums[i])
                    k_sum(k - 1, i + 1, target - nums[i])

                    # backtrack 
                    # remove the number we just picked
                    # so we can try the next possible choice
                    quad.pop()
                
                # important:
                # once this recursive level finishes its loop, stop here
                # and do not continue into the 2-pointer code below
                return

            # base case: k == 2
            # now the problem is just 2Sum in a sorted array
            l, r = start, len(nums) - 1
            while l < r:
                pair_sum = nums[l] + nums[r]
                if pair_sum < target:
                    l += 1
                elif pair_sum > target:
                    r -= 1
                else:
                    # quad already has the previously chosen numbers
                    # nums[l] and nums[r] complete the combination
                    res.append(quad + [nums[l], nums[r]])

                    l += 1
                    # skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        k_sum(4, 0, target)
        return res

