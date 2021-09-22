#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

from typing import List
# @lc code=start


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        hashmap = {}
        for num in nums2:
            while stack and num > stack[-1]:
                key = stack.pop()
                hashmap[key] = num
            stack.append(num)
        while stack:
            hashmap[stack.pop()] = -1

        return [hashmap[num] for num in nums1]


# @lc code=end
r = Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
print(r)
assert r == [-1, 3, -1]
r = Solution().nextGreaterElement([2, 4], [1, 2, 3, 4])
print(r)
assert r == [3, -1]
