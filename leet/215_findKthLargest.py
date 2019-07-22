# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1:
            return max(nums)
        if k == len(nums):
            return min(nums)
        low,pivot,high = 0,nums[0],len(nums)-1
        while low<high:
            while high>low and nums[high] >= pivot:
                high-=1
            nums[low] = nums[high]
            while high>low and nums[low] <= pivot:
                low+=1
            nums[high] = nums[low]
        nums[low] = pivot
        if k<len(nums)-low:
            return self.findKthLargest(nums[low+1:],k)
        elif k>len(nums)-low:
            return self.findKthLargest(nums[:low],k-len(nums)+low)
        else:
            return pivot

s=Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6],4))