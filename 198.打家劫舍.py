#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
import time
from typing import List
count = 0

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+2)
        dp[2] = nums[0]
        # base case
        # dp[i] 表示偷窃房屋 i 到之前房屋带来的总金额
        for i in range(n):
            index = i + 2
            dp[index] = max(dp[index-2] + nums[i], dp[index-1])
        return dp[-1]

# @lc code=end


r = Solution().rob([1, 2, 3, 1])
print(r)
r = Solution().rob([2, 7, 9, 3, 1])
print(r)
