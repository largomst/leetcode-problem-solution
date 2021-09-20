#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

from typing import List
from urllib import response
# @lc code=start


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            index = nums2.index(num)
            for i in range(index, len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])
                    break
            else:
                result.append(-1)
        return result


# @lc code=end
r = Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
assert r == [-1, 3, -1]
