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
        prev_1 = prev_2 = 0

        # base case
        # dp[i] 表示偷窃房屋 i 到之前房屋带来的总金额
        for i in range(n):
            dp = max(prev_1 + nums[i], prev_2)
            prev_1, prev_2 = prev_2, dp
        return dp

# @lc code=end


r = Solution().rob([1, 2, 3, 1])
print(r)
r = Solution().rob([2, 7, 9, 3, 1])
print(r)
