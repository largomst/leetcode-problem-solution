#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * n
        dp[0], dp[1] = 1, 2
        # dp[0] 存储的是 1 阶
        # dp[1] 存储的是 2 阶

        for i in range(2, n):  # i 从 2 开始
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

# @lc code=end


print(Solution().climbStairs(2))
