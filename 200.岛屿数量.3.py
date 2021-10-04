#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import List
# @lc code=start


class UnionFind:
    def __init__(self, n) -> None:
        self._count = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootQ == rootP

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        else:
            if self.size[rootP] < self.size[rootQ]:
                self.parent[rootP] = rootQ
                self.size[rootQ] += self.size[rootP]
            else:
                self.parent[rootQ] = rootP
                self.size[rootP] += self.size[rootQ]
            self._count -= 1

    @property
    def count(self):
        return self._count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        uf = UnionFind(m*n+1)
        dummy = m*n
        d = ((0, 1), (1, 0), (0, -1), (-1, 0))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for k in range(4):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            uf.union(i*n+j, x*n+y)
                if grid[i][j] == '0':
                    uf.union(i*n+j, dummy)
        return uf.count - uf.size[dummy]


# @lc code=end
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
r = Solution().numIslands(grid)
assert r == 3
