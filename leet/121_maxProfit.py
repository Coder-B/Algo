# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if 1>=len(prices):
            return 0
        lowest,mxProfit = prices[0],0-prices[0]
        for i in range(1,len(prices)):
            profit = prices[i]-lowest
            mxProfit = max(mxProfit,profit)
            lowest = min(lowest,prices[i])
        return mxProfit

s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))