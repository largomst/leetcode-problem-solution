#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

from typing import List

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         n = len(nums)
#         result = float('inf')
#         for i in range(n):
#             for j in range(i+1, n+1):
#                 if sum(nums[i:j]) >= target:
#                     if j-i < result:
#                         result = j-i
#         return result if result != float('inf') else 0


# @lc code=start


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        result = float('inf')
        total = 0
        l = 0
        r = 0
        while r < len(nums):
            total += nums[r]
            r += 1
            while total >= target:
                result = min(result, r-l)
                total -= nums[l]
                l += 1
        return 0 if result == float('inf') else result


# @lc code=end
