#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#

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
        return rootP == rootQ

    def union(self, p, q):
        rootP = self.parent[p]
        rootQ = self.parent[q]
        if rootP == rootQ:
            return
        else:
            if self.size[rootP] < self.size[rootQ]:
                self.parent[rootP] = rootQ
                self.size[rootQ] += self.size[rootQ]
            else:
                self.parent[rootQ] = rootP
                self.size[rootP] += self.size[rootQ]
            self._count -= 1

    @property
    def count(self):
        return self._count


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        a = ord('a')
        for eq in equations:
            p, q = eq[0], eq[3]
            if eq[1] == '=':
                uf.union(ord(p) - a, ord(q)-a)

        for eq in equations:
            p, q = eq[0], eq[3]
            if eq[1] == '!':
                if uf.connected(ord(p)-a, ord(q)-a):
                    return False
        return True


# @lc code=end
