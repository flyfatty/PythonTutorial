# @Time : 2020/10/27 13:49
# @Author : LiuBin
# @File : 207.py
# @Description : 
# @Software: PyCharm
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 邻接表
        link_map = {}
        end_cnt = set()
        for end, start in prerequisites:
            if start not in link_map:
                link_map[start] = set()
            link_map[start].add(end)
            end_cnt.add(end)
        root_set = set(link_map.keys()) - end_cnt
        visit = set()
        cnt = 0
        while root_set:
            temp = set()
            size = len(root_set)
            for _ in range(size):
                cur = root_set.pop()
                print(temp)
                if cur in visit:
                    return False
                visit.add(cur)
                cnt += 1
                if cur in link_map:
                    temp = temp.union(link_map[cur])
            root_set = temp
            if cnt >= numCourses and len(temp.intersection(visit)) == 0:
                return True
        return False


print(Solution().canFinish(5, [[5, 4], [5, 3], [3, 2], [4, 1], [1, 0]]))
