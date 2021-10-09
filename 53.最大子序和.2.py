#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        dp_0 = nums[0]
        res = dp_0
        for i in range(1, n):
            dp_i = max(nums[i], nums[i] + dp_0)
            dp_0 = dp_i
            res = max(res, dp_i)

        return res


# @lc code=end
r = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(r)
