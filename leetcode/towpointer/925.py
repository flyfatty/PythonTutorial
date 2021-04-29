# @Time : 2020/10/21 16:29
# @Author : LiuBin
# @File : 925.py
# @Description : 
# @Software: PyCharm
"""长按键入
关键字: 双指针
思路:
1、两个指针指向两个字符串
2、如果相等同时后移两个指针
3、如果typed前后相同也可以后移typed指针
4、最终name应该走完，typed剩余的元素应该和前一个元素相同，所以集合的长度小于等于1。
5、这里注意应该从type[t-1]开始截取，这样才可以截到前一个处理的元素
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = t = 0
        ln, lt = len(name), len(typed)
        while n < ln and t < lt:
            if name[n] == typed[t]:
                n += 1
                t += 1
                continue
            if t > 0 and typed[t] == typed[t - 1]:
                t += 1
                continue
            return False
        return n == ln and len(set(typed[t - 1:])) <= 1


print(Solution().isLongPressedName("abc", "abcd"))
