class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    def mergeSort(self,nums):
        if(len(nums) > 1):
            mid = len(nums)//2
            leftArr = nums[:mid]
            rightArr = nums[mid:]
            self.mergeSort(leftArr)
            self.mergeSort(rightArr)
            
            leftIndex,rightIndex,swapIndex =0,0,0
            while(leftIndex < len(leftArr) and rightIndex < len(rightArr)):
                if(leftArr[leftIndex] < rightArr[rightIndex]):
                    nums[swapIndex] = leftArr[leftIndex]
                    leftIndex+=1
                    swapIndex+=1
                else:
                    nums[swapIndex] = rightArr[rightIndex]
                    rightIndex+=1
                    swapIndex+=1
            while(leftIndex<=len(leftArr)-1):
                nums[swapIndex] = leftArr[leftIndex]
                leftIndex+=1
                swapIndex+=1
                
            while(rightIndex <= len(rightArr)-1):
                nums[swapIndex] = rightArr[rightIndex]
                rightIndex+=1
                swapIndex+=1
        return nums    
            

        