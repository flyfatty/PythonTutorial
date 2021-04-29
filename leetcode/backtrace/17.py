# @Time : 2020/10/21 13:15
# @Author : LiuBin
# @File : 17.py
# @Description : 
# @Software: PyCharm
"""电话号码的字母组合
关键字: 回溯
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        m = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        ret = []

        def backtrace(path):
            if len(path) == len(digits):
                ret.append(path)
                return
            n = digits[len(path)]
            for i in m[n]:
                backtrace(path + i)

        backtrace("")
        return ret


print(Solution().letterCombinations("2233"))
