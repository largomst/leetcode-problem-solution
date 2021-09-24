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
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return binarySearch(matrix[mid], target) != -1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
# @lc code=end


r = Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
r = Solution().searchMatrix([[1]], 0)
print(r)
