#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap = {}
        for c in t:
            if hashmap.get(c, None):
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        for c in s:
            hashmap[c] -= 1
        for k, v in hashmap.items():
            if v == 1:
                return k

# @lc code=end


Solution().findTheDifference("abcd", "abcde")
