# @Time : 2020/10/11 1:08
# @Author : LiuBin
# @File : 102.py
# @Description : 
# @Software: PyCharm

"""二叉树的层序遍历
关键字: BFS、层次遍历
目标: 返回包含每层节点值的嵌套列表
思路: 分层处理
"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        q = [root]
        while q:
            size = len(q)
            curs = []
            for i in range(size):
                cur = q.pop(0)
                curs.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            ret.append(curs)
        return ret


print(Solution().levelOrder(createBiTree([3, 9, 20, None, None, 15, 7])))
