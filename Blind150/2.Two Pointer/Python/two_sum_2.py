# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        l, r = 0 , len(numbers)-1


        while l < r:

            cur_sum = numbers[l] + numbers[r]

            if cur_sum > target:

                r -= 1

            elif cur_sum < target:

                l += 1

            else:
                return [l+1, r+1]

        return [l+1, r+1] # just to stop the language server complaints
