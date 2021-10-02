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
            q = deque()

            visited = set()

            step = 0
            q.append('0000')
            while q:
                size = len(q)
                for i in range(size):
                    cur = q.popleft()

                    if cur in deadends:
                        continue
                    if cur == target:
                        return step
                    print(cur)

                    for i in range(4):
                        up = upOne(cur, i)
                        if up not in visited:
                            q.append(up)
                            visited.add(up)
                        down = downOne(cur, i)
                        if down not in visited:
                            q.append(down)
                            visited.add(down)

                step += 1
            return -1
        return dfs(set(deadends), target)
# @lc code=end


r = Solution().openLock(["0201", "0101", "0102", "1212", "2002"],
                        "0202")

print(r)
