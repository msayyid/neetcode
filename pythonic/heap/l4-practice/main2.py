# Exercise 10: Top K Frequent Elements
# Given:
# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# Return the 2 most frequent elements.

# Expected answer:
# [1, 2]
# Hint:
# 1. Count frequencies using a dictionary.
# 2. Push (-frequency, number) into heap.
# 3. Pop k times.


import heapq

nums = [1, 1, 1, 2, 2, 3]
k = 2

freq = {}
for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)

heap = [(-f, n) for n, f in freq.items()]
heapq.heapify(heap)
print(heap)

result = []
for _ in range(k):
    result.append(heapq.heappop(heap)[1])

print(result)