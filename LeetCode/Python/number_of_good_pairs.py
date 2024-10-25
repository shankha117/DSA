"""
https://leetcode.com/problems/number-of-good-pairs/
"""

from collections import defaultdict
from typing import List


class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        result = 0
        
        for num in nums:
            if num in count:
                result += count[num]
                count[num] += 1
            else:
                count[num] = 1
        
        return result

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

    s2  = Solution2()    
    print(f" number of good pairs is  {s2.numIdenticalPairs(nums=nums)}")
