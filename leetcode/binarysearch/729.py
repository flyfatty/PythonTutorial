# @Time : 2020/9/26 22:16
# @Author : LiuBin
# @File : 729.py
# @Description : 
# @Software: PyCharm

"""我的日程安排表 I
关键字: 二分查找
目标:每次申请一个区间，如果区间出现重叠返回False，否则开辟区间并返回True
思路:
    1、二分查找，维护每个区间start的有序列表
    2、使用字典维护start:end。如果能进入start列表，一定满足 i+1的start>=i的end(左闭右开)
    3、找出所有重叠的情况，剩下的就可以加入start列表，并且更新字典
"""


class MyCalendar:

    def __init__(self):
        self.map = dict()
        self.slist = list()

    def binary_search(self, n, s, e):
        if s >= e:
            return s
        m = (s + e) >> 1
        if self.slist[m] > n:
            return self.binary_search(n, s, m)
        elif self.slist[m] < n:
            return self.binary_search(n, m + 1, e)
        else:
            return m

    def book(self, start: int, end: int) -> bool:
        idx = self.binary_search(start, 0, len(self.slist))
        if self.slist:
            if idx >= len(self.slist):
                if self.map[self.slist[idx - 1]] > start:
                    return False
            else:
                if self.slist[idx] == start or end > self.slist[idx] or idx - 1 >= 0 and self.map[
                    self.slist[idx - 1]] > start:
                    return False
        self.slist.insert(idx, start)
        self.map[start] = end
        return True


if __name__ == '__main__':
    ins = MyCalendar()
    print(ins.book(4, 10))
    print(ins.book(0, 2))
    print(ins.book(3, 4))
    # print(ins.book(9, 13))
    # print(ins.book(13, 14))
    # print(ins.book(0, 14))
    print(ins.slist, ins.map)
