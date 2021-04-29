# @Time : 2020/11/4 22:22
# @Author : LiuBin
# @File : 322【完全背包问题】.py
# @Description : 
# @Software: PyCharm

"""零钱兑换
给定无线（物品，重量），组成amount的最少物品数

状态：重量w , 可选物品i
选择： 选择/不选择物品
dp定义： dp[i][w] 前i个物品可以组成w重量的最少物品数
dp转移： dp[i][w] = min(dp[i-1][w],dp[i][w-coins[i-1]]+1)
base case：dp[0][..] = -1 , dp[..][0] = 0

思路
1、最少数量，想到BFS,但是会超时
2、记忆化搜索: 利用DFS缩小问题规模,返回每个规模的最少硬币数
3、DP: dp[i] = min(dp[t-i] + 1 , dp[i])
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        for w in range(1, amount + 1):
            dp.append(float('inf'))
            for coin in coins:
                if w - coin >= 0:
                    dp[w] = min(dp[w], dp[w - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


    def coinChangeByDFS(self, coins: List[int], amount: int) -> int:
        visit = {}

        def dfs(amount):
            if amount in visit:
                return visit[amount]
            if amount == 0: return 0
            if amount < 0: return -1
            res = float('inf')
            for coin in coins:
                sub_res = dfs(amount - coin)
                if sub_res == -1: continue
                res = min(res, sub_res + 1)
            visit[amount] = -1 if res == float('inf') else res
            return visit[amount]

        return dfs(amount)

    def coinChangeByBFS(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        q = [amount - coin for coin in coins if amount - coin >= 0]
        step = 1
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.pop(0)
                if cur == 0: return step
                for coin in coins:
                    if cur - coin >= 0:
                        q.append(cur - coin)
            step += 1
        return -1


print(Solution().coinChange(coins=[2], amount=3))
