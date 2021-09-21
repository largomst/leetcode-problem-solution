#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        hashmap = [0]*26
        for c in s:
            hashmap[ord(c)-97] -= 1
        for c in t:
            hashmap[ord(c)-97] += 1
        return chr(hashmap.index(1)+97)


# @lc code=end

Solution().findTheDifference("abcd", "abcde")
