class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffHash ={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffHash:
                return [i,diffHash[diff]]
            diffHash[nums[i]] = i
            
            