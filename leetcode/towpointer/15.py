# @Time : 2020/11/2 16:22
# @Author : LiuBin
# @File : 15.py
# @Description : 
# @Software: PyCharm
"""三数之和
关键字: 双指针 O(n^2)+O(nlogn) 、 正负分组法O(n^2)+O(n)
思路:
1、分组--正数、负数
2、满足条件的三种情况:
    ① 0,0,0
    ② - target +
    ③ - - + / - + +


更通用的方法  【双指针+递归】 解决nSum问题,需要返回值而不是索引
"""
from typing import List


class Solution:
    def nSum(self, nums, target, start, n):

        res = []
        if n == 2:
            i, j = start, len(nums) - 1
            while i < j:
                if nums[i] + nums[j] < target:
                    i += 1
                    while i < j and nums[i - 1] == nums[i]:
                        i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1
                    while i < j and nums[j + 1] == nums[j]:
                        j -= 1
                else:
                    res.append([nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i - 1] == nums[i]:
                        i += 1
                    while i < j and nums[j + 1] == nums[j]:
                        j -= 1
        elif n > 2:
            pre = None
            for i in range(start, len(nums)):
                if pre is None or nums[i] > pre:
                    res.extend([nums[i]] + l for l in self.nSum(nums, target - nums[i], i + 1, n - 1))
                pre = nums[i]
        return res

    def fourSum(self, nums):
        nums.sort()
        return self.nSum(nums, 0, 0, 4)

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans, m = [], {}
        pos, neg = set(), set()
        for i in nums:
            m[i] = m[i] + 1 if i in m else 1
            pos.add(i) if i > 0 else neg.add(i)

        if 0 in m and m[0] >= 3: ans.append((0, 0, 0))
        for p in pos:
            for n in neg:
                target = -(p + n)
                if target in m and (n < target < p or target in (p, n) and m[target] > 1):
                    ans.append((n, target, p))
        return ans


print(Solution().threeSum2([0, 0, 0, 0]))
