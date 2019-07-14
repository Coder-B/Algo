# https://leetcode.com/problems/trapping-rain-water-ii/
from typing import List
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rowNum = len(heightMap)
        if 0 == rowNum:
            return 0
        colNum = len(heightMap[0])
        left = [[0 for i in range(0,colNum)] for j in range(0,rowNum)]
        right = [[0 for i in range(0,colNum)] for j in range(0,rowNum)]
        top = [[0 for i in range(0,colNum)] for j in range(0,rowNum)]
        bottom = [[0 for i in range(0,colNum)] for j in range(0,rowNum)]
        leftMax,rightMax = [0 for i in range(0,rowNum)],[0 for i in range(0,rowNum)]
        topMax,bottomMax = [0 for i in range(0,colNum)],[0 for i in range(0,colNum)]

        for row in range(0,rowNum):
            for col in range(0,colNum):
                rowMx = max(leftMax[row],heightMap[row][col])
                left[row][col],leftMax[row] = rowMx,rowMx
                colMx = max(topMax[col],heightMap[row][col])
                top[row][col],topMax[col] = colMx,colMx

        for rowDistance in range(1,rowNum+1):
            row = rowNum - rowDistance
            for colDistance in range(1,colNum+1):
                col = colNum - colDistance
                rowMx = max(rightMax[row],heightMap[row][col])
                right[row][col],rightMax[row] = rowMx,rowMx
                colMx = max(bottomMax[col],heightMap[row][col])
                bottom[row][col],bottomMax[col] = colMx,colMx

        vol = 0
        for row in range(0,rowNum):
            print("new row")
            for col in range(0,colNum):
                print(min(left[row][col],right[row][col],top[row][col],bottom[row][col])-heightMap[row][col])
                vol += (min(left[row][col],right[row][col],top[row][col],bottom[row][col])-heightMap[row][col])
        return vol

s = Solution()
print(s.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]))