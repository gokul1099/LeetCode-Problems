import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hashMap={}
        for row in range(len(mat)):
            count=0
            for col in range(len(mat[0])):
                if(mat[row][col]==1):
                    count+=1
            hashMap[row]=count
        heap,res=[],[]
        heapq.heapify(heap)
        for key,val in hashMap.items():
            heapq.heappush(heap,(val,key))
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res    