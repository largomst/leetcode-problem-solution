#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None

        result = []

        def backtrack(track, nums):
            if len(track) == len(nums):
                result.append(track[:])
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(track, nums)
                track.pop()
        track = []
        backtrack(track, nums)
        return result

# @lc code=end
