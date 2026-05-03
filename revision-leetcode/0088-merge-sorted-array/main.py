class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        left = m - 1
        right = n - 1
        while right >= 0: # run until the nums2 is empty
            # check if there's an element in nums1 and whether it is grater
            if left >= 0 and nums1[left] > nums2[right]: 
                nums1[i] = nums1[left]
                i -= 1
                left -= 1
            else: # otherwise, take the element from nums2 and place in nums1[i]
                nums1[i] = nums2[right]
                i -= 1
                right -= 1
        print(nums1)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        left = m - 1
        right = n - 1
        while right >= 0:
            if left >= 0 and nums1[left] > nums2[right]:
                nums1[i] = nums1[left]
                left -= 1
            else:
                nums1[i] = nums2[right]
                right -= 1
            i -= 1
        return nums1
        