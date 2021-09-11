class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in nums:
            if i in hashMap:
                hashMap[i] +=1
                if(hashMap[i] > 1):
                    return True
            else:
                hashMap[i]=1
        return False       
           