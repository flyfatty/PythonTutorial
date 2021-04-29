# @Time : 2020/10/19 18:17
# @Author : LiuBin
# @File : 93.py
# @Description : 
# @Software: PyCharm
"""复原IP地址
关键字: 回溯
"""


class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def dfs(s, path, depth):
            if not s and depth == 4:
                res.append(path[1:])
            if depth > 4:
                return
            for i in range(min(len(s), 3)):
                num = s[:i + 1]
                if i > 0 and num.startswith("0") or i > 1 and num >= "256":
                    continue
                dfs(s[i + 1:], path + "." + num, depth + 1)

        dfs(s, "", 0)
        return res


print(Solution().restoreIpAddresses("010010"))
