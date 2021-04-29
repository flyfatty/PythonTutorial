# @Time : 2020/10/19 19:05
# @Author : LiuBin
# @File : 987.py
# @Description : 
# @Software: PyCharm

"""二叉树的垂序遍历
关键字: 任何遍历
思路：
1、给每个点一个坐标，（x,y,z）
2、x表示横向索引，左孩子-1，右孩子+1 ;y表示深度 ; z表示root的值
3、坐标排序
"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        box = []

        def dfs(root, x, y):
            if not root:
                return
            box.append((x, y, root.val))
            dfs(root.left, x - 1, y + 1)
            dfs(root.right, x + 1, y + 1)

        dfs(root, 0, 0)
        ret = []
        last_x = None
        for x, y, value in sorted(box):
            if last_x is None or last_x != x:
                ret.append([])
            ret[-1].append(value)
            last_x = x

        return ret


print(Solution().verticalTraversal(createBiTree([3, 9, 20, None, None, 15, 7])))
