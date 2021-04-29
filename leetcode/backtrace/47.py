# @Time : 2020/10/23 13:20
# @Author : LiuBin
# @File : 47.py
# @Description : 
# @Software: PyCharm
"""全排列 II
关键字: 回溯
思路:
1、序列有重复数字
2、每个位置选择的时候，使用集合记录该数字是否选择过。防止同一个位置选择重复数字即可
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrace(nums, path):
            if not nums:
                ret.append(path[:])
                return
            visit = set()
            for idx, num in enumerate(nums):
                if num not in visit:
                    visit.add(num)
                    path.append(num)
                    backtrace(nums[:idx] + nums[idx + 1:], path)
                    path.pop()

        backtrace(nums, [])
        return ret


print(Solution().permuteUnique([1, 2, 1]))
