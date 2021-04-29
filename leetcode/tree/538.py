# @Time : 2020/10/20 12:37
# @Author : LiuBin
# @File : 538.py
# @Description : 
# @Software: PyCharm
"""把二叉搜索树转换为累加树
关键字: 中序遍历
思路:
1、先右孩子、再左孩子
2、输入 当前状态作为入参，返回处理后的状态
"""
from utils import TreeNode, createBiTree


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root, sum):
            if not root:
                return sum
            sum = dfs(root.right, sum)
            root.val += sum
            sum = dfs(root.left, root.val)
            return sum

        dfs(root, 0)
        return root


print(Solution().convertBST(createBiTree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])))
