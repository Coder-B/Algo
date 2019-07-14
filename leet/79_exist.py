# https://leetcode.com/problems/word-search/
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if 0 == len(word):
            return True
        if 0 == len(board):
            return False
        visited=[[False for col in range(0,len(board[0]))] for row in range(0,len(board))]
        for row in range(0,len(board)):
            for col in range(0,len(board[0])):
                if board[row][col] == word[0]:
                    if self.existFromStart(board,visited,word,row,col):
                        return True
        return False
        
    def existFromStart(self, board: List[List[str]], visited: List[List[bool]], word: str, startRow: int, startCol: int) -> bool:
        if visited[startRow][startCol] or board[startRow][startCol] != word[0]:
            return False
        if 1 == len(word):
            return True
        else:
            visited[startRow][startCol] = True
            # print("compare char",startRow,startCol,board[startRow][startCol])
            if startRow>0:
                if self.existFromStart(board,visited,word[1:],startRow-1,startCol):
                    return True
            if startRow<len(board)-1:
                if self.existFromStart(board,visited,word[1:],startRow+1,startCol):
                    return True
            if startCol>0:
                if self.existFromStart(board,visited,word[1:],startRow,startCol-1):
                    return True
            if startCol<len(board[0])-1:
                if self.existFromStart(board,visited,word[1:],startRow,startCol+1):
                    return True
            visited[startRow][startCol] = False
            return False

s= Solution()
print(s.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],"SEE"))