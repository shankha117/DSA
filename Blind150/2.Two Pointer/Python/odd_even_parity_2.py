# https://leetcode.com/problems/sort-array-by-parity-ii/description/

from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:


        e, o = 0 , 1


        while e < len(nums) - 1:


            while nums[e] % 2 != 0:

                nums[e], nums[o] = nums[o], nums[e]

                o += 2

            e += 2

        return nums
