# https://leetcode.com/problems/task-scheduler/description/
import heapq

from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        next_task_map = {}

        t = 0

        total_task = len(count.keys())

        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)

        while total_task !=0:

            t += 1

            if nt := next_task_map.get(t):
                heapq.heappush(maxHeap, nt)

            if maxHeap:
                ct = heapq.heappop(maxHeap)

                if ct + 1 == 0:
                    total_task -= 1
                else:
                    next_task_map[t+n+1] = ct + 1


        return t
