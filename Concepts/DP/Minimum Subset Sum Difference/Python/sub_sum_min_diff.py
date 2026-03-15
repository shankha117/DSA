import unittest
from itertools import product
from typing import List


def min_subset_sum_diff(nums: List[int]) -> int:
    """
    Minimum Subset Sum Difference (2D DP approach)

    Given an array of positive integers, partition it into two subsets such that
    the absolute difference of their sums is minimized. Return that minimum difference.

    Approach:
    - Let total be the sum of nums, and target = total // 2.
    - Build a 2D DP table dp[n+1][target+1] where dp[i][j] indicates whether a subset
      using the first i elements can achieve sum j.
    - Initialize dp[i][0] = True for all i (sum 0 is always achievable).
    - Transition:
        if nums[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
    - After filling the table, find the largest j ≤ target such that dp[n][j] is True.
      This j is the closest achievable sum to total // 2.
    - The minimum difference is total - 2*j.

    Time complexity: O(n * total_sum)
    Space complexity: O(n * total_sum)
    """

    n = len(nums)
    if n == 0:
        return 0

    total = sum(nums)
    target = total // 2

    # Build the subset sum 2D DP table
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: sum 0 is achievable with any number of items (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill DP table
    for i, j in product(range(1, n + 1), range(1, target + 1)):
        if nums[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            include = dp[i - 1][j - nums[i - 1]]
            exclude = dp[i - 1][j]
            dp[i][j] = include or exclude

    # Find the largest achievable j (≤ target) from the last row
    sum1 = 0
    for j in range(target, -1, -1):
        # if we can achieve sum j with the given numbers
        if dp[n][j]:
            # then j is the largest achievable sum
            sum1 = j
            break

    sum2 = total - sum1
    return abs(sum2 - sum1)


def min_subset_sum_diff_recursive(nums: List[int]) -> int:
    """
    Straightforward recursive solution to illustrate the logic.

    Idea:
    - We aim to split nums into two subsets with sums as close as possible.
    - Equivalently, try to find a subset sum s as close as possible to total // 2.
    - This recursive approach explores including/excluding each number to track achievable sums.

    This is exponential in the worst case (O(2^n)) and meant only for understanding.
    """

    total = sum(nums)
    target = total // 2

    def can_make_sum(i: int, curr: int) -> bool:
        # Returns True if using items up to index i (0..i) we can achieve sum 'curr'
        if curr == 0:
            return True
        if i < 0 or curr < 0:
            return False
        # Option 1: exclude nums[i]
        if can_make_sum(i - 1, curr):
            return True
        # Option 2: include nums[i]
        return can_make_sum(i - 1, curr - nums[i])

    # Find the largest achievable s <= target
    n = len(nums)
    sum1 = 0
    for s in range(target, -1, -1):
        if can_make_sum(n - 1, s):
            sum1 = s
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

    def test_edge_cases(self):
        self.assertEqual(min_subset_sum_diff([]), 0)
        self.assertEqual(min_subset_sum_diff([5]), 5)
        self.assertEqual(min_subset_sum_diff([1, 1]), 0)
        self.assertEqual(min_subset_sum_diff([2, 2, 2, 2]), 0)

    def test_single_large(self):
        self.assertEqual(
            min_subset_sum_diff([1000, 1, 2, 3]), 994
        )  # closest to half is 6 vs 1000 -> diff 994


if __name__ == "__main__":
    unittest.main()
