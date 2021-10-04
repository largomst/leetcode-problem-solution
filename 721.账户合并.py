#
# @lc app=leetcode.cn id=721 lang=python3
#
# [721] 账户合并
#
from collections import defaultdict
from curses.ascii import SO
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        email_to_account = {}
        for i,  account in enumerate(accounts):
            name, *emails = account
            for email in emails:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i
                # print(email, uf.find(i))
                # print(uf.parent)
        accountDict = defaultdict(set)
        for i, account in enumerate(accounts):
            root = uf.find(i)
            name, *emails = account
            for email in emails:
                accountDict[root].add(email)
        result = []
        # print(accountDict)
        for index, emails in accountDict.items():
            record = []
            record.append(accounts[index][0])
            record.extend(sorted(list(emails)))
            result.append(record)
        return result


        # @lc code=end
r = Solution().accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                              ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])

print(r)
# r = Solution().accountsMerge([["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"], ["Ethan",
#                                                                                                                                            "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"], ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]])
