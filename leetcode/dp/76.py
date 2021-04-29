# @Time : 2021/4/27 21:12
# @Author : LiuBin
# @File : 76.py
# @Description : 
# @Software: PyCharm
"""最小覆盖子串

"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) : return ""
        n = len(s)
        ts = set(t)
        si, ei = 0, 0
        min_ = float('inf')
        for i in range(n):
            for j in range(i + 1, n + 1):
                if len(ts.difference(set(s[i:j]))) == 0:
                    if j - i < min_:
                        si, ei = i, j
                        min_ = min(min_, j - i)
        return s[si:ei]


print(Solution().minWindow("ADOBECODEBANC", "ABCD"))
