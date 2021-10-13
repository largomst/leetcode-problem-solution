#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

count = 0
# @lc code=start


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+2)
        # base case
        dp[2] = 1
        dp[3] = 2
        for i in range(4, n+1):
            for j in range(1, i-1):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
                print(dp)
        return dp[n]


# @lc code=end
print(Solution().integerBreak(10))
print(Solution().integerBreak(2))
