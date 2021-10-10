#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] 两个字符串的最小ASCII删除和
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        memo = [[-1 for j in range(n)] for i in range(m)]

        def dp(s1: str, i: int, s2: str, j: int) -> int:
            # 返回 s1[i...] 和 s2[j...] 删除相同字符需要的次数

            res = 0
            # base case
            if i == m:
                while j < n:
                    res += ord(s2[j])
                    j += 1
                return res
            if j == n:
                while i < m:
                    res += ord(s1[i])
                    i += 1
                return res

            if memo[i][j] != -1:
                return memo[i][j]

            if s1[i] == s2[j]:
                memo[i][j] = dp(s1, i+1, s2, j+1)

            else:
                memo[i][j] = min(
                    ord(s1[i]) + dp(s1, i+1, s2, j),
                    ord(s2[j]) + dp(s1, i, s2, j+1)
                )
            return memo[i][j]

        return dp(s1, 0, s2, 0)


# @lc code=end
print(Solution().minimumDeleteSum(
    'sea', 'eat'
))
