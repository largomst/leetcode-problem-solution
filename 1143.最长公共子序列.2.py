#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

from pprint import pprint
# @lc code=start


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # base case
        dp = [[0 for j in range(n+1)]
              for i in range(m+1)]  # 考虑边界情况，将 dp 数组扩大一点
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:  # 适应扩大的 dp 产生的偏移
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        pprint(dp, width=15)
        return dp[m][n]


# @lc code=end
r = Solution().longestCommonSubsequence('abcde', 'ace')
assert r == 3

r = Solution().longestCommonSubsequence('abc', 'def')
assert r == 0
