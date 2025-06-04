# No Recursive Calls ; No Risk of StackOverflow Error
# ✅ Time Complexity: O(n * W)
# Why?
# You fill a 2D table of size n+1 x W+1 using two nested loops:

from itertools import product


def knapsack_01_bottom_up(n, W, weights, values):

    dp = [[0]*(W+1) for _ in range(n+1)]


    for i, j in product(range(1, n+1), range(W+1)):

        # If the weight of the last item is more than the remaining capacity, skip it
        if weights[i-1] > j:
            dp[i][j] = dp[i-1][j]

        else:

            include = values[i-1] + dp[i-1][j-weights[i-1]]

            exclude = dp[i-1][j]

            dp[i][j] = max(include, exclude)

    return dp[n][W]


import unittest

class TestKnapsack01(unittest.TestCase):
    def test_case_1(self):
        n, W = 3, 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        self.assertEqual(knapsack_01_bottom_up(n, W, weights, values), 220)

    def test_case_2_single_item_fits(self):
        n, W = 1, 10
        weights = [10]
        values = [100]
        self.assertEqual(knapsack_01_bottom_up(n, W, weights, values), 100)

    def test_case_3_single_item_too_heavy(self):
        n, W = 1, 5
        weights = [10]
        values = [100]
        self.assertEqual(knapsack_01_bottom_up(n, W, weights, values), 0)

    def test_case_4_all_items_fit(self):
        n, W = 4, 10
        weights = [1, 2, 3, 4]
        values = [10, 20, 30, 40]
        self.assertEqual(knapsack_01_bottom_up(n, W, weights, values), 100)

    def test_case_5_best_value_per_weight(self):
        n, W = 3, 5
        weights = [4, 2, 3]
        values = [10, 4, 7]
        self.assertEqual(knapsack_01_bottom_up(n, W, weights, values), 11)

    def test_case_6_zero_capacity(self):
        n, W = 4, 0
        weights = [1, 2, 3, 4]
        values = [10, 20, 30, 40]
        self.assertEqual(knapsack_01_bottom_up(n, W, weights, values), 0)

    def test_case_7_zero_capacity(self):
        n, W = 4, 5
        weights = [5, 4, 2, 3]
        values = [10, 40, 30, 50]
        self.assertEqual(knapsack_01_bottom_up(n, W, weights, values), 80)



if __name__ == '__main__':
    unittest.main()
