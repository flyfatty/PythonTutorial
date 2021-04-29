# @Time : 2020/10/21 9:08
# @Author : LiuBin
# @File : 20.py
# @Description : 
# @Software: PyCharm
"""有效的括号
关键字: 栈

"""


class Solution:
    def isValid(self, s: str) -> bool:
        map = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in map.keys():
                stack.append(i)
            else:
                if stack and i == map.get(stack.pop(), ''):
                    continue
                else:
                    return False
        return len(stack) == 0
