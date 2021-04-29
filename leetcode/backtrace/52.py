# @Time : 2020/10/20 18:18
# @Author : LiuBin
# @File : 52.py
# @Description : 
# @Software: PyCharm
"""n皇后 II
关键字: DFS、回溯
思路:
1、暴力穷举即可
2、注意合法条件
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_valid(x, y, map):
            for i, m in enumerate(map):
                if m[y] == 'Q' or y - (x - i) >= 0 and m[y - (x - i)] == 'Q' or y + (x - i) < n and m[
                    y + (x - i)] == 'Q':
                    return False
            return True

        ret = 0

        def dfs(x, map):
            nonlocal n, ret
            if x == n:
                ret += 1
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


print(Solution().totalNQueens(4))
