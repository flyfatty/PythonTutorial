# @Time : 2021/3/29 21:27
# @Author : LiuBin
# @File : 木板覆盖.py
# @Description : 
# @Software: PyCharm
"""绳子覆盖（1D）、木板覆盖（2D）
1、n绳子，使用指定的 2、3长的绳子覆盖，最少需要多少根绳子  line_cover
状态：
2、mxn矩阵，使用指定的1x2,2x3的小矩阵覆盖，最少需要多少块
理论依据是:任何可覆盖的方案一定存在 从某一个位置垂直或水平可切分

状态：模板大小 m、n
选择：垂直或水平切分模板后哪两个子木板容器
dp转移: dp[i][j] = min( dp[i][j] , dp[i-x][j] + dp[x][j] 或 dp[i][j-y] + dp[i][j] ) x <= i , y<=j 水平/垂直切分
base case：符合基础木板大小的木板容器设置为1 ，其他设置为inf
trick： 木板方向提前转换，接下来无需考虑木板方向
"""
from math import ceil

def line_cover(n, ss):
    dp = [0]
    for i in range(1, n + 1):
        dp.append(float('inf'))
        for s in ss:
            if i - s >= 0:
                dp[-1] = min(dp[i - s] + 1, dp[-1])
    return dp[n] if dp[n] != float('inf') else -1


def matrix_cover(m, n, squares):
    squares = set(squares)
    squares.update({(y, x) for x, y in squares})
    dp = [[float("inf")] * (n + 1) for _ in range(0, m + 1)]
    for x, y in squares:
        if x <= m and y <= n:
            dp[x][y] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for x in range(1, ceil((i + 1) / 2)):
                dp[i][j] = min(dp[i][j], dp[i - x][j] + dp[x][j])
            for y in range(1, ceil((j + 1) / 2)):
                dp[i][j] = min(dp[i][j], dp[i][j - y] + dp[i][y])
    return dp[m][n]


print(line_cover(12, [10, 5]))
print(matrix_cover(4, 4, [(1, 3), (2, 2)]))
