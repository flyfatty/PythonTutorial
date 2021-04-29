# @Time : 2020/10/14 10:16
# @Author : LiuBin
# @File : 112.py
# @Description : 
# @Software: PyCharm
"""路径总和
关键字: 先序遍历
思路:
1、有一个特殊情况，就是给定的树是空树，且sum是0，需要返回False（题目限制）。
2、自顶向下缩小问题范围，sum -= root.val，最后到空节点应该等于0，否则分别继续向下探索
"""
from utils import TreeNode, createBiTree


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs(root, sum):
            if not root: # 此时必须保证是叶子节点
                return sum == 0
            elif root.right and root.left:
                sum -= root.val
                return dfs(root.left, sum) or dfs(root.right, sum)
            else:
                sum -= root.val
                return dfs(root.left, sum) if root.left else dfs(root.right, sum)

        if not root:
            return False
        return dfs(root, sum)


print(Solution().hasPathSum(createBiTree([-2, None, -3]), -5))
