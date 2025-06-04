from itertools import product
import unittest
from typing import List

# Placeholder for the function to test
def subset_sum(nums: List[int], target: int) -> bool:

    n = len(nums)

    # cant run test_large_duplicate_set with recursive solution
    # def subset_sum_recursive( n, w):

    #     if w == 0:
    #         return True

        # if n == 0:
        #     # since w is not 0 , means we have some target , but there are no elements in the array
        #     # so return False
        #     return False

    #     if nums[n-1] > w:
    #         return subset_sum_recursive(n-1, w)

    #     include = subset_sum_recursive(n-1, w - nums[n-1])

    #     exclude = subset_sum_recursive(n-1, w)

    #     return include or exclude

    # return subset_sum_recursive(n, target)

######## MEMO ########

    # def subset_sum_memo( n:int, w:int) -> bool:

    #     if w == 0:
    #         return True

    #     if n == 0:
    #         return False

    #     if memo[n][w] != None:
    #         return memo[n][w]

    #     if nums[n-1] > w:
    #         memo[n][w] = subset_sum_memo(n-1, w)
    #     else:
    #         include = subset_sum_memo(n-1, w - nums[n-1])

    #         exclude = subset_sum_memo(n-1, w)

    #         memo[n][w] = (include or exclude)

    #     return memo[n][w]

    # memo = [[None]*(target+1) for _ in range(n+1)]

    # return subset_sum_memo(n, target)

######## BOTTOM UP ########

    # [ dp[i][j] == True ] => if a subset of the first i numbers can sum to j

    # for row from w == 1 will all be false ,
    # since there are no elements in the array (n = 0) , but we need to find a sum

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




class TestSubsetSum(unittest.TestCase):

    def test_all_zeros_target_zero(self):
        self.assertTrue(subset_sum([0, 0, 0, 0], 0))

    def test_medium_case_subset_exists(self):
        self.assertTrue(subset_sum([1, 3, 9, 2, 7, 11], 10))  # 3+7

    def test_medium_hard_case_multiple_options(self):
        self.assertTrue(subset_sum([2, 4, 6, 10, 12, 14, 16], 22))  # 6+16

    def test_hard_case_large_values_subset_exists(self):
        self.assertTrue(subset_sum([100, 200, 300, 400, 500, 600, 700, 800, 900], 2500))  # 400+500+600+1000

    def test_hard_case_no_solution(self):
        self.assertFalse(subset_sum([1000, 2000, 3000, 4000], 123))

    def test_basic_example_true(self):
        self.assertTrue(subset_sum([3, 34, 4, 12, 5, 2], 9))  # 4+5

    def test_basic_example_false(self):
        self.assertFalse(subset_sum([3, 34, 4, 12, 5, 2], 30))

    def test_basic_example_false_2(self):
        self.assertTrue(subset_sum([2, 3, 7, 8, 10], 27))

    def test_large_duplicate_set(self):
        nums = [5] * 50 + [10] * 50
        self.assertTrue(subset_sum(nums, 375))  # 25*5 + 25*10



if __name__ == '__main__':
    unittest.main()
