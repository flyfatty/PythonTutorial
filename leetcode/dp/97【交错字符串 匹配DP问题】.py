# @Time : 2021/4/25 12:01
# @Author : LiuBin
# @File : 97【交错字符串 匹配DP问题】.py
# @Description : 
# @Software: PyCharm
"""交错字符串
记忆递归/DP

状态: s1截止到第i个字符、s2截止到第j个字符是否满足交错字符串
选择：选择s1[i]或s2[j]
dp转移： dp[i][j] =  dp[i-1][j] or dp[i][j-1] if s1[i] == s2[j] == s3[i+j]
                 =  dp[i-1][j] if s1[i] == s3[i+j]
                 =  dp[i][j-1] if s2[j] == s3[i+j]
base case : dp[0][0] = True , 其他False
"""


class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3: return False
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        dp[0][0] = True
        for i in range(1, l1 + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i-1][0]
        for j in range(1, l2 + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = dp[0][j-1]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]

        return dp[l1][l2]

    def isInterleaveByDFS(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        visit = {}

        def dfs(i, j):
            if (i, j) in visit:
                return visit[(i, j)]
            if i + j == len(s3):
                return True
            status = False
            if i < len(s1) and j < len(s2) and s1[i] == s2[j] == s3[i + j]:
                status = dfs(i + 1, j) or dfs(i, j + 1)
            elif i < len(s1) and s1[i] == s3[i + j]:
                status = dfs(i + 1, j)
            elif j < len(s2) and s2[j] == s3[i + j]:
                status = dfs(i, j + 1)
            visit[(i, j)] = status
            return visit[(i, j)]

        return dfs(0, 0)


s1 = "abababab"
s2 = "babababab"
s3 = "ababababbabababab"

print(Solution().isInterleave(s1, s2, s3))
