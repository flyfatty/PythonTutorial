# @Time : 2021/4/14 21:25
# @Author : LiuBin
# @File : 746【最优序列DP】.py
# @Description : 
# @Software: PyCharm

"""使用最小花费爬楼梯
状态: 第i层阶梯
选择: 爬1层、爬2层
dp定义: dp[i] 到达第i层阶梯的最小花费
dp转移: dp[i] = min( dp[i-1] + cost[i-1] , dp[i-1] + cost[i-2] )
base case : dp[0] = cost[0] , dp[1] = cost[1]
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        N = len(cost)
        for i in range(2, N + 1):
            dp[0], dp[1] = dp[1], min(dp[1] + cost[i - 1], dp[0] + cost[i - 2])
        return max(dp)
