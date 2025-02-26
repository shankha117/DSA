# https://leetcode.com/problems/combination-sum/description/

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        N = len(candidates)

        def dfs(idx, s, tmp):

            if s == target:
                ans.append(tmp[:])

            if s > target:
                return

            for i in range(idx, N):

                tmp.append(candidates[i])

                dfs(i, s+candidates[i], tmp)

                tmp.pop()

        dfs(0,0,[])

        return ans
