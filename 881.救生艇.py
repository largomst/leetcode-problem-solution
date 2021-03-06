#
# @lc app=leetcode.cn id=881 lang=python3
#
# [881] 救生艇
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        while l <= r:
            amount = people[l] + people[r]
            if amount <= limit:
                l += 1
            r -= 1  # 重的总是会走
            count += 1  # 每次循环都会走一条小船
        return count


# @lc code=end
