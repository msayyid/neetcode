from typing import List


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = [(nums2[i], i) for i in range(len(nums2))]
        sorted_nums2.sort()
        # print(nums1)
        # print(sorted_nums2)
        left = 0
        right = len(nums2) - 1
        result = [None] * len(nums1)

        left2 = 0
        right2 = len(nums2) - 1

        while left2 <= right2:
            # if the smallest of nums1 > than smallest of nums2 we win
            if nums1[left] > sorted_nums2[left2][0]:
                # we won, so we put the won element to its place
                result[sorted_nums2[left2][1]] = nums1[left]
                left += 1
                left2 += 1
            else: # if we do not win, if the smallest of nums1
                  # can't beat the smallest of nums2, it is useless
                  # we use it to lose for the biggest (sacrifice)
                result[sorted_nums2[right2][1]] = nums1[left]
                right2 -= 1
                right -= 1
                left += 1
            # print(f"{result} - left1: {left}; left2: {left2}; right1: {right}; righ2: {right2}")
            
        # print(result)
                
        return result
    
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted_nums2 = [(nums2[i], i) for i in range(len(nums2))]
        sorted_nums2.sort()

        left = 0
        result = [None] * len(nums1)

        left2 = 0
        right2 = len(nums2) - 1

        while left2 <= right2:
            if nums1[left] > sorted_nums2[left2][0]:
                result[sorted_nums2[left2][1]] = nums1[left]
                left += 1
                left2 += 1
            else:
                result[sorted_nums2[right2][1]] = nums1[left]
                right2 -= 1
                left += 1
                
        return result
    
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        # store each nums2 value with its original index
        # this is to match the original order of nums2
        sorted_nums2 = [(nums2[i], i) for i in range(len(nums2))]
        sorted_nums2.sort()

        # pointer for the smallest number in nums1
        left = 0

        result = [None] * len(nums1)

        # pointers for the smallest and largest remaining values in sorted nums2
        left2 = 0
        right2 = len(nums2) - 1

        while left2 <= right2:
            # if the smallest remaining nums1 can beat the smallest remaining nums2
            # use it and win
            if nums1[left] > sorted_nums2[left2][0]:
                result[sorted_nums2[left2][1]] = nums1[left]
                left += 1
                left2 += 1

            # otherwise, this nums1 val cannot beat even the smallest nums2 val,
            # so it cannot beat anyone, sacrifice it against the largest nums2 val
            else:
                result[sorted_nums2[right2][1]] = nums1[left]
                right2 -= 1
                left += 1
                
        return result