# https://leetcode.com/problems/delete-operation-for-two-strings/
class Solution:
    # Runtime: 256 ms, faster than 91.51% of Python3 online submissions for Delete Operation for Two Strings.
    # Memory Usage: 13.9 MB, less than 87.39% of Python3 online submissions for Delete Operation for Two Strings.
    def minDistance(self, word1: str, word2: str) -> int:
        len1,len2 = len(word1),len(word2)
        t = [0 for i in range(len1+1)]
        for row in range(1,len2+1):
            pre,cur = 0,0
            for col in range(1,len1+1):
                cur = t[col]
                if word1[col-1] == word2[row-1]:
                    t[col] = pre+1
                else:
                    t[col] = max(t[col],t[col-1])
                pre = cur
        return len1+len2-2*t[len1]

    def minDistance0(self, word1: str, word2: str) -> int:
        len1,len2 = len(word1),len(word2)
        t = [[0 for i in range(len1+1)] for j in range(len2+1)]
        for row in range(1,len2+1):
            for col in range(1,len1+1):
                if word1[col-1] == word2[row-1]:
                    t[row][col] = t[row-1][col-1]+1
                else:
                    t[row][col] = max(t[row-1][col],t[row][col-1])
        return len1+len2-2*t[len2][len1]

s = Solution()
print(s.minDistance0("sea","eat") )
