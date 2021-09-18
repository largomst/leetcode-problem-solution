#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next

        return dummy.next


# @lc code=end
