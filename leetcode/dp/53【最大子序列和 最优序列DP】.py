# @Time : 2020/11/9 12:37
# @Author : LiuBin
# @File : 53【最大子序列和 最优序列DP】.py
# @Description : 
# @Software: PyCharm
"""最大子序列和
关键字: DP、贪心
思路1:
1、dp[i] 以a[i]为结尾的最大子数组和
2、dp[i] = max( 0, dp[i-1] ) + a[i]
思路2:
1、维护最大值max_ 和 sum_
2、max_ = max( max_ , max( 0, sum_ ) + a[i] ) ; 初始化 max_ = a[0]
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_, sum_ = nums[0], 0
        for num in nums:
            sum_ = max(sum_, 0) + num
            max_ = max(max_, sum_)
        return max_


print(Solution().maxSubArray([-2]))
