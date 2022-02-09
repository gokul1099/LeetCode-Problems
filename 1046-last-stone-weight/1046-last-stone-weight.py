import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if(len(stones) == 1):
            return stones[0]
        if stones == []:
            return []
        stones = [-val for val in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            val1 = heapq.heappop(stones)
            val2 = heapq.heappop(stones)
            if(val1!=val2):
                heapq.heappush(stones,val1-val2)
        if(stones == []):
            return 0
        else:
            return -1*stones[0]
        