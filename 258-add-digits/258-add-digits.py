class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        ans =0
        while num!=0:
            ans +=(num%10)
            num = num//10
        if ans%9==0:
            return 9
        else:
            return ans%9
        