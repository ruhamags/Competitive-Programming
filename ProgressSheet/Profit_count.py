class Solution(object):
    def maxProfit(self, prices):
        total = 0 
        for i in range(len(prices) - 1): 
            if prices[i + 1] > prices[i]:  
                total += prices[i + 1] - prices[i]  
        return total
