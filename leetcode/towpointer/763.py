# @Time : 2020/10/22 22:27
# @Author : LiuBin
# @File : 763.py
# @Description : 
# @Software: PyCharm

"""划分字母区间
关键字: 双指针 + 贪心
"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = {}
        for i, s in enumerate(S):
            last_index[s] = i
        start = end = 0
        res = []
        for i, s in enumerate(S):
            end = max(last_index[s], end)
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
