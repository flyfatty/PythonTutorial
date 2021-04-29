# @Time : 2020/10/24 15:35
# @Author : LiuBin
# @File : 1024.py
# @Description : 
# @Software: PyCharm
"""视频拼接
关键字: 贪心
思路:
1、排序,按照 ( x1 , -x2 )
2、维护last_clip状态,分情况讨论当前clip与last_clip的关系
"""
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips = sorted(clips, key=lambda x: (x[0], -x[1]))
        count = 0
        last_clip = [-1, 0]
        for clip in clips:
            if clip[0] > last_clip[1]:
                return -1
            if clip[1] > last_clip[1]:
                if clip[0] > last_clip[0]:
                    count += 1
                    last_clip[0] = last_clip[1]
                last_clip[1] = clip[1]
            if last_clip[1] >= T:
                break
        return count if last_clip[1] >= T else -1


print(Solution().videoStitching([[5, 7], [1, 8], [0, 0], [2, 3], [4, 5], [0, 6], [5, 10], [7, 10]], 5))
