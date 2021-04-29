# @Time : 2021/4/25 21:13
# @Author : LiuBin
# @File : 87【扰乱字符串 匹配DP问题 3D】.py
# @Description : 
# @Software: PyCharm

"""扰乱字符串
上三角dp
状态： s1的第i个字符开始 和 s2第j个字符开始 ，长度为n 是否是扰乱字符串
选择： 选择 x from 0 to n , 切分n
dp转移： dp[i,j,n] = dp[i,j,x] & dp[i+x,j+x,n-x] | dp[i,j+n-x,x] & dp[i+x,j,n-x]  , x∈1,n
base case : s1[i:i+n] == s2[j:j+n]
"""


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        N = len(s1)
        dp = [[[False] * N for _ in range(N)] for _ in range(N + 1)]
        for n in range(N + 1):
            for i in range(N - 1, -1, -1):
                for j in range(N - 1, -1, -1):
                    if i + n <= N and j + n <= N:
                        dp[n][i][j] = s1[i:i + n] == s2[j:j + n]
                    for x in range(n):
                        if i + x < N and j + x < N:
                            dp[n][i][j] |= dp[x][i][j] and dp[n - x][i + x][j + x]
                        if i + x < N and j + n - x < N:
                            dp[n][i][j] |= dp[x][i][j + n - x] and dp[n - x][i + x][j]
        return dp[N][0][0]

    def isScrambleByDFS(self, s1: str, s2: str) -> bool:
        visit = {}

        def dfs(i, j, n):
            if (i, j, n) in visit: return visit[(i, j, n)]
            if s1[i:i + n] == s2[j:j + n]:
                visit[(i, j, n)] = True
                return True
            # 剪枝
            for ch in set(s1[i:i + n]):
                if s1[i:i + n].count(ch) != s2[j:j + n].count(ch):
                    return False
            flag = False
            for k in range(1, n):
                flag = flag or dfs(i, j, k) and dfs(i + k, j + k, n - k) \
                       or dfs(i, j + n - k, k) and dfs(i + k, j, n - k)
                if flag: break
            visit[(i, j, n)] = flag
            return flag

        return dfs(0, 0, len(s1))


rs = Solution().isScramble("great", "rgeat")
print(rs)
