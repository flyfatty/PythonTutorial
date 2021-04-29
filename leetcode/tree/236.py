# @Time : 2020/10/14 17:40
# @Author : LiuBin
# @File : 236.py
# @Description : 
# @Software: PyCharm

"""二叉树的最近公共祖先
关键字: 后序遍历
思路:
1、遇到直接返回找到的目标节点
2、如果左右子树各贡献了节点，那么最早遇到的父节点就是公共祖先
3、如果只有一个子树贡献节点，那么属于目标节点本身即是公共祖先。
"""
from utils import TreeNode, createBiTree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == q or root == p: return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if not l: return r
        if not r: return l
        return root


a = Solution().lowestCommonAncestor(createBiTree([-1, 0, 3, -2, 4, None, None, 8]),
                                    TreeNode(8), TreeNode(4))
print(a)
