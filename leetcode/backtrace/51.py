# @Time : 2020/10/20 16:05
# @Author : LiuBin
# @File : 51.py
# @Description : 
# @Software: PyCharm
"""n皇后
关键字: DFS、回溯
思路:
1、暴力穷举即可
2、注意合法条件

"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def is_valid(x, y, map):
            for i, m in enumerate(map):
                if m[y] == 'Q' or y - (x - i) >= 0 and m[y - (x - i)] == 'Q' or y + (x - i) < n and m[
                    y + (x - i)] == 'Q':
                    return False
            return True

        ret = []

        def dfs(x, map):
            nonlocal n
            if x == n:
                ret.append([''.join(m) for m in map])
                return
            map.append(['.'] * n)
            for y in range(n):
                if is_valid(x, y, map):
                    map[x][y] = 'Q'
                    dfs(x + 1, map)
                    map[x][y] = '.'
            map.pop()

        dfs(0, [])
        return ret


print(Solution().solveNQueens(4))
