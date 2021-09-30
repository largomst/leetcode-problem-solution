#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def traverse(root):
            if not root:
                return

            traverse(root.right)
            self.sum += root.val
            root.val = self.sum
            traverse(root.left)
        traverse(root)
        return root


# @lc code=end
