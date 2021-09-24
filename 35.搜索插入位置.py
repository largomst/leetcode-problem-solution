#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

from typing import List
# @lc code=start


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid+1
        if nums[l] < target:
            return l + 1
        else:
            return l

# @lc code=end


assert 3 == Solution().searchInsert([0, 1, 2, 4, 5, 6], 3)
