# import heapq
from typing import List

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # map nums to map
#         my_map = dict()
#         for i in range(len(nums)):
#             my_map[nums[i]] = my_map.get(nums[i], 0) + 1

#         heap = []
#         for key, val in my_map.items():
#             # if len(heap) <= k:
#             #     heapq.heappush(heap, (val, key))
#             # heapq.heappop(heap)
#             heapq.heappush(heap, (val, key))
#             if len(heap) > k:
#                 heapq.heappop(heap)

#         res = []
#         for i in heap:
#             # res = []
#             res.append(i[1])
#         return res
        


# bucket sort approach

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map nums to map
        my_map = dict()
        freq = []
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1

        
        for _ in range(len(nums) + 1):
            # we need + 1 because of the index nature which starts from 0? (correct me)
            freq.append([])

        for key, val in my_map.items():
            freq[val].append(key)
            # now we're filling the lists of our freq list
        
        result = []
        for i in range(len(freq)-1, 0, -1):
            for j in range(len(freq[i])):
                result.append(freq[i][j])
                if len(result) == k:
                    return result
                
# Top K Frequent Elements — Two Approaches

# Approach 1: Min Heap

# Map each number to its frequency. Push (freq, num) onto a min heap — Python's heapq is a min heap 
# (smallest on top, not max). Keep heap size bounded at K by popping whenever it exceeds K. 
# The popped element is always safe to remove because it's already been beaten by K others 
# in the heap — the logic is self-correcting at every step.

# Heap operations cost O(log K) because the heap never grows beyond K.

# Time: O(N log K) — N for mapping, N log K for heap operations

# Space: O(N) — map in worst case, O(K) for heap

# Approach 2: Bucket Sort

# Use frequency as index. Create a list of N+1 empty buckets — +1 because max frequency is N (all same number), 
# so index N must be valid. Fill buckets, then iterate from high to low frequency, 
# collecting until you have K elements. The nested loop is O(N) not O(N²) because total elements across all buckets is N, and you stop at K.

# Time: O(N) — linear, the trade-off for slightly more involved implementation

# Space: O(N) — same as heap approach

# Trade-off: Bucket sort is faster (O(N) vs O(N log K)) with same space. Min heap is easier to reason about.