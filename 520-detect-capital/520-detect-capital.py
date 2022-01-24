class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cond1,cond2,cond3 = True,True,True
        for i in word:
            if not i.isupper():
                cond1=False
                break
        count=0
        if(word[0].isupper()):
            count+=1
        for i in word:
            if not i.isupper():
                count+=1
                
        if(count == len(word)):
            cond2=True
        else:
            cond2=False
    
        if(cond1==True or cond2==True):
            return True
        else:
            return False
            
        