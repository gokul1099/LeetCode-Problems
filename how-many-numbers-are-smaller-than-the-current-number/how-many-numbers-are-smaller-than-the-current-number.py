class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res=[]
        for index1 in range(len(nums)):
            temp_count=0
            for index2 in range(len(nums)):
                if(nums[index2] != nums[index1] and nums[index2] < nums[index1]):
                    temp_count+=1
            res.append(temp_count)
        return res     