# @Time : 2020/10/20 13:03
# @Author : LiuBin
# @File : 515.py
# @Description : 
# @Software: PyCharm
"""	在每个树行中找最大值
关键字: 任何遍历
思路:
1、维护每行的最大值数组，深度对应索引
"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        ret = []

        def dfs(root, depth):
            if not root:
                return
            nonlocal ret
            if len(ret) <= depth:
                ret.append(root.val)
            else:
                ret[depth] = max(ret[depth], root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return ret


print(Solution().largestValues(createBiTree([1, 3, 2, 5, 3, None, 9])))
