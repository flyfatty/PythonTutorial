# @Time : 2020/10/20 12:53
# @Author : LiuBin
# @File : 563.py
# @Description : 
# @Software: PyCharm
"""二叉树的坡度
关键字: 后序遍历
思路:
1、维护左右子树的和
2、累加当前节点的坡度
"""
from utils import TreeNode, createBiTree


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total_slope = 0

        def dfs(root):
            if not root:
                return 0
            l_sum = dfs(root.left)
            r_sum = dfs(root.right)
            nonlocal total_slope
            total_slope += abs(l_sum - r_sum)
            return l_sum + root.val + r_sum

        dfs(root)
        return total_slope


print(Solution().findTilt(createBiTree([1, 2, 3, 4, 5])))
