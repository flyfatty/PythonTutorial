# @Time : 2020/10/10 23:47
# @Author : LiuBin
# @File : 111.py
# @Description : 
# @Software: PyCharm

"""二叉树的最小深度
关键字: BFS、层次遍历
目标: 根节点到叶子节点的最短路径节点数量
思路:
1、注意是连接到叶子结点,使用后序遍历方法的时候容易出错!
2、加速技巧：能迭代一起处理的尽量一起处理。解答中一次while处理一层的节点数量
"""
from utils import TreeNode, createBiTree


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        depth = 1
        while q:
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                if not cur.left and not cur.right:
                    return depth
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            depth += 1

    def minDepthByLevelOrder(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [(root, 1)]

        while q:
            node, depth = q.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left: q.append((node.left, depth + 1))
            if node.right: q.append((node.right, depth + 1))

    def minDepthByPostOrder(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            if left == right == 0:
                return 1
            elif left == 0 or right == 0:
                return left + right + 1
            else:
                return min(left, right) + 1

        return dfs(root)


print(Solution().minDepth(createBiTree([3, 9, 20, None, None, 15, 7])))
