class Solution:
    def sortSentence(self, s: str) -> str:
        hashMap = ['' for i in range(10)]
        for words in s.split(" "):
            index=int(words[-1])
            hashMap[index] = words[0:-1]
        res=''
        for i in hashMap:
            if(i!= ""):
                res+=i+" "
        return res[:-1]
            