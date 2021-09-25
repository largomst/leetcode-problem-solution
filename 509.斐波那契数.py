#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start

def fib(n: int):
    return n if n < 2 else fib(n-1) + fib(n-2)


class Solution:
    def fib(self, n: int) -> int:
        return fib(n)
# @lc code=end
