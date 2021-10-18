class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ptr1,ptr2=0,3
        count=0
        flag=0
        while(ptr2<=len(s)):
            hashMap={}
            tempStr =s[ptr1:ptr2]
            for i in tempStr:
                if i not in hashMap:
                    hashMap[i] = 1
                else:
                    flag=1
                    break
            print(hashMap)        
            if(flag==0):
                count+=1
            flag=0
            ptr1+=1
            ptr2+=1
        return count    
            