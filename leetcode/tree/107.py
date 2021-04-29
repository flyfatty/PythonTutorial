# @Time : 2020/10/11 1:25
# @Author : LiuBin
# @File : 107.py
# @Description : 
# @Software: PyCharm
"""二叉树的层次遍历 II
关键字: BFS、DFS
思路: 与【二叉树的层次遍历】思路一样，最终结果取倒序即可
"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if not root:
            return ret

        def dfs(root, depth):
            if len(ret) < depth:
                ret.append([])
            ret[depth - 1].append(root.val)
            if root.left: dfs(root.left, depth + 1)
            if root.right: dfs(root.right, depth + 1)

        dfs(root, 1)
        return ret[::-1]

    def levelOrderBottomByLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return ret[::-1]


print(Solution().levelOrderBottom(createBiTree([3, 9, 20, None, None, 15, 7])))
