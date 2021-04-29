# @Time : 2020/10/13 11:43
# @Author : LiuBin
# @File : 103.py
# @Description : 
# @Software: PyCharm
"""二叉树的锯齿形层次遍历
关键字: 层次遍历
思路:
1、设置深度作为奇偶性标志位
"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ret = []
        depth = 1
        while q:
            size = len(q)
            if len(ret) < depth:
                ret.append([])
            for i in range(size):
                cur = q.pop(0)
                if depth % 2 == 1:
                    ret[depth - 1].append(cur.val)
                else:
                    ret[depth - 1].insert(0, cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            depth += 1

        return ret


print(Solution().zigzagLevelOrder(createBiTree([1, 2, None, 3, None, 4, 5])))
