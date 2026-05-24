import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        for n1 in nums1:
            for n2 in nums2:
                cur_sum = n1 + n2
                result.append([cur_sum, n1, n2])
        result.sort()
        res = []
        # for s, f, sec in result:
        #     res.append([f, sec])
        #     if len(res) == k:
        #         return res
        # print(result)
        
        for i in range(len(result)):
            result[i] = result[i][1:]
            if i == k - 1:
                # print(result[:i])
                return result[:i + 1]


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        for n1 in nums1:
            for n2 in nums2:
                cur_sum = n1 + n2
                heapq.heappush(result, (cur_sum, [n1, n2]))

        # print(result)
        res = []
        for i in range(k):
            res.append(heapq.heappop(result)[1])
        # print(res)
        return res
    

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(pairs, [nums1[i] + nums2[0], i, 0])

        result = []
        for _ in range(k):
            cu_sum, i, j = heapq.heappop(pairs)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heapq.heappush(pairs, [nums1[i] + nums2[j + 1], i, j + 1])

        return result
    

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []

        # first imagine we have a matrix of pairs with sums, because the arrays are sorted
        # it is possible
        # then we heappush the first column of each row or at most k rows to the pairs
        # this way we are guaranteed to have the smallest pair of all the matrix
        for i in range(min(len(nums1), k)):
            # now we push [sum, i, 0]
            # i - index of nums1's elements
            # 0 - index of nums2's elements
            heapq.heappush(pairs, [nums1[i] + nums2[0], i, 0])
        # since we heappushed, smallest pair is the first to be popped


        # print(pairs)
        result = []

        # now we loop k times and fill the result
        for _ in range(k):
            # pop the pairs, destructure and append to the result
            cur_sum, i, j = heapq.heappop(pairs)
            result.append([nums1[i], nums2[j]])

            # now check if nums2 has more columns
            if j + 1 < len(nums2): # if yes
                # if yes we heappush this next element, because it could potentially 
                # be our next smallest pair
                heapq.heappush(pairs, [nums1[i] + nums2[j + 1], i, j + 1])

            # if not, we simply keep popping the next of pairs,
            # as they are the next smallest ones

        return result