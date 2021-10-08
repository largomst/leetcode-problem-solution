#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # base case
        dp = [1]*n  # dp[i] 表示以 nums[i] 结尾的递增子序列的长度
        dp[0] = 1  # 以 nums[1] 结尾的递增子序列长度是 1
        for i in range(n):
            for j in range(i):
                # 找到那些结尾比 nums[i] 小的序列，将 nums[i] 接到末尾，
                # 从所有可能中找到最大的那个。
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)  #
        return max(dp)
# @lc code=end
