#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

count = 0


def printIndent(n):
    for _ in range(n):
        print(' ', end='')


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # global count
        # printIndent(count)
        # print(f'args: {head.val}')
        if not head or not head.next:
            # printIndent(count)
            # print(f'return {head.val}')
            return head
        # count += 1
        last = self.reverseList(head.next)
        # count -= 1
        head.next.next = head
        head.next = None
        # printIndent(count)
        # print(f'return {head.val}')
        return last


# @lc code=end
