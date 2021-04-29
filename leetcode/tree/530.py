# @Time : 2020/10/20 13:10
# @Author : LiuBin
# @File : 530.py
# @Description : 
# @Software: PyCharm
"""二叉搜索树的最小绝对差
关键字: 中序遍历
思路:
1、获得有序数列
2、维护最小的前后元素的差值
"""
from utils import TreeNode, createBiTree


class Solution:
    def getMinimumDifference(self, root: TreeNode):
        min_ = None
        last_val = None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nonlocal min_, last_val
            if last_val is not None:
                if not min_ or root.val - last_val < min_:
                    min_ = root.val - last_val

            last_val = root.val
            dfs(root.right)

        dfs(root)
        return min_


print(Solution().getMinimumDifference(createBiTree([1, None, 5, 3])))
