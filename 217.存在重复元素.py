#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        duplicated = False
        for num in nums:
            if num in visited:
                duplicated = True
                break
            else:
                visited.add(num)
        return duplicated
# @lc code=end
