# @Time : 2020/10/27 18:22
# @Author : LiuBin
# @File : 1293.py
# @Description : 
# @Software: PyCharm
"""网格中的最短路径
关键字: BFS
思路:
1、因为可以障碍物,地图扩成三维数组，第三维记录消除障碍物的数量
2、小优化：如果可消除障碍物的大于m+n-3，直接可以走最少步数,即 m+n-2
"""
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        directs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        if k >= m + n - 3:
            return m + n - 2

        def is_valid(x, y):
            nonlocal m, n
            return m > x >= 0 and n > y >= 0

        q = [(0, 0, 0)]
        visit = set()
        visit.add((0, 0, 0))
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y, z = q.pop(0)

                if (x, y) == (m - 1, n - 1):
                    return step

                for sx, sy in directs:
                    x_, y_ = x + sx, y + sy
                    if is_valid(x_, y_):
                        if grid[x_][y_] == 0:
                            if (x_, y_, z) not in visit:
                                q.append((x_, y_, z))
                                visit.add((x_, y_, z))
                        elif z < k:
                            if (x_, y_, z + 1) not in visit:
                                q.append((x_, y_, z + 1))
                                visit.add((x_, y_, z + 1))
            step += 1
        return -1


print(Solution().shortestPath(
    [[0, 0, 0],
     [1, 1, 0],
     [1, 0, 0],
     [0, 1, 1],
     [0, 0, 0]], k=1))
