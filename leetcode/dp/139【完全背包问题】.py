# @Time : 2020/11/2 9:17
# @Author : LiuBin
# @File : 139【完全背包问题】.py
# @Description : 
# @Software: PyCharm
"""单词拆分
状态: 截止到i是否可拆分
选择: 可选单词里只要有一个满足即可
dp转移: dp[i] = s[:i].endswith(w) and dp[i-len(w)]  w ∈ word_dict
base case: dp[0] = True

关键字: 记忆化递归、DP
思路:
# 状态: dp[i] 截止到i,是否可以拆分
# 状态转移方程:   dp[i] = dp[j] and check(j,i)
"""
from typing import List


class Solution:
    def wordBreakByDP(self, s: str, wordDict: List[str]) -> bool:
        dp = [True]
        for i in range(1, len(s) + 1):
            dp.append(False)
            for word in wordDict:
                dp[-1] = s[:i].endswith(word) and dp[i - len(word)]
                if dp[-1]: break
        return dp[-1]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [True]
        for i in range(1, len(s) + 1):
            dp.append(False)
            for j in range(0, i):
                dp[-1] = dp[j] and s[j:i] in wordSet
                if dp[-1]: break
        return dp[-1]

    def wordBreakByDFS(self, s: str, wordDict: List[str]) -> bool:
        visit = {}

        def dfs(i):
            if i in visit:
                return visit[i]
            if i == len(s):
                return True
            flag = False
            for word in wordDict:
                if s[i:].startswith(word):
                    flag = dfs(i + len(word))
                    if flag:
                        break
            visit[i] = flag
            return flag

        return dfs(0)


print(Solution().wordBreak(s="PythonTutorial", wordDict=["leet", "code", "sand", "and", "cat"]))
print(Solution().wordBreakByDP(s="PythonTutorial", wordDict=["leet", "code", "sand", "and", "cat"]))
