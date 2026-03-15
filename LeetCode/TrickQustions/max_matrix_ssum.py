# https://leetcode.com/problems/maximum-matrix-sum/description/?envType=daily-question&envId=2026-01-05

from itertools import product
from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        mat_min = float("inf")
        max_sum = 0
        neg_count = 0

        for i, j in product(range(len(matrix)), range(len(matrix[0]))):
            cell = matrix[i][j]

            max_sum += abs(cell)
            mat_min = min(mat_min, abs(cell))

            if cell < 0:
                neg_count += 1

        if neg_count & 1:  # if this is odd
            max_sum -= mat_min * 2

        return max_sum
