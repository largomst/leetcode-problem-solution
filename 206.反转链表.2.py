#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev = None
        cur = head
        while cur.next:
            next_next = cur.next.next
            cur.next.next = head
            head = cur.next
            cur.next = next_next
        return head


# @lc code=end
