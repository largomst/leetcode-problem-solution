#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
from pprint import pprint
from typing import List
# @lc code=start


def count(s):
    zeroNum = sum([1 for c in s if c == '0'])
    oneNum = len(s) - zeroNum
    return zeroNum, oneNum


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        # dp[i][j] 的定义是最多有 i 个 0 和 j 个 1 的子集的最大大小为 dp[i][j]
        for ch in strs:
            zeroNum, oneNum = count(ch)
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if i-zeroNum >= 0 and j-oneNum >= 0:
                        dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
                    # else:
                        # break
            # pprint(dp, width=15)
        return dp[m][n]

        pass

# @lc code=end


print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
