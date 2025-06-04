from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")]* (amount+1)

        dp[0] = 0

        # allows me to do an early break , i.e if the current coin is more then the next coins wiill also be more ,
        # so no point of going ahead
        coins.sort()

        # fill the DP array
        for c in range(1, amount+1):

            # check every coin
            for cur in coins:

                if c - cur < 0:
                    break

                dp[c] = min(dp[c], 1 + dp[c-cur]) # min(take the current coin, dont take the current coin)

        return dp[amount] if dp[amount] != float("inf") else -1
