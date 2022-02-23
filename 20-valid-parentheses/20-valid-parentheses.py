class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {"{":"}","[":"]","(":")"}
        for i in range(len(s)):
            if s[i] in '[{(':
                stack.append(s[i])
                continue
            elif(stack!=[] and s[i] == pairs[stack[-1]]):
                stack.pop()
            else:
                return False
        return stack==[]    
         
        