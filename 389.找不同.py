#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
from collections import Counter


def counter(s: str) -> dict:
    hashmap = {}
    for c in s:
        if hashmap.get(c, None):
            hashmap[c] += 1
        else:
            hashmap[c] = 1
    return hashmap


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap_s = counter(s)
        hashmap_t = counter(t)
        for k, _ in hashmap_s.items():
            hashmap_t[k] -= hashmap_s[k]
        for k, v in hashmap_t.items():
            if v == 1:
                return k

# @lc code=end


Solution().findTheDifference("abcd", "abcde")
