#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
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


# count = 0


# def printIndent(n):
#     print('    '*n, end='')


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def build(nums, l, r) -> TreeNode:
            # global count
            # printIndent(count)
            # print(f'{l}, {r}')
            if l > r:  # 考虑输入一个元素的时候
                return

            # 找到最大值
            maxVal = -float('inf')
            maxIndex = l
            for i in range(l, r+1):
                if nums[i] > maxVal:
                    maxVal = nums[i]
                    maxIndex = i

            # 构造根结点
            root = TreeNode(maxVal)
            # 找到左孩子的最大值
            # count += 1
            root.left = build(nums, l, maxIndex-1)
            # 找到右孩子的最大值
            root.right = build(nums, maxIndex + 1, r)
            # count -= 1

            return root
        return build(nums, 0, len(nums)-1)
# @lc code=end
