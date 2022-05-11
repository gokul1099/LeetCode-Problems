class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        srcVal = image[sr][sc]
        def recur(i,j):
            if(i<0 or i>=row or j<0 or j>=col):
                return
            elif(image[i][j]!= srcVal):
                return
            image[i][j] = newColor
            recur(i,j-1)
            recur(i,j+1)
            recur(i-1,j)
            recur(i+1,j)
        if(image[sr][sc] == newColor):
            return image
        recur(sr,sc)
        return image