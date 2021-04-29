# @Time : 2020/10/21 9:38
# @Author : LiuBin
# @File : 78.py
# @Description : 
# @Software: PyCharm
"""子集
关键字: 回溯
思路:
1、因为是子集,和元素顺序无关,只需要传递数组后半部分，防止重复
2、空集也是子集
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrace(nums, path):
            if not nums:
                return

            for idx, num in enumerate(nums):
                path.append(num)
                ret.append(path[:])
                backtrace(nums[idx + 1:], path)
                path.pop()

        backtrace(nums, [])
        ret.append([])
        return ret


print(Solution().subsets([1, 2, 3, 4]))
