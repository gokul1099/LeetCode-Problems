class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start =0
        end=len(nums)-1
        res=[]
        while(start <= end):
            if(abs(nums[start]) >= abs(nums[end])):
                res.append(nums[start]**2)
                start+=1
            else:
                res.append(nums[end]**2)
                end-=1
        return res[::-1]   
                