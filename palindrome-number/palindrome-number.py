class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num=0
        refNum = x
        while(refNum >0):
            temp = refNum%10
            num = num*10 + temp
            refNum= refNum//10
        if(num == x):
            return True
        return False
            
        