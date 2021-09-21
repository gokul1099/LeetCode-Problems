class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ptr1,ptr2= 0,0
        maxCount,tempCount=0,0
        while(ptr1 <len(nums) and ptr2 <len(nums)):
            if nums[ptr2] == 1:
                ptr2+=1
                tempCount+=1
            else:
                ptr2 +=1
                ptr1 = ptr2
                tempCount=0
            if(tempCount > maxCount):
                maxCount = tempCount
        return maxCount         