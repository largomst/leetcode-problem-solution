#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = set()
        c1 = headA
        while c1:
            visited.add(c1)
            c1 = c1.next
        c2 = headB
        found = None
        while c2:
            if c2 in visited:
                found = c2
                break
            c2 = c2.next
        return found


# @lc code=end
