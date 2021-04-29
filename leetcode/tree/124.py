# @Time : 2020/10/9 15:40
# @Author : LiuBin
# @File : 124.py
# @Description : 
# @Software: PyCharm

"""二叉树中的最大路径和
关键字: 后序遍历、贪心、分治
目标:寻找二叉树的最大路径和
思路:
    1、二叉树后序遍历，划分为子问题
    2、维护全局最大的路径和（贪心）
    3、左孩子/右孩子返回的通向父亲的单向路径和与父亲本身的值 与 全局值比较
    注意：某一组成的路径和是负数需要忽略
"""

from utils import TreeNode, createBiTree


class Solution:
    max_path_sum = -1 << 31

    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if not root:
                return 0
            leftPathSum = max(dfs(root.left), 0)
            rightPathSum = max(dfs(root.right), 0)
            self.max_path_sum = max(self.max_path_sum, leftPathSum + rightPathSum + root.val)
            return max(leftPathSum, rightPathSum) + root.val

        dfs(root)
        return self.max_path_sum


root = createBiTree([10, 5, None, 7])

res = Solution().maxPathSum(root)
print(res)
