import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)
        for i in range(0,k):
            heapq.heappush(minHeap,nums[i])
        for i in range(k,len(nums)):
            if(minHeap[0] < nums[i]):
                heapq.heappop(minHeap)
                heapq.heappush(minHeap,nums[i])
        return minHeap[0]       
        
        