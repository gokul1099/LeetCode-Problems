class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d={}
        res=[]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row+col not in d:
                    d[row+col] = [mat[row][col]]
                else:
                    d[row+col].append(mat[row][col])
        for key,val in d.items():
            if key%2==1:
                res+=(val)
            else:
                res+=val[::-1]
        return res        
                
        