# @Time : 2020/11/13 17:47
# @Author : LiuBin
# @File : 365.py
# @Description : 
# @Software: PyCharm
"""

"""
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z: return False
        if z in (0, x, y, x + y): return True

        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)

        return z % gcd(x, y) == 0

    def canMeasureWaterByBFS(self, x: int, y: int, z: int) -> bool:
        if x + y < z: return False
        if z in (x, y, x + y, 0): return True
        drop_x = lambda x_, y_: (0, y_)
        drop_y = lambda x_, y_: (x_, 0)
        fill_x = lambda x_, y_: (x, y_)
        fill_y = lambda x_, y_: (x_, y)
        x_to_y = lambda x_, y_: (max(0, x_ + y_ - y), min(x_ + y_, y))
        y_to_x = lambda x_, y_: (min(x_ + y_, x), max(x_ + y_ - x, 0))
        choices = [drop_x, drop_y, fill_x, fill_y, x_to_y, y_to_x]
        q = [(0, 0)]
        visit = set()
        while q:
            size = len(q)
            for _ in range(size):
                cur_x, cur_y = q.pop(0)
                if z in (cur_x, cur_y, cur_x + cur_y):
                    return True
                visit.add((cur_x, cur_y))
                for transform in choices:
                    next_x, next_y = transform(cur_x, cur_y)
                    if (next_x, next_y) not in visit:
                        q.append((next_x, next_y))
        return False
