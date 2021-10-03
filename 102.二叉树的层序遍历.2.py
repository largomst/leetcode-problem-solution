#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(root, level):
            if not root:
                return
            if level > len(res) - 1:
                res.append([])
            res[level].append(root.val)

            if root.left:
                dfs(root.left, level+1)
            if root.right:
                dfs(root.right, level+1)

        dfs(root, 0)
        return res

# @lc code=end


root = TreeNode(
    3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))
)
r = Solution().levelOrder(root)
print(r)
