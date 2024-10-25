# https://leetcode.com/problems/sort-array-by-parity/description/

from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        p = 0

        for i in range(0, len(nums)):

            if nums[i] % 2 == 0:

                nums[i], nums[p] = nums[p], nums[i]

                p += 1

        return nums
