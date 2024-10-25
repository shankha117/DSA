
# https://leetcode.com/problems/search-a-2d-matrix/description/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        t, b = 0, ROWS - 1

        row = None

        while t <= b:

            mid = t + (b-t) // 2

            if target > matrix[mid][-1]:

                t = mid + 1
            elif target < matrix[mid][0]:
                b = mid - 1
            else:
                row = mid
                break

        if row == None:
            return False

        l,r = 0 , COLS - 1

        while l <= r:

            mid = l + (r-l) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
