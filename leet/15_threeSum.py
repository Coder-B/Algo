# https://leetcode.com/problems/3sum/
from typing import List
class Solution:
    # 1072 ms 版本
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        numLen = len(nums)
        i = 0
        while i < numLen-2:
            if nums[i]>0:
                break
            low,high,residue = i+1,numLen-1,0-nums[i]
            while low<high:
                if nums[low]+nums[high] == residue:
                    res.append([nums[i],nums[low],nums[high]])
                    # 防止 nums[low+1] 越界
                    while low < high and nums[low] == nums[low+1]:
                        low+=1
                    while low < high and nums[high] == nums[high-1]:
                        high-=1
                    low+=1
                    high-=1
                elif nums[low]+nums[high] < residue:
                    while low < high and nums[low] == nums[low+1]:
                        low+=1
                    low+=1
                else:
                    while low < high and nums[high] == nums[high-1]:
                        high-=1
                    high-=1
            while i<numLen-2 and nums[i] == nums[i+1]:
                i+=1
            i+=1
        return res

    # best version
    # 以正负区分nums，仍然以map方式进行目标数查找，且不需要list以强顺序排列
    # 时间复杂度约O(n^2 / 4)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        count = {}
        # 将nums记录在dict中，分别记录其个数
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        # 将nums以正负区分开来
        neg = [num for num in count if num < 0]
        pos = [num for num in count if num > 0]

        if 0 in count and count[0] >= 3:
            result.append([0,0,0])
            
        for p in pos:
            for n in neg:
                other = -(p+n)
                if other in count:
                    if other == n and count[n] > 1:
                        result.append([n,n,p])
                    elif other == p and count[p] > 1:
                        result.append([n,p,p])
                    elif n < other < p:
                        result.append([n,other,p])
        return result

s=Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
