# https://leetcode.com/problems/valid-anagram/description/


from collections import Counter
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)




######### OR WE CAN WRITE LIKE THIS

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        counts, countt = {}, {}

        for cs, ct in zip(s,t):

            counts[cs] = 1 + counts.get(cs,0)
            countt[ct] = 1 + countt.get(ct,0)

        return counts == countt
