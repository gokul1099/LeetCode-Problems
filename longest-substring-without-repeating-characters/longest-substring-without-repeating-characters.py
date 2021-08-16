class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength=0
        if len(s) == 0:
            return 0
        if len(s)==1:
            return 1
        for index in range(len(s)):
            tempMaxCount=0
            hashMap = {}
            for index2 in range(index,len(s)):
                if(s[index2] not in hashMap):
                    hashMap[s[index2]] =1
                    tempMaxCount+=1
                else:
                    break
              
            if(tempMaxCount>maxLength):
                maxLength = tempMaxCount
           
        return maxLength            
                
        