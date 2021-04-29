# @Time : 2020/10/10 9:40
# @Author : LiuBin
# @File : 98.py
# @Description : 
# @Software: PyCharm

"""验证二叉搜索树
关键字: 先序遍历、中序遍历
目标: 给定一棵二叉树，验证是否是一颗BST
思路:
1、定义法 前序遍历 验证符合定义
2、特征法 中序遍历 验证有序序列
"""
from utils import TreeNode, createBiTree


class Solution:
    flag = True
    pre = None

    def isValidBSTByInOrder(self, root: TreeNode) -> bool:

        def dfs(root):
            if not root:
                return
            if self.flag:
                dfs(root.left)
            if self.pre is not None and self.pre >= root.val:
                self.flag = False
            else:
                self.pre = root.val
            if self.flag:
                dfs(root.right)

        dfs(root)
        return self.flag

    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, min_=float('-inf'), max_=float('inf')):
            if not root:
                return True
            if min_ >= root.val or max_ <= root.val or not dfs(root.left, min_, root.val) or not dfs(root.right,
                                                                                                     root.val,
                                                                                                     max_):
                return False
            return True

        return dfs(root)


print(Solution().isValidBST(createBiTree([1, 1])))
