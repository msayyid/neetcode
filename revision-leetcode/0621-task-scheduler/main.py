from collections import deque, Counter
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time

        count = Counter(tasks) # fill frequency counter map
        max_heap = [-cnt for cnt in count.values()] # fill the max heap
        heapq.heapify(max_heap) # sort/heapify the heap
        
        time = 0

        q = deque() # pairs of [-cnt, idle_time]

        while max_heap or q:
            time += 1

            if max_heap:
                # we are popping the most frequent task, and decrementing it
                # since max_heap content is negative, us adding 1 means decreasing by 1
                # so the cnt is the current task but decremented by 1
                cnt = 1 + heapq.heappop(max_heap) 

                # if there's still tasks left (if the current task is not zero)
                if cnt: 
                    # we append it to the queue, which has the tasks
                    # (their frequency, tracked frequency - how many more tasks of the kind
                    # left) and the time this task is going to be available again
                    # which is time + n (n being the idle time needed after a task completed)
                    # this means, whenver our time is equal to q[i][1], q[i][0] is available
                    q.append([cnt, time + n])

                # in here, we check if q and q's first task's time is equal to our time
                # meaning, it is time for the task that we processed earlier to be processed 
                # again, if yes:
            if q and q[0][1] == time:
                # we popleft our queue, since this task is going to be processed now
                # and we heappush it to our max_heap, because we removed the task 
                # from max_heap earlier, and this task may still be the most frequent one
                # meaning it still needs to be processed first or sooner to keep
                # the idle time minimum
                heapq.heappush(max_heap, q.popleft()[0])
        return time
    

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0

        q = deque()

        while max_heap or q:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time