#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

from typing import List
# @lc code=start


def heapify(heap: List[int], index: int, heapSize: int):
    left = index * 2 + 1
    while left < heapSize:
        if left+1 < heapSize and heap[left+1] > heap[left]:
            largest = left+1
        else:
            largest = left
        if heap[largest] > heap[index]:
            heap[largest], heap[index] = heap[index], heap[largest]
            index = largest
        else:
            break
        left = index * 2 + 1


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n-1, -1, -1):
            heapify(nums, i, n)
        while k > 1:
            nums[0] = nums[n-1]
            heapify(nums, 0, n)
            n -= 1
            k -= 1

        return nums[0]


# @lc code=end
# assert 5 == Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
assert -1 == Solution().findKthLargest([-1, 2, 0], 3)
