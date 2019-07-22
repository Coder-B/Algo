# https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row,col = len(grid),len(grid[0])
        minPath = [[0 for i in range(col)] for j in range(row)]
        minPath[row-1][col-1] = grid[row-1][col-1]
        for i in reversed(range(col-1)):
            minPath[row-1][i] = minPath[row-1][i+1] + grid[row-1][i]
        for j in reversed(range(row-1)):
            minPath[j][col-1] = minPath[j+1][col-1] + grid[j][col-1]

        for i in reversed(range(row-1)):
            for j in reversed(range(col-1)):
                minPath[i][j] = min(minPath[i+1][j],minPath[i][j+1])+grid[i][j]
        return minPath[0][0]