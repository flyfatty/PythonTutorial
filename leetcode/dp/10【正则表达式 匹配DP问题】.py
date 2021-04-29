# @Time : 2020/10/21 16:21
# @Author : LiuBin
# @File : 10【正则表达式 匹配DP问题】.py
# @Description : 
# @Software: PyCharm
"""正则表达式

关键字: 回溯 、 DP
思路:
1、DFS + 回溯
    单元素匹配:  p[0] in ( s[0] , '.')
    *匹配:  匹配空串 or p[0] in ( s[0] , '.') and 匹配一个单元素
2、记忆化递归
    思路1改成索引表示,方便记忆状态
3、DP  两个序列都是有序的，需要考虑两个状态
    状态：dp[i][j]  截止到s[i] p[j]是否匹配
    选择：*匹配
        dp[i][j] |= dp[i][j-2] or dp[i-1][j] and p[i-1] in ( s[i] , '.' ) # 不匹配任何元素 / 匹配一个元素
        单元素匹配
        dp[i][j] = dp[i-1][j-1] and p[i] in ( s[i] , '.' )
        不匹配
        保持False

"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # init
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        # init s 为空串
        for j in range(1, n + 1):
            # 若 p 的第 j 个字符 p[j - 1] 是 '*'
            # 说明第 j - 1、j 位可有可无
            # 那么如果前 j - 2 个已经匹配上，前 j 个也可以匹配上
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in (s[i - 1], '.'):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] |= dp[i][j - 2]
                    if p[j - 2] in (s[i - 1], '.'):
                        dp[i][j] |= dp[i - 1][j]
        return dp[m][n]

    def isMatchByDFS(self, s: str, p: str) -> bool:
        len_s, len_p = len(s), len(p)
        visit = {}

        def dfs(si, pi):
            if (si, pi) in visit:
                return visit[(si, pi)]
            flag = False
            if si == len_s and pi == len_p:
                return True
            if pi < len_p - 1 and p[pi + 1] == "*":
                flag = dfs(si, pi + 2) or si < len_s and p[pi] in (s[si], '.') and dfs(si + 1, pi)
            elif si < len_s and pi < len_p and (p[pi] in (s[si], '.')):
                flag = dfs(si + 1, pi + 1)
            visit[(si, pi)] = flag
            return flag

        return dfs(0, 0)


print(Solution().isMatch("aa", "a*"))
