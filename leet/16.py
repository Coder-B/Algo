# https://leetcode.com/problems/3sum-closest/
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i,numLen,closestDiff = 0,len(nums),10000000
        closestTar = 0
        while i<numLen-2:
            if i>0:
                # add i 边界监测
                while  i<numLen-2 and nums[i] == nums[i-1]:
                    i+=1
            low,high = i+1,numLen-1
            while low < high:
                if nums[i]+nums[low]+nums[high] == target:
                    return target
                else:
                    diff = nums[i]+nums[low]+nums[high] - target
                    if abs(diff) < closestDiff:
                        closestDiff = abs(diff)
                        closestTar = nums[i]+nums[low]+nums[high]
                    if diff > 0:
                        while low < high and nums[high] == nums[high-1]:
                            high-=1
                        high-=1
                    else:
                        while low < high and nums[low] == nums[low+1]:
                            low+=1
                        low+=1
            i+=1
        return closestTar


s= Solution()
print(s.threeSumClosest([-1, 2, 1, -4],1))