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
        dummy = ListNode()
        dummy.next = head
        while head and head.next:  # head 作为当前结点
            dummy_next = dummy.next  # 记住头节点的位置
            dummy.next = head.next  # 将新头节点设置成当前结点的下一个结点
            head.next = head.next.next  # 将当前结点的下一个结点设置成当前结点的下下个结点
            dummy.next.next = dummy_next  # 讲新的头结点的下个结点设置成旧的头节点
        return dummy.next

# @lc code=end
