# @Time : 2020/10/20 14:04
# @Author : LiuBin
# @File : 501.py
# @Description : 
# @Software: PyCharm
"""二叉搜索树中的众数
关键字: 中序遍历
思路:
1、有序数列寻找众数
2、前后值比较,相同累加次数,不同更新众数状态
3、维护众数状态，即众数和出现次数
"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        count = -1
        mode, mode_cnt = [], 0
        pre = None

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nonlocal count, pre, mode, mode_cnt
            if pre and pre.val == root.val:
                count += 1
            else:
                if count > mode_cnt:
                    mode, mode_cnt = [pre.val], count
                elif count == mode_cnt:
                    mode.append(pre.val)
                count = 1
            pre = root
            dfs(root.right)

        dfs(root)
        if count > mode_cnt:
            mode = [pre.val]
        elif count == mode_cnt:
            mode.append(pre.val)
        return mode


print(Solution().findMode(createBiTree([1, 1, 2, None, None, 2])))
