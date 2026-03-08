import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map nums to map
        my_map = dict()
        for i in range(len(nums)):
            my_map[nums[i]] = my_map.get(nums[i], 0) + 1

        heap = []
        for key, val in my_map.items():
            # if len(heap) <= k:
            #     heapq.heappush(heap, (val, key))
            # heapq.heappop(heap)
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in heap:
            # res = []
            res.append(i[1])
        return res
        


        


        