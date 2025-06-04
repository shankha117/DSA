# https://leetcode.com/problems/sort-colors/description/
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        z = 0              # z: next position for 0
        t = N - 1          # t: next position for 2
        p = 0              # p: current pointer

        while p <= t:
            if nums[p] == 0:
                nums[p], nums[z] = nums[z], nums[p]
                z += 1
                p += 1
            elif nums[p] == 2:
                nums[p], nums[t] = nums[t], nums[p]
                t -= 1
                # do not increment p here because the new nums[p] might be 0 or 2
            else:
                p += 1
