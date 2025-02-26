# https://neetcode.io/problems/string-encode-and-decode
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s))+"C"+s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0


        while i < len(s):

            j = i

            while str(s[j]) != "C":
                j += 1

            count = int(s[i:j])

            res.append(s[j+1: j+1+count])

            i = j+1+count

        return res
