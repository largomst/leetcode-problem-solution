#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

from functools import cmp_to_key
from operator import itemgetter
from typing import List
# @lc code=start


def cmp(p, q):
    return p[1] - q[1]


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # intervals.sort(key=itemgetter(1))
        # intervals.sort(key=cmp_to_key(cmp))
        intervals.sort(key=lambda x: x[1])

        count = 1
        x_end = intervals[0][1]
        for interval in intervals:
            start = interval[0]
            if x_end <= start:
                count += 1
                x_end = interval[1]

        return len(intervals) - count

# @lc code=end


Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]])
