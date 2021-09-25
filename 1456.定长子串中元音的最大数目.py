#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s:
            return 0

        result = 0
        l = r = total = 0
        while r < len(s) and r - l + 1 <= k:
            # print(l-r+1)
            if s[r] in 'aeiou':
                total += 1
                result = max(result, total)
            r += 1
        # print(total)
        while r < len(s):
            # print(total)
            if s[r] in 'aeiou':
                total += 1
                # print(total)
            if s[l] in 'aeiou' and l != r:
                total -= 1
            result = max(result, total)
            r += 1
            l += 1

        return result


# @lc code = end
