#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

from typing import List
# @lc code=start


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        amount = sum(nums)
        if amount % 2 == 1:
            return False
        target = amount // 2
        dp = [0] * (target+1)  # dp[j] 表示容量为 j 的背包能容纳的最大数值之和。
        dp[0] = 0  # base case
        for i in range(n):
            for j in range(target, nums[i]-1, -1):  # 从后向前遍历，要保证 j-nums[i] >=0
                dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
        return dp[target] == target


# @lc code=end
r = Solution().canPartition([1, 5, 11, 5])
print(r)
