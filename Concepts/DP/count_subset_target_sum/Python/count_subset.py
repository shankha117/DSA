from itertools import product
import unittest

def count_subsets(nums, target):

    #### RECURSICE SOLUTIN

    # n = len(nums)

    # def subsets(n, t):
    #     if t == 0:
    #         return 1

    #     if n == 0:
    #         return 0

    #     if nums[n-1] > t:
    #         return subsets(n-1,t)

    #     include = subsets(n-1, t- nums[n-1])

    #     exclude = subsets(n-1, t)

    #     return include + exclude


    #### BOTTOM UP

    n = len(nums)

    dp = [[0]*(target+1) for _ in range(n+1)]

    # make the first column 1
    for i in range(n):
        dp[i][0] = 1


    for i,j in product(range(1, n+1), range(1, target+1)):

        if nums[i-1] > j:
            dp[i][j] = dp[i-1][j]

        else:
            include = dp[i-1][j- nums[i-1]]

            exclude = dp[i-1][j]

            dp[i][j] = include + exclude

    return dp[n][target]



class TestCountSubsets(unittest.TestCase):

    def test_easy_cases(self):
        self.assertEqual(count_subsets([1, 2, 3], 4), 1)  # [1,3]
        self.assertEqual(count_subsets([1, 1, 1, 1], 2), 6)  # C(4,2)

    def test_medium_cases(self):
        self.assertEqual(count_subsets([2, 3, 5, 6, 8, 10], 10), 3)
        self.assertEqual(count_subsets([1, 2, 3, 3], 6), 3)
        self.assertEqual(count_subsets([5, 5, 5, 5], 10), 6)  # Pairs: (0,1),(0,2),(0,3),(1,2),(1,3),(2,3)

    def test_hard_cases(self):
        self.assertEqual(count_subsets([1]*20, 10), 184756)  # C(20,10)
        self.assertEqual(count_subsets([3, 34, 4, 12, 5, 2], 9), 2)  # [4,5], [2,3,4] not possible (invalid), only [4,5] and [2, 3, 4] if it existed

    def test_no_subsets(self):
        self.assertEqual(count_subsets([2, 4, 6], 5), 0)
        self.assertEqual(count_subsets([1, 2, 3], 7), 0)

if __name__ == "__main__":
    unittest.main()
