# @Time : 2020/11/7 21:07
# @Author : LiuBin
# @File : 338【最优序列DP】.py
# @Description : 
# @Software: PyCharm
"""比特位计数
关键字: DP、位运算
动态规划：找到“相邻”的元素 转移到新的元素
思路:
1、 n & (n-1) 去掉二进制最后一个1得到的数
2、dp[i] = dp[i&(i-1)] + 1 或  dp[i] = dp[i>>2] + i%2
3、 base case:  dp[0] = 0
"""
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1, num + 1):
            dp.append(dp[i & (i - 1)] + 1)
        return dp


print(Solution().countBits(10))
