class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minsofar=prices[0]
        
        max_profit=0
        
        for i in range(len(prices)):
          
          minsofar=min(minsofar,prices[i])
          profit=prices[i]-minsofar
          
          max_profit=max(max_profit, profit)
        return max_profit
      
      