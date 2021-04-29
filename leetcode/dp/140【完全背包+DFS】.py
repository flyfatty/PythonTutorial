# @Time : 2020/11/1 21:21
# @Author : LiuBin
# @File : 140【完全背包+DFS】.py
# @Description : 
# @Software: PyCharm
"""单词划分II
DP+DFS
i位置是否可拆分使用DP,记录前置索引，打印所有方案使用DFS，遍历邻接表的方法
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return []
        dp = [True]
        res = [[]]
        for i in range(1, len(s) + 1):
            dp.append(False)
            res.append([])
            for word in wordDict:
                if s[:i].endswith(word) and dp[i - len(word)]:
                    dp[-1] = True
                    res[-1].append(i - len(word))

        def dfs(c):
            if c == 0:
                return ['']
            res_path = []
            for last in res[c]:
                res_path.extend([tail + ' ' + s[last:c] for tail in dfs(last)])
            return res_path

        return [k.lstrip() for k in dfs(len(s))]


print(Solution().wordBreak("abcd", ["a", "abc", "b", "cd"]))
print(Solution().wordBreak("abcd", ["a", "abc", "b", "cd", "d"]))
