#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start

count = 0


def printIndend(n):
    # print(f'{n:-02}', end='')
    for _ in range(n):
        print('    ', end='')


class Solution:
    def fib(self, n: int) -> int:
        global count
        printIndend(count)
        print('args', n)
        count += 1  # 在此之后执行的递归调用层级加一

        if n < 2:
            count -= 1  # 本层的递归掉调用层级需要减一
            printIndend(count)
            print(f'return {n}')
            return n
        else:
            r = self.fib(n-1)+self.fib(n-1)
            count -= 1
            printIndend(count)
            print(f'return {r}')
            return r


# @lc code=end
Solution().fib(4)
