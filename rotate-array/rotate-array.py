class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,ptr1,ptr2):
            while(ptr1 < ptr2):
                nums[ptr1],nums[ptr2] = nums[ptr2],nums[ptr1]
                ptr1+=1
                ptr2-=1
        reverse(nums,0,len(nums)-1)
        ptr2=k%len(nums) -1
        reverse(nums,0,ptr2)
        reverse(nums,ptr2+1,len(nums)-1)