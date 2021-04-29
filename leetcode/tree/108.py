# @Time : 2020/10/11 0:54
# @Author : LiuBin
# @File : 108.py
# @Description : 
# @Software: PyCharm

"""将有序数组转换为二叉搜索树
关键字: 分治法
思路:
1、取数组中间的数值建立当前的根节点
2、使用同样的方法获得左子树和右子树
3、返回当前根节点
"""
from utils import TreeNode
from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        if not nums:
            return
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


root = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.right.left.val)
