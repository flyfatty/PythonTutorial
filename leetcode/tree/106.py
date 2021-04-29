# @Time : 2020/10/14 13:23
# @Author : LiuBin
# @File : 106.py
# @Description : 
# @Software: PyCharm
"""从中序与后序遍历序列构造二叉树
关键字: 后序遍历
思路:
1、利用后序遍历列表定位root
2、利用中序遍历列表定位左右子树，注意是先右再左
3、递归缩减问题规模
"""

from utils import TreeNode
from typing import List


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        if not postorder or not inorder:
            return
        root_val = postorder.pop()
        root = TreeNode(root_val)
        idx = inorder.index(root_val)
        root.right = self.buildTree(inorder[idx + 1:], postorder)
        root.left = self.buildTree(inorder[:idx], postorder)
        return root


print(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
