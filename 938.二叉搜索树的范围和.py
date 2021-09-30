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
    def __init__(self) -> None:
        self.sum = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def traverse(root):
            if not root:
                return

            traverse(root.left)

            # 中序遍历
            if low <= root.val <= high:
                self.sum += root.val

            traverse(root.right)
        traverse(root)
        return self.sum


# @lc code=end
