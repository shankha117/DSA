# https://leetcode.com/problems/k-closest-points-to-origin/description/
import heapq
from typing import List

class Solution:

    @staticmethod
    def get_ditance_from_origin(x,y):
        return (x**2) + (y**2)


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # python will use the first value by default as key for the heap
        minHeap = [(self.get_ditance_from_origin(i[0],i[1]), i) for i in points]


        heapq.heapify(minHeap)

        ans = []

        while k and minHeap:

            ele = heapq.heappop(minHeap)
            ans.append(ele[1])
            k -= 1

        return ans
