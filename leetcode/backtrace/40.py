# @Time : 2020/10/23 13:48
# @Author : LiuBin
# @File : 40.py
# @Description : 
# @Software: PyCharm
"""组合总和 II
关键字: 回溯+排序
思路:
1、因为有重复数字,而且是组合，所以先排序,下一层的选择只能比之前的数字大
2、有重复数字,当前层使用集合记录访问过的数字,不重复选择访问过的数字
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()

        def backtrace(candidates, target, path):
            if target <= 0:
                if target == 0:
                    ret.append(path[:])
                return
            visit = set()
            for idx, candidate in enumerate(candidates):
                if candidate not in visit:
                    visit.add(candidate)
                    path.append(candidate)
                    backtrace(candidates[idx + 1:], target - candidate, path)
                    path.pop()

        backtrace(candidates, target, [])
        return ret


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
