# @Time : 2020/11/5 14:02
# @Author : LiuBin
# @File : 64【最优序列DP】.py
# @Description : 
# @Software: PyCharm
"""最小路径和

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

状态：数字大小（重量）
状态: dp[i][j] 表示 走到 (i,j) 的最小路径和
转移方程: dp[i][j] = min(dp[i-1][j] , dp[i][j-1]) + grid[i][j]
进一步优化: 空间 dp[i]
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == j ==0:
                    dp[j] = grid[i][j]
                else:
                    left = dp[j - 1] if j > 0 else float('inf')
                    up = dp[j] if i > 0 else float('inf')
                    dp[j] = min(left, up) + grid[i][j]
        return dp[n - 1]


print(Solution().minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]))
