class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(nums,target,start,end):
            mid = (start+end)//2
            if(start > end):
                return start
            if(nums[mid] == target):
                return mid
            if(target > nums[mid]):
                start = mid+1
            if(target < nums[mid]):
                end = mid-1
            return binary_search(nums,target,start,end)
        return binary_search(nums,target,0,len(nums)-1)
                