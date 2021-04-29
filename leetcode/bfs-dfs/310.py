# @Time : 2020/10/26 12:59
# @Author : LiuBin
# @File : 310.py
# @Description : 
# @Software: PyCharm
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        node_map = [[0] * n for i in range(n)]
        for n1, n2 in edges:
            node_map[n1][n2] = 1
            node_map[n2][n1] = 1
        