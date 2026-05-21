# Kth largest element
import heapq

nums = [3, 2, 1, 5, 6, 4]
k = 2

# approach 1: max heap, pop k - 1 times 
heap = [-n for n in nums] # O(n)
heapq.heapify(heap) # O(n)
print(heap)

for _ in range(k - 1): # popping k-1 times => O(k log n)
    heapq.heappop(heap) # each pop O(log n)

# total time complexity is On + O(k log n) => O(n + klogn)
print(-heap[0])

# approach 2: min heap of size k
# keep only the largest k elements seen so far
# loop through each number
# if heap size becomes bigger than k:
#       pop the smallest number
# because if we only wnat the top k largest numbers, any smaller extra number
# should be removed

nums = [3, 2, 1, 5, 6, 4]
k = 2
heap = []
# -------------------------------------------------------------------------------
# heap operation cost depends on the size of the heap, not always the size of the
# original array
# -------------------------------------------------------------------------------

for n in nums:
    heapq.heappush(heap, n)

    if len(heap) > k: # heap never grows bigger than k + 1, so each heap operation costs logk not logn
        heapq.heappop(heap)
# so total is O(n log k)
print(heap[0])