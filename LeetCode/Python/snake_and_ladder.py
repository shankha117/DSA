from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        length = len(board)

        def intToPos(square):
            r = (length - 1) - (square - 1) // length
            c = (square - 1) % length
            if (length - 1 - r) % 2 == 1:  # row is reversed
                c = length - 1 - c
            return [r, c]

        q = deque()
        q.append([1, 0])  # [square, moves]
        visit = set()
        visit.add(1)

        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1
