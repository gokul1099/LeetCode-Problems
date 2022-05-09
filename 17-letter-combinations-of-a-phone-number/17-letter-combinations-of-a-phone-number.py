class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashMap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def helper(index):
            if index == len(digits):
                return {""}
            temp=helper(index+1)
            ans = []
            for i in hashMap[digits[index]]:
                for j in temp:
                    ans.append(i+j)
            return ans
        if(digits == ""):
            return []
        index=0
        return helper(index)
                    
            
                
        