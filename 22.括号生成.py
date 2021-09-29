#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import List

count = 0


def printIndent(n):
    print(' '*4*n, end='')


# @lc code=start

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def isValid(track):
            stack = []
            valid = True
            for i in track:
                if i == '(':
                    stack.append('(')
                else:
                    if stack:
                        stack.pop()
                    else:
                        valid = False
            if stack:
                valid = False

            return valid

        def trackback(track, i):
            # global count
            # printIndent(count)
            # print(f'args {track} {i}')

            if i == n*2:
                if isValid(track):
                    result.append(''.join(track))
                    # printIndent(count)
                    # print(f'return')
                return

            for bracket in '()':

                track.append(bracket)
                # count += 1
                trackback(track[:], i+1)
                # count -= 1
                track.pop()

        track = ['(']
        trackback(track, 1)
        return result
# @lc code=end


r = Solution().generateParenthesis(3)
print(r)
