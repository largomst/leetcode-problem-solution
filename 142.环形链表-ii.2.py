#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

from comparar import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: 'ListNode') -> 'ListNode':
        slow = head
        fast = head
        while True:
            if fast is None or fast.next is None:
                return None  # 无环
            else:
                slow = slow.next
                fast = fast.next
                fast = fast.next
                if slow == fast:
                    break
        fast = head
        while fast and slow:
            if fast == slow:
                return slow
            else:
                fast = fast.next
                slow = slow.next
        return None


# @lc code=end
correct = 0
times = 500_000
for i in tqdm.tqdm(range(times)):
    gen = choice([genRandomCyclicNodeListWithIndex,
                 genRandomNodeListWithIndex])
    l, exp = gen()
    r = Solution().detectCycle(l)
    if exp == r:
        correct += 1


print('Correct rate:', correct / times*100, '%')
