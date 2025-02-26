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


""".DS_Store
What happens at r = 3 (second 'a')?
'a' is already in seen_map at index 0.

If we blindly updated l = seen_map['a'] + 1 = 0 + 1 = 1, it would incorrectly move backward to l = 1, which is wrong.

Instead, max() ensures:
"""
