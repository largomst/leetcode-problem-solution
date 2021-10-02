#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.ans = -float('inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def oneSideMax(root):
            if not root:
                return 0
            left = max(0, oneSideMax(root.left))
            right = max(0, oneSideMax(root.right))

            self.ans = max(self.ans, root.val+left+right)
            return max(root.val+left, root.val + right)
        oneSideMax(root)
        return self.ans


# @lc code=end
