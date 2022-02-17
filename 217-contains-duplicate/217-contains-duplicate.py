class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic ={}
        for i in  nums:
            if i not in dic:
                dic[i]=0
            else:
                dic[i]+=1
                return True
        return False    
                
        