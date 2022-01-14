class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        sign=0
        res=0
        MAX = pow(2,31)-1
        MIN = -pow(2,31)
        while(index< len(s) and s[index] ==" "):
            index+=1
        if(index< len(s) and s[index] == "-"):    
            sign = -1
            index+=1
        elif(index<len(s) and s[index] == "+"):
            sign=1
            index+=1
        else:
            sign=1 
        while(index< len(s) and s[index].isdigit()):
            digit = ord(s[index]) - ord('0')
            if((res > MAX//10) or (res == MAX//10 and digit > MAX%10)):
                return MAX if sign == 1 else MIN
            res = res*10+digit
            index+=1
        return sign*res        
               