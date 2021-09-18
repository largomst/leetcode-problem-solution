#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

from typing import List
# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        left = 0
        right = len(nums)-1
        while left < right:
            while left < right and nums[left] != val:
                left += 1
            while left < right and nums[right] == val:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] != val:
            left += 1
        return left


# @lc code=end
