# 辗转相除法，获取两个整数的最大公约数
# 辗转相除法， 又名欧几里德算法（Euclidean algorithm），是求最大公约数的一种方法。它的具体做法是：用较大数除以较小数，再用出现的余数（第一余数）去除除数，再用出现的余数（第二余数）去除第一余数，如此反复，直到最后余数是0为止。如果是求两个数的最大公约数，那么最后的除数就是这两个数的最大公约数。
# 最小公倍数，a/gcd(a,b) * b
class Solution:
    def gcd(self, a:int, b:int) -> int:
        if b==0:
            return a
        else:
            return self.gcd(b,a%b)

    def lcm(self, a:int, b:int) -> int:
        return int(a/self.gcd(max(a,b),min(a,b)) * b)

s = Solution()
print("gcd:",s.gcd(26,13))
print("lcm:",s.lcm(26,13))