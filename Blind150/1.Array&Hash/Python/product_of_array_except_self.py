# https://leetcode.com/problems/product-of-array-except-self/description/
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        s = len(nums)
        ans, prefix, postfix = [0]*s,[0]*s, [0]*s


        for i in range(s):

            prefix[i] = nums[i] * (prefix[i-1] if i !=0 else 1)

            postfix[s-i-1] = nums[s-i-1] * (postfix[s-i] if i !=0 else 1)



        for i in range(s):

            ans[i] = (prefix[i-1] if i !=0 else 1) * (postfix[i+1] if i!=s-1 else 1)

        return ans



# but , we can do better by not including the
# prefix and postfix arrays .


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]*len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums)-1, -1, -1):

            res[i] *= postfix
            postfix *= nums[i]

        return res
