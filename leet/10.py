# https://leetcode.com/problems/regular-expression-matching/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen,plen = len(s),len(p)
        # 不使用dp = [[0]*(slen+1)]*(plen+1) 方式初始化，有坑
        dp = [[False for i in range(slen+1)] for j in range(plen+1)]
        dp[0][0] = True
        # 处理 s="abcd", p="" 的情况
        i = 1
        while i <= slen :
            dp[0][i] = False
            i = i + 1

        # 处理 s="", p="$%^&" 的情况 
        if plen > 0:
            dp[1][0] = False
        i = 2
        while i<=plen:
            if i%2 == 1:
                dp[i][0] = False
            else:
                dp[i][0] = dp[i-2][0] and (p[i-1] == '*')
            i = i + 1

        startS = 1
        while startS <= slen:
            startP = 1
            while startP <= plen:
                if p[startP-1] == '*':
                    # * 取值为0, dp[startP-2][startS]
                    # * 取值为1, dp[startP-1][startS]
                    # * 取值大于1, dp[startP][startS-1] and isSingleMatch(s,p)
                    dp[startP][startS] = dp[startP-2][startS] or dp[startP-1][startS] or (dp[startP][startS-1] and self.isSingleMatch(s[startS-1],p[startP-2]))
                else:
                    dp[startP][startS] = dp[startP-1][startS-1] and self.isSingleMatch(s[startS-1],p[startP-1])
                startP = startP + 1
            startS = startS + 1
        return dp[plen][slen]


    def isSingleMatch(self,s: str,p:str) -> bool:
        if p == '.':
            return True
        else:
            return s == p


s = Solution()
print(s.isMatch("aa","a"))


