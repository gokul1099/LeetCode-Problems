class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def recur(i,j):
            if(i<0 or i>=row or j<0 or j>=col):
                return False
            if(grid[i][j] == 1):
                return True
            grid[i][j] = 1
            right = recur(i,j+1)
            left = recur(i,j-1)
            up = recur(i-1,j)
            down = recur(i+1,j)
            return right and left and up and down
        if(len(grid)==0):
            return 0
        count =0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0 and recur(i,j):
                    count+=1
        return count            
                    