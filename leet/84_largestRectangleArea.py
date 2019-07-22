# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length,mxArea = len(heights),0
        for i in range(length):
            if i+1 < length and heights[i+1] >= heights[i]:
                continue
            minH = heights[i]
            for j in reversed(range(i+1)):
                minH = min(minH,heights[j])
                mxArea = max(mxArea,minH*(i-j+1))
        return mxArea
