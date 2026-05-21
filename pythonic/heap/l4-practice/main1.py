# Exercise 9: Last Stone Weight
# Given:
# stones = [2, 7, 4, 1, 8, 1]
# Each turn:
# Take the two heaviest stones.
# If they are equal, both disappear.
# If not equal, push back their difference.

# Expected answer:
# 1
# Hint: use a max heap with negative values.
# This is a very good beginner heap problem.

import heapq

stones = [2, 7, 4, 1, 8, 1]

heap = [-s for s in stones]
heapq.heapify(heap)
print(heap)

while len(heap) > 2:
    one = -heapq.heappop(heap)
    two = -heapq.heappop(heap)
    if one != two:
        diff = one - two
        heapq.heappush(heap, -diff)

if heap:
    print(-heap[0])
else:
    print(0)