#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[-1 for i in range(n)] for j in range(m)]

        def dp(s1, i, s2, j):
            # print(i, j)
            # 返回 s1[i...] 和 s[j...] 的最长公共子序列的长度

            if i == len(s1) or j == len(s2):  # 任意一个为空序列都没有结果
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            if s1[i] == s2[j]:
                return 1 + dp(s1, i+1, s2, j+1)
            else:
                res = max(dp(s1, i+1, s2, j),
                          dp(s1, i, s2, j+1))
                memo[i][j] = res
                return res
        return dp(text1, 0, text2, 0)


# @lc code=end
r = Solution().longestCommonSubsequence('abcde', 'ace')
assert r == 3

r = Solution().longestCommonSubsequence('abc', 'def')
assert r == 0
