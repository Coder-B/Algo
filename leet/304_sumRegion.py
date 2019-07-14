# https://leetcode.com/problems/range-sum-query-2d-immutable/
from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix)>0:
            self.sumMatrix = [[0 for i in range(0,len(matrix[0])+1)]]
            for row in range(0,len(matrix)):
                rowsum,rowArr = 0,[0]
                for col in range(0,len(matrix[0])):
                    rowsum+=matrix[row][col]
                    rowArr.append(rowsum)
                if 0 < row:
                    for col in range(0,len(self.sumMatrix[0])):
                        rowArr[col]+=self.sumMatrix[row][col]
                self.sumMatrix.append(rowArr)
            # print(self.sumMatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumMatrix[row2+1][col2+1] - self.sumMatrix[row1][col2+1] - self.sumMatrix[row2+1][col1] + self.sumMatrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

obj = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(obj.sumRegion(2,1,4,3))

# ["NumMatrix","sumRegion","sumRegion","sumRegion"]
# [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]