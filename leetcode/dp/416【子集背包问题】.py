# @Time : 2021/4/11 23:41
# @Author : LiuBin
# @File : 416【子集背包问题】.py
# @Description : 
# @Software: PyCharm

"""分割等和子集（子集背包问题）
转换成 W是sum/2 N个物品的背包问题
状态： 求和sum、可选数字
选择： 选择/不选择数字
dp定义： dp[i][w] 前i个数字求和是否恰好是w
base case: dp[0][..] = false ; dp[..][0] = true
dp转移: dp[i][w] = dp[i-1][w] or dp[i-1][w-nums[i-1]]

"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 == 1: return False
        N = len(nums)
        dp = [False] * (sum_ // 2 + 1)
        dp[0] = True
        for i in range(1, N + 1):
            for w in range(sum_ // 2, 0, -1):
                if w - nums[i - 1] >= 0:
                    dp[w] = dp[w] or dp[w - nums[i - 1]]
        return dp[sum_ // 2]


res = Solution().canPartition([1, 5, 11, 5])
print(res)
