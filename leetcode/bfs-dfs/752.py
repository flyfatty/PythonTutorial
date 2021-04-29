# @Time : 2020/10/24 20:38
# @Author : LiuBin
# @File : 752.py
# @Description : 
# @Software: PyCharm
"""打开转盘锁
关键字: 双向BFS
思路:
1、典型的BFS
2、优雅小技巧: 禁止访问的密码列表可以初始化为visited集合
3、因为知道终点,可以优化为双向BFS,因为涉及到交集来判断是否相遇,添加visit需要滞后添加
4、双向BFS小优化: q1和q2每次访问数量少的集合，而非交替
"""
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def plus_one(s, i):
            ls = list(s)
            if ls[i] == '9':
                ls[i] = '0'
            else:
                ls[i] = str(int(ls[i]) + 1)
            return ''.join(ls)

        def minus_one(s, i):
            ls = list(s)
            if ls[i] == '0':
                ls[i] = '9'
            else:
                ls[i] = str(int(ls[i]) - 1)
            return ''.join(ls)

        visited = set(deadends)
        q1, q2 = set(), set()
        q1.add("0000")
        q2.add(target)
        step = 0
        while len(q1) > 0 and len(q2) > 0:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            temp = set()
            for cur in q1:
                if cur in visited:
                    continue
                if cur in q2:
                    return step
                visited.add(cur)
                for j in range(4):  # 四位数分别操作
                    up = plus_one(cur, j)
                    if up not in visited:
                        temp.add(up)
                    down = minus_one(cur, j)
                    if down not in visited:
                        temp.add(down)

            step += 1
            q1 = temp
        return -1


print(Solution().openLock(["0000"], target="8888"))
