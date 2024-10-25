# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if len(s) in [ 1, 0]:
            return len(s)

        l = 0
        seen_map = {s[l]:0}


        max_length = 1

        for r in range(1, len(s)):

            if s[r] in seen_map:

                l = max(seen_map[s[r]] + 1, l) # why need a max func ? dry run "abba"

            seen_map[s[r]] = r

            max_length = max(max_length, (r-l)+1)

        return max_length
