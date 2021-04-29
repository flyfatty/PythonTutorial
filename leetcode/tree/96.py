# @Time : 2020/10/14 14:12
# @Author : LiuBin
# @File : 96.py
# @Description : 
# @Software: PyCharm
"""不同的二叉搜索树
关键字: 记忆化递归
思路:
1、设定好最小问题的边界值
2、问题依次放大，用子问题的结果解决大问题
3、使用访问字典记录访问过的结果，防止重复计算
"""


class Solution:
    visit = {0: 1, 1: 1}

    def numTrees(self, n: int) -> int:
        s = 0
        if n in self.visit:
            return self.visit[n]
        for i in range(1, n + 1):
            s += self.numTrees(i - 1) * self.numTrees(n - i)
        self.visit[n] = s
        return s


print(Solution().numTrees(5))
