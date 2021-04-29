# @Time : 2020/10/30 23:18
# @Author : LiuBin
# @File : 200.py
# @Description : 
# @Software: PyCharm
"""岛屿数量
关键字: BFS、DFS
思路:
1、遍历矩阵,一旦遇到1就开始DFS赋值为0,扫描完记录的1的次数就是岛屿数量
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(x, y):
            for sx, sy in directs:
                x_, y_ = x + sx, y + sy
                if 0 <= x_ < m and 0 <= y_ < n and grid[x_][y_] == '1':
                    grid[x_][y_] = '0'
                    dfs(x_, y_)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count


print(Solution().numIslands([["1", "1", "1"],
                             ["0", "1", "0"],
                             ["1", "1", "1"]]

                            ))
