import unittest
from typing import List
from itertools import product

def unbounded_knapsack(n: int, W: int, values: List[int], weights: List[int]) -> int:


    # from functools import lru_cache
    # # recursive Solution
    # def solve(w,n):
    #     if n==0 or w == 0:
    #         return 0 # this could be the max profit

    #     # If the weight of the last item is more than the remaining capacity, skip it
    #     if weights[n-1] > w:
    #         return solve(w, n-1)


    #     include = values[n-1] + solve(w-weights[n-1], n)

    #     exclude = solve(w, n-1)

    #     return max(include, exclude)

    # return solve(W,n)

    dp = [[0]*(W+1) for _ in range(n+1)]

    for i, j in product(range(1, n+1), range(W+1)):

        # If the weight of the last item is more than the remaining capacity, skip it
        if weights[i-1] > j:
            dp[i][j] = dp[i-1][j]

        else:

            include = values[i-1] + dp[i][j-weights[i-1]]

            exclude = dp[i-1][j]

            dp[i][j] = max(include, exclude)

    return dp[n][W]

class TestUnboundedKnapsack(unittest.TestCase):
    def test_case_1(self):
        # Pick 3 items of weight 2 and value 10 -> total 30
        self.assertEqual(unbounded_knapsack(2, 6, [10, 12], [2, 3]), 30)

    def test_case_2(self):
        # Optimal: pick 2 items of weight 4 (value 50) = 100
        self.assertEqual(unbounded_knapsack(3, 8, [10, 40, 50], [1, 3, 4]), 100)

    def test_case_3(self):
        # Optimal: 2 items of weight 2 and 1 of weight 1 → 20 + 20 + 10 = 50
        self.assertEqual(unbounded_knapsack(3, 5, [10, 20, 30], [1, 2, 3]), 50)

    def test_case_4(self):
        # Optimal: 2 items of weight 3 (value 40) = 80
        self.assertEqual(unbounded_knapsack(3, 6, [10, 40, 50], [2, 3, 4]), 80)

    def test_case_5(self):
        self.assertEqual(unbounded_knapsack(3, 0, [10, 20, 30], [1, 2, 3]), 0)  # No capacity

    def test_case_6(self):
        # Best to use 10 items of weight 10 and value 50
        self.assertEqual(unbounded_knapsack(2, 100, [10, 50], [5, 10]), 500)

    def test_case_7(self):
        # Use 5 items of any weight 2 → total weight 10 → value = 50
        self.assertEqual(unbounded_knapsack(3, 10, [10, 10, 10], [2, 2, 2]), 50)

    def test_case_8(self):
        # All weights > capacity → no item can be taken
        self.assertEqual(unbounded_knapsack(3, 5, [60, 100, 120], [10, 20, 30]), 0)

    def test_case_9(self):
        # Optimal: pick (1×5 + 1×2) → total weight = 7, value = 10+4=14
        self.assertEqual(unbounded_knapsack(2, 7, [10, 4], [5, 2]), 14)

    def test_case_10(self):
        # Multiple 1-weight 1-value items → max = 10
        self.assertEqual(unbounded_knapsack(1, 10, [1], [1]), 10)

if __name__ == "__main__":
    unittest.main()
