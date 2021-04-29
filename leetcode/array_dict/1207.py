# @Time : 2020/10/29 11:31
# @Author : LiuBin
# @File : 1207.py
# @Description : 
# @Software: PyCharm
"""独一无二的出现次数
关键字: 哈希表
"""
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mm = {}
        ss = set()
        for a in arr:
            if a not in mm:
                mm[a] = 0
            mm[a] += 1
        for v in mm.values():
            if v in ss:
                return False
            ss.add(v)
        return True


print(Solution().uniqueOccurrences([1, 2]))
