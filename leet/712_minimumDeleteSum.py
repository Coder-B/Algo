# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len1,len2 = len(s1),len(s2)
        t=[0 for i in range(len1+1)]
        for i in range(1,len1+1):
            t[i]=t[i-1]+ord(s1[i-1])
        for row in range(1,len2+1):
            pre,cur = t[0],t[0]
            for col in range(len1+1):
                cur = t[col]
                if 0 == col:
                    t[col] = cur+ord(s2[row-1])
                else:
                    if s2[row-1] == s1[col-1]:
                        t[col] = pre
                    else:
                        t[col] = min(cur+ord(s2[row-1]),t[col-1]+ord(s1[col-1]))
                pre = cur
        return t[len1]

s=Solution()
s.minimumDeleteSum("ihlnqpdwqgcd","mgrumwmpjedv")