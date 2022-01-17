class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(num):
            if num == 0:
                return nums[0]
            if num ==1 :
                return max(nums[0],nums[1])
            if num not in memo:
                memo[num] = max(dp(num-1) , nums[num]+dp(num-2))
            return memo[num]    
        return dp(len(nums)-1)    