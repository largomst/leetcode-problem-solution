#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur:
                result.append(cur.val)
            else:
                continue
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        result.reverse()
        return result

# @lc code=end
