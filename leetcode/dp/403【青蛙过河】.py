# @Time : 2021/4/16 9:11
# @Author : LiuBin
# @File : 403【青蛙过河】.py
# @Description : 
# @Software: PyCharm
"""青蛙过河
1、记忆化搜索
2、集合DP
状态: 第i个石头跳到下一个石头可以走步的k集合
选择: k-1/k/k+1
"""
from typing import List
from collections import defaultdict


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)
        dp = defaultdict(set)
        dp[0] = {0}
        for stone in stones:
            for step in dp[stone]:
                for d in [-1, 0, 1]:
                    if step + d > 0 and stone + step + d in stones_set:
                        dp[stone + step + d].add(step + d)
        return len(dp[stones[-1]]) > 0

    def canCrossByDFS(self, stones: List[int]) -> bool:
        stones_set = set(stones)
        visit = {}

        def dfs(pos, step):
            if (pos, step) in visit: return visit[(pos, step)]
            if pos == stones[-1]: return True
            for d in [-1, 0, 1]:
                if step + d > 0 and pos + step + d in stones_set:
                    if dfs(pos + step + d, step + d):
                        visit[(pos, step)] = True
                        return True
            visit[(pos, step)] = False
            return False

        return dfs(0, 0)


print(Solution().canCrossByDFS([0, 1, 3, 6, 7, 8, 9]))
print(Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11]))
print(Solution().canCrossByDFS([0, 2]))
