class Solution:
    def match(self,a,b):
         if((a== "(" and b==")") or
                   (a == "{" and b=="}") or
                   (a == "[" and b=="]")):
            return True
         return False
    def isValid(self, s: str) -> bool:
        stack=[]
        if s=="":
            return False
        for i in range(len(s)):
            if s[i] in "[{(":
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                elif(not self.match(stack[-1],s[i])):
                    return False
                else:
                    stack.pop()
        if(stack == []):
            return True
        return False
        