#LC121
#Best time to buy and sell stocks
#Input: prices = [7,1,5,3,6,4]
#Output: 5

class Solution(object):
    def maxProfit(self, prices):
        
        l=0
        r=1
        maxProfit=0
        while(r<len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                maxProfit = max(maxProfit,profit)
            else:
                l = r
            r+=1
        return maxProfit