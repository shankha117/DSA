from typing import List
from itertools import product

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        N = len(coins)

        dp = [[0]*(amount+1) for _ in range(N+1)]

        for t in range(N+1):
            dp[t][0] = 1

        for i,j in product(range(1,N+1), range(1, amount+1)):

            if coins[i-1] > j:
                dp[i][j] = dp[i-1][j]

            else:
                include = dp[i][j-coins[i-1]]
                exclude = dp[i-1][j]
                dp[i][j] = include + exclude

        return dp[N][amount]
