# https://leetcode.com/problems/trapping-rain-water/
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        vol,left = 0,[0 for i in range(0,len(height))]
        mx,length = 0,len(height)
        for i in range(0,length):
            mx = max(mx,height[i])
            left[i]=mx
        mx = 0
        for i in range(0,length):
            idx = length-i-1
            mx = max(mx,height[idx])
            vol+=(min(left[idx],mx) - height[idx])
        return vol
s=Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

