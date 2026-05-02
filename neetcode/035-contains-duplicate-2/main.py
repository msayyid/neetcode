from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] == nums[j] and abs(i - j) <= k:
                        return True

        return False
    

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if i >= k:
                window.remove(nums[i - k]) # remove the element that is k steps behind current index
        return False
    

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # This set will store the "last k elements"
        # Think of it as our sliding window
        window = set()

        # We iterate through the array using index i
        for i in range(len(nums)):

            # STEP 1: Check
            # If current number already exists in window,
            # it means we saw it within the last k indices
            if nums[i] in window:
                return True

            # STEP 2: Add current number to window
            window.add(nums[i])

            # STEP 3: Maintain window size
            # We only want to keep the last k elements
            # So once i >= k, we remove the element that is k steps behind
            if i >= k:
                # nums[i - k] is now too far (distance > k), so remove it
                window.remove(nums[i - k])

        # If no such pair found
        return False