# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:

            mid = l + (r - l) //2

            if target == nums[mid]:
                return mid


            # if the mid is in the left side sorted array
            if nums[mid] >= nums[l] :

                if nums[mid] < target or target < nums[l]:

                    l = mid + 1
                else:
                    r = mid - 1

            # mid is in the right side sorted array
            else:

                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
