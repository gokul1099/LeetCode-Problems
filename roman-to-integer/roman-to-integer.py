class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}
        res=romanNum[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if romanNum[s[i]] >= romanNum[s[i+1]]:
                res+=romanNum[s[i]]
            else:
                res-=romanNum[s[i]]
        return res        