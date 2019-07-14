# https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if 0 == len(nums):
        	return 0
        return self.divideProduct(nums,0,len(nums)-1)

    def divideProduct(self, nums: List[int], low: int, high: int) -> int:
    	if low >= high:
    		return nums[low]
    	if low+1 == high:
    		return max(nums[low],nums[high],nums[low]*nums[high])
    	mid = int((low+high)/2)
    	leftProduct,rightProduct = self.divideProduct(nums,low,mid-1),self.divideProduct(nums,mid+1,high)
    	mxMidPro,midProduct = nums[mid],nums[mid]
    	
