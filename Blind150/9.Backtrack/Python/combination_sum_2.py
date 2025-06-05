# https://leetcode.com/problems/combination-sum-ii/
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        N = len(candidates)

        candidates.sort()

        ans = []

        def dfs(idx, tot, tmp):

            if tot == target:
                ans.append(tmp[::])
                return

            if tot > target:
                return

            for i in range(idx, N):

                # consider this example
                # [2,5,2,1,2]
                # after we sort this becomes [1,2,2,2,5]
                # when we have added [1,2,2] we need to make sure we dont also add another [1,2,2]
                # that is [N(0),N(1),N(3)] ;
                # we need to skip the candidate[i] if the same number is added previously at the same for loop (idx)

                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                cur = candidates[i]

                tmp.append(cur)

                dfs(i+1, tot+cur, tmp)

                tmp.pop()

        dfs(0,0,[])
        return ans
