class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        holding = [False]*len(prices)
        @lru_cache(None)
        def solve(stock,Tremaining,hold):
            if Tremaining == 0 or stock==len(prices):
                return 0
            skip = solve(stock+1,Tremaining,hold)
            val=0
            if(hold==1):
                val = prices[stock] + solve(stock+1,Tremaining-1,0)
            else:
                val = -prices[stock] + solve(stock+1,Tremaining,1)
            return max(val,skip)  
        return solve(0,k,0)
                
                
        