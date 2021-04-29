# @Time : 2020/10/24 18:44
# @Author : LiuBin
# @File : 993.py
# @Description : 
# @Software: PyCharm
"""二叉树的堂兄弟节点
关键字: 层次遍历
"""
from utils import TreeNode, createBiTree


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = [root]
        if root.val in [x, y]:
            return False
        while q:
            size = len(q)
            count = 0
            for i in range(size):
                cnt = 0
                cur = q.pop(0)
                if cur.left:
                    if cur.left.val in [x, y]:
                        count += 1
                        cnt += 1
                    q.append(cur.left)
                if cur.right:
                    if cur.right.val in [x, y]:
                        count += 1
                        cnt += 1
                    q.append(cur.right)
                if cnt == 2:
                    return False
            if count == 1:
                return False
            if count == 2:
                return True
        return False


print(Solution().isCousins(createBiTree([1, 2, 3, None, 4, None, 5]), 5, 4))
