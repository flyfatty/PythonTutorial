# @Time : 2020/10/15 9:48
# @Author : LiuBin
# @File : 95.py
# @Description : 
# @Software: PyCharm

"""不同的二叉搜索树 II
关键字: 后序遍历
思路:
1、遍历根节点
2、缩减问题规模,得到左子树和右子树的所有组合集合
3、根据左子树和右子树的所有组合与根节点组合所有可能的组合
4、边界条件，如果没有元素可选，返回None列表
"""
from utils import TreeNode
from typing import List


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(low, high):
            if low > high:
                return [None]
            trees = []
            for i in range(low, high + 1):
                left_set = dfs(low, i - 1)
                right_set = dfs(i + 1, high)
                trees += [TreeNode(i, left, right) for left in left_set for right in right_set]
            return trees

        if n == 0:
            return []
        return dfs(1, n)


print(Solution().generateTrees(3))
