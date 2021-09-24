#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
from typing import List

# @lc code=start


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
            print(l, r)
        return l


# @lc code=end
l = [1, 2, 1, 3, 5, 6, 4]
r = Solution().findPeakElement(l)
print(r)
