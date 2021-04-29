# @Time : 2021/4/28 22:07
# @Author : LiuBin
# @File : 639【解码方法II】.py
# @Description : 
# @Software: PyCharm


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1]
        N = len(s)
        for i in range(1, N + 1):
            dp.append(0)
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
                if s[i - 1] == '*':
                    dp[i] += 9 - 1
            if i - 2 >= 0:
                if s[i - 1] != '*' and s[i - 2] == '*':
                    dp[i] += dp[i - 2] + 2 - 1
                elif s[i - 1] != '*' and s[i - 2] not in ('*', '0') and int(s[i - 2:i]) <= 26:
                    dp[i] += dp[i - 2]
                elif s[i - 1] == '*' == s[i - 2]:
                    dp[i] += dp[i - 2] + 17 - 1
                elif s[i - 1] == '*':
                    if s[i - 2] == '1':
                        dp[i] += dp[i - 2] + 10 - 1
                    elif s[i - 2] == '2':
                        dp[i] += dp[i - 2] + 7 - 1
        return dp[N]


print(Solution().numDecodings("1*"))
