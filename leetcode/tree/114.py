# @Time : 2020/10/14 15:24
# @Author : LiuBin
# @File : 114.py
# @Description : 
# @Software: PyCharm
"""二叉树展开为链表
关键字: 后序遍历
思路:
1、最后的结果是使用的右孩子，所以考虑优先处理右子树
2、后序遍历记录pre节点和父亲节点, 该节点指向pre节点,父亲节点的右孩子指向该节点
"""
from utils import TreeNode, createBiTree


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None

        def dfs(root, parent):
            if not root:
                return
            dfs(root.right, root)
            dfs(root.left, root)
            nonlocal pre

            if parent:
                root.right = pre
                if parent.left is root:
                    parent.left = None
                    parent.right = root
            pre = root

        dfs(root, None)


root = createBiTree([3, 2])
Solution().flatten(root)
print(root)
