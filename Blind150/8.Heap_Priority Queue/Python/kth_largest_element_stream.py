# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.store = nums
        self.k = k

        heapq.heapify(nums)

        while len(self.store) > k:
            heapq.heappop(self.store)


    def add(self, val: int) -> int:

        if len(self.store) < self.k:
            heapq.heappush(self.store, val)
        else:
            heapq.heappushpop(self.store, val)

        return self.store[0]
