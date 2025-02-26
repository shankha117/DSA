# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if len(s1) != len(s2):
            return False

        if s1 == s2:
            return True

        set_s1 = set()
        set_s2 = set()
        not_matched = 0


        for x,y in zip(s1,s2):

            if x != y:
                set_s1.add(x)
                set_s2.add(y)

                not_matched += 1

                if not_matched > 2:
                    return False


        return True if set_s1 == set_s2 else False
