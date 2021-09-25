#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s or len(s) < k:  # 面试时注意提问边界条件
            return 0

        vowels = set('aeiou')
        result = 0
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
            result = max(result, count)

        # print(result)
        for i in range(k, len(s)):
            out = s[i-k]
            in_ = s[i]
            print(out, in_)
            if out in vowels:
                count -= 1
            if in_ in vowels:
                count += 1
            result = max(result, count)

        return result


# @lc code=end
# r = Solution().maxVowels('abciiidef', 3)
# print(r)

r = Solution().maxVowels('zazzzzzzz', 1)
print(r)
