# https://leetcode.com/problems/container-with-most-water/
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        startIdx,endIdx,maxVol = 0,len(height)-1,0
        while startIdx<endIdx:
            vol = min(height[startIdx],height[endIdx]) * (endIdx - startIdx)
            if vol > maxVol:
                maxVol = vol
            if min(height[endIdx-1],height[startIdx]) > min(height[startIdx+1],height[endIdx]):
                endIdx = endIdx-1
            else:
                startIdx = startIdx + 1

        return maxVol

s=Solution()
l = [1,3,2,5,25,24,5]
print(s.maxArea(l))
