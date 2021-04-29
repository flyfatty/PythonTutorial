# @Time : 2020/11/4 14:33
# @Author : LiuBin
# @File : 18.py
# @Description : 
# @Software: PyCharm
"""四数之和
关键字: 双指针+递归

"""
from typing import List


class Solution:
    def nSum(self, nums, target, start, n):

        res = []
        if n == 2 and len(nums) - start >= 2:
            i, j = start, len(nums) - 1
            while i < j:
                sum_ = nums[i] + nums[j]
                left, right = nums[i], nums[j]
                if sum_ < target:
                    while i < j and left == nums[i]: i += 1
                elif sum_ > target:
                    while i < j and right == nums[j]: j -= 1
                else:
                    res.append([nums[i], nums[j]])
                    while i < j and left == nums[i]: i += 1
                    while i < j and right == nums[j]: j -= 1
        elif n > 2:
            pre = None
            for i in range(start, len(nums)):
                if pre is None or nums[i] > pre:
                    res.extend([nums[i]] + l for l in self.nSum(nums, target - nums[i], i + 1, n - 1))
                pre = nums[i]
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.nSum(nums, target, 0, 4)


print(Solution().fourSum([-3, -1, 0, 2, 4, 5], 0))
