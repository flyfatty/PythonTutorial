# @Time : 2020/10/21 9:56
# @Author : LiuBin
# @File : 60.py
# @Description : 
# @Software: PyCharm
"""第k个全排列
关键字: 回溯、数学
思路:
1、暴力回溯法效率非常低，回溯法返回第k个结果
2、计算k所在位置的迭代数学公式,直接得出第k个全排列结果
"""

from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        pool = list(range(1, n + 1))
        while n:
            fact = factorial(n - 1)
            i = (k - 1) // fact  # 对应池子的第几个数字
            num = pool.pop(i)
            nums.append(str(num))
            k = (k - 1) % fact + 1
            n -= 1
        return ''.join(nums)

    def getPermutationByBackTrace(self, n: int, k: int) -> str:
        count = 0

        def backtrace(nums, path):
            if not nums:
                nonlocal count, k
                count += 1
                if count == k:
                    return "".join(map(str, path))
            for idx, num in enumerate(nums):
                path.append(num)
                flag = backtrace(nums[:idx] + nums[idx + 1:], path)
                if flag:
                    return flag
                path.pop()

        return backtrace(list(range(1, n + 1)), [])


print(Solution().getPermutation(5, 1))
print(Solution().getPermutation(5, 2))
# print(Solution().getPermutation(4, 3))
# print(Solution().getPermutation(4, 4))
# print(Solution().getPermutation(4, 5))
# print(Solution().getPermutation(4, 6))
