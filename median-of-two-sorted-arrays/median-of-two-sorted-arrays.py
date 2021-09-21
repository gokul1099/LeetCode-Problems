class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combinedArr = nums1+nums2
        combinedArr.sort()
        if(len(combinedArr)%2 ==0):
            val1= combinedArr[len(combinedArr)//2]
            val2 = combinedArr[(len(combinedArr)//2 )-1 ]
            return (val1+val2)/2
        else:
            return combinedArr[len(combinedArr)//2]
            