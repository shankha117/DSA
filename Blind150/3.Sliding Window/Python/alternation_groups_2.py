# https://leetcode.com/problems/alternating-groups-ii/description

# CIRCULAR ARRAY

from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = 0
        l = 0
        N = len(colors)

        for r in range(1, N+(k-1)):

            if colors[r%N] == colors[(r-1)%N]:
                l = r

            if r - l + 1 == k:

                res += 1
                l += 1
        return res
