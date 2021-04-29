# @Time : 2020/10/23 11:13
# @Author : LiuBin
# @File : 234.py
# @Description : 
# @Software: PyCharm
"""回文链表
关键字: 栈
思路:
1、利用栈记录链表的倒序序列
2、依次比较栈和链表的值是否相等即可
"""
from utils import ListNode, createList


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        root = head
        while head:
            stack.append(head.val)
            head = head.next
        while root:
            if stack.pop() != root.val:
                return False
            root = root.next
        return True


print(Solution().isPalindrome(createList([1, 2, 1])))
