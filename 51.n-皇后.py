#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

from typing import List
# @lc code=start


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def isValid(board, row, col):
            # 每行只有一个皇后，不需要判断

            # 检查列
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # 检查左上
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # 检查右上
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(board: List[List[str]], row: int):
            # 每一行都放完了皇后，记录棋盘
            if row == n:
                board = [''.join(row) for row in board]
                result.append(board)
                return
            for col in range(n):
                # 判断当前位置是否会被其他皇后攻击
                if not isValid(board, row, col):
                    continue
                # 做选择
                board[row][col] = 'Q'
                # 到下一行放皇后
                backtrack(board, row+1)
                # 撤销选择
                board[row][col] = '.'

        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(board, 0)
        return result


# @lc code=end
Solution().solveNQueens(4)
