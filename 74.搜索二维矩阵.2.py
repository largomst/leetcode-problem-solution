#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#


from typing import List
# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = row*col - 1
        while l <= r:
            mid = (l+r)//2
            element = matrix[mid//col][mid % col]
            if target == element:
                return True
            elif target < element:
                r = mid - 1
            else:
                l = mid + 1
        return False
# @lc code=end


r = Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
r = Solution().searchMatrix([[1]], 0)
print(r)
