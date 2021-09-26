#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

from typing import List

count = 0


def printIndent(n, ):
    for _ in range(n):
        print('    ', end='')

    # @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        def majorityElement(nums, left, right):
            # global count
            # printIndent(count)
            # print(f'args {nums[left:right+1]}')

            if left == right:
                # printIndent(count)
                # print(f'return {nums[left]}')
                return nums[left]
            else:
                mid = (left + right) // 2
                # count += 1
                leftMajority = majorityElement(nums, left, mid)
                rightMajority = majorityElement(nums, mid+1, right)
                # count -= 1
                if leftMajority == rightMajority:
                    # printIndent(count)
                    # print(f'return {leftMajority}')
                    return leftMajority
                else:
                    leftCount = 0
                    rightCount = 0
                    for i in range(left, right+1):
                        if nums[i] == leftMajority:
                            leftCount += 1
                        if nums[i] == rightMajority:
                            rightCount += 1
                    # printIndent(count)
                    # print(f'leftCount {leftCount}')
                    # printIndent(count)
                    # print(f'rightCount {rightCount}')
                    if leftCount > rightCount:
                        # printIndent(count)
                        # print(f'return {leftMajority}')
                        return leftMajority
                    else:
                        # printIndent(count)
                        # print(f'return {rightMajority}')
                        return rightMajority
        return majorityElement(nums, 0, len(nums)-1)


# @lc code=end
# Solution().majorityElement([2, 2, 1, 1, 1, 2, 2])
Solution().majorityElement([8, 9, 8, 9, 8])
