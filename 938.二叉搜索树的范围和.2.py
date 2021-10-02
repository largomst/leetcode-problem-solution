#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def rangeSumBST(root):
            res = 0
            if not root:
                return 0
            leftSum = rangeSumBST(root.left)
            rightSum = rangeSumBST(root.right)
            res = leftSum + rightSum
            if low <= root.val <= high:
                res += root.val
            return res
        return rangeSumBST(root)


# @lc code=end
