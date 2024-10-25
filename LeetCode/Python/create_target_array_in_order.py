"""
https://leetcode.com/problems/create-target-array-in-the-given-order/description/
"""

from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for n,i in zip(nums,index): 
            ans[i:i] = [n]
        return ans


"""
how does ths slicing works
>>> x = [1,2,4,5]
>>> x[1:1]
[]
>>> x[1:]
[2, 4, 5]
>>> x[1:1] = [1]
>>> x
[1, 1, 2, 4, 5]
>>> x[1:1] = [2,3]
>>> x
[1, 2, 3, 1, 2, 4, 5]
>>> x[1:4] = [1]
>>> x
[1, 1, 2, 4, 5]
>>> x[0:2] = [1]
>>> x
[1, 2, 4, 5]
>>> 

"""

if __name__ == "__main__":
    
    nums1 = [0,1,2,3,4] 
    index1 = [0,1,2,2,1]    
    # ans [0,4,1,3,2]

    s  = Solution()    
    print(f"Target array is ---->>> {s.createTargetArray(nums1, index1)}")

