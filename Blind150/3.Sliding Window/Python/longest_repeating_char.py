# https://leetcode.com/problems/longest-repeating-character-replacement/description/


### Using 26 char of Dict // O(26.n) to get the max(count_map.values())
import string
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        count_map = {}

        res = 1

        l = 0
        r = 1

        count_map[s[l]] = 1

        while r < len(s):

            count_map[s[r]] = 1 + count_map.get(s[r] , 0)

            cur_len = (r-l)+1

            if  (cur_len - max(count_map.values())) <= k:

                res = max(res, cur_len)

                r += 1

            else:

                count_map[s[l]] -= 1
                count_map[s[r]] -= 1 # because if the same loop run for r again , we will increment the count for r , but we had seen it before !

                l += 1

        return res




### O(n) solution using a maxf

class Solution2:

    def characterReplacement(self, s: str, k: int) -> int:


        count_map = {}

        res = 1

        l = 0
        r = 1

        count_map[s[l]] = 1

        maxf = 0

        while r < len(s):

            count_map[s[r]] = 1 + count_map.get(s[r] , 0)
            maxf = max(maxf, count_map[s[r]])

            cur_len = (r-l)+1

            if  (cur_len - maxf) <= k:

                res = max(res, cur_len)

                r += 1

            else:

                count_map[s[l]] -= 1
                count_map[s[r]] -= 1

                l += 1

        return res
