class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        dp = [[0 for i in range(len(multipliers))]for j in range(len(multipliers))]
        def helper(start,index):
            if(index >= len(multipliers)):
                return 0
            if not dp[start][index]:
                end = len(nums) - 1 -(index-start)
                dp[start][index]= max(multipliers[index] * nums[start]+helper(start+1,index+1),multipliers[index] * nums[end]+helper(start,index+1))
            return dp[start][index]
        return helper(0,0)