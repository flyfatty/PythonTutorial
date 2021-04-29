# @Time : 2020/10/23 15:59
# @Author : LiuBin
# @File : 44.py
# @Description : 
# @Software: PyCharm
"""通配符匹配
关键字: 双指针 + 回溯
思路:
1、使用cache记录当前最后一个*的位置pi和匹配s后的si
2、如果si匹配pi,同时后移指针
3、如果pi是*,cache记录*的位置和当前si的位置，pi++
4、以上都不符合,且记录过*,一定匹配错误,指针回到前面的状态重新走,pi指向*的后面,si比上次多匹配一个字符
5、匹配完成s,如果剩下的p都是*,可以忽略
"""
class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        cache = [-1, -1]  # 当前最后一个*的位置,和 *匹配后s的位置
        si = pi = 0
        while si < len(s):
            if pi < len(p) and (p[pi] == s[si] or p[pi] == '?'):
                pi += 1
                si += 1
            elif pi < len(p) and p[pi] == '*':
                cache = [pi, si]
                pi += 1
            elif cache[0] != -1:
                pi = cache[0] + 1
                si = cache[1] + 1
                cache[1] = si
            else:
                return False
        while pi < len(p) and p[pi] == '*':
            pi += 1
        return pi == len(p)

    def isMatchByDFS(self, s: str, p: str) -> bool:
        def backtrace(si, pi):
            if pi == len(p): return si == len(s)
            if si < len(s) and p[pi] in (s[si], '?') and backtrace(si + 1, pi + 1):
                return True
            elif p[pi] == '*':
                if (si < len(s) and (backtrace(si + 1, pi) or backtrace(si + 1, pi + 1))) or backtrace(si, pi + 1):
                    return True
            return False

        return backtrace(0, 0)


print(Solution().isMatchByDFS("abcabc", "*abc"))
print(Solution().isMatchByDFS(
    "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
    "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))
