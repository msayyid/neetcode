import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)

        for _ in range(k):
            ans = heapq.heappop(heap)

        return -ans
    

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])

            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
