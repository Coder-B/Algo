# https://leetcode.com/problems/gray-code/
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if 0==n:
            return []
        ret = [0,1]
        base = 1
        for i in range(1,n):
            base <<= 1
            for j in reversed(range(0,len(ret))):
                ret.append(base+ret[j])
        return ret

s= Solution()
print(s.grayCode(2))