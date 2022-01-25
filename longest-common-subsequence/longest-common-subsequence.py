class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1 for i in range(1001)]for j in range(1001)]
        def helper(index1,index2):
            if index1 >= len(text1) or index2 >=len(text2):
                return 0
            if(dp[index1][index2] ==-1):
                if(text1[index1] == text2[index2]):
                    dp[index1][index2] = 1 + helper(index1+1,index2+1)
                else:
                    val1 = helper(index1+1,index2)
                    val2 = helper(index1,index2+1)
                    dp[index1][index2] = max(val1,val2)
                    
            return dp[index1][index2]        
              
        
        return helper(0,0)