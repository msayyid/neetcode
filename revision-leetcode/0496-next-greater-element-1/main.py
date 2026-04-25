from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = False
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            result.append(nums2[k])
                            found = True
                            break
                    if not found:
                        result.append(-1)
                    break
        return result
    

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            cur_max = -1
            for i in range(len(nums2) - 1, -1, -1):
                if nums2[i] == num:
                    if cur_max > num:
                        result.append(cur_max)
                    else:
                        result.append(-1)
                    break

                if nums2[i] > num:
                    cur_max = nums2[i]
        return result
    

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        my_map = {}
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                my_map[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])

        # handle the numbers do not have greater to their right
        while stack:
            my_map[stack.pop()] = -1

        for i in range(len(nums1)):
            result.append(my_map[nums1[i]])
        return result
    
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        my_map = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                # we assign waiting number = first greater to the right number
                my_map[stack[-1]] = num
                stack.pop()

            stack.append(num)

        while stack:
            my_map[stack.pop()] = -1

        for num in nums1:
            result.append(my_map[num])

        return result