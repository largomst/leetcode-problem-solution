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
        dp = [[1 if i == 0 or j == 0 else 0
               for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


# @lc code=end
print(Solution().uniquePaths(3, 2))
