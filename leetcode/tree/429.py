# @Time : 2020/10/14 17:25
# @Author : LiuBin
# @File : 429.py
# @Description : 
# @Software: PyCharm
"""N叉树的层序遍历
"""
from utils import Node
from typing import List


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ret = []
        q = [root]
        depth = 1
        while q:
            size = len(q)
            if len(ret) < depth:
                ret.append([])
            for i in range(size):
                cur = q.pop(0)
                ret[depth - 1].append(cur.val)
                if not cur.children:
                    continue
                for child in cur.children:
                    q.append(child)
            depth += 1
        return ret


root = Node(1)
root.children = [Node(3), Node(2), Node(4)]
root.children[0].children = [Node(5), Node(6)]
print(Solution().levelOrder(root))
