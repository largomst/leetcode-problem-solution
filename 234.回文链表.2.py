#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head: ListNode) -> ListNode:
    cur = head
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            # 判断空或单个元素时的情况
            return True
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next
            fast = fast.next

        fast = slow.next
        fast = reverseList(fast)
        slow = head
        while slow and fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True


# @lc code=end
