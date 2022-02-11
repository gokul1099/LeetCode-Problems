class UnionFind:
        def __init__(self,n):
            self.count = n
            self.rank = [1]*n
            self.root = [i for i in range(0,n)]
        def find(self,x):
            if x==self.root[x]:
                return x
            self.root[x] = self.find(self.root[x])
            return self.root[x]
        def union(self,x,y):
            rootX = self.find(x)
            rootY = self.find(y)
            if(rootX == rootY):
                return 
            if(rootX != rootY):
                if(self.rank[rootX] > self.rank[rootY]):
                    self.root[rootY] = rootX 
                elif(self.rank[rootX] < self.rank[rootY]):
                    self.root[rootX] = rootY
                else:
                    self.root[rootY] = rootX
                    self.rank[rootX] +=1
            self.count -=1       
        def cnt(self):
            return self.count
class Solution:
            
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        union = UnionFind(n)
        for i in range(n):
            for j in range(len(isConnected[0])):
                if(isConnected[i][j] == 1):
                    union.union(i,j)
        return union.cnt()            
        
        