class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        largest=0
        # if(len(matrix) ==1 and len(matrix[0])==1):
        #     if matrix[0][0]=="1":
        #         return 1
        #     else:
        #         return 0
        dp=[[0 for i in range (len(matrix[0])+1)]for j in range(len(matrix)+1)]
        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                if matrix[i-1][j-1]=="1":
                   
                    dp[i][j] =1+ int(min(dp[i-1][j],min(dp[i-1][j-1],dp[i][j-1])))
                    if(dp[i][j] > largest):
                        largest = dp[i][j]
        return largest*largest
        