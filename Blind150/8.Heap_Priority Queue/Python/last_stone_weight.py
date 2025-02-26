# https://leetcode.com/problems/last-stone-weight/description/
import heapq
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = [s*-1 for s in stones]

        heapq.heapify(hq)


        while hq:
            if len(hq) == 1:
                return hq[0]*-1

            stone1 , stone2 = heapq.heappop(hq), heapq.heappop(hq)

            if stone1 == stone2:
                continue
            else:
                heapq.heappush(hq, -1*abs(stone1 - stone2))

        return 0
