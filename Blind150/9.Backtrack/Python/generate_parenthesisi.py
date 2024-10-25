# https://leetcode.com/problems/generate-parentheses/description/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(op, cl, st):

            if op == cl == n:

                ans.append(st)
                return

            if op < n:
                backtrack(op+1, cl, st+"(")

            if cl < op:
                backtrack(op, cl+1, st+")")

        ans = []
        backtrack(0,0,"")

        return ans
