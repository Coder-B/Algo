# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen,tLen = len(s),len(t)
        if sLen > tLen:
            return False
        elif sLen == tLen:
            return s==t
        if 0 == len(s):
            return True
        else:
            idx = -1
            for i in range(0,tLen-sLen+1):
                if t[i] == s[0]:
                    idx = i
                    break
            if idx<0:
                return False
            else:
                return self.isSubsequence(s[1:],t[idx+1:])

s=Solution()
print(s.isSubsequence("abc", "ahbgdc"))