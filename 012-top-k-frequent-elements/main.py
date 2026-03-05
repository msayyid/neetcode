# import heapq
from typing import List

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         my_map = dict()
#         freq = list()
#         for i in range(len(nums)):
#             my_map[nums[i]] = my_map.get(nums[i], 0) + 1

        
#         heap = []
        
#         for key, val in my_map.items():

#             heapq.heappush(heap, (val, key))
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         result = []
#         for el in heap:
#             result.append(el[1])

#         return result

# O (m *log k) time, On space


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = dict()
        freq = list()
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1
        
        for i in range(len(nums) + 1):
            freq.append([])
        
        for key, val in my_map.items():
            freq[val].append(key)
        
        result = []
        for i in range(len(freq)-1, 0, -1):
            for j in range(len(freq[i])):
                result.append(freq[i][j])
                print(result)
                if len(result) == k:
                    return result



s = Solution()

print(s.topKFrequent([1,1,1,2,2,3], 2))
print(s.topKFrequent([1], 1))
print(s.topKFrequent([5,5,5,5], 1))
print(s.topKFrequent([1,2,3,4], 2))
print(s.topKFrequent([4,4,4,6,6,1,1,1,1], 2))
print(s.topKFrequent([-1,-1,-1,-2,-2,-3], 2))
print(s.topKFrequent([7, 7], 1))

#         Top K Frequent Elements

# What I did:

# Built a frequency map using .get(key, 0) + 1 to count occurrences of each element.

# Solution 1 (min-heap): Used heapq (Python's min-heap) pushing (frequency, element) 
# tuples so heap sorts by frequency, smallest on top. After each push, if heap size exceeds k, 
# pop the smallest — this keeps only the top k frequent elements. 
# Finally extracted index [1] from each tuple to get actual elements.

# Solution 2 (bucket sort): Created list freq of size n+1 where index = frequency, 
# value = list of elements with that frequency. Iterated from the back (highest frequency first), 
# collecting elements until result has k elements.

# Mistakes made: Mixed up .get() syntax. Had unnecessary if/else branches doing the same thing in heap version. 
# Returned heap tuples directly instead of extracting keys. Tried extracting from my_map instead of heap. 
# Didn't immediately understand why freq must be pre-initialized as lists — you can't .append() to something that doesn't exist yet.

# New things learned: heapq is a min-heap — smallest on top. Push tuples to sort by first element. 
# Push first then pop if size exceeds k, not the other way around. Min-heap capped at k is better 
# than max-heap of all elements in both time and space. Bucket sort trick — frequency as index, iterate from back for top k.

# Time: Solution 1: O(n + m log k) | Solution 2: O(n)
# Space: Solution 1: O(m + k) | Solution 2: O(n)