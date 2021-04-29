# @Time : 2020/10/21 9:25
# @Author : LiuBin
# @File : 257.py
# @Description : 
# @Software: PyCharm
"""二叉树的所有路径
关键字: 先序遍历
思路:
1、记录访问的路径
2、最后一步删除最前面的箭头
"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ret = []
        if not root:
            return []

        def dfs(root, path):
            if not root.left and not root.right:
                ret.append((path + "->" + str(root.val))[2:])
                return
            if root.left: dfs(root.left, path + "->" + str(root.val))
            if root.right: dfs(root.right, path + "->" + str(root.val))

        dfs(root, "")
        return ret


print(Solution().binaryTreePaths(createBiTree([1])))
