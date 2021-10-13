#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

from typing import List
# @lc code=start


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        choices = range(n)

        res = []

        def backtrack(track: set, choices: List[int]):
            print(track)
            sum1 = sum(nums[i] for i in track)
            sum2 = sum(nums[i] for i in choices if i not in track)
            if sum1 == sum2:
                res.append(track.copy())
                return

            for choice in choices:
                if choice in track:
                    continue
                track.add(choice)
                backtrack(track, choices)
                track.remove(choice)
        track = set()
        backtrack(track, choices)
        if res:
            return True
        else:
            return False


# @lc code=end
r = Solution().canPartition([1, 5, 11, 5])
print(r)
