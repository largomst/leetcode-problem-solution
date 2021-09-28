#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
from collections import deque
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
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    def levelOrder(self, root: TreeNode):
        result = []

        def traverse(root):
            if not root:
                return

            level = 0
            queue = deque()
            queue.append(root)
            while queue:
                tmp = []
                for _ in range(len(queue)):
                    cur = queue.popleft()

                    # 前序遍历

                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                    tmp.append(cur.val)
                result.append(tmp)

        traverse(root)
        return result


# @lc code=end


root = TreeNode(
    3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))
)
r = Solution().levelOrder(root)
print(r)
