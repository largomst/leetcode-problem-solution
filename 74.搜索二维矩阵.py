#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#


from typing import List
# @lc code=start


def binarySearch(nums: List[int], target) -> int:
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid-1
    return -1


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                if binarySearch(row, target) != -1:
                    return True
        return False

# @lc code=end
