# https://leetcode.com/problems/subsets-ii/
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []

        N = len(nums)

        nums.sort()

        def dfs(tmp, idx):

            ans.append(tmp[::])


            for i in range(idx, N):

                if i > idx and nums[i] == nums[i-1]:
                    continue

                tmp.append(nums[i])

                dfs(tmp,i+1)

                tmp.pop()

        dfs([],0)

        return ans
