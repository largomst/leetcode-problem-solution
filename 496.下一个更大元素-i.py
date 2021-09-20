#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

from typing import List
# @lc code=start


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        result = []
        for x in nums1:
            index = nums2.index(x)
            for i in range(index+1, n2):
                if nums2[i] > x:
                    result.append(nums2[i])
                    break
            else:
                result.append(-1)
        return result


# @lc code=end
r = Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
assert r == [-1, 3, -1]
