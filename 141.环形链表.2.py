#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: 'ListNode') -> bool:
        if not head:
            return False
        s = head
        f = head
        while s and f and f.next:
            # 先判断 s 或 f 存不存在，再判断 next 存不存在
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False


# @lc code=end
