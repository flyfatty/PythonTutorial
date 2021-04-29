"""最长上升子序列
O(n^2) + O(n)
关键字: DP \ 二分
dp[i] = max( dp[j] + 1 , 1 )  j\<(0,i-1)
"""
from typing import List

class Solution:
    def lengthOfLISByBisect(self, nums: List[int]) -> int:
        import bisect
        dp = []
        for num in nums:
            idx = bisect.bisect_left(dp , num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)


    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j] :
                    dp[-1] = max ( dp[-1] , dp[j] + 1 )
        return max(dp)


if __name__ == "__main__":

    print(Solution().lengthOfLIS([1,2,3]))
