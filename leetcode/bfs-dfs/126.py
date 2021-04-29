# @Time : 2020/11/10 17:41
# @Author : LiuBin
# @File : 126.py
# @Description : 
# @Software: PyCharm

from typing import List
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def parse_path(paths1, paths2):
            if paths2[0].startswith('#'):
                paths1, paths2 = paths2, paths1
            words = []
            for path1 in paths1:
                for path2 in paths2:
                    path = path1[2:].split(" ") + path2.split(' ')[:-1][::-1]
                    words.append([beginWord] + [wordList[int(idx)] for idx in path])
            return words

        if endWord not in wordList:
            return []
        res = []
        edges = defaultdict(set)
        n = len(beginWord)
        flag = False
        q1, q2 = defaultdict(list), defaultdict(list)
        q1[beginWord].append("#")
        for idx, word in enumerate(wordList):
            if word == endWord:
                q2[endWord].append(str(idx))
            for i in range(n):
                edge = word[:i] + '*' + word[i + 1:]
                edges[edge].add((word, str(idx)))

        while q1 and q2:
            if len(q1) > len(q2):
                q2, q1 = q1, q2
            temp = defaultdict(list)
            for word in q1:
                if word in q2:
                    flag = True
                    res.extend(parse_path(q1[word], q2[word]))
                    continue
                for i in range(n):
                    edge = word[:i] + '*' + word[i + 1:]
                    for next_word, idx in edges.get(edge, set()):

                        paths = [path + ' ' + idx for path in q1[word] if idx not in path]
                        if len(paths) > 0:
                            temp[next_word] += paths
            if flag: break
            q1 = temp
        return res


print(Solution().findLadders("ta",
                             "if",
                             ["ts", "sc", "ph", "ca", "jr", "hf", "to", "if", "ha", "is", "io", "cf", "ta"]))
