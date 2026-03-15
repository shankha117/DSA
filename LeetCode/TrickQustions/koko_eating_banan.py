# https://leetcode.com/problems/koko-eating-bananas/description/
from typing import List
from math import ceil

class Solution:
    def can_eat(self, piles, k, h):

        total_time = 0
        for p in piles:
            total_time += ceil(p/k)

        return total_time <= h


    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        res = r

        while l <= r:

            mid = l + (r-l) // 2
            can_eat = self.can_eat(piles, mid , h)

            if can_eat:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1


        return res
