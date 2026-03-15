## RECURSICE SOLTION
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:


#         def find_lcs(l1, l2):

#             if l1 == 0 or l2 == 0:
#                 return 0

#             if text1[l1-1] == text2[l2-1]:
#                 return 1 + find_lcs(l1-1, l2-1)

#             inc_l1 = find_lcs(l1, l2-1)

#             inc_l2 = find_lcs(l1-1, l2)

#             return max(inc_l1, inc_l2)


#         l1,l2 = len(text1) , len(text2)

#         return find_lcs(l1,l2)


### MEMOIZATION SOLUTION
# def find_lcs(l1, l2):

#     if l1 == 0 or l2 == 0:
#         return 0

#     if (val:=dp[l1][l2]) != -1:
#         return val

#     if text1[l1-1] == text2[l2-1]:
#         dp[l1][l2] = 1 + find_lcs(l1-1, l2-1)

#     else:
#         inc_l1 = find_lcs(l1, l2-1)

#         inc_l2 = find_lcs(l1-1, l2)

#         dp[l1][l2] =  max(inc_l1, inc_l2)

#     return dp[l1][l2]


# l1,l2 = len(text1) , len(text2)

# dp = [[-1]*(l2+1) for _ in range(l1+1)]

# return find_lcs(l1,l2)


## BOTTOM UP
from itertools import product
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        l1,l2 = len(text1) , len(text2)

        dp = [[0]*(l2+1) for _ in range(l1+1)]


        for i, j in product(range(1, l1+1), range(1, l2+1)):

            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                inc_l1 =  dp[i][j-1]

                inc_l2 = dp[i-1][j]

                dp[i][j] =  max(inc_l1, inc_l2)

        return dp[l1][l2]
