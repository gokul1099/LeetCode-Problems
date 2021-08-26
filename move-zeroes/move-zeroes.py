class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCnt=0
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[zeroCnt]=nums[i]
                zeroCnt+=1
        for i in range(zeroCnt,len(nums)):
            nums[i]=0