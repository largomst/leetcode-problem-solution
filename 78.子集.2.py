#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List
count = 0
# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []

        def backtrack(track, nums, start):
            res.append(track[:])
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(track, nums, i + 1)
                track.pop()

        backtrack(track, nums, 0)
        return res


# @lc code=end

Solution().subsets([1, 2, 3])
