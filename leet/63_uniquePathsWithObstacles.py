# https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0:
            return 0
        row,col = len(obstacleGrid),len(obstacleGrid[0])
        matrix = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            if 0 == obstacleGrid[i][0]:
                matrix[i][0] = 1
            else:
                break
        for j in range(col):
            if 0 == obstacleGrid[0][j]:
                matrix[0][j] = 1
            else:
                break

        for i in range(1,row):
            for j in range(1,col):
                if 0 == obstacleGrid[i][j]:
                    matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
        return matrix[row-1][col-1]
