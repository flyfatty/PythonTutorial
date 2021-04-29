# @Time : 2020/10/14 11:01
# @Author : LiuBin
# @File : 113.py
# @Description : 
# @Software: PyCharm
"""路径总和II
关键字: 前序遍历、回溯
思路:
1、整体思路同【111】
2、需要注意记录path需要回溯
3、需要找到所有path，所以没必要提前return
"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ret = []

        def dfs(root, sum, path):
            if not root:
                if sum == 0:
                    ret.append(path[:])
            elif root.left and root.right:
                sum -= root.val
                path.append(root.val)
                dfs(root.left, sum, path)
                dfs(root.right, sum, path)
                path.pop()
            else:
                sum -= root.val
                path.append(root.val)
                if root.left:
                    dfs(root.left, sum, path)
                else:
                    dfs(root.right, sum, path)
                path.pop()

        if not root:
            return []
        dfs(root, sum, [])
        return ret


print(Solution().pathSum(createBiTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22))
