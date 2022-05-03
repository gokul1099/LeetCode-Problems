class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedArr = sorted(nums)
        left,right = len(nums)-1,0
        print(right,left)
        for i in range(len(nums)):
            if(sortedArr[i]!= nums[i]):
                left = min(i,left)
                right = max(i,right)
        if(right - left >0):
            return (right - left)+1
        return 0
        