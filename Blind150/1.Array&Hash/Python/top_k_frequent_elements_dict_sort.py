# https://leetcode.com/problems/top-k-frequent-elements/description/


from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        fMap = defaultdict(int)

        for n in nums:
            fMap[n] += 1

        sorted_keys = list(sorted(fMap.items(), key=lambda item: item[1], reverse = True))

        ans = []

        for i in range(k):

            ans.append(sorted_keys[i][0])

        return ans
