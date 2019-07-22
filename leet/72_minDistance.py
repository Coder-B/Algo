# https://leetcode.com/problems/edit-distance/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1,len2 = len(word1),len(word2)
        t = [[0 for i in range(len1+1)] for j in range(len2+1)]
        for col in range(len1+1):
            t[0][col] = col
        for row in range(len2+1):
            t[row][0] = row
        for row in range(1,len2+1):
            for col in range(1,len1+1):
                if word1[col-1] == word2[row-1]:
                    t[row][col] = t[row-1][col-1]
                else:
                    t[row][col] = min(t[row-1][col],t[row][col-1],t[row-1][col-1])+1
        return t[len2][len1]