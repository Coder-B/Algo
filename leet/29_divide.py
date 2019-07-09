# https://leetcode.com/problems/divide-two-integers/
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 正负号
        PosOrNeg = 1
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            PosOrNeg = -1

        MAX_NEG_DIV,MAX_POS_DIV = -1*(2**31),2**31-1
        isMaxNeg = False
        if dividend == MAX_NEG_DIV:
            isMaxNeg = True
            if divisor == -1:
                return MAX_POS_DIV
            elif divisor == MAX_NEG_DIV:
                return 1
            else:
                # 处理溢出情况
                dividend = MAX_POS_DIV
        
        dividend,divisor = abs(dividend),abs(divisor)
        times = 0
        while dividend >= divisor:
            tmpDiv,tmpTime = divisor,1
            while tmpDiv+tmpDiv < dividend:
                tmpDiv = tmpDiv << 1
                tmpTime = tmpTime << 1
            times+=tmpTime
            dividend-=tmpDiv

        if isMaxNeg:
            if dividend+1 >= divisor:
                times+=1

        if PosOrNeg>0:
            return times
        else:
            return 0-times


s=Solution()
print(s.divide(10,3))
