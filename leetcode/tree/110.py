# @Time : 2020/10/15 16:13
# @Author : LiuBin
# @File : 110.py
# @Description : 
# @Software: PyCharm
"""平衡二叉树
关键字: 后序遍历
思路:
1、定义法: 验证左右孩子的深度差是否大于1
"""
from utils import TreeNode, createBiTree


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        flag = True

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(right - left) > 1:
                nonlocal flag
                flag = False
            return max(left, right) + 1

        dfs(root)
        return flag


print(Solution().isBalanced(createBiTree([1, 2, 3, 4, 5, None, None, 8])))
