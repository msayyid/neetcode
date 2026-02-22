# Given an integer array nums, return true if any value 
# appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums) -> bool:
        nums_set = set()
        for i in range(len(nums)):
            if nums[i] in nums_set:
                return True
            else: nums_set.add(nums[i])

        return False


if __name__ == "__main__":
    sol = Solution()

    test = [1, 2, 3]
    result = sol.hasDuplicate(test)

    print("ipnut", test)
    print("output", result)


# explanation
# Contains Duplicate — Explanation
# Approach: Use a set to track elements we've already seen as we iterate through the array.
# Why a set? Lookup in a set is O(1) (constant time), and since we only care about whether an element exists — not storing any associated value — a set is the right data structure for the job.
# Walk-through:
# We loop through nums. For each element, we check if it's already in our set. If it is, we've found a duplicate and immediately return True. If it isn't, we add it to the set and continue. If we finish the loop without finding a duplicate, we return False.
# Complexity:

# Time: O(n) — we loop through the array once, and each set lookup/insert is O(1)
# Space: O(n) — in the worst case (no duplicates), we store every element in the set
# Best case: O(1) time — if a duplicate is found early, we return immediately