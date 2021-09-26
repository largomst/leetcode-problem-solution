#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start

DEBUG = False
if DEBUG:
    count = 0


class Solution:
    def maxSubArray(self, nums) -> int:
        def getCrossLargest(nums, l, r):
            mid = (l+r)//2
            leftSum = 0
            leftLargrst = -float('inf')
            for i in range(mid, l-1, -1):
                leftSum += nums[i]
                leftLargrst = max(leftLargrst, leftSum)
            rightSum = 0
            rightLargest = -float('inf')
            for i in range(mid+1, r+1):
                rightSum += nums[i]
                rightLargest = max(rightLargest, rightSum)
            return rightLargest + leftLargrst

        def maxSubArray(nums, l, r):
            if DEBUG:
                global count
                print('     '*count, f'args {nums[l:r+1]}')
            if l == r:
                if DEBUG:
                    print('     '*count, f'return {nums[l]}')
                return nums[l]
            else:
                mid = (l+r)//2
                if DEBUG:
                    count += 1
                leftLargest = maxSubArray(nums, l, mid)
                rightLargest = maxSubArray(nums, mid+1, r)
                crossLargest = getCrossLargest(nums, l, r)
                if DEBUG:
                    count -= 1
                largest = max(leftLargest, rightLargest, crossLargest)

                if DEBUG:
                    print('     '*count, f'return {largest}')
                return largest
        return maxSubArray(nums, 0, len(nums)-1)


# @lc code=end

Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
