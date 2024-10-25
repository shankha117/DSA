# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
from typing import List

class Solution:

    def evaluate(self,od1:int,od2:int, opr:str):

        if opr == "/":
            return int(od1/od2)

        elif opr == "+":
            return od1 + od2

        elif opr == "-":
            return od1 - od2

        else:
            return od1 * od2

    def evalRPN(self, tokens: List[str]) -> int:

        oprs = ["+", "-", "/", "*"]

        st = []

        for t in tokens:

            if t not in oprs:
                st.append(int(t))

            else:
                od2 = st.pop()
                od1 = st.pop()
                ans = self.evaluate(od1=od1, od2=od2, opr=t)
                st.append(ans)

        return st[0]
