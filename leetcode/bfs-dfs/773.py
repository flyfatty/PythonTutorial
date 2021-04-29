# @Time : 2020/10/29 11:52
# @Author : LiuBin
# @File : 773.py
# @Description : 
# @Software: PyCharm
"""滑动谜题
关键字: BFS
思路:
1、序列化棋盘成为1维数组，每一步记录入口和棋盘，直到找到目标棋盘
"""
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        board = list(map(str, board[0] + board[1]))
        entry = [i for i, v in enumerate(board) if v == '0'][0]
        # 枚举一位数组所有映射二维数组的邻居
        neighbors = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        q = [(entry, board)]
        step = 0
        visit = set()
        visit.add(''.join(board))
        # 找到入口位置

        while q:
            size = len(q)
            for _ in range(size):
                x, board = q.pop(0)
                if ''.join(board) == "123450":
                    return step

                for neighbor in neighbors[x]:
                    cur = board[:]
                    cur[x], cur[neighbor] = cur[neighbor], cur[x]
                    serilized_board = ''.join(cur)
                    if serilized_board not in visit:
                        q.append((neighbor, cur))
                        visit.add(serilized_board)
            step += 1
        return -1


print(Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]]))
