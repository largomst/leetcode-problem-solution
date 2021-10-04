#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

from typing import List
# @lc code=start

count = 0


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m = len(board)
        n = len(board[0])

        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = '#'
            if board[i][n-1] == 'O':
                board[i][n-1] = '#'

        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = '#'
            if board[m-1][j] == 'O':
                board[m-1][j] = '#'

        d = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(board, i, j):
            if 0 <= i < m and 0 <= j < n:
                if board[i][j] == 'O':
                    if '#' in (board[i+1][j], board[i-1][j], board[i][j-1], board[i][j+1]):
                        board[i][j] = '#'
                        for k in range(4):
                            dfs(board, i+d[k][0], j+d[k][1])

        for i in range(1, m-1):
            for j in range(1, n-1):
                dfs(board, i, j)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == '#':
                    board[i][j] = 'O'


# @lc code=end

r = Solution().solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
                     )
print(r)
