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
            global count
            # print(' '*4*count, f'args {track}, {start}')

            res.append(track[:])  # 遍历过程的每个结点都要放到 res 中

            for i in range(start, len(nums)):
                track.append(nums[i])
                count += 1
                backtrack(track, nums, i + 1)
                count -= 1
                track.pop()

        backtrack(track, nums, 0)
        return res


# @lc code=end

Solution().subsets([1, 2, 3])
