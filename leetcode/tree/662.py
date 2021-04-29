# @Time : 2020/10/16 17:41
# @Author : LiuBin
# @File : 662.py
# @Description : 
# @Software: PyCharm
"""二叉树最大宽度
关键字: 中序遍历
"""
from utils import TreeNode, createBiTree


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [(root, 1)]
        width = 1
        while q:
            size = len(q)
            if size > 1:
                (s_root, s_no), (e_root, e_no) = q[0], q[-1]
                width = max(width, e_no - s_no + 1)
            for i in range(size):
                cur, no = q.pop(0)
                if cur.left: q.append((cur.left, no * 2 - 1))
                if cur.right: q.append((cur.right, no * 2))
        return width


print(Solution().widthOfBinaryTree(createBiTree([1, 3, 2, 5, None, None, 9, 6, None, None, 7])))
