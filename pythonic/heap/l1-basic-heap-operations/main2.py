import heapq

# heapify a list
nums = [10, 4, 6, 2, 8]

heapq.heapify(nums) # turn the list into heap if we do not turn it into heap it won't work
print(nums)

while nums:
    print(heapq.heappop(nums))


h = []                  # - heap
h[0]                    # smallest, O(1)
heapq.heappush(h, 1)    # add, O(log n)
heapq.heappop(h)        # remove smallest O(log n)
heapq.heapify(h)        # build heap, O(n)