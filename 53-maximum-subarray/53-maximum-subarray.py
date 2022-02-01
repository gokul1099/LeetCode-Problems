class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr,best =0,-10**4
        for num in nums:
            curr = max(curr+num,num)
            best = max(curr,best)
        return best    
        