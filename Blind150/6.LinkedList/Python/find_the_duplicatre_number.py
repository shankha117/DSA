# https://leetcode.com/problems/find-the-duplicate-number/description/

# EXPLANATION --> https://www.youtube.com/watch?v=wjYnzkAhcNk

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0,0

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            # cycle exists
            # intersection is at slow (or you can say fast)
            # since both are equal
            if slow == fast:
                break

        # shift the fast to the begining
        fast = 0
        while True:

            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return slow
