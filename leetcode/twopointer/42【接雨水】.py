# @Time : 2021/4/27 23:59
# @Author : LiuBin
# @File : 42【接雨水】.py
# @Description : 
# @Software: PyCharm
"""接雨水
DP、双指针

Tips： 每个位置i接雨水的量之和左边或右边较矮的木头有关
ans += min(lmax , rmax) - height[i]
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2: return 0
        ans = 0
        lmax, rmax = height[0], height[-1]
        left, right = 0, len(height) - 1
        while left <= right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])
            if lmax < rmax:
                ans += lmax - height[left]
                left += 1
            else:
                ans += rmax - height[right]
                right -= 1
        return ans


print(Solution().trap([4, 5, 4]))
