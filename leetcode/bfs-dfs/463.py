# @Time : 2020/10/30 11:21
# @Author : LiuBin
# @File : 463.py
# @Description : 
# @Software: PyCharm
"""岛屿的周长
关键字: BFS 、 智力题
思路:
1、找到任意岛屿位置,开始BFS,遇到0或者边界就加1,否则加入队列继续搜索
2、从左到右、从上到下遍历数组，遇到1则检查上或者左是否也是1，消除重复边界。周长=总岛屿*4 - 重复边界*2
"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        counter = dup_counter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    counter += 1
                    if i > 0: dup_counter += grid[i - 1][j]
                    if j > 0: dup_counter += grid[i][j - 1]
        return 4 * counter - 2 * dup_counter

    def islandPerimeterByBFS(self, grid: List[List[int]]) -> int:
        directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        flag = True
        q = []
        visit = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if flag:
                for j in range(n):
                    if grid[i][j] == 1:
                        q.append((i, j))
                        flag = False
                        break
        visit.add(q[0])
        count = 0
        while q:
            x, y = q.pop(0)
            for sx, sy in directs:
                x_, y_ = x + sx, y + sy
                if not (0 <= x_ < m and 0 <= y_ < n) or grid[x_][y_] == 0:
                    count += 1
                elif (x_, y_) not in visit:
                    q.append((x_, y_))
                    visit.add((x_, y_))
        return count


print(Solution().islandPerimeter([[0, 1, 0, 0],
                                  [1, 1, 1, 0],
                                  [0, 1, 0, 0],
                                  [1, 1, 0, 0]]))
