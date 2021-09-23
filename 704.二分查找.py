#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

from typing import List
# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

# @lc code=end


print(Solution().search([0, 1, 2, 3, 4, 5], 3))
