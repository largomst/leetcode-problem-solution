#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
from typing import Optional


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
    def __init__(self):
        self.res = 0
        self.rank = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(root):
            if not root:
                return a
            traverse(root.left)
            # 中序遍历
            self.rank += 1
            if self.rank == k:
                self.res = root.val
                return
            traverse(root.right)
        traverse(root)
        return self.res
# @lc code=end
