#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#


count = 0


def printIndent(n):
    for _ in range(n):
        print('    ', end='')


# @lc code=start

def reverseString(s, l, r):
    # global count
    # printIndent(count)
    # print(f'args {l} {r}')
    if l >= r:
        # printIndent(count)
        # print('return')
        return
    else:
        # count += 1
        reverseString(s, l+1, r-1)
        # count -= 1
        s[l], s[r] = s[r], s[l]
        # printIndent(count)
        # print(s)

        # printIndent(count)
        # print('return')
        return


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        reverseString(s, 0, len(s)-1)

# @lc code=end


l = ["h", "e", "l", "l", "o"]

reverseString(l, 0, len(l)-1)
