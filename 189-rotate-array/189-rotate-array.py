class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(index1,index2,nums):
            while(index1<index2):
                nums[index1],nums[index2] = nums[index2],nums[index1]
                index2-=1
                index1+=1

        reverse(0,len(nums)-1,nums)
        revIndex = k%len(nums)-1
        reverse(0,revIndex,nums)
        reverse(revIndex+1,len(nums)-1,nums)
        
            
        
            