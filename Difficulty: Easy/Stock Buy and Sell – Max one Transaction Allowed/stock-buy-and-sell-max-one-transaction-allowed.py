class Solution:
    def maximumProfit(self, prices):
        # code here
        i=0
        j=1
        ans=0
        while i<len(prices) and j<len(prices):
            if prices[i]>prices[j]:
                i+=1
            else:
                ans=max(ans,prices[j]-prices[i])
                j+=1
        return ans
            