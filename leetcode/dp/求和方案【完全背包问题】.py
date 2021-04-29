# @Time : 2021/4/3 22:06
# @Author : LiuBin
# @File : 求和方案【完全背包问题】.py
# @Description : 
# @Software: PyCharm

"""
给定n、k，返回数字1-k作为元素求和为n的方案总数

可转换为 完全背包问题
状态: 重量n、可选数字i
选择： 选择/不选择i
dp定义： dp[w][i] 前i个数字里求和为w的方案数
dp转移： dp[i][w] = dp[i-1][w] + dp[i][w-i]
base case : dp[0][..] = 0 , dp[..][0] = 0 , dp[0][0] = 1
"""


class Solution:
    def dp(self, n, k):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, k + 1):
            for w in range(1, n + 1):
                if w - i >= 0:
                    dp[w] += dp[w - i]
        return dp[n]

    def frac(self, n, k):
        visit = {}

        def dfs(n, s, k):
            if (n, s) in visit:
                return visit[(n, s)]
            if n == 0:
                return 1
            elif n < 0:
                return 0
            sum_ = 0
            for i in range(s, k + 1):
                sum_ += dfs(n - i, i, k)
            visit[(n, s)] = sum_
            return sum_

        return dfs(n, 1, k)


print(Solution().frac(10, 3))
print(Solution().dp(10, 3))
