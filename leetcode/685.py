# @Time : 2020/10/16 18:25
# @Author : LiuBin
# @File : 685.py
# @Description : 
# @Software: PyCharm

from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        status = {}
        for pre, post in edges:
            if post not in status:
                status[post] = 0
            if pre not in status:
                status[pre] = 0
            status[post] += 1

        return []


print(Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]))
