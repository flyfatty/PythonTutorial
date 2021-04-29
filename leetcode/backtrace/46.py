# @Time : 2020/10/15 9:19
# @Author : LiuBin
# @File : 46.py
# @Description : 
# @Software: PyCharm

"""全排列
关键字: 回溯
思路:
1、维护已经做出的选择列表（路径）
2、找到当前的可选择列表（剩下的可选数字）
3、没有选择的时候保存当前的选择列表（路径）
4、回溯表示已选择列表和可选择列表需要回退到当前做出选择之前的状态
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []

        def backtrace(nums, path):
            if not nums:
                paths.append(path[:])
                return
            for i, n in enumerate(nums):
                backtrace(nums[:i] + nums[i + 1:], path + [n])

        backtrace(nums, [])
        return paths


print(Solution().permute([1, 2]))
