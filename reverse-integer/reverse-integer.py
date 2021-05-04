class Solution:
    def reverse(self, x: int) -> int:
        res =0
        
        num = abs(x)
        while(num!=0):
            temp = num%10
            num=num//10
            res= res*10+temp
       
        if res< -2**31 or res>2**31-1:
            return 0
        if x<0:
            return 0 - res
        return res
        