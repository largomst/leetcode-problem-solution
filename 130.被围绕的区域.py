#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

from typing import List
# @lc code=start


class UnionFind:
    def __init__(self, n) -> None:
        self._count = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    @property
    def count(self):
        return self._count

    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def connected(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

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


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m = len(board)
        n = len(board[0])
        uf = UnionFind(m*n+1)
        dummy = m*n  # 用于作为边缘的 O 的根

        # 判断首行、末行和首列和末列中的 O
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(i*n, dummy)
            if board[i][n-1] == 'O':
                uf.union(i*n + n-1, dummy)
        for j in range(n):
            if board[0][j] == 'O':
                uf.union(j, dummy)
            if board[m-1][j] == 'O':
                uf.union((m-1)*n+j, dummy)

        d = ((0, 1), (1, 0), (0, -1), (-1, 0))

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    for k in range(4):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if board[x][y] == 'O':
                            uf.union(x*n+y, i*n+j)

        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O' and not uf.connected(i*n+j, dummy):
                    board[i][j] = 'X'


# @lc code=end
if __name__ == '__main__':
    uf = UnionFind(10)
    # find
    assert uf.find(0) == 0
    # union
    uf.union(0, 1)
    assert uf._count == 9
    # connected
    assert uf.connected(0, 1)
    assert not uf.connected(0, 2)
