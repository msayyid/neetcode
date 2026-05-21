# simulate a max heap
import heapq

heap = []

nums = [5, 1, 9, 3, 7]

for n in nums:
    heapq.heappush(heap, -n)
print(heap)

while heap:
    print(-(heapq.heappop(heap)))

# Python's heapq is a min heap, so we store negative values to simulate a max heap.