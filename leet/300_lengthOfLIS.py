# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List
class Solution:
    # Runtime: 1096 ms, faster than 35.54% of Python3 online submissions for Longest Increasing Subsequence.
    # Memory Usage: 14.1 MB, less than 5.28% of Python3 online submissions for Longest Increasing Subsequence.
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if 1>=length:
            return length
        arr,mxLen = [1 for i in range(length)],1
        for i in range(1,length):
            for j in reversed(range(0,i)):
                if nums[j] < nums[i]:
                    arr[i] = max(arr[j]+1,arr[i])
                if arr[i] > mxLen:
                    mxLen = arr[i]
                    break
        return mxLen

    # def lengthOfLIS(self, nums: List[int]) -> int:

s=Solution()
print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))