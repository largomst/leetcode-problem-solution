#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
from typing import List
# @lc code=start


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        # dp[j] 表示凑成金额 j 需要的最大金币组合数
        dp[0] = 1
        for i in coins:
            for j in range(i, amount+1):
                dp[j] += dp[j-i]
                # print(dp)
        return dp[amount]


# @lc code=end

Solution().change(5, [1, 2, 5])
