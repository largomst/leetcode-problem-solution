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
        # global count
        # print(' '*4*count, f'args {nums}')
        if not nums:
            # print(' '*4*count, f'return {[]}')
            return [[]]
        n = nums.pop()
        # count += 1
        res = self.subsets(nums)
        # count -= 1
        size = len(res)
        # print(' '*4*count, f'size {size}')

        for i in range(size):
            res.append(res[i][:])
            res[-1].append(n)

        # print(' '*4*count, f'return {res}')
        return res


# @lc code=end

Solution().subsets([1, 2, 3])
