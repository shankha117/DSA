""""""""""""""""""""""""
# NOT VERY INTUATIVE ; USE THE 1D DP
""""""""""""""""""""""""



from typing import List
from itertools import product
import unittest


def coin_change(coins: List[int], amount: int) -> int:

    N = len(coins)

    # keep all the blocks to inf , because we need to compute MIN
    dp = [[float("inf")]*(amount+1) for _ in range(N+1)]

    # inistilize the first COL to 0
    for t in range(N+1):
        dp[t][0] = 0


    for i,j in product(range(1,N+1), range(1, amount+1)):

        # if the cur sum (j) is less than the last coin of the current coins array (coins[i-1])
        # then we can not take the last coiin
        if coins[i-1] > j:
            dp[i][j] = dp[i-1][j]

        else:
            include = 1+dp[i][j-coins[i-1]]
            exclude = dp[i-1][j]
            dp[i][j] = min(include, exclude)

    return dp[N][amount] if dp[N][amount] != float("inf") else -1





class TestCoinChange(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)   # 5 + 5 + 1
        self.assertEqual(coin_change([2], 3), -1)         # Not possible
        self.assertEqual(coin_change([1], 0), 0)          # Zero amount
        self.assertEqual(coin_change([1], 2), 2)          # 1 + 1
        self.assertEqual(coin_change([2, 3, 5], 7), 2)     # 2 + 5
        self.assertEqual(coin_change([186, 419, 83, 408], 6249), 20)  # Large input
        self.assertEqual(coin_change([3, 7, 405, 436], 8839), 25)     # Edge case
        self.assertEqual(coin_change([2, 5, 10, 1], 27), 4) # 10 + 10 + 5 + 2
        self.assertEqual(coin_change([186, 419, 83, 408], 6248), 19) # Not possible

if __name__ == "__main__":
    unittest.main()
