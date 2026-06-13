class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar=prices[0]
        n=len(prices)
        res=0
        for i in range(1,n):
            minsofar=min(minsofar,prices[i])
            res=max(res,prices[i]-minsofar)
        return res
