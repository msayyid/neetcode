from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) # O(N)
        # print(freq)
        heap = []
        for key, val in freq.items(): # O(m log m)
            heapq.heappush(heap, (-val, key))

        result = []
        for i in range(k): # O(k log m)
            result.append(heapq.heappop(heap)[1])

        # print(result)
        return result
    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) # O(N)
        # print(freq)
        heap = []
        for key, val in freq.items():

            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for f, v in heap:
            result.append(v)

        return result
    

class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        count = [[] for _ in range(len(nums) + 1)]
        freq = Counter(nums) 
        result = []

        for key, val in freq.items(): 
            count[val].append(key) 

        for i in range(len(count) - 1, -1, -1):
            for j in range(len(count[i])):
                result.append(count[i][j])
                if len(result) == k:
                    return result
        return result