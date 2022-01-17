class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        cost=cost+[0]
        def dp(i):
            if i in memo:
                return memo[i]
            if i<0:
                return 0
            cost1 = dp(i-1)
            cost2 = dp(i-2)
            memo[i] = min(cost1,cost2)+cost[i]
            return memo[i]
        return dp(len(cost)-1)
        