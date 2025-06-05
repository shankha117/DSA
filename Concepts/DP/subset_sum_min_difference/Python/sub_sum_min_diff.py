import unittest
from itertools import product
from typing import List

def min_subset_sum_diff(nums: List[int]) -> int:


    def subset_sum(nums, target):

        dp = [[False]*(target+1) for _ in range(n+1)]

        for r in range(n+1):
            dp[r][0] = True


        for i, j in product(range(1, n+1), range(1, target+1)):

            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]

            else:
                include = dp[i-1][j - nums[i-1]]
                exclude = dp[i-1][j]
                dp[i][j] = (include or exclude)

        return dp


    total = sum(nums)
    n = len(nums)
    target = total // 2

    dp = subset_sum(nums, target)

    # Find largest j from the last ROW (≤ total // 2) for which dp[n][j] is True
    for j in range(target, 0, -1):
        if dp[n][j]:
            sum1 = j
            break

    sum2 = total - sum1
    return abs(sum2 - sum1)

class TestMinSubsetSumDiff(unittest.TestCase):
    def test_easy(self):
        self.assertEqual(min_subset_sum_diff([1, 6, 11, 5]), 1)

    def test_medium(self):
        self.assertEqual(min_subset_sum_diff([3, 1, 4, 2, 2, 1]), 1)
        self.assertEqual(min_subset_sum_diff([1, 2, 3, 9]), 3)

    def test_hard(self):
        self.assertEqual(min_subset_sum_diff([10, 20, 15, 5, 25]), 5)
        self.assertEqual(min_subset_sum_diff([1, 2, 7, 1, 5]), 0)
        self.assertEqual(min_subset_sum_diff([1, 2, 3, 4, 5, 6, 7]), 0)
        self.assertEqual(min_subset_sum_diff([1] * 30 + [100]), 70)

if __name__ == "__main__":
    unittest.main()
