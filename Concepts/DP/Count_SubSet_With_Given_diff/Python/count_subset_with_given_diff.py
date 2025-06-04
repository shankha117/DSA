from typing import List
from itertools import product
from functools import lru_cache
import unittest

def count_subsets_with_diff(nums: List[int], diff: int) -> int:
    n = len(nums)
    total = sum(nums)

    if (total + diff) % 2 != 0:
        return 0

    target = (total + diff) // 2

    # def count_subsets(n, t):

    #     ## If no elements are left (n == 0), the only valid subset is the empty subset, and it only counts if the remaining target is 0.

    #     if n == 0:
    #         return 1 if t == 0 else 0

    #     if nums[n - 1] > t:
    #         return count_subsets(n - 1, t)

    #     return count_subsets(n - 1, t - nums[n - 1]) + count_subsets(n - 1, t)
    # return count_subsets(n, target)

    ### BOTTOM UP

    dp = [[0] * (target + 1) for _ in range(n + 1)]

    # Base case: one way to make sum 0 (empty subset)
    for i in range(n + 1):
        dp[i][0] = 1

    # NOTICE ::::: we are not taking(1, target+1) Like other
    # This is to match the base case like we did in recursice approach
    # We must include j = 0 in the inner loop because we want to build all subset sums starting from 0 up to target.

    for i,j in product(range(1, n+1), range(target+1)):
        if nums[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            include = dp[i - 1][j - nums[i - 1]]
            exclude = dp[i - 1][j]
            dp[i][j] = include + exclude

    return dp[n][target]

    # make the





class TestCountSubsetsWithDiff(unittest.TestCase):

    def test_cases(self):
        self.assertEqual(count_subsets_with_diff([1, 1, 2, 3], 1), 3)
        self.assertEqual(count_subsets_with_diff([1, 2, 7, 1, 5], 9), 0)
        self.assertEqual(count_subsets_with_diff([1, 2, 3, 4, 5], 3), 3)
        self.assertEqual(count_subsets_with_diff([1, 2, 3], 7), 0)  # total = 6, (6+7)=13 → odd
        self.assertEqual(count_subsets_with_diff([1, 1, 1, 1, 1], 3), 5)
        self.assertEqual(count_subsets_with_diff([], 0), 1)
        self.assertEqual(count_subsets_with_diff([], 1), 0)
        self.assertEqual(count_subsets_with_diff([0, 0, 0, 0], 0), 16)  # 2^4 subsets with 0 sum

if __name__ == "__main__":
    unittest.main()
