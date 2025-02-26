# https://leetcode.com/problems/subsets/description/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def dfs(idx, tmp):

            ans.append(tmp[:])

            for i in range(idx, len(nums)):

                tmp.append(nums[i])

                dfs(i+1, tmp)

                tmp.pop()

        dfs(0, [])

        return ans
