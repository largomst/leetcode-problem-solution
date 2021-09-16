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
        if not headA or not headB:
            return None

        curA = headA
        curB = headB
        n = 0

        while curA.next:
            curA = curA.next
            n += 1

        while curB.next:
            curB = curB.next
            n -= 1

        if curA != curB:
            return None
        else:
            if n > 0:
                curA, curB = headA, headB
            else:
                curA, curB = headB, headA

            for _ in range(abs(n)):
                curA = curA.next
            while True:
                if curA == curB:
                    return curA
                else:
                    curA = curA.next
                    curB = curB.next


# @lc code=end

l1 = ListNode(4)
l1.next = ListNode(1)
l1.next.next = ListNode(8)
l1.next.next.next = ListNode(4)
l1.next.next.next .next = ListNode(5)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(1)
l2.next.next.next = l1.next.next


Solution().getIntersectionNode(l1, l2)
