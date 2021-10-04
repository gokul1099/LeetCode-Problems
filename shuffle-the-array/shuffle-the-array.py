class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        ptr1,ptr2=0,n
        while(ptr2<len(nums)):
            res.append(nums[ptr1])
            res.append(nums[ptr2])
            ptr1+=1
            ptr2+=1
        return res     