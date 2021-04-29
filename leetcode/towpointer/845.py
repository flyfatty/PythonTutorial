# @Time : 2020/10/25 23:53
# @Author : LiuBin
# @File : 845.py
# @Description : 
# @Software: PyCharm
"""数组中的最长山脉
思路: dp、双指针
1、分别扫一遍截止到当前元素的最大升序和最大降序，然后求和得到最大的值
2、双指针
"""
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        last = A[0]
        dp_pre = [0]
        for a in A:
            if a > last:
                dp_pre.append(dp_pre[-1] + 1)
            else:
                dp_pre.append(0)
            last = a
        last = A[-1]
        dp_post = [0]
        for a in A[::-1]:
            if a > last:
                dp_post.insert(0, dp_post[0] + 1)
            else:
                dp_post.insert(0, 0)
            last = a
        max_ = 0
        for pre, post in zip(dp_pre[1:], dp_post[:-1]):
            if pre and post:
                max_ = max(pre + post + 1, max_)
        return max_


print(Solution().longestMountain([2, 1, 4, 7, 3, 2, 5]))
