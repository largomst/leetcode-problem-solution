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
            res = []
            while q:
                tmp = []
                size = len(q)
                for i in range(size):
                    cur = q.popleft()
                    if cur == None:
                        tmp.append('#')
                        continue
                    tmp.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
                res.append(tmp)
            found = False
            for row in res:
                for cur in row:
                    if cur == '#':
                        found = True
                    if found and cur != '#':
                        return False
            return True

        return traverse(root)


# @lc code=end
