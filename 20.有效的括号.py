#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
BRCAETS = {
    ')': '(',
    '}': '{',
    ']': '['
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = True
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if stack:
                    if BRCAETS[c] != stack[-1]:
                        valid = False
                        break
                    else:
                        stack.pop()
                else:
                    valid = False
                    break
        if stack:
            valid = False
        return valid

# @lc code=end


assert Solution().isValid("(){}[]") == True
assert Solution().isValid("(}[]") == False
assert Solution().isValid("(((({{{[[[") == False
assert Solution().isValid(")))]]]}}}") == False
