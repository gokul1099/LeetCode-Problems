class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=""
        maxLen = max(len(a),len(b))
        carry=0
        a= a.zfill(maxLen)
        b=b.zfill(maxLen)
        for i in range(maxLen-1,-1,-1):
            res = carry
            res+= 1 if a[i]=="1" else 0
            res+= 1 if b[i]=="1" else 0
            ans = ('1' if res%2==1 else '0' )+ ans
            carry = 0 if res<2 else 1
        if carry!=0:
            ans = "1" + ans
        return ans.zfill(maxLen)
        