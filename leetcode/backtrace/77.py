# @Time : 2020/10/21 9:48
# @Author : LiuBin
# @File : 77.py
# @Description : 
# @Software: PyCharm
"""组合
关键字: 回溯
思路:
1、元素前后顺序无关,只需要传递数组之后的元素
2、到达指定长度path就可以把path添加进结果
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        if n == 0 or k == 0:
            return []

        def backtrace(nums, path):
            nonlocal k
            if len(path) == k:
                ret.append(path[:])
                return
            for i, num in enumerate(nums):
                path.append(num)
                backtrace(nums[i + 1:], path)
                path.pop()

        backtrace(list(range(1, n + 1)), [])
        return ret


print(Solution().combine(0, 0))
