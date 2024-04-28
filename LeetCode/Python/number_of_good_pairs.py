"""
https://leetcode.com/problems/number-of-good-pairs/
"""

from collections import defaultdict
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        seen_dict  = defaultdict(list)

        ans = 0

        for pos, val in enumerate(nums):
            
            if val_list := seen_dict.get(val):

                ans += len(val_list)
                        
            seen_dict[val].append(pos)
                
        return ans
                
if __name__ == "__main__":
    
    nums = [1,2,3,1,1,3]
    
    s  = Solution()
    
    print(f" number of good pairs is  {s.numIdenticalPairs(nums=nums)}")
