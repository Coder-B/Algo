# https://leetcode.com/problems/target-sum/
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        length = len(nums)
        preDict = dict()
        preDict[0] = 1
        for i in range(1,length+1):
            curDict = dict()
            for key in preDict:
                addItem,delItem = key+nums[i-1],key-nums[i-1]
                if addItem in curDict:
                    curDict[addItem] += preDict[key]
                else:
                    curDict[addItem] = preDict[key]

                if delItem in curDict:
                    curDict[delItem] += preDict[key]
                else:
                    curDict[delItem] = preDict[key]
            preDict = curDict
            print(preDict)
        if S in preDict:
            return preDict[S]
        else:
            return 0

s=Solution()
s.findTargetSumWays([1,1,1,1,1],3)