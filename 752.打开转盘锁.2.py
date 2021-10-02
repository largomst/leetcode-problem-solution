#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def downOne(s: str, i):
            slist = list(s)
            if slist[i] == '0':
                slist[i] = '9'
            else:
                slist[i] = chr(ord(slist[i])-1)
            return ''.join(slist)

        def upOne(s, i):
            slist = list(s)
            if slist[i] == '9':
                slist[i] = '0'
            else:
                slist[i] = chr(ord(slist[i])+1)
            return ''.join(slist)

        def dfs(deadends, target):
            q1 = set()
            q2 = set()
            visited = set()
            step = 0

            q1.add('0000')
            q2.add(target)

            # visited.add('0000')
            # visited.add(target)

            while len(q1) != 0 and len(q2) != 0:

                temp = set()
                for cur in q1:
                    if cur in deadends:
                        continue
                    if cur in q2:
                        return step
                    visited.add(cur)
                    for i in range(4):
                        up = upOne(cur, i)
                        if up not in visited:
                            # visited.add(up)
                            temp.add(up)
                        down = downOne(cur, i)
                        if down not in visited:
                            # visited.add(down)
                            temp.add(down)
                step += 1
                q1 = q2
                q2 = temp

            return -1

        return dfs(set(deadends), target)
# @lc code=end


r = Solution().openLock(["0201", "0101", "0102", "1212", "2002"],
                        "0202")

print(r)
