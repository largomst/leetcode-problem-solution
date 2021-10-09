#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def get_lcs(word1, word2):
            m = len(word1)
            n = len(word2)
            dp = [[0 for j in range(n+1)] for j in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp[m][n]
        lcs = get_lcs(word1, word2)
        # print(lcs)
        return len(word1) - lcs + len(word2) - lcs


# @lc code=end
Solution().minDistance('sea', 'eat')
