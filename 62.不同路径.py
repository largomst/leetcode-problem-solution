#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#


from collections import defaultdict
count = 0
# @lc code=start


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(lambda: defaultdict(lambda: None))

        def dfs(board, i, j):
            if i == 0 and j == 0:
                memo[0][0] = 1
                return 1
            if not (0 <= i < m and 0 <= j < n):
                memo[i][j] = 0
                return 0
            if memo[i][j] != None:
                return memo[i][j]

            paths = dfs(board, i-1, j) + dfs(board, i, j-1)
            memo[i][j] = paths
            return paths
        board = [[None for j in range(n)] for i in range(m)]
        return dfs(board, m-1, n-1)

# @lc code=end


Solution().uniquePaths(3, 2)
