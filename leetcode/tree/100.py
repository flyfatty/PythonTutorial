# @Time : 2020/10/10 14:03
# @Author : LiuBin
# @File : 100.py
# @Description : 
# @Software: PyCharm

"""相同的树
关键字: 先序遍历
思路:
1、同时遍历,同时比较两个节点
"""
from utils import TreeNode, createBiTree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


a = createBiTree([1, None, 3, 2])
b = createBiTree([1, None, 3])
print(Solution().isSameTree(a, b))
