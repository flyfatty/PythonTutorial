# @Time : 2020/11/5 12:54
# @Author : LiuBin
# @File : 70【方案序列DP】.py
# @Description : 
# @Software: PyCharm
"""爬楼梯
关键字: DP 、斐波那契数列

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        pre1, pre2 = 1, 2
        if n < 3: return n
        for i in range(3, n):
            pre1, pre2 = pre2, pre1 + pre2
        return pre1 + pre2

    def climbStairsByDFS(self, n: int) -> int:
        visit = {}

        def dfs(i):
            if i in visit: return visit[i]
            if i <= 2: return i
            visit[i] = dfs(i - 1) + dfs(i - 2)
            return visit[i]

        return dfs(n)


print(Solution().climbStairs(4))
