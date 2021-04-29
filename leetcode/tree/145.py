# @Time : 2020/10/14 16:32
# @Author : LiuBin
# @File : 145.py
# @Description : 
# @Software: PyCharm
"""二叉树的后序遍历
"""
from utils import TreeNode
from typing import List


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        l = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            l.append(root.val)

        dfs(root)
        return l
