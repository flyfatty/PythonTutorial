# @Time : 2020/10/28 16:58
# @Author : LiuBin
# @File : 222.py
# @Description : 
# @Software: PyCharm
from utils import TreeNode, createBiTree


class Solution:

    def countNodesByDFS(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodesByDFS(root.left) + self.countNodesByDFS(root.right) + 1

    def countNodes(self, root: TreeNode) -> int:
        def dfs_left(root):
            if not root:
                return 0
            return dfs_left(root.left) + 1

        if not root:
            return 0

        depth = dfs_left(root)
        res = 0

        def dfs_right(root, curdep, idx):
            nonlocal depth, res
            if not root:
                return 0
            if curdep == depth:
                res = idx
            if not res: dfs_right(root.right, curdep + 1, 2 * idx + 1)
            if not res: dfs_right(root.left, curdep + 1, 2 * idx)

        dfs_right(root, 1, 1)
        return res


print(Solution().countNodes(createBiTree([1, 2, 3, 4, 5, 6, 7])))
