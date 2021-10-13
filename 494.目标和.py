#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

from typing import List
# @lc code=start


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = []

        def backtrack(track, i):
            if len(nums) == i:
                if sum(track) == target:
                    res.append(1)
                return

            track.append(-nums[i])
            backtrack(track, i+1)
            track.pop()

            track.append(nums[i])
            backtrack(track, i+1)
            track.pop()

        track = []
        backtrack(track, 0)

        return sum(res)

# @lc code=end


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
