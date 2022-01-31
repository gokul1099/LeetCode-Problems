class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0
        for i in range(len(accounts)):
            if sum(accounts[i]) > maxSum:
                maxSum = sum(accounts[i])
        return maxSum        
        