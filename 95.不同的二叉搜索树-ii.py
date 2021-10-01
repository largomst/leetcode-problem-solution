#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

from typing import List
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def build(lo, hi):
            res = []
            if lo > hi:
                res.append(None)
                return res
            for i in range(lo, hi+1):
                leftTree = build(lo, i-1)
                rightTree = build(i+1, hi)
                for left in leftTree:
                    for right in rightTree:
                        root = TreeNode(i, left, right)
                        res.append(root)
            return res
        if n == 0:
            return []
        else:
            return build(1, n)

# @lc code=end
