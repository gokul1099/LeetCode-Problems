class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        arr=[]
        for i in nums2:
            if i in nums1:
                arr.append(i)
        return arr          
        