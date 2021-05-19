class Solution:
    def match(self,a,b):
         if((a== "(" and b==")") or
                   (a == "{" and b=="}") or
                   (a == "[" and b=="]")):
            return True
         return False   
    def isValid(self, s: str) -> bool:
        stack =[]
        if(s== ""):
            return False
        for index in range(len(s)):
            if(s[index] in "[{("):
                stack.append(s[index])
            else:
                if(stack==[]):
                    return False
                elif(not self.match(stack[-1],s[index])):
                    return False
                else:
                    stack.pop()
               
        if(stack==[]):
            return True
        