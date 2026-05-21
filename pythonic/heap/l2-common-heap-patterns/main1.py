# find the k smallest numbers
import heapq

nums = [8, 3, 10, 1, 6, 14, 4] # nums is altered, to keep nums use copy()
k = 3
heapq.heapify(nums)
result = []
for _ in range(k):
    result.append(heapq.heappop(nums))

print(result)
