"""
https://leetcode.com/problems/left-and-right-sum-differences/description/
"""

from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        

        l_sum , r_sum = 0, sum(nums)

        n = len(nums)

        answer = [0] * n

        for pos, val in enumerate(nums):

            l_sum += nums[pos-1] if pos > 0 else 0

            r_sum -= nums[pos]

            answer[pos] = abs(l_sum - r_sum)
        
        return answer



if __name__ == "__main__":
    
    nums = [10,4,8,3]
    nums2 = [1]
    
    s  = Solution()    
    print(f" ans for {nums} is   {s.leftRightDifference(nums=nums)}")
    print(f" ans for {nums2}   {s.leftRightDifference(nums=nums2)}")

