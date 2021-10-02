#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def bfs(root):
            if not root:
                return 0

            queue = deque()
            depth = 1

            queue.append(root)

            while queue:
                size = len(queue)
                for i in range(size):
                    cur = queue.popleft()
                    if not cur.left and not cur.right:  # 到达叶子
                        return depth
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                depth += 1
        return bfs(root)


# @lc code=end
