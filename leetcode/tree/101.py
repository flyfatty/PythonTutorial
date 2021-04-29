# @Time : 2020/10/10 14:09
# @Author : LiuBin
# @File : 101.py
# @Description : 
# @Software: PyCharm

"""对称二叉树
关键字: 反向先序遍历
目标: 验证一颗二叉树是不是镜面对称的二叉树
思路:
1、对同一棵树同时使用先序遍历
2、先序遍历的方向相反,一个先访问左孩子,然后右孩子,一个先访问右孩子,然后左孩子
3、这样的先序遍历的路径是镜像对称的,比较两个节点是否一样
"""
from utils import TreeNode, createBiTree


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and root2 and root1.val == root2.val:
                return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)
            return False

        return dfs(root, root)


print(Solution().isSymmetric(createBiTree([1, 2, 2, None, 3,  3])))
