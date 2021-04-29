# @Time : 2020/10/15 16:00
# @Author : LiuBin
# @File : 226.py
# @Description : 
# @Software: PyCharm

"""翻转二叉树
关键字: 后序遍历
"""
from utils import TreeNode, createBiTree


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


print(Solution().invertTree(createBiTree([1, 2, 3])))
