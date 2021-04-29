# @Time : 2020/10/23 13:28
# @Author : LiuBin
# @File : 39.py
# @Description : 
# @Software: PyCharm
"""组合总和
关键字: 回溯
思路:
1、组合,以后只访问索引大于等于当前选择的候选元素
2、递归缩小问题规模,target==0时成功找到路径,target<0时是错误路径
3、序列中没有重复数字,不需要事先排序
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def backtrace(candidates, target, path):
            if target <= 0:
                if target == 0:
                    ret.append(path[:])
                return
            for idx, candidate in enumerate(candidates):
                path.append(candidate)
                backtrace(candidates[idx:], target - candidate, path)
                path.pop()
        backtrace(candidates, target, [])
        return ret


print(Solution().combinationSum([2, 3, 5], 8))
