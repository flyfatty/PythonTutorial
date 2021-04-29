# @Time : 2020/10/15 19:02
# @Author : LiuBin
# @File : 199.py
# @Description : 
# @Software: PyCharm
"""二叉树的右视图
关键字: 层序遍历
思路:
1、每次只取当前层的最后一个节点
"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = [root]
        ret = []
        while q:
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                if i + 1 == size:
                    ret.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return ret


print(Solution().rightSideView(createBiTree([1, 2, 3, None, 5, None, 4])))
