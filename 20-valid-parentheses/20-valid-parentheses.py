class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {"{":"}","[":"]","(":")"}
        opening = set(['[','{','('])
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
                continue
            elif(stack!=[] and s[i] == pairs[stack[-1]]):
                stack.pop()
            else:
                return False
        return stack==[]    
         
        