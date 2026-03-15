from itertools import product
class Solution:
    def longestCommonSubstring(self, text1: str, text2: str) -> int:

        l1,l2 = len(text1) , len(text2)

        dp = [[0]*(l2+1) for _ in range(l1+1)]
        max_length = 0


        for i, j in product(range(1, l1+1), range(1, l2+1)):

            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_length = max(max_length, dp[i][j])

            else:
                dp[i][j] =  0

        return max_length
def test_lcs():
    s = Solution()

    test_cases = [
        ("abcde", "abcde", 5),            # identical strings
        ("abc", "def", 0),               # no common substring
        ("", "abc", 0),                  # one empty string
        ("abc", "", 0),                  # one empty string
        ("abcxyz", "xyzabc", 3),        # common substring at the end/start
        ("abcdxyz", "xyzabcd", 4),      # common substring in the middle
        ("abcdef", "zcdemf",3),        # small common substring
        ("aaaaa", "aaa", 3),            # repeated characters
        ("abcabcbb", "babcacb", 4),    # overlapping substrings
        ("thequickbrownfox", "quickbrown", 10),  # long substring inside
    ]

    for i, (text1, text2, expected) in enumerate(test_cases, 1):
        result = s.longestCommonSubstring(text1, text2)
        if result == expected:
            print(f"✅ Test Case {i}: PASS | Got: {result}")
        else:
            print(f"❌ Test Case {i}: FAIL | Got: {result}, Expected: {expected}")


if __name__ == "__main__":
    test_lcs()
