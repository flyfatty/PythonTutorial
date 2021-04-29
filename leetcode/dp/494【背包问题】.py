# @Time : 2020/11/5 16:51
# @Author : LiuBin
# @File : 494【背包问题】.py
# @Description : 
# @Software: PyCharm
"""目标和

状态：  重量（数字）、物品（前i个数字）
选择：  符号（+-）
dp定义： dp[i][w] 前i个数字求和组成w的方案数
dp转移： dp[i][w] = dp[i-1][w-nums[i-1]] + dp[i-1][w+nums[i-1]]  # 状态压缩：影响两端：滚动数组
base case :  dp[..][0] = 0 , dp[0][0] = 1

关键字: 记忆化搜索、DP
思路:DP
1、dp[i][j] 前i个元素目标和是j的方案总数
2、dp[i][j] = dp[i-1][j-a[i]] + dp[i-1][j+a[i]]  , dp[0][0] = 1
3、空间优化: 因为第一维只和前一个索引有关,j和上一层的左右两边都有关，所以使用滚动数组  dp[j] = dp[j-a[i]] + dp[j+a[i]]   dp[0] = 1
4、由于涉及到负数  amount = sum(nums)  索引范围 -amount --> amount
   由于dp[-j] = dp[j] (正负对称性），索引范围只需要 0-amoount即可 dp[j] = dp[abs(j-a[i])] + dp[j+a[i]]
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        N = len(nums)
        amount = sum(nums)
        if abs(S) > amount: return 0 # 剪枝
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(1,N+1):
            temp_dp = [0] * (amount + 1)
            for j in range(1,amount + 1):
                left = dp[j - nums[i-1]] if j - nums[i-1] >= 0 else 0
                right = dp[j + nums[i-1]] if j + nums[i-1] <= 2 * amount else 0
                temp_dp[j] = left + right
            dp = temp_dp
        return dp[S + amount]

    def findTargetSumWaysByDFS(self, nums: List[int], S: int) -> int:
        n = len(nums)
        visit = {}

        def dfs(i, s):
            if (i, s) in visit:
                return visit[(i, s)]
            if i == n:
                return 1 if s == 0 else 0
            visit[(i, s)] = dfs(i + 1, s - nums[i]) + dfs(i + 1, s + nums[i])
            return visit[(i, s)]

        return dfs(0, S)


print(Solution().findTargetSumWays([1000], -1000))
