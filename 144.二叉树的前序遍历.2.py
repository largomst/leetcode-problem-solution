#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

from collections import deque
from typing import List


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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = [root]

        cur = root
        while stack:
            cur = stack.pop()
            if cur:
                result.append(cur.val)
            else:
                continue
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return result


# @lc code=end

tree = TreeNode(5, TreeNode(4, TreeNode(2), TreeNode(1)), TreeNode(6))
r = Solution().preorderTraversal(tree)
print(r)
