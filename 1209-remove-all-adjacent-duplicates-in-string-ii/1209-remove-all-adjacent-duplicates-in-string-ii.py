class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in range(len(s)):
            if(stack and stack[-1][0] == s[i]):
                stack[-1][1] +=1
            else:
                stack.append([s[i],1])
            if(stack[-1][1] == k):
                stack.pop()
        res=""       
        for i in range(len(stack)):
            res += stack[i][0] * stack[i][1]
        return res    
                
        