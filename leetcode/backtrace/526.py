# @Time : 2020/10/20 18:25
# @Author : LiuBin
# @File : 526.py
# @Description : 
# @Software: PyCharm
""" 优美的排列
关键字: DFS 、回溯
思路:
1、合法条件需要用深度index判断
2、dfs需要添加深度index参数
"""


class Solution:
    def countArrangement(self, N: int) -> int:
        ret = 0

        def dfs(arr, index):
            if not arr:
                nonlocal ret
                ret += 1
                return
            for i, v in enumerate(arr):
                if (index + 1) % v == 0 or v % (index + 1) == 0:
                    dfs(arr[:i] + arr[i + 1:], index + 1)

        dfs(list(range(1, N + 1)), 0)
        return ret


print(Solution().countArrangement(3))
