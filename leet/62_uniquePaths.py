# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        matrix = [[0 for i in range(0,m)] for j in range(0,n)]
        for col in range(0,m):
            matrix[0][col] = 1
        for row in range(0,n):
            matrix[row][0] = 1
        for row in range(1,n):
            for col in range(1,m):
                matrix[row][col] = matrix[row-1][col]+matrix[row][col-1]
        return matrix[m-1][n-1]