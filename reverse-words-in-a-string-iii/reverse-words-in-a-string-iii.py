class Solution:
    def reverseWords(self, s: str) -> str:
        sArray = [i for i in s]
        indexes={}
        index_1,index_2=0,0
        def reverse(s,index_1,index_2):
            if(index_1 >= index_2):
                return
            s[index_1],s[index_2] = s[index_2],s[index_1]
            return reverse(s,index_1+1,index_2-1)
        while(index_2 <= len(sArray)-1):
            if(sArray[index_2] == " "):
                indexes[index_1]=index_2-1
                index_1= index_2+1
            index_2+=1
        indexes[index_1] = len(sArray)-1    
        for (key,value) in indexes.items():
            reverse(sArray,key,value)
        return "".join(sArray)