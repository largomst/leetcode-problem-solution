#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        amount = sum(stones)
        target = amount // 2
        dp = [0] * (target+1)  # dp[j] 表示容量为 j 的背包能够容纳的石头重量的最大值
        dp[0] = 0  # base case
        for i in range(0, n):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return (amount - dp[target]) - dp[target]


# @lc code=end
