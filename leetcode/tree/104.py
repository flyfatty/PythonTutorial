# @Time : 2020/10/10 9:28
# @Author : LiuBin
# @File : 104.py
# @Description : 
# @Software: PyCharm

"""二叉树的最大深度
关键字:后序遍历、分治
目标:获得从根节点到最远的叶子结点的节点数
思路:
1、获得左子树的最大深度；获得右子树的最大深度
2、返回左/右子树的最大的深度 + 1（自己贡献了1个深度）
"""
from utils import TreeNode, createBiTree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        return max(left_max_depth, right_max_depth) + 1


print(Solution().maxDepth(createBiTree([3, 9, 20, None, None, 15, 7])))
