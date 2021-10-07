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
        memo = {}

        def dp(coins, amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if memo.get(amount):
                return memo[amount]

            res = inf
            for coin in coins:
                subProblem = dp(coins, amount - coin)
                if subProblem == -1:
                    continue
                res = min(res, subProblem+1)

            memo[amount] = res
            return -1 if res == inf else res
        return dp(coins, amount)


# @lc code=end
