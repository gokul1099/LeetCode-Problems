class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
       
        
        rows,cols,point,diag,antidiag=[0]*3,[0]*3,1,0,0
        for row,col in moves:
            rows[row] +=point
            cols[col] +=point
            if(row == col):
                diag+=point
            if(row+col==2):
                antidiag+=point
            if(abs(rows[row]) == 3 or abs(cols[col])==3 or abs(diag)==3 or abs(antidiag) ==3):
                if(point == 1):
                    return "A"
                else:
                    return "B"
            point = -point
        if(len(moves) == 9):
            return "Draw"
        return "Pending"   
            
                
            