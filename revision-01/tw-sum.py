class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map: number -> index
        # It stores numbers we have already seen.
        my_map = {}

        for i in range(len(nums)):
            # The number we need to pair with nums[i]
            complement = target - nums[i]

            # Check first:
            # if the complement was seen earlier, we found the answer.
            if complement in my_map:
                return [my_map[complement], i]

            # Then store the current number and its index
            # so future elements can use it.
            my_map[nums[i]] = i


# Corrected note:
# We check for the complement before inserting the current number.
# This is important because if we built the full map first,
# duplicate values could overwrite earlier indices.
# For example, in [5, 5], a full map would end up storing only one index for 5.
# That could cause incorrect matching or require extra checks to avoid
# using the same element twice.
#
# In this one-pass approach, the map only contains previously seen elements,
# so duplicates are handled naturally.
#
# Also, my_map[complement] is always smaller than i when we return,
# because the current index i has not been inserted into the map yet.
# The map only stores indices from earlier iterations.