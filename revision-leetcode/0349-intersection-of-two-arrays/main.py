from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersections = []
        for i in range(len(nums1)):
            if nums1[i] not in intersections and nums1[i] in nums2:
                intersections.append(nums1[i])
        return intersections


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersections = set()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and nums1[i] not in intersections:
                    intersections.add(nums1[i])
        return list(intersections)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
    

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = []
        for num in set1:
            if num in set2:
                result.append(num)

        return result
    

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set2 = set(nums2)
        result = set()
        for num in nums1:
            if num in set2:
                result.add(num)

        return list(result)
    

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        ans = []
        for num in nums2:
            if num in set1:
                ans.append(num)
                set1.remove(num)
        return ans
    
# ### Idea

# * Put `nums1` into a set → fast lookup
# * Loop through `nums2`
# * If number is in set → add to result **and remove it**

# ---

# ### Why remove?

# * So we **don’t add duplicates**
# * Once used → it’s “consumed”

# ---

# ### One-line memory trick

# > “Check in set, add to answer, remove to avoid duplicates.”

# ---

# ### Complexity

# * Time: O(n + m)
# * Space: O(n)
