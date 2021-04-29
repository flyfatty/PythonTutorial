# @Time : 2020/10/26 9:26
# @Author : LiuBin
# @File : 1365.py
# @Description : 
# @Software: PyCharm

"""有多少小于当前数字的数字
关键字: 数组
思路:
方法1、预置数组
方法2、排序
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = [0] * 101
        for n in nums:
            dic[n] += 1
        sum_ = [0]
        for n in dic:
            sum_.append(sum_[-1] + n)
        return [sum_[n] for n in nums]

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        idx_nums = sorted(enumerate(nums), key=lambda x: x[1])

        last_value = None
        ret = []
        for idx, num in idx_nums:
            if last_value is not None and last_value == num:
                ret.append((idx, ret[-1][1]))
            else:
                ret.append((idx, len(ret)))
            last_value = num
        return [count for _, count in sorted(ret)]


print(Solution().smallerNumbersThanCurrent([1, 3, 2, 4, 2, 1]))
