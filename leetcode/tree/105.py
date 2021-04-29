# @Time : 2020/10/14 12:48
# @Author : LiuBin
# @File : 105.py
# @Description : 
# @Software: PyCharm

"""从前序与中序遍历序列构造二叉树
关键字: 前序遍历
思路:
1、利用前序遍历列表定位root
2、利用中序遍历列表定位左右子树
3、递归缩减问题规模
"""
from utils import TreeNode
from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]):
        if not preorder or not inorder:
            return
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx + 1:])
        return root


print(Solution().buildTree([1], [1]))
