# @Time : 2020/10/30 17:47
# @Author : LiuBin
# @File : 1162【同542】.py
# @Description : 
# @Software: PyCharm
"""地图分析
关键字: 多源BFS 、 DP
思路:  与542题目一样
"""
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_ = -1
        for i in range(m):
            for j in range(n):
                grid[i][j] = abs(grid[i][j] - 1)  # 颠倒1和0
                if grid[i][j]:
                    top = grid[i - 1][j] if i > 0 else float("inf")
                    left = grid[i][j - 1] if j > 0 else float("inf")
                    grid[i][j] = min(top, left) + 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if grid[i][j]:
                    down = grid[i + 1][j] if i < m - 1 else float("inf")
                    right = grid[i][j + 1] if j < n - 1 else float("inf")
                    grid[i][j] = min(down + 1, right + 1, grid[i][j])
                    max_ = max(max_, grid[i][j])
        return -1 if max_ == float('inf') else max_

    def maxDistanceByBFS(self, grid: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        directs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        q = []
        visit = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    visit.add((i, j))
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.pop(0)
                for sx, sy in directs:
                    x_, y_ = x + sx, y + sy
                    if is_valid(x_, y_) and (x_, y_) not in visit:
                        visit.add((x_, y_))
                        q.append((x_, y_))
            step += 1
        return step - 1 if step > 1 else -1


print(Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
