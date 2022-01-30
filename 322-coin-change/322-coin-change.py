class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for i in range(amount+1)]
        MAX_VALUE = 10**4
        def helper(rem):
            if rem<0:
                return -1
            if rem==0:
                return 0
            
            if dp[rem]!=0:
                return dp[rem]
            min = MAX_VALUE
            for coin in coins:
                res = helper(rem-coin)
                if(res>=0 and res<min):
                    min=1+res
            if(min == MAX_VALUE):
                dp[rem]=-1
            else:
                dp[rem]=min
            return dp[rem]  
        return helper(amount)
            