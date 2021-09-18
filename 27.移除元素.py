#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

from typing import List
# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        index = 0
        for i in range(n):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
            else:
                pass
        while len(nums) != index:
            nums.pop()
        return index

# @lc code=end
