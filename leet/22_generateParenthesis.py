# https://leetcode.com/problems/generate-parentheses/
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        retList = []
        if 0 < n:
            self.generate("(",1,1,n,retList)
        return retList


    def generate(self, prefix: str, unclosed: int, used: int, n: int, list: List[str]):
        if used == n:
            prefix += ")"*unclosed
            print(prefix)
            list.append(prefix)
        else:
            self.generate(prefix+"(",unclosed+1,used+1,n,list)
            if unclosed > 0:
                self.generate(prefix+")",unclosed-1,used,n,list)
        return

s=Solution()
print(s.generateParenthesis(3))
