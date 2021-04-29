# @Time : 2020/10/10 17:00
# @Author : LiuBin
# @File : 94.py
# @Description : 
# @Software: PyCharm
"""中序遍历

"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []

        def inOrder(root, ret):
            if not root:
                return
            inOrder(root.left, ret)
            ret.append(root.val)
            inOrder(root.right, ret)

        inOrder(root, ret)
        return ret


print(Solution().inorderTraversal(createBiTree([1, None, 2, 3])))
