# https://leetcode.com/problems/permutations/description/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        seen = set()
        ans = []
        N = len(nums)

        def dfs(tmp, seen):

            if len(tmp) == N:
                ans.append(tmp[::])
                return

            for i in nums:

                if i not in seen:
                    tmp.append(i)
                    seen.add(i)
                    dfs(tmp, seen)
                    tmp.pop()
                    seen.remove(i)

        dfs([], seen)

        return ans
