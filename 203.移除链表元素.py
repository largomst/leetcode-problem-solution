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
        if not head:
            return None

        prev = None
        cur = head
        while cur:
            if cur.val == val:
                if prev == None:
                    head = head.next
                    cur = head
                else:
                    prev.next = cur.next
                    cur = prev.next
            else:
                prev = cur
                cur = cur.next

        return head


# @lc code=end
