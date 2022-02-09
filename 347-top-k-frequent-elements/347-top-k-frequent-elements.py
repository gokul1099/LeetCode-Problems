import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = Counter(nums)
        minHeap = [(-val,key) for key,val in hashMap.items()]
        heapq.heapify(minHeap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res
        
        
        
        
        