#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        dp = nums[:]
        for i in range(1, n):
            dp[i] = max(dp[i], nums[i] + dp[i-1])

        return max(dp)


# @lc code=end
r = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(r)
