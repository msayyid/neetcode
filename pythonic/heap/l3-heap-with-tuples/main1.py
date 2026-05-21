# Exercise 7: Sort Tasks by Priority
# Each task is stored as:
# (priority, task_name)
# Given:
# tasks = [
#     (3, "write code"),
#     (1, "fix bug"),
#     (2, "review PR")
# ]
# Push them into a heap and process them by priority.
# Expected order:
# fix bug
# review PR
# write code
# Goal: understand that heaps compare tuples by the first value first.

import heapq

tasks = [
    (3, "write code"),
    (1, "fix bug"),
    (2, "review PR")
]

heap = []
for t in tasks:
    heapq.heappush(heap, t)

while heap:
    task = heapq.heappop(heap)
    print(task[1])