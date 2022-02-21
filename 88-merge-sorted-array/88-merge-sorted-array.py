class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index=0
        for i in range(m,len(nums1)):
            nums1[i]=nums2[index]
            index+=1
        index=0
        while(index < len(nums1)-1):
            if(nums1[index]>nums1[index+1]):
                nums1[index],nums1[index+1] = nums1[index+1],nums1[index]
                index=-1
            index+=1
        return nums1   
            