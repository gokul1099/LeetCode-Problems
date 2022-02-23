class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {"{":"}","[":"]","(":")"}
        opening = set(['[','{','('])
        for i in s:
            if i in opening:
                stack.append(i)
                continue
            elif(stack!=[] and i == pairs[stack[-1]]):
                stack.pop()
            else:
                return False
        return stack==[]    
         
        