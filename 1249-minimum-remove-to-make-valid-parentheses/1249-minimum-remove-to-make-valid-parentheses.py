class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        sSet = set()
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            elif(s[i]==")"):
                if(len(stack)>=1 and s[stack[-1]] == "("):
                    stack.pop()
                else:
                    sSet.add(i)
        ans = ""
        if(stack):
            for i in stack:
                sSet.add(i)
        for i in range(len(s)):
            if i not in sSet:
                ans+=s[i]
                
        return ans        