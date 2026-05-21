# find the k largest numbers
import heapq

nums = [8, 3, 10, 1, 6, 14, 4]
k = 3


heap = [-n for n in nums]
# heap = nums.copy() # copy nums content to heap, nums is not altered - O(n) time
# for i in range(len(heap)): # i am not sure if this is needed, but i did it this way O(N) time
#     heap[i] = -heap[i]

print(heap)
heapq.heapify(heap) # now build a heap
print(heap)

result = []

for _ in range(k):
    result.append(-heapq.heappop(heap)) 

print(result)
