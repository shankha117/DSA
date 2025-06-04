from itertools import product
import unittest
def rod_cutting(prices: list[int], n: int):

    # l = remaining length of the ROD

    N = len(prices)
    length = [x for x in range(1, N+1)]


    # Recursive
    # def rod_cutting_unbounded(n, l):

    #     if n == 0 or l == 0:
    #         return 0

    #     # if the Rods current length is more than the last item of the available length Length[1-n] then skip the last
    #     # valid length
    #     if length[n-1] > l:
    #         return rod_cutting_unbounded(n-1, l)

    #     # cut a piece from the rod of length Length[1-n] ; so subtract the length Length[1-n] from the rod
    #     # take the price of the piece of size Length[1-n]
    #     # but we can again take the same length Length[1-n] , so pass again n
    #     include = prices[n-1] + rod_cutting_unbounded(n, l - length[n-1])

    #     exclude = rod_cutting_unbounded(n-1, l)

    #     return max(include, exclude)

    # return rod_cutting_unbounded(N, n)


    dp = [[0]*(n+1) for _ in range(N+1)]


    for i,j in product(range(1, N+1), range(1, n+1)):

        # if the last item is more than the remianing length then skip that item
        if length[i-1] > j:
            dp[i][j] = dp[i-1][j]

        else:
            include = prices[i-1] + dp[i][j-length[i-1]]

            exclude = dp[i-1][j]


            dp[i][j] = max(include, exclude)

    print(dp)

    return dp[N][n]



class TestRodCutting(unittest.TestCase):
    def test_case_1(self):
        # prices for lengths 1 to 4: [1, 5, 8, 9]
        # Best way: 2 cuts of length 2 (5 + 5 = 10)
        self.assertEqual(rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8), 22)

    # def test_case_2(self):
    #     # prices for lengths 1 to 8
    #     # Optimal: 2+6 = 5+17 = 22
    #     self.assertEqual(rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8), 22)

    # def test_case_3(self):
    #     # prices: [2, 5, 7, 8] for lengths 1 to 4
    #     # For length 10 → best is 5 cuts of length 2: 5×5 = 25
    #     self.assertEqual(rod_cutting([2, 5, 7, 8], 10), 25)

    # def test_case_4(self):
    #     # length = 1, only one piece possible
    #     self.assertEqual(rod_cutting([3], 1), 3)

    # def test_case_5(self):
    #     # prices all zero
    #     self.assertEqual(rod_cutting([0, 0, 0, 0], 4), 0)

    # def test_case_6(self):
    #     # prices: [1, 5, 8] → best: 3 cuts of length 2 = 3×5 = 15
    #     self.assertEqual(rod_cutting([1, 5, 8], 6), 16)

    # def test_case_7(self):
    #     # prices: [2, 3, 7] → best: 3 cuts of length 2 = 3×3 = 9
    #     self.assertEqual(rod_cutting([2, 3, 7], 6), 14)

    # def test_case_8(self):
    #     # zero length rod
    #     self.assertEqual(rod_cutting([1, 2, 3], 0), 0)

    # def test_case_9(self):
    #     # prices: [2, 5, 8, 9, 10] → best: length 2 + 3 = 5 + 8 = 13
    #     self.assertEqual(rod_cutting([2, 5, 8, 9, 10], 5), 13)

if __name__ == "__main__":
    unittest.main()
