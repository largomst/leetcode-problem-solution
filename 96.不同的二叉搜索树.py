#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
from collections import defaultdict


class Solution:

    def numTrees(self, n: int) -> int:
        memo = defaultdict(lambda: defaultdict(int))

        def count(lo, hi):
            if lo > hi:
                return 1
            if memo[lo][hi] != 0:
                return memo[lo][hi]

            res = 0
            for i in range(lo, hi+1):
                left = count(lo, i-1)
                right = count(i+1, hi)
                res += left * right
            memo[lo][hi] = res
            return res
        return count(1, n)


# @lc code=end
r = Solution().numTrees(3)
print(r)
