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
        cur = head
        visited = set()
        found = False
        while cur:
            if cur in visited:
                found = True
                break
            visited.add(cur)
            cur = cur.next
        return found


# @lc code=end
