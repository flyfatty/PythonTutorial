# @Time : 2020/10/28 19:18
# @Author : LiuBin
# @File : 62【方案序列DP】.py
# @Description : 
# @Software: PyCharm
"""不同路径
从矩阵左上角到右下角的不同路径数量

关键字: DP
思路:
1、填充m*n矩阵
2、dp[i][j] = dp[i-1][j] + dp[i][j-1]
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[n - 1]


print(Solution().uniquePaths(18, 18))
