# Exercise 8: Closest Points to Origin
# Given points:

# points = [(1, 2), (3, 4), (0, 1), (2, 2)]
# k = 2

# Return the 2 closest points to (0, 0).
# Distance formula:
# x*x + y*y
# Expected answer:
# [(0, 1), (1, 2)]
# Hint: push this into heap:
# (distance, point)
# No need to use square root.

import heapq

points = [(1, 2), (3, 4), (0, 1), (2, 2)]
k = 2

heap = []
for p in points:
    dist = p[0] * p[0] + p[1] * p[1]
    heapq.heappush(heap, (dist, (p)))

print(heap)

result = []
for _ in range(k):
    result.append(heapq.heappop(heap)[1])
print(result)