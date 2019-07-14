# https://leetcode.com/problems/longest-string-chain/
from typing import List
class Solution:
    # Runtime: 2328 ms, faster than 5.15% of Python3 online submissions for Longest String Chain.
    def longestStrChain0(self, words: List[str]) -> int:
        if len(words)<=1:
            return len(words)
        result = 1
        words.sort(key=len)
        length = len(words)
        dp=[1 for i in range(0,length)]
        for i in range(0,length):
            for j in reversed(range(0,i)):
                if len(words[i])-len(words[j]) > 1:
                    break
                if self.isPre(words[j],words[i]):
                    maxlen = max(dp[i],dp[j]+1)
                    dp[i] = maxlen
                    result = max(maxlen,result)
        return result

    def isPre(self,a:str,b:str) -> bool:
        lenA,lenB = len(a),len(b)
        if lenB-lenA!=1:
            return False
        else:
            for i in range(0,lenA):
                if b[i]!=a[i]:
                    return b[i+1:] == a[i:]
            return True

    # Runtime: 128 ms, faster than 77.67% of Python3 online submissions for Longest String Chain.
    def longestStrChain(self, words: List[str]) -> int:
        if len(words)<=1:
            return len(words)
        result = 1
        words.sort(key=len)
        length = len(words)
        dp,prenum = [1 for i in range(0,length)],dict()
        for i in range(0,length):
            allPre = self.findPossiblePre(words[i])
            maxPre = 0
            for pre in allPre:
                if pre in prenum:
                    maxPre = max(maxPre,prenum[pre])
            dp[i] = (maxPre+1)
            prenum[words[i]] = dp[i]

        return max(dp)

    def findPossiblePre(self, word:str):
        allPre = []
        for i in range(0,len(word)):
            allPre.append(word[0:i]+word[i+1:])
        return allPre

s=Solution()
print(s.longestStrChain(["a","b","ba","bca","bda","bdca"]))
