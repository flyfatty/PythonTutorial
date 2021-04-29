# @Time : 2020/10/14 16:37
# @Author : LiuBin
# @File : 235.py
# @Description : 
# @Software: PyCharm
"""二叉搜索树的最近公共祖先
关键字: 前序遍历
"""
from utils import TreeNode, createBiTree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p, q) -> 'TreeNode':
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


print(Solution().lowestCommonAncestor(createBiTree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]), TreeNode(2), TreeNode(8)))
