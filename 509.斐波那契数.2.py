#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start


class Solution:
    def fib(self, n: int) -> int:
        F = [0, 1]
        for i in range(2, n+1):
            F.append(F[i-1] + F[i-2])
        return F[n]


# @lc code=end
