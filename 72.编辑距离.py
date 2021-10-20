#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        # dp[i][j] 表示以 i-1 结尾的 s 的字符串前缀 s' 到以 j-1 结尾的 t 的字符串前缀 t' 的最短距离
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = min(
                    dp[i-1][j-1] if s[i-1] == t[j-1] else dp[i-1][j-1]+1,
                    dp[i-1][j]+1,
                    dp[i][j-1]+1
                )
        return dp[m][n]
 # @lc code=end
