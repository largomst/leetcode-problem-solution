#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBST(root, min, max):
            if not root:
                return True
            if min and root.val <= min.val:
                return False
            if max and max.val <= root.val:
                return False
            return isValidBST(root.left, min, root) and isValidBST(root.right, root, max)
        return isValidBST(root, None, None)


# @lc code=end
