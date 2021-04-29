# @Time : 2021/4/11 22:28
# @Author : LiuBin
# @File : 【01背包问题】.py
# @Description : 
# @Software: PyCharm

from typing import List


class Solution():
    """
    空间复杂度 O(W)  状态压缩
    时间复杂度 O(NW)
    """
    def bag01(self, W: int, wt: List[int], val: List[int]) -> int:
        N = len(wt)
        dp = [0] * (W + 1)
        for i in range(1, N + 1):
            for w in range(W, 0, -1):
                if w - wt[i - 1] >= 0:
                    dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])
        return dp[W]


print(Solution().bag01(4, [1, 2, 3], [2, 2, 3]))
# 物品有两个属性：重量wt、价值val
# 优化目标：求限制总重量下的最大价值-->限制背包重量+n个可选物品=动态规划问题
# 状态： 背包容量w 可选物品i
# 选择： 装/不装
# dp定义： dp[i][w] 背包容量w能够装前i个物品的最大价值  dp[N][W]
# base case: dp[0][..] = dp[..][0] = 0
# 为什么这么定义： 为了方便状态转移，这是套路
