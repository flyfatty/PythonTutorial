"""回文子串
关键字: 中心扩展法、马拉车算法
思路:
    O(n) 最大的羽翼能够cover住的部分可以不用重复计算
    1. 没有覆盖住按照中心扩展法做
    2. 主翼能够覆盖子翼,直接获取中心对称结果
    3. 主翼与子翼在右边重合,子翼继续中心扩展往前探索
    4. 子翼右边超过主翼右边(超过字符串长度),截取子翼右边部分

"""

class Solution:
    def manacher(self, s: str) -> str:
        s = '#' + '#'.join(s) + '#'
        size = len(s)
        def get_palindrome( l , r ):
            step = 0
            while l >= 0 and r < size and s[l] == s[r]:
                l -= 1
                r += 1
                step += 1
            return step

        max_right = center = -1
        p = []
        for i in range(size):
            if i > max_right:
                step = get_palindrome( i-1 , i+1 )
                p.append(step)
                center = i
                max_right = i + step
            elif p[2*center-i]+i < max_right:
                p.append(p[2*center-i])
            elif p[2*center-i]+i == max_right:
                step = get_palindrome( 2*i-max_right-1 , max_right+1 )
                p.append(p[2*center-i] + step)
                max_right += step
                center = i
            else:
                p.append(max_right-i)
                center = i

        sum_ = 0
        for i , pp in enumerate(p):
            sum_ += (pp + (i % 2))//2
        return sum_



    def countSubstrings(self, s: str) -> int:
        size = len(s)
        def get_palindrome( l , r ):
            while l >= 0 and r < size and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return (r - l)//2+1

        res = 0
        for i in range(size):
            res += get_palindrome(i, i) + get_palindrome(i, i+1)
        return res
            




print(Solution().manacher("abababababab"))
print(Solution().manacher("babad"))
print(Solution().manacher("cbbd"))
print(Solution().manacher("aaaa"))
