class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans=0
        sum=0
        for i in range(2,len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                ans+=1
                sum+=ans
            else:
                ans=0
        return sum        