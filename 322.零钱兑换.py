#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

from typing import List
# @lc code=start

inf = float('inf')


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        # print(dp)
        return -1 if dp[amount] == amount + 1 else dp[amount]


# @lc code=end
# r = Solution().coinChange([2], 3)
# r = Solution().coinChange([1, 2, 3], 11)
# r = Solution().coinChange([1, ], 0)
r = Solution().coinChange([11, ], 10)
