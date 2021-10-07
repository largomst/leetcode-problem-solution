#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
#
from collections import deque


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
    def isCompleteTree(self, root: TreeNode) -> bool:
        def traverse(root):
            q = deque()
            q.append(root)
            found = False
            while q:
                size = len(q)
                for i in range(size):
                    cur = q.popleft()
                    if found and cur:
                        return False
                    if cur == None:
                        found = True
                        continue
                    q.append(cur.left)
                    q.append(cur.right)
            return True

        return traverse(root)


# @lc code=end
