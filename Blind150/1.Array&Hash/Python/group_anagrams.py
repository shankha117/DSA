# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)

        for s in strs:
            ans["".join(sorted(s))].append(s)

        return ans.values()
