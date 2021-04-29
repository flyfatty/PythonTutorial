# @Time : 2020/10/30 16:36
# @Author : LiuBin
# @File : 542【最优序列DP】.py
# @Description : 
# @Software: PyCharm
"""01 矩阵
关键字: 多源BFS 、DP
思路:
1、以所有0元素作为根,开始BFS,自然得到与最近的0的距离 （慢！！）
2、DP：左上到右下扫一遍,右下到左上扫一遍,只看1的位置
"""
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    top = matrix[i - 1][j] if i > 0 else float("inf")
                    left = matrix[i][j - 1] if j > 0 else float("inf")
                    matrix[i][j] = min(top, left) + 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if matrix[i][j]:
                    down = matrix[i + 1][j] if i < m - 1 else float("inf")
                    right = matrix[i][j + 1] if j < n - 1 else float("inf")
                    matrix[i][j] = min(down + 1, right + 1, matrix[i][j])
        return matrix

    def updateMatrixByBFS(self, matrix: List[List[int]]) -> List[List[int]]:
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        directs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(matrix), len(matrix[0])
        q = []
        visit = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
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
                        matrix[x_][y_] = step + 1
                        q.append((x_, y_))
            step += 1
        return matrix


print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
