# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        MaxHeap = [-1*i for i in nums]

        heapq.heapify(MaxHeap)


        while k > 1:

            heapq.heappop(MaxHeap)

            k -= 1

        return heapq.heappop(MaxHeap)*-1
