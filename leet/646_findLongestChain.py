# https://leetcode.com/problems/maximum-length-of-pair-chain/
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        length = len(pairs)
        if length <= 1:
            return length
         