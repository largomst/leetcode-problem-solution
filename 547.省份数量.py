#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
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

    def getSize(self, p):
        return self.size[p]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
                    # print(uf.count)
        return uf.count
# @lc code=end


Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
