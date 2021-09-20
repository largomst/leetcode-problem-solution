#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

from typing import List
# @lc code=start


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        stack = []
        for num in nums1:
            found = False
            max = -1
            while nums2 and not found:
                top = nums2.pop()  # nums2 作为一个栈，取栈顶元素
                if top > num:
                    max = top
                if top == num:
                    found = True
                stack.append(top)
            while stack:
                nums2.append(stack.pop())
            result.append(max)
        return result


# @lc code=end
r = Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
assert r == [-1, 3, -1]
