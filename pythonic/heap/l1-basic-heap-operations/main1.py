import heapq

h = []

nums = [5, 1, 9, 3, 7]
# heapq.heappush(h, 5)
# heapq.heappush(h, 1)
# heapq.heappush(h, 9)
# heapq.heappush(h, 3)
# heapq.heappush(h, 7)
for n in nums:
    heapq.heappush(h, n)
print(h)
while h:
    print(heapq.heappop(h))
# print(h)