class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def solve(step):
            if step ==1:
                return 1
            if step==2:
                return 2
            if step in dp:
                return dp[step]
            dp[step] = solve(step-1) + solve(step-2)
            return dp[step]
        return solve(n)

            
        