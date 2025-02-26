# https://leetcode.com/problems/permutation-in-string/description/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l1, l2 = len(s1), len(s2)

        if l2 < l1:
            return False

        p_hash = sum(map(hash, s1))
        s_hash = sum(hash(s2[i]) for i in range(l1))

        if p_hash == s_hash:
            return True

        for i in range(l2-l1):
            s_hash = s_hash - hash(s2[i]) + hash(s2[i + l1])
            if s_hash == p_hash:
                return True

        return False
