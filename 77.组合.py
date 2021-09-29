#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

from typing import List
# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(track, start):
            if len(track) == k:
                result.append(track[:])
            for i in range(start, n+1):
                track.append(i)
                backtrack(track, i+1)
                track.pop()
        track = []
        backtrack(track, 1)
        return result
# @lc code=end
