#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

from typing import Optional, List
from unittest import result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memory = {}
        res = []

        def traverse(root):
            if not root:
                return '#'

            left = traverse(root.left)
            right = traverse(root.right)

            subTree = left + ',' + right + ',' + str(root.val)

            freq = memory.get(subTree, 0)
            # 重复的子树只会加入到 res 中一次

            if freq == 1:
                res.append(root)

            memory[subTree] = freq + 1

            return subTree

        traverse(root)
        return res

# @lc code=end
