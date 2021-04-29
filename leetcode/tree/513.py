# @Time : 2020/10/20 12:44
# @Author : LiuBin
# @File : 513.py
# @Description : 
# @Software: PyCharm
"""找树左下角的值
关键字: 中序遍历
思路:
1、一旦进入更深层的树，更新第一个该深度遍历的节点即可
"""
from utils import TreeNode, createBiTree


class Solution:
    def findBottomLeftValue(self, root: TreeNode):
        ret, dep = None, 0

        def dfs(root, depth):
            if not root:
                return
            dfs(root.left, depth + 1)
            nonlocal ret, dep
            if depth > dep:
                ret, dep = root.val, depth
            dfs(root.right, depth + 1)

        dfs(root, 1)
        return ret


print(Solution().findBottomLeftValue(createBiTree([1, 2, 3, 4, 5, 6, None, None, 7])))
