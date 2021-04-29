# @Time : 2021/4/12 0:14
# @Author : LiuBin
# @File : 518【完全背包问题】.py
# @Description : 
# @Software: PyCharm

"""零钱兑换II
转换为 完全背包问题（无限物品）
状态： amount 金额 w 、 coins 可选硬币 i
选择： 是否选择第i个面值的硬币
dp定义： dp[i][w] 前i个物品组成重量为w的方案数
目标： dp[N][amount] 总方案数
dp转移： dp[i][w] = dp[i-1][w] + dp[i][w-coins[i-1]]
base case: dp[0][..] = 0 , dp[..][0] = 1
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(1, N + 1):
            for w in range(1, amount + 1):
                if w - coins[i - 1] >= 0:
                    dp[w] += dp[w - coins[i - 1]]
        return dp[amount]
