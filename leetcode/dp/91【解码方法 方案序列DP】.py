# @Time : 2021/4/21 0:07
# @Author : LiuBin
# @File : 91【解码方法 方案序列DP】.py
# @Description : 
# @Software: PyCharm

"""解码方法
状态: 截止到第i个字符有多少种解码方法
选择: 选择最后两位、选择最后一位
dp定义： dp[i] = x  截止到i字符共有x中解码方案
dp转移： dp[i] = dp[i-1] if s[i-1] in 1,9 + dp[i-2] if s[i-2:i] in 1,26 else 0
base case : dp[0] = 1
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1]
        N = len(s)
        for i in range(1, N + 1):
            dp.append(0)
            dp[i] += dp[i - 1] if s[i - 1] != '0' else 0
            dp[i] += dp[i - 2] if i - 2 >= 0 and s[i - 2] != '0' and 1 <= int(s[i - 2:i]) <= 26 else 0
            if dp[i] == 0: return 0
        return dp[N]


print(Solution().numDecodings("06"))
