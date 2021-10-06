class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            nums[i] = (nums[i]-1)*(nums[i+1]-1)
        return max(nums[:-1])
        