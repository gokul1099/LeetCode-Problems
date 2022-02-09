class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return math.sqrt((0-x)**2 + (0-y)**2)
        heap =[]
        heapq.heapify(heap)
        index=0
        for point in points:
            dist = distance(point[0],point[1])
            heapq.heappush(heap,(dist,index))
            index+=1
        res=[]    
        while(k>0):
            index=heapq.heappop(heap)[1]
            res.append(points[index])
            k-=1
        return res
            