# @Time : 2020/10/30 22:57
# @Author : LiuBin
# @File : 690.py
# @Description : 
# @Software: PyCharm
"""员工的重要性
关键字: 简单BFS
"""
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_map = {}
        for emp in employees:
            employees_map[emp.id] = (emp.importance, emp.subordinates)
        q = [id]
        sum_ = 0
        while q:
            id = q.pop(0)
            importance, subordinates = employees_map[id]
            sum_ += importance
            q.extend(subordinates)
        return sum_


print(Solution().getImportance([Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])], 1))
