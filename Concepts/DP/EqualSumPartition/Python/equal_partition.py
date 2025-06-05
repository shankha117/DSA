from itertools import product
import unittest
from typing import List

# Placeholder for the function to test
def subset_sum(nums: List[int], target: int) -> bool:

    n = len(nums)

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

    return dp[n][target]



def equal_sum_partitin(nums):

    tot = sum(nums)

    if tot % 2 == 0:

        return subset_sum(nums, tot//2)

    else:
        return False


class TestEqualSumPartition(unittest.TestCase):

    def test_easy_cases(self):
        self.assertTrue(equal_sum_partitin([1, 5, 11, 5]))
        self.assertFalse(equal_sum_partitin([1, 2, 3, 5]))
        self.assertFalse(equal_sum_partitin([2, 2, 3, 5]))
        self.assertTrue(equal_sum_partitin([3, 1, 1, 2, 2, 1]))

    def test_medium_cases(self):
        self.assertTrue(equal_sum_partitin([15, 5, 20, 10, 35, 15, 10]))
        self.assertFalse(equal_sum_partitin([15, 5, 20, 10, 35]))
        self.assertFalse(equal_sum_partitin([1, 2, 5, 11, 6]))  # 1+5+6=12 and 2+11=13 → False
        self.assertFalse(equal_sum_partitin([1, 2, 5, 11, 6]))

    def test_hard_cases(self):
        self.assertTrue(equal_sum_partitin([100, 100, 100, 100, 100, 100, 100, 100, 100, 100]))
        self.assertFalse(equal_sum_partitin([100, 100, 100, 100, 100, 100, 100, 100, 100, 99]))  # Sum = 999 → odd
        self.assertTrue(equal_sum_partitin([3]*100 + [6]*50))  # Even total sum
        self.assertFalse(equal_sum_partitin([1]*201))  # Total sum is 201 → odd → False

if __name__ == "__main__":
    unittest.main()
