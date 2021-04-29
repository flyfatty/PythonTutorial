# @Time : 2020/10/13 13:28
# @Author : LiuBin
# @File : 129.py
# @Description : 
# @Software: PyCharm

"""求根到叶子节点数字之和
关键字:先序遍历
思路:
1、记录访问过的路径,得到所有数字,遇到叶子节点就加入总和
2、如果不允许使用字符串,则使用后序遍历,需要记录位数列表,列表的长度同样是叶子(路径)的数量
"""
from utils import TreeNode, createBiTree


class Solution:
    def sumNumbersByPostOrder(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0, []
            left_sum, left_loc = dfs(root.left)
            right_sum, right_loc = dfs(root.right)
            if not left_loc and not right_loc:
                return root.val, [1]
            s = 0
            loc = []
            for i in left_loc + right_loc:
                s += 10 ** i * root.val
                loc.append(i + 1)
            return s + left_sum + right_sum, loc

        s, _ = dfs(root)
        return s

    def sumNumbers(self, root: TreeNode) -> int:
        ret = 0
        if not root:
            return 0

        def helper(path, node):
            nonlocal ret
            if not node.left and not node.right:
                ret += int(path)
                return

            if node.left:
                helper(path + str(node.left.val), node.left)
            if node.right:
                helper(path + str(node.right.val), node.right)

        helper(str(root.val), root)
        return ret


print(Solution().sumNumbers(createBiTree([4, 9, 0, 5, 1])))
