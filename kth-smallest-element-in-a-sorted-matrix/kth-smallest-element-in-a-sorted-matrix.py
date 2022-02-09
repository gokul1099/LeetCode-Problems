class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for mat in matrix:
            for x in mat:
                heapq.heappush(heap,x)
        while(k>1):
            heapq.heappop(heap)
            k-=1
        return heap[0]    
        
        