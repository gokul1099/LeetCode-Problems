class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recur(i,j):
            if(i<0 or i>=row or j<0 or j>=col or grid[i][j]!="1"):
                return
            grid[i][j] = "-1"
            recur(i,j-1)
            recur(i,j+1)
            recur(i+1,j)
            recur(i-1,j)
            
        row = len(grid)
        col = len(grid[0])
        if(len(grid)==0):
            return 0
        count=0
        for i in range(row):
            for j in range(col):
                if(grid[i][j] == "1"):
                    count+=1
                    recur(i,j)        
        return count            