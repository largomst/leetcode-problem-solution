#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import List
# @lc code=start


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def one_to_zero(grid, row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                if grid[row][col] == "1":
                    grid[row][col] = "0"
                    one_to_zero(grid, row, col+1)
                    one_to_zero(grid, row, col-1)
                    one_to_zero(grid, row-1, col)
                    one_to_zero(grid, row+1, col)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    one_to_zero(grid, row, col)

        return count


# @lc code=end

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
r = Solution().numIslands(grid)
print(r)
