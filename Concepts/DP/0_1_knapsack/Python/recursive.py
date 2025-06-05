# ⏱ Time Complexity:
# Exponential: O(2^n)

# Each item has two choices: include or exclude → total of 2^n combinations.

# W == capacity
def knapsack_01(n, W, weights, values):

    if n == 0 or W == 0:
        return 0 # this could be the max profit

    # If the weight of the last item is more than the remaining capacity, skip it
    if weights[n-1] > W:
        return knapsack_01(n-1, W, weights, values)


    include = values[n-1] + knapsack_01(n-1, W-weights[n-1], weights, values)

    exclude = knapsack_01(n-1, W, weights, values)

    return max(include, exclude)


import unittest

class TestKnapsack01(unittest.TestCase):
    def test_case_1(self):
        n, W = 3, 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        self.assertEqual(knapsack_01(n, W, weights, values), 220)

    def test_case_2_single_item_fits(self):
        n, W = 1, 10
        weights = [10]
        values = [100]
        self.assertEqual(knapsack_01(n, W, weights, values), 100)

    def test_case_3_single_item_too_heavy(self):
        n, W = 1, 5
        weights = [10]
        values = [100]
        self.assertEqual(knapsack_01(n, W, weights, values), 0)

    def test_case_4_all_items_fit(self):
        n, W = 4, 10
        weights = [1, 2, 3, 4]
        values = [10, 20, 30, 40]
        self.assertEqual(knapsack_01(n, W, weights, values), 100)

    def test_case_5_best_value_per_weight(self):
        n, W = 3, 5
        weights = [4, 2, 3]
        values = [10, 4, 7]
        self.assertEqual(knapsack_01(n, W, weights, values), 11)

    def test_case_6_zero_capacity(self):
        n, W = 4, 0
        weights = [1, 2, 3, 4]
        values = [10, 20, 30, 40]
        self.assertEqual(knapsack_01(n, W, weights, values), 0)

    def test_case_7_zero_capacity(self):
        n, W = 4, 5
        weights = [5, 4, 2, 3]
        values = [10, 40, 30, 50]
        self.assertEqual(knapsack_01(n, W, weights, values), 80)



if __name__ == '__main__':
    unittest.main()
