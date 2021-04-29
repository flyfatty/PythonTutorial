# @Time : 2020/10/20 11:52
# @Author : LiuBin
# @File : 508.py
# @Description : 
# @Software: PyCharm
"""	出现次数最多的子树元素和
关键字:   后序遍历
思路:
1、字典维护所有子树和与出现次数
2、全局变量维护最大的出现次数
3、字典里找到全局变量相等的v对应的k返回
"""
from utils import TreeNode, createBiTree
from typing import List


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        d = {}
        max_ = 0

        def dfs(root):
            if not root:
                return 0
            sum = dfs(root.left) + root.val + dfs(root.right)
            if sum not in d:
                d[sum] = 0
            d[sum] += 1
            nonlocal max_
            max_ = max(d[sum], max_)
            return sum

        dfs(root)
        ret = []
        for k, v in d.items():
            if v == max_:
                ret.append(k)
        return ret


print(Solution().findFrequentTreeSum(createBiTree([5, 2, -3])))
