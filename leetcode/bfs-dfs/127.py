# @Time : 2020/10/24 19:09
# @Author : LiuBin
# @File : 127.py
# @Description : 
# @Software: PyCharm
"""单词接龙
关键字: 双向BFS
思路:
1、利用修改某个字符作为通配符,构造边集合，然后BFS找到答案
"""
from typing import List
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        # 构建通用状态字典  O(MN)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        q, q2 = set(), set()
        q.add(beginWord)
        q2.add(endWord)
        visit = set()
        step = 1
        while q and q2:
            temp = set()
            for cur in q:
                if cur in visit:
                    continue
                visit.add(cur)
                if cur in q2:
                    return step
                for i in range(len(cur)):
                    key = cur[:i] + '*' + cur[i + 1:]
                    if key in all_combo_dict:
                        for word in all_combo_dict[key]:
                            if word not in visit:
                                temp.add(word)
            step += 1
            q = q2
            q2 = temp
        return 0


print(Solution().ladderLength("hit", "dog", ["hot", "cog", "dot", "dog", "lot", "log"]))
