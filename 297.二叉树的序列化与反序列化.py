#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

from typing import Deque, List
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
SEP = ','
NULL = '#'


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def traverse(root, sb):
            if not root:
                sb.append(NULL)
                sb.append(SEP)
                return

            sb.append(str(root.val))
            sb.append(SEP)

            traverse(root.left, sb)
            traverse(root.right, sb)

        sb = []
        traverse(root, sb)
        return ''.join(sb)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.strip(',').split(',')
        nodes = deque(data)

        def deserializer(nodes):
            if not nodes:
                return None

            first = nodes.popleft()
            if first == NULL:
                return None
            root = TreeNode(int(first))
            root.left = deserializer(nodes)
            root.right = deserializer(nodes)

            return root

        return deserializer(nodes)

# @lc code=end
