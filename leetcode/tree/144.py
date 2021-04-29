# @Time : 2020/10/14 16:29
# @Author : LiuBin
# @File : 144.py
# @Description : 
# @Software: PyCharm

"""二叉树的前序遍历
"""
from utils import TreeNode
from typing import List


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l = []

        def dfs(root):
            if not root:
                return
            l.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return l
