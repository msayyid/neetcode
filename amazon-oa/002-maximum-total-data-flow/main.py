import heapq
from typing import List


# def determineMaxDataFlow(bandwidth: List[int], streamCount: int) -> int:
#     total = 0
#     max_total = 0
#     the_list = set()
#     for i in range(len(bandwidth)):
#         the_list = set()
#         total = 0
#         # for j in range(len(bandwidth)):
#         j = 0
#         while j < len(bandwidth) and len(the_list) <= streamCount: 
#             # if len(the_list) != streamCount:
#             the_list.add((bandwidth[i], bandwidth[j]))
#             total += bandwidth[i] + bandwidth[j]
#             # else:
#             max_total = max(total, max_total)
#             j += 1
#         print(the_list)
#                 # break
#             # if len(the_list) == streamCount:
#             #     max_total = max(total, max_total)
#             #     break
#         print(f"this is total right now - {total}")
#         print(f"this is max_total right now - {max_total}")

#     print(f"the answer: {max_total}")

# def determineMaxDataFlow(bandwidth: List[int], streamCount: int) -> int:
#     pairs = []
#     total = 0
#     for i in range(len(bandwidth)):
#         for j in range(len(bandwidth)):
#             pairs.append(bandwidth[i] + bandwidth[j])
    
#     pairs.sort(reverse=True)
#     print(pairs)
#     for i in range(streamCount):
#         total += pairs[i]

#     print(total)
#     return total


def determineMaxDataFlow(bandwidth: List[int], streamCount: int) -> int:
    bandwidth.sort(reverse=True)
    heap = []
    n = len(bandwidth)
    heapq.heappush(heap, (-(bandwidth[0] + bandwidth[0]), 0, 0))
    visited = {(0, 0)}
    total = 0

    for _ in range(streamCount):
        neg_sum, i, j = heapq.heappop(heap)
        total += -neg_sum

        if i + 1 < n and (i + 1, j) not in visited:
            new_sum = bandwidth[i + 1] + bandwidth[j]
            heapq.heappush(heap, (-new_sum, i + 1, j))
            visited.add((i + 1, j))

        if j + 1 < n and (i, j + 1) not in visited:
            new_sum = bandwidth[i] + bandwidth[j + 1]
            heapq.heappush(heap, (-new_sum, i, j + 1))
            visited.add((i, j + 1))
    print(heap)
    print(total)
    return total

print("##################################")

# Example from problem
bandwidth = [6, 4, 7]
streamCount = 4
# expected = 52
determineMaxDataFlow(bandwidth, streamCount)
print("##################################")
# Sample from screenshot
bandwidth = [5, 4, 8, 4, 7]
streamCount = 6
# expected = 86
determineMaxDataFlow(bandwidth, streamCount)
print("##################################")


# Only one node, self-pair allowed
bandwidth = [1]
streamCount = 1
# expected = 2
determineMaxDataFlow(bandwidth, streamCount)
print("##################################")


# Need only the best pair
bandwidth = [1, 2]
streamCount = 1
# expected = 4
determineMaxDataFlow(bandwidth, streamCount)
print("##################################")


# # Ordered pairs matter: 2+1 and 1+2 both count
# bandwidth = [1, 2]
# streamCount = 2
# expected = 7
# # Taking all possible pairs
# bandwidth = [1, 2]
# streamCount = 4
# expected = 12
# # Duplicate values
# bandwidth = [5, 5, 5]
# streamCount = 5
# expected = 50
# # Larger simple case
# bandwidth = [10, 1, 5]
# streamCount = 3
# expected = 55