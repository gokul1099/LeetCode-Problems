class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        for i in range(len(s[0])):
            for j in range(1,len(s)):
                if i >= len(s[j]):
                    return s[0][:i]
                if not s[j][i] == s[0][i]:
                    return s[0][:i]
        return s[0]         
                 

