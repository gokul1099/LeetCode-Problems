class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(numbers,target,start,end):
            mid = (start+end) //2
            if(start > end):
                return -1
            if(numbers[mid] == target):
                return mid
            if(target > numbers[mid]):
                start = mid+1
            if(target < numbers[mid]):
                end = mid-1
            return binary_search(numbers,target,start,end)
        for i in range(len(numbers)):
            target_1 = i
            target_2 = binary_search(numbers,target - numbers[target_1] ,i+1,len(numbers)-1)
            if(numbers[target_1] + numbers[target_2] == target):
                return [target_1+1,target_2+1]
            
            