# @Time : 2020/10/9 17:42
# @Author : LiuBin
# @File : 99.py
# @Description : 
# @Software: PyCharm

"""恢复二叉搜索树
关键字: 中序遍历
思路:
1、寻找规律，找到需要交换的两个节点拥有同一个规律。pre > cur
2、如果需要交换的两个节点相邻,则 pre和cur交换值即可，如果不相邻，则交换第一组的pre和第二组的cur
3、综上所述，pre一旦获得(s保存)永远不会变，每次满足条件更新cur(t保存)的值即可。
"""
from utils import TreeNode, createBiTree


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = s = t = None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nonlocal s, t, pre
            if pre and pre.val > root.val:
                s = pre if not s else s
                t = root
            pre = root
            dfs(root.right)

        dfs(root)
        s.val, t.val = t.val, s.val


root = createBiTree([68, 41, None, -85, None, -73, -49, -98, None, None, None, -124])
print(root)
Solution().recoverTree(root)
print(root)
