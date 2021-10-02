#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import List
# @lc code=start

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        queue = deque()
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    queue.append((row, col))
                    while queue:
                        r, c = queue.popleft()
                        if r + 1 < rows and grid[r+1][c] == '1':
                            grid[r+1][c] = "0"
                            queue.append((r+1, c))
                        if 0 <= r - 1 and grid[r-1][c] == '1':
                            grid[r-1][c] = "0"
                            queue.append((r-1, c))
                        if c+1 < cols and grid[r][c+1] == '1':
                            grid[r][c+1] = "0"
                            queue.append((r, c+1))
                        if 0 <= c-1 and grid[r][c-1] == '1':
                            grid[r][c-1] = "0"
                            queue.append((r, c-1))
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
