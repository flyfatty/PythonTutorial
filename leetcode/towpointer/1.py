# @Time : 2020/11/4 12:16
# @Author : LiuBin
# @File : 1.py
# @Description : 
# @Software: PyCharm
"""两数之和
关键字: 哈希表
思路:  注意返回结果是索引
1、扫描一遍数组,如果答案不在字典里，存储当前值；如果答案在数组里，直接返回索引
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num not in d:
                d[num] = i
            else:
                return [i, d[target - num]]


print(Solution().twoSum([2, 7, 11, 15], 9))
