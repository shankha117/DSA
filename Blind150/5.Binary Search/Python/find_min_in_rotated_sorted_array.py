# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = nums[0]
        l, r = 0, len(nums) -1

        while l <= r:
            # if the array is sorted then we take min of the
            if nums[l] < nums[r]:
                return min(res,nums[l])
            m = (l+r)//2
            res = min(res, nums[m])

            # if m > l search, means the mid is on the left side
            # then search on the right side
            if nums[m] >= nums[l]:
                l = m + 1

            # else if m is in the right side then search
            # on left side
            else:
                r = m - 1
        return res
